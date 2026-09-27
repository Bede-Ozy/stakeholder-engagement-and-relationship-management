const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const EDGE_PATH = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const URL = 'http://localhost:8080/index.html';

async function captureAllSlides() {
  const outputDir = path.join(__dirname, 'snapshots');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  console.log('Launching Edge browser at:', EDGE_PATH);
  const browser = await puppeteer.launch({
    executablePath: EDGE_PATH,
    headless: 'new',
    protocolTimeout: 120000,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu', '--disable-dev-shm-usage']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 2 });

  console.log('Navigating to:', URL);
  await page.goto(URL, { waitUntil: 'domcontentloaded', timeout: 30000 });
  await new Promise(r => setTimeout(r, 1200));

  // Hide the HUD, Dock, and other overlays for a clean slide canvas snapshot
  await page.evaluate(() => {
    document.body.classList.add('is-fullscreen');
    const hud = document.getElementById('presentationHud');
    const dock = document.getElementById('presentationDock');
    const shortcuts = document.getElementById('shortcutPill');
    const canvas = document.getElementById('ambientNodesCanvas');
    if (hud) hud.style.display = 'none';
    if (dock) dock.style.display = 'none';
    if (shortcuts) shortcuts.style.display = 'none';
    if (canvas) canvas.style.display = 'none';

    // Freeze CSS animations for instant screenshot rendering
    const style = document.createElement('style');
    style.innerHTML = '* { animation-play-state: paused !important; }';
    document.head.appendChild(style);
  });

  const stage = await page.$('#slideStage');
  const box = await stage.boundingBox();

  const themes = ['light', 'dark'];

  for (const theme of themes) {
    console.log(`\n--- Capturing theme: ${theme.toUpperCase()} ---`);
    await page.evaluate((t) => {
      document.body.setAttribute('data-theme', t);
    }, theme);

    await new Promise(r => setTimeout(r, 400));

    for (let slideNum = 1; slideNum <= 16; slideNum++) {
      // Activate target slide
      await page.evaluate((num) => {
        const slides = Array.from(document.querySelectorAll('.slide-card'));
        slides.forEach((s, idx) => {
          if (idx + 1 === num) {
            s.classList.add('active');
            s.style.opacity = '1';
            s.style.transform = 'none';
          } else {
            s.classList.remove('active');
            s.style.opacity = '0';
          }
        });
      }, slideNum);

      const stage = await page.$('#slideStage');
      const filename = `slide_${theme}_${String(slideNum).padStart(2, '0')}.png`;
      const filepath = path.join(outputDir, filename);

      await stage.screenshot({ path: filepath, type: 'png' });
      console.log(`Saved ${filename}`);
    }
  }

  await browser.close();
  console.log('\nAll 32 snapshots (16 light + 16 dark) captured successfully!');
}

captureAllSlides().catch(err => {
  console.error('Error capturing slides:', err);
  process.exit(1);
});
