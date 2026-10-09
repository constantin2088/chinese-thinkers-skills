import tempfile,unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from sync_series import replace_block,block,load_catalog
class SeriesTests(unittest.TestCase):
    def test_preserve_and_idempotent(self):
        c={'homepage':'https://example.test','skills':[{'id':'one','name_zh':'One','status':'published','repo':'owner/one'},{'id':'two','name_zh':'Two','status':'planned'}]}
        new=block(c,'three'); original='# Original\nKeep this section.\n'
        once=replace_block(original,new)
        self.assertTrue(once.endswith(original)); self.assertEqual(replace_block(once,new),once)
        self.assertNotIn('owner/two',once)
    def test_invalid_markers_rejected(self):
        with self.assertRaises(ValueError):replace_block('<!-- SERIES:START -->','x')
