#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
records=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))['skills']
ids=[x['id'] for x in records]
assert len(ids)==len(set(ids)), 'Duplicate Skill ID'
for item in records:
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',item['id']), item['id']
    assert item['status'] in {'published','planned','archived'},item
    if item['status']=='published': assert item.get('repo'),item
for name in ('README.md','README.en.md','QUALITY_STANDARD.md','ROADMAP.md','assets/banner.svg'):
    assert (ROOT/name).exists(),name
print('OK:',len(records),'unique thinkers and essential files')
