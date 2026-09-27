import base64
import os

def build_deck_data():
    print("Encoding PPTX files to base64...")
    with open('stakeholder_engagement_light.pptx', 'rb') as f:
        light_b64 = base64.b64encode(f.read()).decode('ascii')
    print(f"Light deck encoded: {len(light_b64)} chars")

    with open('stakeholder_engagement_dark.pptx', 'rb') as f:
        dark_b64 = base64.b64encode(f.read()).decode('ascii')
    print(f"Dark deck encoded: {len(dark_b64)} chars")

    with open('deck_data.js', 'w', encoding='utf-8') as f:
        f.write('// Auto-generated presentation deck binaries (Base64 encoded for offline file:// protocol download)\n')
        f.write('window.__DECK_DATA__ = {\n')
        f.write('  light: "' + light_b64 + '",\n')
        f.write('  dark: "' + dark_b64 + '"\n')
        f.write('};\n')

    size_mb = os.path.getsize('deck_data.js') / (1024 * 1024)
    print(f"deck_data.js created successfully! File size: {size_mb:.2f} MB")

if __name__ == '__main__':
    build_deck_data()
