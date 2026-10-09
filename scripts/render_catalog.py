"""Generate bilingual catalog blocks, leaving the rest of each README unchanged."""
import argparse,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
START='<!-- CATALOG:START -->';END='<!-- CATALOG:END -->'
def render(catalog,english=False):
    rows=[START,'| '+('Thinker | Focus | Repository | Status' if english else '人物 | 核心能力 | 项目 | 状态')+' |','|---|---|---|---|']
    for s in catalog['skills']:
        repo=s['id']
        if s['status']=='published':repo=f"[{s['id']}](https://github.com/{s['repo']})"
        state={'published':'Released' if english else '已发布','planned':'Planned' if english else '规划中','archived':'Archived' if english else '已归档'}[s['status']]
        rows.append(f"| **{s['name_en'] if english else s['name_zh']}** | {s['focus']} | {repo} | {state} |")
    rows.extend(['', 'Only published entries are installable.' if english else '只有“已发布”项目可安装；规划项目尚不可用。','', '```bash'])
    rows.extend('npx skills add '+s['repo'] for s in catalog['skills'] if s['status']=='published')
    rows.extend(['```',END])
    return '\n'.join(rows)
def update(text,new):
    if START in text:return re.sub(re.escape(START)+r'.*?'+re.escape(END),lambda _:new,text,flags=re.S)
    return re.sub(r'\| (人物|Thinker) \|.*?(?=\n## )',lambda _:new+'\n',text,count=1,flags=re.S)
def main():
    p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args()
    c=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))
    for name in ['README.md','README.en.md']:
        path=ROOT/name;old=path.read_text(encoding='utf-8');new=update(old,render(c,name.endswith('.en.md')))
        if a.check and new!=old:raise SystemExit(name+' generated catalog is stale')
        if not a.check:path.write_text(new,encoding='utf-8')
if __name__=='__main__':main()
