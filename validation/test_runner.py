"""Exercise CLI exit codes using real notebooks in isolated temporary repos."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


class RunnerTests(unittest.TestCase):
    def run_notebook(self, source=None, malformed=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            validation = root / 'validation'
            validation.mkdir()
            runner = validation / 'run_notebooks.py'
            shutil.copyfile(Path(__file__).with_name('run_notebooks.py'), runner)
            if malformed:
                (root / 'example.ipynb').write_text('not JSON')
            elif source is not None:
                notebook = dict(nbformat=4, nbformat_minor=5, metadata={}, cells=[
                    dict(id='example', cell_type='code', metadata={}, execution_count=None,
                         outputs=[], source=source)])
                (root / 'example.ipynb').write_text(json.dumps(notebook))
            result = subprocess.run([sys.executable, str(runner)], capture_output=True,
                                    text=True, timeout=210)
            summary = validation / 'runs' / 'summary.json'
            return result, json.loads(summary.read_text())

    def test_success_exits_zero(self):
        result, summary = self.run_notebook('assert 2 + 2 == 4')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(summary[0]['status'], 'PASS')

    def test_cell_failure_exits_nonzero(self):
        result, summary = self.run_notebook('raise ValueError("expected failure")')
        self.assertEqual(summary[0]['status'], 'FAIL')
        self.assertEqual(result.returncode, 1, result.stderr)

    def test_startup_failure_exits_nonzero(self):
        result, summary = self.run_notebook(malformed=True)
        self.assertEqual(summary[0]['status'], 'FAIL')
        self.assertEqual(result.returncode, 1, result.stderr)

    def test_empty_suite_exits_nonzero(self):
        result, summary = self.run_notebook()
        self.assertEqual(summary, [])
        self.assertEqual(result.returncode, 1, result.stderr)


if __name__ == '__main__':
    unittest.main()
