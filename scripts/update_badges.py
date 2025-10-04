#!/usr/bin/env python3
"""
Parse doc/implementation-plan.md and update README.md badges with counts and project status.

Behavior:
- Counts numbered tasks under sections '## P0', '## P1', '## P2'.
- A task is considered done if its text or the following 3 lines contain '[x]' or the word 'done' (case-insensitive).
- Updates the README badges block between '<!-- Status badges -->' and the next blank line.
"""
import re
from pathlib import Path


def parse_tasks(md_text: str):
    # Split into sections P0/P1/P2
    sections = {}
    current = None
    lines = md_text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r'^##\s+P(\d)\b', line)
        if m:
            current = 'P' + m.group(1)
            sections.setdefault(current, [])
            continue
        if current is None:
            continue
        # Match numbered task lines like '1) Task...' or '1.'
        if re.match(r'^\s*\d+\)', line) or re.match(r'^\s*\d+\.', line):
            sections[current].append((i, line.strip()))
    return sections, lines


def is_task_done(start_idx, lines):
    # Check up to the next 3 lines for markers
    text = lines[start_idx]
    window = lines[start_idx:start_idx+4]
    block = '\n'.join(window).lower()
    if '[x]' in block or 'done' in block:
        return True
    return False


def compute_counts(sections, lines):
    counts = {}
    total = 0
    done = 0
    for sec, tasks in sections.items():
        sec_total = len(tasks)
        sec_done = 0
        for idx, taskline in tasks:
            if is_task_done(idx, lines):
                sec_done += 1
        counts[sec] = {'total': sec_total, 'done': sec_done}
        total += sec_total
        done += sec_done
    return counts, total, done


def project_status(done, total):
    pct = int(round((done/total*100))) if total>0 else 0
    if pct >= 95:
        return 'Complete', 'brightgreen'
    if pct >= 70:
        return 'Nearly Done', 'green'
    if pct >= 40:
        return 'In Progress', 'yellow'
    return 'Early', 'red'


def make_badge_lines(counts, total, done):
    remaining = total - done
    status_label, color = project_status(done, total)

    implemented_badge = f"![Implemented](https://img.shields.io/badge/implemented-{done}%2F{total}-blue)"
    remaining_badge = f"![Remaining](https://img.shields.io/badge/remaining-{remaining}-orange)"
    status_badge = f"![Project Status](https://img.shields.io/badge/status-{status_label.replace(' ','%20')}-{color})"
    # Keep existing badges for CI/deploy/pages/last-commit/dependabot
    ci_badge = f"[![CI](https://img.shields.io/github/actions/workflow/status/xvenca/wenzl/.github/workflows/ci.yml?branch=main)](https://github.com/xvenca/wenzl/actions/workflows/ci.yml)"
    deploy_badge = f"[![Deploy](https://img.shields.io/github/actions/workflow/status/xvenca/wenzl/.github/workflows/deploy.yml?branch=main)](https://github.com/xvenca/wenzl/actions/workflows/deploy.yml)"
    pages_badge = f"[![Pages Status](https://img.shields.io/website?down_color=red&down_message=down&up_color=green&up_message=up&url=https://xvenca.github.io/wenzl/)](https://xvenca.github.io/wenzl/)"
    last_commit = f"[![Last Commit](https://img.shields.io/github/last-commit/xvenca/wenzl)](https://github.com/xvenca/wenzl/commits/main)"
    dependabot = f"[![Dependabot](https://img.shields.io/badge/dependabot-enabled-brightgreen)](https://github.com/xvenca/wenzl/security/dependabot)"

    lines = [
        '<!-- Status badges -->',
        ci_badge,
        deploy_badge,
        pages_badge,
        last_commit,
        dependabot,
        '',
        implemented_badge,
        remaining_badge,
        status_badge,
        '',
        f"[Plan details](doc/implementation-plan.md)"
    ]
    return '\n'.join(lines) + '\n'


def update_readme(badges_block_text):
    readme = Path('README.md')
    txt = readme.read_text(encoding='utf-8')
    if '<!-- Status badges -->' in txt:
        # Replace block from marker to next blank line after marker set
        start = txt.index('<!-- Status badges -->')
        # find next heading or two consecutive newlines after start
        rest = txt[start:]
        # find where the badges block ends: look for two newlines followed by '# ' (next header) or end of badges we inserted earlier
        # Simpler: replace until the first occurrence of '\n\n' after the marker plus 10 lines; but safer: find the marker and replace the following lines up to the first two newlines in a row plus next line not an image or link.
        # We'll locate the line after the marker block by searching for '\n\n' after start and treat that as end
        # However to be robust, replace the entire previously inserted sequence between marker and the next header '##' or first blank line followed by non-badge content.
        pattern = re.compile(r'<!-- Status badges -->.*?\n\n', re.S)
        if pattern.search(txt):
            new_txt = pattern.sub(badges_block_text + '\n', txt)
        else:
            # fallback: insert badges after the title line
            parts = txt.splitlines()
            parts.insert(1, badges_block_text)
            new_txt = '\n'.join(parts)
    else:
        # Prepend badges at top
        new_txt = badges_block_text + '\n' + Path('README.md').read_text(encoding='utf-8')
    readme.write_text(new_txt, encoding='utf-8')


def main():
    md = Path('doc/implementation-plan.md')
    if not md.exists():
        print('No implementation plan found.')
        return 1
    text = md.read_text(encoding='utf-8')
    sections, lines = parse_tasks(text)
    counts, total, done = compute_counts(sections, lines)
    badges = make_badge_lines(counts, total, done)
    update_readme(badges)
    print(f'Updated README badges: {done}/{total} done')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
