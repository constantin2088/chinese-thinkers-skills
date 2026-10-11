import hashlib,json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from sync_series import block,related,replace_block
from render_catalog import render,guide
from find_skill import find
from publish_series import sync_shared
class DiscoveryQualityTests(unittest.TestCase):
 def catalog(self):
  return {'homepage':'https://example.test','discovery_paths':[dict(id='learning',name_zh='学习',name_en='Learning',question_zh='怎么学',question_en='How to learn')], 'skills':[dict(id='one',name_zh='甲',name_en='One',status='published',repo='owner/one',focus='行动',focus_en='Action',discovery_path='learning'),dict(id='two',name_zh='乙',name_en='Two',status='published',repo='owner/two',focus='学习',focus_en='Learning',discovery_path='learning',discovery_rank=1),dict(id='three',name_zh='丙',name_en='Three',status='published',repo='owner/three',focus='练习',focus_en='Practice',discovery_path='learning'),dict(id='draft',name_zh='草案',name_en='Draft',status='planned',focus='学习',focus_en='Learning',discovery_path='learning')]}
 def test_related_excludes_self_and_drafts_and_prioritizes_editorial_rank(self):
  self.assertEqual([x['id'] for x in related(self.catalog(),'one')],['two','three'])
  self.assertEqual(related(self.catalog(),'unknown'),[])
 def test_related_is_visible_and_full_list_remains_collapsed(self):
  text=block(self.catalog(),'one')
  self.assertIn('适合处理',text)
  self.assertIn('owner/two',text.split('<details>')[0])
  self.assertIn('<summary>相关推荐（2个作品）</summary>',text)
  self.assertNotIn('owner/one',text);self.assertNotIn('owner/draft',text)
 def test_full_index_and_commands_remain_available_in_compact_layout(self):
  text=render(self.catalog())
  self.assertIn('<summary>展开全部4位人物</summary>',text)
  self.assertIn('npx skills add owner/one',text)
  self.assertNotIn('npx skills add owner/draft',text)
  self.assertIn('docs/choose-a-skill.md#learning',text)
 def test_english_task_field_is_used(self):
  text=render(self.catalog(),True)
  self.assertIn('Learning',text);self.assertNotIn('学习',text)
 def test_task_guide_keeps_all_published_items_and_stable_anchor(self):
  text=guide(self.catalog())
  self.assertIn('<a id="learning"></a>',text)
  for slug in ('one','two','three'):self.assertIn('owner/'+slug,text)
  self.assertNotIn('owner/draft',text)
 def test_keyword_search_is_bilingual_and_never_returns_drafts(self):
  self.assertEqual([x['id'] for x in find(self.catalog(),'学习')],['two'])
  self.assertEqual([x['id'] for x in find(self.catalog(),'practice')],['three'])
  self.assertEqual(find(self.catalog(),'不存在'),[]);self.assertEqual(find(self.catalog(),''),[])
 def test_shared_update_rejects_unknown_content_before_any_write(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);(root/'scripts').mkdir();(root/'templates/scripts').mkdir(parents=True)
   (root/'scripts/sync_series.py').write_text('known',encoding='utf-8')
   (root/'templates/scripts/sync_series.py.tmpl').write_text('custom',encoding='utf-8')
   known={hashlib.sha256(b'known').hexdigest()}
   with self.assertRaises(ValueError):sync_shared(root,'new',known)
   self.assertEqual((root/'scripts/sync_series.py').read_text(),'known')
   self.assertEqual((root/'templates/scripts/sync_series.py.tmpl').read_text(),'custom')
 def test_shared_update_accepts_known_version_and_is_idempotent(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);(root/'scripts').mkdir();p=root/'scripts/sync_series.py';p.write_text('known',encoding='utf-8')
   self.assertEqual(sync_shared(root,'new',{hashlib.sha256(b'known').hexdigest()}),['scripts/sync_series.py'])
   self.assertEqual(sync_shared(root,'new',set()),['scripts/sync_series.py']);self.assertEqual(p.read_text(),'new')
 def test_real_catalog_has_unique_paths_and_every_person_is_classified(self):
  c=json.loads((Path(__file__).resolve().parents[1]/'catalog/skills.json').read_text(encoding='utf-8'))
  paths={p['id'] for p in c['discovery_paths']}
  self.assertEqual(len(paths),6)
  for s in c['skills']:
   self.assertIn(s['discovery_path'],paths);self.assertTrue(s['focus_en'])
   self.assertLessEqual(len(related(c,s['id'])),3)
   self.assertNotIn(s['id'],[x['id'] for x in related(c,s['id'])])
if __name__=='__main__':unittest.main()
