#!/usr/bin/env python3
"""
Simple CI check: validate SKILL.md frontmatter contains display_name and examples paths exist.
Run from repo root: python scripts/ci/validate_skills.py
"""
import os
import sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def find_skill_files(root):
    skills = []
    for dirpath, dirs, files in os.walk(os.path.join(root, 'skills')):
        if 'SKILL.md' in files:
            skills.append(os.path.join(dirpath, 'SKILL.md'))
    return skills

def parse_frontmatter_simple(path):
    fm = {}
    with open(path, 'r', encoding='utf-8') as f:
        in_fm = False
        current_key = None
        for line in f:
            if line.strip() == '---':
                if not in_fm:
                    in_fm = True
                    continue
                else:
                    break
            if in_fm:
                if ':' in line and not line.strip().startswith('-'):
                    key, val = line.split(':', 1)
                    key = key.strip()
                    val = val.strip().strip('"')
                    current_key = key
                    if key == 'examples':
                        fm['examples'] = []
                    else:
                        fm[key] = val
                elif line.strip().startswith('-') and current_key == 'examples':
                    item = line.strip().lstrip('-').strip().strip('"')
                    fm['examples'].append(item)
    return fm

def main():
    skills = find_skill_files(ROOT)
    failed = False
    for s in skills:
        fm = parse_frontmatter_simple(s)
        rel = os.path.relpath(s, ROOT)
        print(f'Checking {rel}...')
        if 'display_name' not in fm:
            print(f'  ERROR: missing display_name in {rel}')
            failed = True
        if 'examples' in fm:
            for ex in fm['examples']:
                ex_path = os.path.join(os.path.dirname(s), ex)
                if not os.path.exists(ex_path):
                    print(f'  ERROR: example file not found: {ex} (from {rel})')
                    failed = True
    if failed:
        print('\nValidation failed')
        sys.exit(2)
    print('\nAll SKILL.md files passed basic validation')

if __name__ == '__main__':
    main()
