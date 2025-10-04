import json
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data_file = ROOT / 'data' / 'generated_images.json'
with open(data_file, 'r', encoding='utf-8') as f:
    imgs = json.load(f)

# Map of target page bundles
targets = {
    'farm.png': [ROOT / 'content' / 'no' / 'gard', ROOT / 'content' / 'en' / 'farm'],
    'app.png': [ROOT / 'content' / 'no' / 'app', ROOT / 'content' / 'en' / 'app'],
}

for name, b64 in imgs.items():
    data = base64.b64decode(b64)
    for bundle in targets.get(name, []):
        bundle.mkdir(parents=True, exist_ok=True)
        out = bundle / name
        with open(out, 'wb') as f:
            f.write(data)
        print(f'Wrote {out}')
