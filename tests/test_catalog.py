import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from render_catalog import render,update
class CatalogTests(unittest.TestCase):
    def test_publication_controls_install_links_and_preserves_editorial_text(self):
        c={'skills':[{'id':'one','name_zh':'甲','name_en':'One','focus':'F','status':'planned'}]}
        original='Intro\n\n| 人物 | 核心能力 | 项目 | 状态 |\nOld table\n\n## Other\nKeep me\n'
        planned=update(original,render(c))
        self.assertNotIn('npx skills add owner/one',planned)
        self.assertTrue(planned.startswith('Intro'));self.assertTrue(planned.endswith('## Other\nKeep me\n'))
        c['skills'][0].update(status='published',repo='owner/one')
        published=update(planned,render(c))
        self.assertIn('npx skills add owner/one',published)
        self.assertEqual(update(published,render(c)),published)
