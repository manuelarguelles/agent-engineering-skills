import json
import tempfile
import unittest
from pathlib import Path
from new_project import create
class NewProjectTests(unittest.TestCase):
    def test_no_overwrite_existing_context(self):
        with tempfile.TemporaryDirectory() as d:
            dest=Path(d)/'work';dest.mkdir();(dest/'contexto.md').write_text('existing evidence')
            with self.assertRaises(FileExistsError):create('demo','documental',dest)
            self.assertEqual((dest/'contexto.md').read_text(),'existing evidence')
    def test_deterministic_does_not_gain_authority(self):
        with tempfile.TemporaryDirectory() as d:
            dest=create('nightly','determinista',Path(d)/'work')
            state=json.loads((dest/'invocation.json').read_text())
            self.assertIsNone(state['authorization_scope']);self.assertIsNone(state['cost']['value'])
            decisions=json.loads((dest/'decisiones.json').read_text())
            self.assertTrue(all(x['status']=='pending' and x['selected'] is None for x in decisions['decisions']))
    def test_invalid_kind_does_not_write(self):
        with tempfile.TemporaryDirectory() as d:
            dest=Path(d)/'work'
            with self.assertRaises(ValueError):create('demo','unknown',dest)
            self.assertFalse(dest.exists())
    def test_invalid_name_does_not_write(self):
        with tempfile.TemporaryDirectory() as d:
            dest=Path(d)/'work'
            with self.assertRaises(ValueError):create('../escape','documental',dest)
            self.assertFalse(dest.exists())
if __name__=='__main__':unittest.main()
