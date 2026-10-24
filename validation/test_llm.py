import ast
import json
from pathlib import Path
import unittest
import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
ROOT = Path(__file__).resolve().parents[1]

def cells(name):
    return [c['source'] if isinstance(c['source'], str) else ''.join(c['source']) for c in json.loads((ROOT / name).read_text())['cells']]

def evaluator():
    tree = ast.parse('\n'.join(cells('LLM_Eval_Regression_Testing_Framework.ipynb')))
    nodes = [n for n in tree.body if (isinstance(n, ast.FunctionDef) and n.name in {'evaluate_model', 'deployment_gate'}) or (isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id.startswith(('MIN_', 'MAX_')) for t in n.targets))]
    ns = dict(pd=pd, accuracy_score=accuracy_score, precision_recall_fscore_support=precision_recall_fscore_support, LABELS=['SOFTWARE', 'FINANCE'])
    exec(compile(ast.Module(body=nodes, type_ignores=[]), '<notebook>', 'exec'), ns)
    return ns

class RegressionTests(unittest.TestCase):
    def test_invalid_outputs_are_failures(self):
        ns = evaluator()
        dataset = pd.DataFrame({'text':['x','y'], 'expected_label':['SOFTWARE','FINANCE']})
        for invalid in ['', None, 'TYPO', ['SOFTWARE']]:
            metrics, _ = ns['evaluate_model']('invalid', lambda text: invalid, dataset)
            self.assertEqual(metrics['failure_rate'], 1.0)

    def test_gate_rejects_invalid_metrics(self):
        gate = evaluator()['deployment_gate']
        good = dict(accuracy=.9, f1=.9, failure_rate=0.)
        self.assertEqual(gate(good, good, pd.DataFrame({'change':[0.]}), 0)['decision'], 'PASS')
        for bad in [float('nan'), float('inf'), -1., 2., None]:
            for field in ['accuracy', 'f1', 'failure_rate']:
                invalid = dict(good, **{field: bad})
                for baseline, candidate in [(good, invalid), (invalid, good)]:
                    self.assertEqual(gate(baseline, candidate, pd.DataFrame({'change':[0.]}), 0)['decision'], 'FAIL')
        self.assertEqual(gate(good, {}, pd.DataFrame({'change':[]}), 0)['decision'], 'FAIL')
        for frame in [pd.DataFrame({'change':[float('nan')]}), pd.DataFrame({'change':[2.]}), pd.DataFrame({'other':[0.]})]:
            self.assertEqual(gate(good, good, frame, 0)['decision'], 'FAIL')

    def test_confusion_matrix_preserves_failures(self):
        source = cells('LLM_Eval_Regression_Testing_Framework.ipynb')[15]
        class Display:
            @staticmethod
            def from_predictions(truth, pred, **kw):
                self.assertEqual(int(confusion_matrix(truth, pred, labels=kw['labels']).sum()), len(truth))
        class Plot:
            def __getattr__(self, name): return lambda *a, **k: None
        exec(source, dict(ConfusionMatrixDisplay=Display, golden_data=pd.DataFrame({'expected_label':['SOFTWARE','FINANCE']}), candidate_results=pd.DataFrame({'prediction':['SOFTWARE','ERROR']}), LABELS=['SOFTWARE','FINANCE'], plt=Plot()))

    def test_experiment_rerun_resets_logs(self):
        source = cells('Prompt_Versioning_AB_Testing_Platform.ipynb')[19]
        logs = []
        ns = dict(experiment_logs=logs, golden_data=pd.DataFrame({'query':['q'],'expected':['e']}), pd=pd)
        ns['run_request'] = lambda **kw: ns['experiment_logs'].append(kw)
        exec(source, ns); first = len(ns['experiment_logs']); exec(source, ns)
        self.assertEqual(len(ns['experiment_logs']), first)

    def test_split_used_for_purpose(self):
        from datetime import datetime, timezone
        source = cells('Hybrid_RAG_Retrieval_Eval_Pipeline.ipynb')
        validation = pd.DataFrame({'query':['validation query']})
        test = pd.DataFrame({'query':['test one','test two']})
        seen = []
        def metric(data, *args):
            seen.append(data)
            return .5
        ns = dict(pd=pd, validation_data=validation, test_data=test,
                  golden_data=pd.DataFrame({'query':['pooled query']}),
                  lexical_search=None, semantic_search=None, hybrid_search=None,
                  evaluate_retriever=lambda retriever, data, k: metric(data),
                  recall_at_k=metric, mean_reciprocal_rank=metric,
                  auto_rate=.5, review_rate=.5, datetime=datetime, timezone=timezone,
                  CONFIG=dict(project='test',version='test',lexical_weight=.5,
                              semantic_weight=.5,top_k=3,confidence_threshold=.5,margin_threshold=.1))
        exec(next(cell for cell in source if cell.startswith('comparison_rows =')), ns)
        self.assertEqual(len(seen),12)
        self.assertTrue(all(data is validation for data in seen))
        seen.clear()
        queries = []
        ns['logged_rag_pipeline'] = lambda query: queries.append(query)
        exec(next(cell for cell in source if 'demo_queries =' in cell), ns)
        self.assertEqual(queries, test['query'].tolist())
        exec(next(cell for cell in source if 'evaluation_summary = pd.DataFrame' in cell), ns)
        exec(next(cell for cell in source if cell.startswith('experiment_report =')), ns)
        self.assertTrue(seen and all(data is test for data in seen))
        self.assertEqual(ns['experiment_report']['test_examples'],2)

if __name__ == '__main__': unittest.main()
