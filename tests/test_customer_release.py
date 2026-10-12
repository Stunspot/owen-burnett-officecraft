"""Tiny synthetic product tests; never builds or seals the real candidate."""
import importlib.util,sys,tempfile,unittest,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import build_customer_release as builder
from verify_customer_release import verify


def fixture(root):
    root.mkdir()
    for n in builder.ROOT_FILES:(root/n).write_text('0.2.1\n'if n=='VERSION'else'# Synthetic fixture\n',encoding='utf-8')
    for n in builder.SOURCE_DIRS:(root/n).mkdir()
    for skill in builder.SKILLS:
        d=root/'codex'/skill;d.mkdir();(d/'SKILL.md').write_text('# Synthetic '+skill+'\n',encoding='utf-8')
    for n in ['archive_paths.py','verify_customer_release.py']:(root/'tools'/n).write_bytes((ROOT/'tools'/n).read_bytes())


class ReleaseTests(unittest.TestCase):
    def test_synthetic_success_channels_and_tamper(self):
        with tempfile.TemporaryDirectory()as temp:
            root=Path(temp)/'source';fixture(root);out=root/'candidate';builder.build(out,root)
            self.assertTrue(verify(out/'package')['valid'])
            archive=next(out.glob('*.zip'))
            with zipfile.ZipFile(archive)as z:self.assertIn('Owen-Burnett-Officecraft-v0.2.1/codex/officecraft-reviewer/SKILL.md',z.namelist())
            (out/'package/codex/officecraft-reviewer/SKILL.md').write_text('tamper',encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'bytes differ'):verify(out/'package')

    def test_existing_output_and_outside_source_are_preserved(self):
        with tempfile.TemporaryDirectory()as temp:
            root=Path(temp)/'source';fixture(root);out=root/'accepted';out.mkdir();old=out/'keep.txt';old.write_bytes(b'prior accepted bytes')
            for target in [out,Path(temp)/'outside',root/'codex/new-candidate']:
                with self.assertRaises(ValueError):builder.build(target,root)
            self.assertEqual(old.read_bytes(),b'prior accepted bytes');self.assertFalse((Path(temp)/'outside').exists());self.assertFalse((root/'codex/new-candidate').exists())

if __name__=='__main__':unittest.main()