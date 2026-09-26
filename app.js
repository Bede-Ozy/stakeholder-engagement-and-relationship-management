/**
 * STAKEHOLDER ENGAGEMENT & RELATIONSHIP MANAGEMENT IN THE CIVIL SERVICE
 * Presentation Controller & Interactive Engine
 */

document.addEventListener('DOMContentLoaded', () => {
  // DOM References
  const slides = Array.from(document.querySelectorAll('.slide-card'));
  const totalSlides = slides.length;
  let currentSlide = 1;

  const currentSlideNumEl = document.getElementById('currentSlideNum');
  const totalSlidesNumEl = document.getElementById('totalSlidesNum');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const slideTrack = document.getElementById('slideTrack');

  // HUD & Dock Elements
  const presentationHud = document.getElementById('presentationHud');
  const presentationDock = document.getElementById('presentationDock');
  const hudHoverZone = document.getElementById('hudHoverZone');
  const dockHoverZone = document.getElementById('dockHoverZone');

  // Speaker Notes Elements
  const notesToggleBtn = document.getElementById('notesToggleBtn');
  const speakerNotesDrawer = document.getElementById('speakerNotesDrawer');
  const notesDrawerOverlay = document.getElementById('notesDrawerOverlay');
  const notesCloseBtn = document.getElementById('notesCloseBtn');
  const notesBody = document.getElementById('notesBody');
  const notesSlideTag = document.getElementById('notesSlideTag');

  // Grid Modal Elements
  const gridToggleBtn = document.getElementById('gridToggleBtn');
  const gridModalOverlay = document.getElementById('gridModalOverlay');
  const gridCloseBtn = document.getElementById('gridCloseBtn');
  const gridCardsContainer = document.getElementById('gridCardsContainer');

  // References Modal Elements
  const referencesBtn = document.getElementById('referencesBtn');
  const referencesModalOverlay = document.getElementById('referencesModalOverlay');
  const referencesCloseBtn = document.getElementById('referencesCloseBtn');

  // Theme & Fullscreen Elements
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  const fullscreenBtn = document.getElementById('fullscreenBtn');

  // Presentation Timer Elements
  const timerWidget = document.getElementById('timerWidget');
  const timerDisplay = document.getElementById('timerDisplay');
  let timerSeconds = 0;
  let timerInterval = null;
  let isTimerRunning = true;

  // Shortcuts hint pill
  const shortcutPill = document.getElementById('shortcutPill');

  // Slide Data Registry (Metadata & Speaker Notes for Consultants)
  const slideRegistry = [
    {
      id: 1,
      title: "Title & Executive Overview",
      kicker: "OPENING KEYNOTE",
      time: "2-3 Mins",
      takeaway: "Set the executive tone: stakeholder engagement is not political people-pleasing, but a rigorous public-sector administrative discipline.",
      points: [
        "Welcome delegates to this National Leadership Masterclass. Establish executive authority immediately.",
        "Emphasize the core thesis: Good policy fails when administrators focus solely on technical brilliance while ignoring the human and institutional ecosystem.",
        "Highlight the 4 foundational pillars: Administrative Procedures + Stakeholder Engagement + Emotional Intelligence + Decision Making.",
        "Frame the conference objective: equipping directors, permanent secretaries, and administrators with a repeatable playbook for durable governance."
      ]
    },
    {
      id: 2,
      title: "The Real Challenge: Decision ≠ Implementation",
      kicker: "EXECUTIVE REALITY",
      time: "3 Mins",
      takeaway: "A technically sound policy without stakeholder alignment collapses at the point of execution.",
      points: [
        "Walk the audience through the 5 cascading failure points: Wrong people consulted → Concerns ignored → Expectations unmanaged → Communication delayed → Implementation failure.",
        "Give a relatable civil service example: A digital attendance or ERP rollout launched without engaging labour unions or departmental desk officers.",
        "Stress the bottom callout: 'Decision ≠ Implementation'. Approval in council or internal memo is just 10% of the journey; 90% is managing the human transition."
      ]
    },
    {
      id: 3,
      title: "Who is a Stakeholder? Ecosystem Mapping",
      kicker: "ECOSYSTEM MAPPING",
      time: "3-4 Mins",
      takeaway: "Expand the mental map beyond immediate hierarchical superiors to all 4 distinct quadrants of public value.",
      points: [
        "Challenge the traditional narrow view: A stakeholder is anyone who can affect the outcome OR who will be affected by the outcome.",
        "Break down the 4 groups: Internal (our own colleagues and field staff), Government (sister MDAs, regulators, oversight legislators), External (citizens, civil society, businesses), and Implementers (contractors, vendors).",
        "Point out the dangerous blindspot: Ignoring internal implementers often leads to quiet departmental sabotage."
      ]
    },
    {
      id: 4,
      title: "Engagement is a Spectrum",
      kicker: "ENGAGEMENT ARCHITECTURE",
      time: "3 Mins",
      takeaway: "Engagement is not one-size-fits-all. Calibrate engagement levels to avoid either superficial communication or bureaucratic paralysis.",
      points: [
        "Explain the 4 levels: Inform (one-way announcements), Consult (seeking feedback), Involve (working together on options), Collaborate (joint partnership and co-design).",
        "Quote: 'Not every stakeholder needs the same level of engagement.' Trying to collaborate with everyone causes endless committee gridlock; only informing critical power players causes revolt.",
        "Ask the audience: On your major current initiative, which stakeholders are you mistakenly under-engaging or over-engaging?"
      ]
    },
    {
      id: 5,
      title: "Power × Interest Matrix",
      kicker: "STRATEGIC PRIORITISATION",
      time: "4 Mins",
      takeaway: "Map stakeholders systematically before committing time, political capital, and public resources.",
      points: [
        "Explain the 2×2 grid: Y-axis represents statutory or informal Power/Influence; X-axis represents Interest/Vulnerability.",
        "Quadrant 1 (High Power / High Interest): Manage Closely. These are key ministers, affected communities, permanent secretaries.",
        "Quadrant 2 (High Power / Low Interest): Keep Satisfied. Regulators, Auditor-General, Treasury. Brief them early so they don't issue surprise stop orders.",
        "Quadrant 3 (Low Power / High Interest): Keep Informed. Frontline staff and vulnerable citizens. They hold critical operational insights.",
        "Quadrant 4 (Low Power / Low Interest): Monitor. Low overhead.",
        "Close with the 3 golden diagnostic questions: Who matters? Why do they matter? What do they need?"
      ]
    },
    {
      id: 6,
      title: "Don't Stop at Positions: Position ≠ Interest",
      kicker: "NEGOTIATION & ALIGNMENT",
      time: "3-4 Mins",
      takeaway: "Positions polarize; underlying interests create the bridge for lawful administrative compromise.",
      points: [
        "Introduce the Harvard Negotiation Project principle: Position is what people say they want; Interest is WHY they want it.",
        "Walk through the funnel diagram: When a Director yells 'I will not support this policy!', don't argue with the statement. Ask WHY.",
        "Reveal the hidden anxiety: 'My department will carry the audit and implementation risk without adequate budget.'",
        "Target the true needs: Clarity, Resources, Accountability. When you solve the underlying interest, resistance evaporates."
      ]
    },
    {
      id: 7,
      title: "Where Emotional Intelligence Enters",
      kicker: "LEADERSHIP MATURITY",
      time: "3 Mins",
      takeaway: "Emotional intelligence in the civil service is not weakness—it is strategic self-control and situational mastery.",
      points: [
        "Present the 5 sequential stages: Self-awareness → Self-control → Empathy → Social awareness → Relationship management.",
        "Key phrase: 'Manage yourself before managing the room.' If an administrator reacts defensively to criticism, they surrender control of the meeting.",
        "Emphasize the bottom rule: 'Emotionally intelligent ≠ agreeing with everyone.' It means understanding their emotions so you can uphold public interest firmly without creating unnecessary enemies."
      ]
    },
    {
      id: 8,
      title: "The Power of Active Listening",
      kicker: "ADMINISTRATIVE DIALOGUE",
      time: "3 Mins",
      takeaway: "Active listening is an intelligence-gathering tool, not an act of submission.",
      points: [
        "Detail the 4-step cadence: Listen without interrupting → Clarify ambiguous terms → Reflect their core fear back to them → Respond with reasoned procedural facts.",
        "Highlight the contrast box: Instead of the bureaucratic reflex 'That's not possible!', train teams to say: 'What specifically concerns you about the proposal?'",
        "Reinforce: Always listen on 3 frequencies: What they say (the words), What they mean (the emotion), and What they need (the institutional imperative)."
      ]
    },
    {
      id: 9,
      title: "When Stakeholders Become Difficult",
      kicker: "CONFLICT DE-ESCALATION",
      time: "4 Mins",
      takeaway: "Do not personalize friction. Diagnose the archetype and apply the corresponding administrative antidote.",
      points: [
        "Walk through the 5 tactical cards: Angry (de-escalate and lower vocal tone), Resistant (uncover past broken promises), Silent (create safe structured channels), Dominant (strictly enforce meeting standing orders), Unreasonable (anchor on statutory boundaries and Public Service Rules).",
        "Deliver the key rule: 'Don't match emotional intensity with emotional intensity.' When an external party shouts, the professional civil servant becomes calm, factual, and anchored in due process."
      ]
    },
    {
      id: 10,
      title: "Managing Disagreement: Positions → Interests",
      kicker: "CONSTRUCTIVE DELIBERATION",
      time: "3 Mins",
      takeaway: "Disagreement is evidence of diverse institutional stakes. The goal is to make disagreement productive.",
      points: [
        "Demonstrate the inquiry ladder: Turn a rigid 'NO' into curiosity by asking 'WHY?', pinpointing 'WHAT CONCERNS YOU?', and concluding with 'WHAT WOULD ADDRESS THAT CONCERN?'.",
        "Explain that when stakeholders participate in crafting the solution, their commitment to implementation skyrockets.",
        "Remind leaders: Groupthink in MDAs leads to disastrous policies. Welcoming constructive pushback protects the government from blindspots."
      ]
    },
    {
      id: 11,
      title: "Stakeholders & Decision Making",
      kicker: "DECISION-MAKING FILTER",
      time: "3-4 Mins",
      takeaway: "Run every policy, project, and circular through the 6-question diagnostic filter before final approval.",
      points: [
        "Briefly review the 6 convergence questions: WHO will be affected? WHY (what are their interests)? WHAT evidence do we have? RISK (what could go wrong)? RULES (what does administrative procedure dictate)? IMPLEMENTATION (can field staff execute this?).",
        "Show how these 6 inputs converge into a 'BETTER DECISION' that is legitimate, lawful, sustainable, and workable."
      ]
    },
    {
      id: 12,
      title: "The Trust Equation",
      kicker: "INSTITUTIONAL CURRENCY",
      time: "3 Mins",
      takeaway: "Public sector trust is a multiplicative equation—if any single component is zero, total trust collapses.",
      points: [
        "Explain the formula: Competence × Fairness × Transparency × Responsiveness × Consistency = TRUST.",
        "Demonstrate the mathematics: You can have high technical competence, but if your transparency is zero, public trust is zero.",
        "Bottom maxim: 'Every interaction either builds trust or erodes trust.' How an MDA officer answers a citizen's phone call or treats a departmental file impacts institutional credibility."
      ]
    },
    {
      id: 13,
      title: "The Nigerian Civil Service Context",
      kicker: "INSTITUTIONAL FOUNDATIONS",
      time: "4 Mins",
      takeaway: "Stakeholder engagement is not an imported novelty; it is enshrined in our Public Service Rules and SERVICOM Charters.",
      points: [
        "Left Column: Highlight OHCSF Federal Public Service Rules principles—Efficiency, Effectiveness, Performance, Due Process, and Probity.",
        "Right Column: Connect directly to the SERVICOM mandate—published Service Standards, Citizen Expectations, Complaints Redress, and Feedback loops.",
        "Punchline: 'Good administration must work for people, not only on paper.' Rules without empathy produce bureaucracy; empathy without rules produces chaos. We need both."
      ]
    },
    {
      id: 14,
      title: "The 5R Model (Signature Playbook)",
      kicker: "SIGNATURE PLAYBOOK",
      time: "4-5 Mins",
      takeaway: "The 5R Model is your practical, repeatable 5-step operational playbook for every project and reform.",
      points: [
        "Position this as the centerpiece takeaway of the masterclass.",
        "1. RECOGNISE: Who matters? Map the power-interest landscape.",
        "2. READ: What do they need? Decode the unvoiced anxieties beneath their positions.",
        "3. RELATE: How do we build trust? Listen actively and demonstrate procedural fairness.",
        "4. RESPOND: How do we engage and decide? Frame the decision within public service rules and explain trade-offs.",
        "5. REVIEW: What did we learn? Evaluate the rollout and close the feedback loop.",
        "Invite delegates to memorize the rhythm: RECOGNISE → READ → RELATE → RESPOND → REVIEW."
      ]
    },
    {
      id: 15,
      title: "From Engagement to Action: Close the Loop",
      kicker: "CLOSING THE LOOP",
      time: "3 Mins",
      takeaway: "The most damaging administrative mistake is holding a consultation and then disappearing into institutional silence.",
      points: [
        "Follow the 5-stage loop: Listen → Decide → Communicate → Act → Follow up.",
        "Emphasize the 3 non-negotiable updates every stakeholder must receive: WHAT was decided, WHY it was decided, and WHAT happens next.",
        "Even when an MDA decides against a stakeholder's demand, explaining the legal/budgetary rationale preserves goodwill. Silence creates suspicion.",
        "Point to the continuous loop: Engagement is an ongoing institutional discipline, not a one-off town hall meeting."
      ]
    },
    {
      id: 16,
      title: "Closing: People Support What They Understand",
      kicker: "CLOSING MANIFESTO",
      time: "2-3 Mins",
      takeaway: "Summarize the masterclass into a memorable, inspiring executive leadership charge.",
      points: [
        "Deliver the opening truth: 'People support what they understand.' When citizens and staff understand the why, they become co-owners of reform.",
        "Reiterate the 4 conditions: When people feel HEARD, RESPECTED, FAIRLY TREATED, and INFORMED, resistance turns into collaboration.",
        "Recite the closing manifesto with authority and conviction:",
        "• ENGAGE PEOPLE.",
        "• UNDERSTAND INTERESTS.",
        "• MANAGE EMOTIONS.",
        "• RESPECT PROCEDURE.",
        "• MAKE BETTER DECISIONS.",
        "Conclude and open the floor for executive Q&A, reflections, and panel discussion."
      ]
    }
  ];

  // ==========================================
  // INITIALIZE TRACK & GRID TILES
  // ==========================================
  function initTrackAndGrid() {
    // 1. Populate Bottom Dock Track Pips
    slideTrack.innerHTML = '';
    slides.forEach((_, idx) => {
      const pip = document.createElement('div');
      pip.className = `track-pip ${idx === 0 ? 'active' : ''}`;
      pip.title = `Go to Slide ${idx + 1}: ${slideRegistry[idx]?.title || ''}`;
      pip.addEventListener('click', () => goToSlide(idx + 1));
      slideTrack.appendChild(pip);
    });

    // 2. Populate Grid Overview Modal
    gridCardsContainer.innerHTML = '';
    slideRegistry.forEach((item) => {
      const thumb = document.createElement('div');
      thumb.className = `grid-card-thumb ${item.id === 1 ? 'active' : ''}`;
      thumb.setAttribute('data-target-slide', item.id);
      thumb.innerHTML = `
        <div class="thumb-header">
          <span class="thumb-num">SLIDE ${String(item.id).padStart(2, '0')}</span>
          <span class="thumb-kicker">${item.kicker}</span>
        </div>
        <div class="thumb-title">${item.title}</div>
        <div class="thumb-kicker" style="color: var(--accent-gold);">${item.time}</div>
      `;
      thumb.addEventListener('click', () => {
        goToSlide(item.id);
        closeGridModal();
      });
      gridCardsContainer.appendChild(thumb);
    });

    // Total Slide Counter (if present)
    if (totalSlidesNumEl) {
      totalSlidesNumEl.textContent = String(totalSlides).padStart(2, '0');
    }
  }

  // ==========================================
  // NAVIGATION CONTROLLER
  // ==========================================
  function goToSlide(targetSlide) {
    if (targetSlide < 1 || targetSlide > totalSlides) return;

    // Update active class on slides
    slides.forEach((slide, idx) => {
      const slideNum = idx + 1;
      if (slideNum === targetSlide) {
        slide.classList.add('active');
      } else {
        slide.classList.remove('active');
      }
    });

    currentSlide = targetSlide;

    // Update HUD indicator (if present)
    if (currentSlideNumEl) {
      currentSlideNumEl.textContent = String(currentSlide).padStart(2, '0');
    }

    // Update Track pips
    const pips = Array.from(slideTrack.querySelectorAll('.track-pip'));
    pips.forEach((pip, idx) => {
      pip.classList.remove('active', 'completed');
      if (idx + 1 === currentSlide) {
        pip.classList.add('active');
      } else if (idx + 1 < currentSlide) {
        pip.classList.add('completed');
      }
    });

    // Update Grid active thumb
    const thumbs = Array.from(gridCardsContainer.querySelectorAll('.grid-card-thumb'));
    thumbs.forEach((th, idx) => {
      if (idx + 1 === currentSlide) {
        th.classList.add('active');
      } else {
        th.classList.remove('active');
      }
    });

    // Update Button States
    prevBtn.disabled = currentSlide === 1;
    nextBtn.disabled = currentSlide === totalSlides;

    // Update URL Hash without reload
    window.location.hash = `slide-${currentSlide}`;

    // Update Speaker Notes if drawer is open or prepared
    updateSpeakerNotes(currentSlide);
  }

  function nextSlide() {
    if (currentSlide < totalSlides) {
      goToSlide(currentSlide + 1);
    }
  }

  function prevSlide() {
    if (currentSlide > 1) {
      goToSlide(currentSlide - 1);
    }
  }

  // ==========================================
  // SPEAKER NOTES LOGIC
  // ==========================================
  function updateSpeakerNotes(slideIdx) {
    const data = slideRegistry[slideIdx - 1];
    if (!data) return;

    notesSlideTag.textContent = `SLIDE ${String(data.id).padStart(2, '0')}`;
    
    notesBody.innerHTML = `
      <div class="notes-section">
        <span class="notes-heading">Slide Topic</span>
        <h4 style="font-family: var(--font-display); font-size: 1.25rem; font-weight: 800; color: var(--text-main);">${data.title}</h4>
        <div class="notes-timing-badge">
          <svg style="width: 14px; height: 14px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          <span>Suggested Time: ${data.time}</span>
        </div>
      </div>

      <div class="notes-section">
        <span class="notes-heading">Executive Core Takeaway</span>
        <p class="notes-takeaway">${data.takeaway}</p>
      </div>

      <div class="notes-section">
        <span class="notes-heading">Facilitator Talking Points &amp; Nuance</span>
        <ul class="notes-points-list">
          ${data.points.map(pt => `<li>${pt}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  function openSpeakerNotes() {
    updateSpeakerNotes(currentSlide);
    speakerNotesDrawer.classList.add('active');
    notesDrawerOverlay.classList.add('active');
  }

  function closeSpeakerNotes() {
    speakerNotesDrawer.classList.remove('active');
    notesDrawerOverlay.classList.remove('active');
  }

  function toggleSpeakerNotes() {
    if (speakerNotesDrawer.classList.contains('active')) {
      closeSpeakerNotes();
    } else {
      openSpeakerNotes();
    }
  }

  // ==========================================
  // MODAL CONTROLLERS (Grid & References)
  // ==========================================
  function openGridModal() {
    gridModalOverlay.classList.add('active');
  }

  function closeGridModal() {
    gridModalOverlay.classList.remove('active');
  }

  function toggleGridModal() {
    if (gridModalOverlay.classList.contains('active')) {
      closeGridModal();
    } else {
      openGridModal();
    }
  }

  function openReferencesModal() {
    referencesModalOverlay.classList.add('active');
  }

  function closeReferencesModal() {
    referencesModalOverlay.classList.remove('active');
  }

  function toggleReferencesModal() {
    if (referencesModalOverlay.classList.contains('active')) {
      closeReferencesModal();
    } else {
      openReferencesModal();
    }
  }

  function closeAllModals() {
    closeSpeakerNotes();
    closeGridModal();
    closeReferencesModal();
  }

  // ==========================================
  // THEME SWITCHER (Dark Navy Default / Light Template)
  // ==========================================
  function initTheme() {
    const savedTheme = localStorage.getItem('cs_deck_theme') || 'dark';
    document.body.setAttribute('data-theme', savedTheme);
  }

  function toggleTheme() {
    const currentTheme = document.body.getAttribute('data-theme') || 'dark';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.body.setAttribute('data-theme', newTheme);
    localStorage.setItem('cs_deck_theme', newTheme);
  }

  // ==========================================
  // PRESENTATION REHEARSAL TIMER
  // ==========================================
  function formatTime(totalSecs) {
    const mins = Math.floor(totalSecs / 60);
    const secs = totalSecs % 60;
    return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  }

  function startTimer() {
    if (timerInterval) clearInterval(timerInterval);
    timerInterval = setInterval(() => {
      if (isTimerRunning) {
        timerSeconds++;
        timerDisplay.textContent = formatTime(timerSeconds);
      }
    }, 1000);
  }

  function toggleTimer() {
    isTimerRunning = !isTimerRunning;
    timerWidget.style.opacity = isTimerRunning ? '1' : '0.6';
  }

  // ==========================================
  // FULLSCREEN & ZOOM TO CANVAS ENGINE
  // ==========================================
  function toggleFullscreen() {
    const isAlreadyFullscreen = Boolean(document.fullscreenElement) || document.body.classList.contains('is-fullscreen');

    if (!isAlreadyFullscreen) {
      document.body.classList.add('is-fullscreen');
      if (document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen().catch(() => {
          // Native fullscreen request was denied or blocked, CSS fullscreen fallback active!
        });
      }
    } else {
      document.body.classList.remove('is-fullscreen');
      if (document.fullscreenElement && document.exitFullscreen) {
        document.exitFullscreen().catch(() => {});
      }
    }
  }

  document.addEventListener('fullscreenchange', () => {
    if (!document.fullscreenElement) {
      document.body.classList.remove('is-fullscreen');
    } else {
      document.body.classList.add('is-fullscreen');
    }
  });

  // ==========================================
  // TOP HUD & DOCK HOVER REVEAL ENGINE
  // ==========================================
  let hudHideTimer = null;

  function showHud() {
    if (hudHideTimer) clearTimeout(hudHideTimer);
    if (presentationHud) presentationHud.classList.add('is-revealed');
  }

  function hideHud() {
    hudHideTimer = setTimeout(() => {
      if (presentationHud) presentationHud.classList.remove('is-revealed');
    }, 450);
  }

  if (hudHoverZone) {
    hudHoverZone.addEventListener('mouseenter', showHud);
    hudHoverZone.addEventListener('mouseleave', hideHud);
  }

  if (presentationHud) {
    presentationHud.addEventListener('mouseenter', showHud);
    presentationHud.addEventListener('mouseleave', hideHud);
  }

  if (dockHoverZone) {
    dockHoverZone.addEventListener('mouseenter', () => presentationDock && presentationDock.classList.add('is-revealed'));
    dockHoverZone.addEventListener('mouseleave', () => presentationDock && presentationDock.classList.remove('is-revealed'));
  }

  if (presentationDock) {
    presentationDock.addEventListener('mouseenter', () => presentationDock.classList.add('is-revealed'));
    presentationDock.addEventListener('mouseleave', () => presentationDock.classList.remove('is-revealed'));
  }

  // Window cursor position tracking for instant, fluid slide-in/out
  window.addEventListener('mousemove', (e) => {
    // Reveal top HUD when cursor is within top 55px
    if (e.clientY <= 55) {
      showHud();
    } else if (e.clientY > 85 && (!presentationHud || !presentationHud.matches(':hover'))) {
      hideHud();
    }

    // Reveal dock when cursor is within bottom 70px
    if (window.innerHeight - e.clientY <= 70) {
      if (presentationDock) presentationDock.classList.add('is-revealed');
    } else if (presentationDock && !presentationDock.matches(':hover')) {
      presentationDock.classList.remove('is-revealed');
    }
  });

  // ==========================================
  // EVENT LISTENERS & KEYBOARD BINDINGS
  // ==========================================
  prevBtn.addEventListener('click', prevSlide);
  nextBtn.addEventListener('click', nextSlide);

  if (notesToggleBtn) notesToggleBtn.addEventListener('click', toggleSpeakerNotes);
  if (notesCloseBtn) notesCloseBtn.addEventListener('click', closeSpeakerNotes);
  if (notesDrawerOverlay) notesDrawerOverlay.addEventListener('click', closeSpeakerNotes);

  if (gridToggleBtn) gridToggleBtn.addEventListener('click', toggleGridModal);
  if (gridCloseBtn) gridCloseBtn.addEventListener('click', closeGridModal);
  if (gridModalOverlay) {
    gridModalOverlay.addEventListener('click', (e) => {
      if (e.target === gridModalOverlay) closeGridModal();
    });
  }

  if (referencesBtn) referencesBtn.addEventListener('click', toggleReferencesModal);
  if (referencesCloseBtn) referencesCloseBtn.addEventListener('click', closeReferencesModal);
  if (referencesModalOverlay) {
    referencesModalOverlay.addEventListener('click', (e) => {
      if (e.target === referencesModalOverlay) closeReferencesModal();
    });
  }

  if (themeToggleBtn) themeToggleBtn.addEventListener('click', toggleTheme);
  if (fullscreenBtn) fullscreenBtn.addEventListener('click', toggleFullscreen);
  if (timerWidget) timerWidget.addEventListener('click', toggleTimer);

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    // If typing in an input or textarea (none currently, but good practice)
    if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;

    switch (e.key) {
      case 'ArrowRight':
      case 'PageDown':
      case ' ': // Spacebar
        e.preventDefault();
        nextSlide();
        break;

      case 'ArrowLeft':
      case 'PageUp':
        e.preventDefault();
        prevSlide();
        break;

      case 'Home':
        e.preventDefault();
        goToSlide(1);
        break;

      case 'End':
        e.preventDefault();
        goToSlide(totalSlides);
        break;

      case 's':
      case 'S':
        e.preventDefault();
        toggleSpeakerNotes();
        break;

      case 'g':
      case 'G':
        e.preventDefault();
        toggleGridModal();
        break;

      case 'r':
      case 'R':
        e.preventDefault();
        toggleReferencesModal();
        break;

      case 'f':
      case 'F':
        e.preventDefault();
        toggleFullscreen();
        break;

      case 'Escape':
        closeAllModals();
        break;

      default:
        break;
    }
  });

  // Touch Swipe gestures for tablets / touchscreen displays
  let touchStartX = 0;
  let touchStartY = 0;

  window.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
    touchStartY = e.changedTouches[0].screenY;
  }, { passive: true });

  window.addEventListener('touchend', (e) => {
    const touchEndX = e.changedTouches[0].screenX;
    const touchEndY = e.changedTouches[0].screenY;
    const diffX = touchEndX - touchStartX;
    const diffY = touchEndY - touchStartY;

    // Minimum swipe threshold 50px, horizontal dominant
    if (Math.abs(diffX) > 50 && Math.abs(diffX) > Math.abs(diffY)) {
      if (diffX < 0) {
        nextSlide();
      } else {
        prevSlide();
      }
    }
  }, { passive: true });

  // Handle URL Hash on load
  function checkInitialHash() {
    const hash = window.location.hash;
    if (hash && hash.startsWith('#slide-')) {
      const parsedNum = parseInt(hash.replace('#slide-', ''), 10);
      if (!isNaN(parsedNum) && parsedNum >= 1 && parsedNum <= totalSlides) {
        goToSlide(parsedNum);
        return;
      }
    }
    goToSlide(1);
  }

  // Fade out shortcut pill after 8 seconds
  setTimeout(() => {
    if (shortcutPill) {
      shortcutPill.style.opacity = '0';
    }
  }, 8000);

  // ==========================================
  // AMBIENT CONSTELLATION NODES ENGINE (Canvas)
  // ==========================================
  const nodesCanvas = document.getElementById('ambientNodesCanvas');
  if (nodesCanvas) {
    const ctx = nodesCanvas.getContext('2d');
    let width = (nodesCanvas.width = nodesCanvas.offsetWidth || window.innerWidth);
    let height = (nodesCanvas.height = nodesCanvas.offsetHeight || window.innerHeight);

    const NODE_COUNT = 24;
    const MAX_DISTANCE = 135;
    const nodes = [];

    function resizeCanvas() {
      if (!nodesCanvas) return;
      width = nodesCanvas.width = nodesCanvas.offsetWidth || window.innerWidth;
      height = nodesCanvas.height = nodesCanvas.offsetHeight || window.innerHeight;
    }

    window.addEventListener('resize', resizeCanvas);

    // Create subtle nodes
    for (let i = 0; i < NODE_COUNT; i++) {
      nodes.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.4,
        radius: Math.random() * 1.5 + 1.0
      });
    }

    function renderNodes() {
      ctx.clearRect(0, 0, width, height);

      const isDark = document.body.getAttribute('data-theme') !== 'light';
      const dotColor = isDark ? 'rgba(56, 189, 248, 0.35)' : 'rgba(2, 132, 199, 0.25)';
      const lineColorRgb = isDark ? '56, 189, 248' : '2, 132, 199';

      // Update and draw nodes
      for (let i = 0; i < nodes.length; i++) {
        const n = nodes[i];
        n.x += n.vx;
        n.y += n.vy;

        // Bounce gently at boundaries
        if (n.x < 0 || n.x > width) n.vx *= -1;
        if (n.y < 0 || n.y > height) n.vy *= -1;

        ctx.beginPath();
        ctx.arc(n.x, n.y, n.radius, 0, Math.PI * 2);
        ctx.fillStyle = dotColor;
        ctx.fill();

        // Connect nearby nodes
        for (let j = i + 1; j < nodes.length; j++) {
          const n2 = nodes[j];
          const dx = n.x - n2.x;
          const dy = n.y - n2.y;
          const dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < MAX_DISTANCE) {
            const alpha = (1 - dist / MAX_DISTANCE) * (isDark ? 0.12 : 0.08);
            ctx.beginPath();
            ctx.moveTo(n.x, n.y);
            ctx.lineTo(n2.x, n2.y);
            ctx.strokeStyle = `rgba(${lineColorRgb}, ${alpha})`;
            ctx.lineWidth = 1;
            ctx.stroke();
          }
        }
      }

      requestAnimationFrame(renderNodes);
    }

    // Start subtle animation loop
    renderNodes();
  }

  // Initialize
  initTheme();
  initTrackAndGrid();
  startTimer();
  checkInitialHash();
});
