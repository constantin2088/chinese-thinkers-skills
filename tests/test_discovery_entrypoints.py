import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from render_catalog import render

class DiscoveryEntryPoints(unittest.TestCase):
 def item(self,name,rank=None,status='published'):
  r=dict(id=name,name_zh=name+'中文',name_en=name,focus='一个具体任务',repo='constantin2088/'+name,status=status)
  if rank is not None:r['discovery_rank']=rank
  return r
 def test_featured_order_uses_catalog_and_keeps_complete_list(self):
  text=render(dict(skills=[self.item('later',2),self.item('first',1),self.item('ordinary')]))
  feature=text.split('### 完整目录')[0]
  self.assertLess(feature.index('first中文'),feature.index('later中文'))
  self.assertNotIn('ordinary中文',feature)
  self.assertIn('ordinary中文',text)
 def test_planned_item_has_no_install_or_feature_entry(self):
  text=render(dict(skills=[self.item('draft',1,'planned'),self.item('ready',2)]),True)
  self.assertNotIn('draft',text.split('### Full catalog')[0])
  self.assertNotIn('npx skills add constantin2088/draft',text)
  self.assertIn('npx skills add constantin2088/ready',text)
 def test_old_catalog_remains_supported(self):
  self.assertNotIn('### 完整目录',render(dict(skills=[self.item('old')])) )

if __name__=='__main__':unittest.main()
