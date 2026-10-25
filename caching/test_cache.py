import json
from pathlib import Path
import unittest

NOTEBOOK = Path(__file__).resolve().parents[1] / 'LLM_cost_Autopilot.ipynb'


def load():
    namespace = {}
    notebook = json.loads(NOTEBOOK.read_text())
    for cell in notebook['cells']:
        source = ''.join(cell['source'])
        if cell['cell_type'] != 'code':
            continue
        if source.startswith('def budget_remaining'):
            exec(source.split('\nllm_autopilot(')[0], namespace)
            break
        exec(source, namespace)
    return namespace


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.n = load()

    def test_repeat_skips_inference_and_spending(self):
        first = self.n['llm_autopilot']('What is Python?')
        spent = self.n['spent_this_session']
        def forbidden(*args):
            raise AssertionError('Cache hit called model')
        self.n['mock_llm'] = forbidden
        second = self.n['llm_autopilot']('What is Python?')
        self.assertEqual(first['response'], second['response'])
        self.assertTrue(second['cache_hit'])
        self.assertEqual(second['cost'], 0)
        self.assertEqual(self.n['spent_this_session'], spent)
        self.assertEqual(len(self.n['request_logs']), 2)

    def test_hit_allowed_after_budget_exhaustion(self):
        self.n['llm_autopilot']('What is Python?')
        self.n['SESSION_BUDGET'] = self.n['spent_this_session']
        self.assertTrue(self.n['llm_autopilot']('What is Python?')['cache_hit'])
        self.assertEqual(self.n['llm_autopilot']('New prompt')['status'], 'BLOCKED_BUDGET')

    def test_expiry(self):
        self.n['CACHE_TTL_SECONDS'] = 0
        self.n['llm_autopilot']('What is Python?')
        self.assertFalse(self.n['llm_autopilot']('What is Python?')['cache_hit'])

    def test_config_invalidation(self):
        self.n['llm_autopilot']('What is Python?')
        self.n['RESPONSE_CONFIG_VERSION'] = 'new'
        self.assertFalse(self.n['llm_autopilot']('What is Python?')['cache_hit'])

    def test_model_invalidation(self):
        self.n['llm_autopilot']('What is Python?')
        self.n['QUALITY_REQUIREMENTS']['low'] = 2
        self.assertFalse(self.n['llm_autopilot']('What is Python?')['cache_hit'])

    def test_bound_and_lru(self):
        self.n['CACHE_MAX_ENTRIES'] = 2
        for prompt in ['A', 'B', 'A', 'C']:
            self.n['llm_autopilot'](prompt)
        self.assertEqual(len(self.n['response_cache']), 2)
        self.assertTrue(self.n['llm_autopilot']('A')['cache_hit'])
        self.assertFalse(self.n['llm_autopilot']('B')['cache_hit'])

    def test_disabled_and_exact_matching(self):
        self.n['llm_autopilot']('Hello')
        self.assertFalse(self.n['llm_autopilot']('hello')['cache_hit'])
        self.assertFalse(self.n['llm_autopilot']('Hello', use_cache=False)['cache_hit'])

    def test_failure_not_cached_or_charged(self):
        def failing(*args):
            raise RuntimeError('Provider failed')
        self.n['mock_llm'] = failing
        with self.assertRaises(RuntimeError):
            self.n['llm_autopilot']('Hello')
        self.assertEqual(self.n['spent_this_session'], 0)
        self.assertEqual(len(self.n['response_cache']), 0)
        self.assertEqual(self.n['request_logs'][-1]['status'], 'ERROR')


if __name__ == '__main__':
    unittest.main()
