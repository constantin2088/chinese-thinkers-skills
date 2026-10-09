#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
catalog=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))
records=catalog['skills']
assert catalog['maintainer']=='constantin2088', 'Unexpected maintainer'
assert catalog['homepage']=='https://github.com/constantin2088/chinese-thinkers-skills', 'Unexpected series URL'
for topic in catalog['topics']:
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',topic) and len(topic)<=50, topic
ids=[x['id'] for x in records]
assert len(ids)==len(set(ids)), 'Duplicate Skill ID'
for item in records:
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',item['id']), item['id']
    assert item['status'] in {'published','planned','archived'},item
    assert item.get('name_zh') and item.get('name_en') and item.get('focus'),item
    if item['status']=='published': assert item.get('repo')=='constantin2088/'+item['id'],item
for name in ('README.md','README.en.md','QUALITY_STANDARD.md','ROADMAP.md','assets/banner.svg'):
    assert (ROOT/name).exists(),name
print('OK:',len(records),'unique thinkers and essential files')
