#!/usr/bin/env python3
from pathlib import Path
import re

CONTENT_DIR = Path('content')
DEFAULT_IMAGE = '/images/hero.svg'

def process_file(p: Path):
    txt = p.read_text(encoding='utf-8')
    if txt.lstrip().startswith('---'):
        # find frontmatter block
        m = re.match(r'^(---\s*\n)(.*?\n)(---\s*\n)(.*)$', txt, re.S)
        if not m:
            # fallback: more general search
            parts = txt.split('---')
            if len(parts) >= 3:
                fm = parts[1]
                rest = '---'.join(parts[2:])
                fm_lines = fm.splitlines()
            else:
                return False
        else:
            fm = m.group(2)
            rest = m.group(4)
            fm_lines = fm.splitlines()

        keys = {line.split(':',1)[0].strip() for line in fm_lines if ':' in line}
        changed = False
        insert_lines = []
        if 'description' not in keys:
            insert_lines.append('description: ""')
            changed = True
        if 'image' not in keys:
            insert_lines.append(f'image: "{DEFAULT_IMAGE}"')
            changed = True

        if changed:
            # Append before end of frontmatter
            new_fm = fm.rstrip('\n') + '\n' + '\n'.join(insert_lines) + '\n'
            new_txt = '---\n' + new_fm + '---\n' + rest
            p.write_text(new_txt, encoding='utf-8')
            print(f'Patched frontmatter for {p}')
            return True
        return False
    else:
        # No frontmatter, create one
        title = p.stem.replace('-', ' ').replace('_', ' ').title()
        new_fm = f"---\n# auto-added frontmatter\ntitle: \"{title}\"\ndescription: \"\"\nimage: \"{DEFAULT_IMAGE}\"\n---\n\n"
        new_txt = new_fm + txt
        p.write_text(new_txt, encoding='utf-8')
        print(f'Added frontmatter to {p}')
        return True

def main():
    patched = []
    for p in CONTENT_DIR.rglob('*.md'):
        if 'README' in p.name:
            continue
        if process_file(p):
            patched.append(str(p))
    print(f'Total patched: {len(patched)}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
