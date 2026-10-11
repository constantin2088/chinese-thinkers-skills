"""Find a published method in the local canonical catalog; never installs anything."""
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def find(catalog,query,limit=10):
 terms=query.casefold().split()
 if not terms:return []
 hits=[]
 for i,s in enumerate(catalog['skills']):
  if s['status']!='published':continue
  text=' '.join(str(s.get(k,'')) for k in ('id','name_zh','name_en','focus','focus_en','category','discovery_path')).casefold()
  score=sum(1 for t in terms if t in text)
  if score:hits.append((score,i,s))
 hits.sort(key=lambda x:(-x[0],x[1]));return [s for _,_,s in hits[:limit]]
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('query');p.add_argument('--limit',type=int,default=10);a=p.parse_args()
 if a.limit<1 or a.limit>100:p.error('--limit must be between 1 and 100')
 c=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))
 rows=find(c,a.query,a.limit)
 if not rows:print('没有匹配；试试人物中英文名、关键任务，或参阅 docs/choose-a-skill.md。');return
 for s in rows:
  print(s['name_zh']+' / '+s['name_en']+' — '+s['focus'])
  print('https://github.com/'+s['repo']);print('npx skills add '+s['repo']);print()
if __name__=='__main__':main()
