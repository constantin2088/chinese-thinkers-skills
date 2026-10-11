"""Owner-authenticated metadata/links synchronization; defaults to preview."""
import argparse,json,subprocess,tempfile,hashlib
from pathlib import Path
from sync_series import metadata,sync_readme
ROOT=Path(__file__).resolve().parents[1]
def run(*args,**kwargs):return subprocess.run(list(args),check=True,**kwargs)
# Previous canonical renderer, checked across the published series before this update.
KNOWN_SHARED={'f8730d8e2314e03df1c9426fc3b061ea6a72e31dc9482238e8aba4399432a151'}
def sync_shared(root,source,known_previous=KNOWN_SHARED):
    root=Path(root);files=['scripts/sync_series.py']
    if (root/'templates/scripts/sync_series.py.tmpl').exists():files.append('templates/scripts/sync_series.py.tmpl')
    # Inspect every target before writing any: custom edits must be preserved.
    for rel in files:
        actual=(root/rel).read_text(encoding='utf-8')
        if actual!=source and hashlib.sha256(actual.encode('utf-8')).hexdigest() not in known_previous:
            raise ValueError('Unexpected shared renderer edits: '+str(root/rel))
    for rel in files:(root/rel).write_text(source,encoding='utf-8')
    return files

def main():
    p=argparse.ArgumentParser();p.add_argument('--apply',action='store_true');a=p.parse_args()
    c=json.loads((ROOT/'catalog/skills.json').read_text(encoding='utf-8'))
    if c['maintainer']!='constantin2088':raise ValueError('Unexpected owner')
    repos=[s['repo'] for s in c['skills'] if s['status']=='published']+['constantin2088/thinkers-skill-template']
    for repo in repos:
        if not repo.startswith('constantin2088/') or repo.count('/')!=1:raise ValueError('Unexpected repo')
    metadata(c,'chinese-thinkers-skills',a.apply)
    for repo in repos:
        slug=repo.split('/')[1];metadata(c,slug,a.apply)
        if not a.apply:continue
        with tempfile.TemporaryDirectory() as tmp:
            checkout=Path(tmp)/slug
            run('git','clone','--depth','1','https://github.com/'+repo+'.git',str(checkout))
            files=sync_shared(checkout,(ROOT/'scripts/sync_series.py').read_text(encoding='utf-8'))
            sync_readme(checkout,c,slug)
            files.append('README.md')
            if slug=='thinkers-skill-template':
                path=checkout/'templates/series-catalog.json.tmpl'
                path.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');files.append(str(path.relative_to(checkout)))
            run('git','add',*files,cwd=checkout)
            changed=subprocess.run(['git','diff','--cached','--quiet'],cwd=checkout)
            if changed.returncode==1:
                run('git','-c','user.name=constantin2088','-c','user.email=314848087+constantin2088@users.noreply.github.com','commit','-m','Sync series links from canonical catalog',cwd=checkout)
                run('git','push',cwd=checkout)
            elif changed.returncode!=0:raise RuntimeError('Cannot inspect changes')
if __name__=='__main__':main()
