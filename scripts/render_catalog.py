"""Render discovery paths, featured skills and a compact complete bilingual index."""
import argparse,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
START='<!-- CATALOG:START -->';END='<!-- CATALOG:END -->'
def name(s,en):return s['name_en'] if en else s['name_zh']
def focus(s,en):return s.get('focus_en',s['focus']) if en else s['focus']
def picks(c,key,limit=3):
 items=[s for s in c['skills'] if s['status']=='published' and s.get('discovery_path')==key]
 return sorted(items,key=lambda s:s.get('discovery_rank',100000))[:limit]
def render(catalog,english=False):
 rows=[START];en=english
 paths=catalog.get('discovery_paths',[])
 if paths:
  rows+=['### '+('Choose by the problem' if en else '按问题选方法'),'','| '+('Your task | Start here' if en else '你遇到的问题 | 先试这些方法')+' |','|---|---|']
  for p in paths:
   links=' · '.join('['+name(s,en)+'](https://github.com/'+s['repo']+')' for s in picks(catalog,p['id']))
   rows.append('| ['+p['question_en' if en else 'question_zh']+'](docs/choose-a-skill.md#'+p['id']+') | '+links+' |')
  rows+=['','[Explore every skill by task](docs/choose-a-skill.md) · [Search the catalog](docs/installation.md#find-a-method)' if en else '[查看六类场景的全部方法](docs/choose-a-skill.md) · [按关键词找方法](docs/installation.md#find-a-method)','']
 featured=sorted((s for s in catalog['skills'] if s['status']=='published' and s.get('discovery_rank')),key=lambda s:s['discovery_rank'])
 if featured:
  rows+=['### '+('Start with a familiar task' if en else '从熟悉的问题开始'),'','| '+('Thinker | What you can do' if en else '人物入口 | 可以完成什么')+' |','|---|---|']
  for s in featured:rows.append('| ['+name(s,en)+'](https://github.com/'+s['repo']+') | '+focus(s,en)+' |')
  rows+=['','### '+('Full catalog' if en else '完整目录'),'']
 if paths:rows+=['<details>','<summary>'+('All '+str(len(catalog['skills']))+' thinkers' if en else '展开全部'+str(len(catalog['skills']))+'位人物')+'</summary>','']
 rows+=['| '+('Thinker | Focus | Repository | Status' if en else '人物 | 核心能力 | 项目 | 状态')+' |','|---|---|---|---|']
 for s in catalog['skills']:
  repo='['+s['id']+'](https://github.com/'+s['repo']+')' if s['status']=='published' else s['id']
  state={'published':'Published' if en else '已发布','planned':'Planned' if en else '规划中','archived':'Archived' if en else '已归档'}[s['status']]
  rows.append('| **'+name(s,en)+'** | '+focus(s,en)+' | '+repo+' | '+state+' |')
 if paths:rows+=['','</details>','','<details>','<summary>'+('Individual install commands' if en else '展开逐个人物安装命令')+'</summary>','']
 rows+=['','Only published entries are installable.' if en else '选择一个已发布的方法安装即可。','', '```bash']
 rows+=['npx skills add '+s['repo'] for s in catalog['skills'] if s['status']=='published']
 rows+=['```']
 if paths:rows+=['','</details>']
 rows+=[END];return '\n'.join(rows)
def guide(c):
 rows=['# 按问题选择 Skill / Choose a method','','先选眼前的问题，再选人物。下列分组和全部链接由唯一目录生成；推荐只表示编辑入口。','','[返回系列首页](../README.md) · [安装说明](installation.md)','']
 for p in c.get('discovery_paths',[]):
  rows+=['<a id="'+p['id']+'"></a>','','## '+p['name_zh']+' / '+p['name_en'],'',p['question_zh']+' '+p['question_en'],'','| 人物 / Thinker | 适用问题 / Task |','|---|---|']
  for s in c['skills']:
   if s['status']=='published' and s.get('discovery_path')==p['id']:
    rows+=['| ['+s['name_zh']+' / '+s['name_en']+'](https://github.com/'+s['repo']+') | '+s['focus']+'<br>'+s.get('focus_en','')+' |']
  rows+=['']
 rows+=['选择后阅读人物仓库的例子、资料卡与边界。历史资料与现代工作流的归属分别标注，客户端模型评测状态另行报告。','']
 return '\n'.join(rows)
def update(text,new):
 if START in text:
  if text.count(START)!=1 or text.count(END)!=1:raise ValueError('Malformed catalog markers')
  return re.sub(re.escape(START)+r'.*?'+re.escape(END),lambda _:new,text,flags=re.S)
 return re.sub(r'\| (人物|Thinker) \|.*?(?=\n## )',lambda _:new+'\n',text,count=1,flags=re.S)
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args()
 c=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))
 targets={'README.md':None,'README.en.md':None,'docs/choose-a-skill.md':guide(c)}
 for file,generated in targets.items():
  path=ROOT/file;old=path.read_text(encoding='utf-8') if path.exists() else ''
  new=generated if generated is not None else update(old,render(c,file.endswith('.en.md')))
  if a.check and new!=old:raise SystemExit(file+' generated discovery guide is stale')
  if not a.check:path.write_text(new,encoding='utf-8')
if __name__=='__main__':main()
