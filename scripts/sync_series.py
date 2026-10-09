#!/usr/bin/env python3
"""Generate series links from the canonical catalog. Only managed README blocks change."""
import argparse, json, re, subprocess
from pathlib import Path
from urllib.request import urlopen

CATALOG_URL='https://raw.githubusercontent.com/constantin2088/chinese-thinkers-skills/main/catalog/skills.json'
START='<!-- SERIES:START -->'
END='<!-- SERIES:END -->'
def load_catalog(path=None):
    if path:return json.loads(Path(path).read_text(encoding='utf-8'))
    with urlopen(CATALOG_URL,timeout=30) as response:return json.load(response)
def block(catalog,slug):
    lines=[START,'> **属于 [Chinese Thinkers as Skills 系列]('+catalog['homepage']+')** · [完整作品目录]('+catalog['homepage']+'#作品目录)']
    published=[s for s in catalog['skills'] if s['status']=='published' and s['id']!=slug]
    if published:lines+=['','**相关推荐**：'+' · '.join('['+s['name_zh']+'](https://github.com/'+s['repo']+')' for s in published)]
    lines+=['', '> 系列入口与推荐由总仓库 catalog/skills.json 生成。',END]
    return '\n'.join(lines)
def replace_block(text,new):
    if text.count(START)!=text.count(END) or text.count(START)>1:raise ValueError('Malformed series markers')
    if START in text:return re.sub(re.escape(START)+r'.*?'+re.escape(END),lambda _:new,text,flags=re.S)
    return new+'\n\n'+text
def sync_readme(root,catalog,slug,check=False):
    path=Path(root)/'README.md'
    old=path.read_text(encoding='utf-8');new=replace_block(old,block(catalog,slug))
    if check and old!=new:raise ValueError('Series block is stale')
    if not check:path.write_text(new,encoding='utf-8')
    return old!=new
def metadata(catalog,slug,apply=False):
    repo='constantin2088/'+slug
    item=next((s for s in catalog['skills'] if s['id']==slug),None)
    if slug=='chinese-thinkers-skills':description=catalog['description']
    elif item:repo=item.get('repo',repo);description=item['name_zh']+'：'+item['focus']+'。Chinese Thinkers as Skills 系列。'
    else:description='Chinese Thinkers as Skills 官方开发模板：证据、工作流、示例、评测与系列关联自动生成。'
    topics=list(dict.fromkeys(catalog['topics']+(item.get('topics',[]) if item else ['skill-development'])))
    # Merge extra topics instead of replacing unrelated existing metadata.
    if apply:
        existing=json.loads(subprocess.check_output(['gh','api','repos/'+repo+'/topics'],text=True))['names']
        topics=list(dict.fromkeys(topics+existing))
        if len(topics)>20:raise ValueError('GitHub allows at most 20 topics; review existing topics')
    payload={'description':description,'homepage':catalog['homepage']}
    print(json.dumps({'repo':repo,**payload,'topics':topics},ensure_ascii=False))
    if apply:
        subprocess.run(['gh','api','--method','PATCH','repos/'+repo,'--input','-'],input=json.dumps(payload),text=True,stdout=subprocess.DEVNULL,check=True)
        subprocess.run(['gh','api','--method','PUT','repos/'+repo+'/topics','--input','-'],input=json.dumps({'names':topics}),text=True,stdout=subprocess.DEVNULL,check=True)
def main():
    p=argparse.ArgumentParser();p.add_argument('--catalog');p.add_argument('--snapshot');p.add_argument('--root',default='.');p.add_argument('--slug',required=True);p.add_argument('--check',action='store_true');p.add_argument('--metadata',action='store_true');p.add_argument('--apply',action='store_true');a=p.parse_args()
    catalog=load_catalog(a.catalog)
    if a.snapshot:Path(a.snapshot).write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if a.metadata:metadata(catalog,a.slug,a.apply)
    else:sync_readme(a.root,catalog,a.slug,a.check)
if __name__=='__main__':main()
