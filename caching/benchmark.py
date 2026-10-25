"""Run from any directory; measures simulated inference, not provider performance."""
import contextlib
import io
import json
from pathlib import Path
import time
from test_cache import load


def benchmark():
    results = []
    for label, prompts in [('repeated', ['What is Python?', 'Explain caching.', 'Design an architecture.'] * 8),
                           ('unique', [f'What is item {i}?' for i in range(24)])]:
        responses = []
        for enabled in (False, True):
            with contextlib.redirect_stdout(io.StringIO()):
                n = load()
            start = time.perf_counter()
            replies = [n['llm_autopilot'](p, use_cache=enabled) for p in prompts]
            elapsed = (time.perf_counter() - start) * 1000
            responses.append([r['response'] for r in replies])
            results.append(dict(workload=label, cache_enabled=enabled, requests=len(prompts),
                                model_calls=sum(not r['cache_hit'] for r in replies),
                                cache_hits=sum(r['cache_hit'] for r in replies),
                                elapsed_ms=round(elapsed, 3),
                                estimated_cost=n['spent_this_session']))
        assert responses[0] == responses[1], 'Cached responses changed'
    return results


if __name__ == '__main__':
    result = {'scope': 'Single-run benchmark of mock_llm; costs are estimates, not actual charges.',
              'results': benchmark()}
    Path(__file__).with_name('benchmark_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
