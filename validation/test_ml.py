"""Focused notebook tests; no training or external calls."""
import ast
import contextlib
import io
import json
from pathlib import Path
import types
import tempfile
import joblib
import unittest
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]

def source(name, index):
    return ''.join(json.loads((ROOT / name).read_text())['cells'][index]['source'])

def execute(name, index, ns):
    exec(compile(source(name, index), f'{name}:cell{index}', 'exec'), ns)

class NotebookTests(unittest.TestCase):
    def test_template_and_text_disjoint_splits(self):
        ns = dict(np=np, pd=pd, train_test_split=train_test_split, RANDOM_STATE=42, rng=np.random.default_rng(42))
        with contextlib.redirect_stdout(io.StringIO()):
            execute('Neural_Network_JEV (1).ipynb', 2, ns)
            execute('Neural_Network_JEV (1).ipynb', 3, ns)
        parts = [ns[k] for k in ('train_data','validation_data','test_data')]
        for i, left in enumerate(parts):
            self.assertEqual(set(left.document_type), set(ns['templates']))
            for right in parts[i+1:]:
                self.assertTrue(set(left.text.str.casefold().str.split().str.join(' ')).isdisjoint(right.text.str.casefold().str.split().str.join(' ')))
                self.assertTrue(set(left.template_id).isdisjoint(right.template_id))
        self.assertEqual(sum(map(len,parts)),600)

    def test_online_routes_fail_closed(self):
        ns = {'requests': types.SimpleNamespace(RequestException=type('RequestException',(Exception,),{}))}
        for index in (12,13,19):
            execute('Neural_Network_JEV (1).ipynb',index,ns)
        row = dict(document_quality=.95,previous_failures=0,business_risk='LOW',contains_sensitive_data=False,model_confidence=.99)
        # An unverified service payload must never be treated as a routing decision.
        for payload in ({'routing':'AUTO_PROCESS'}, {}, {'decision':'INVENTED'}, None):
            ns['ask_jev'] = lambda row, payload=payload: payload
            result=ns['route_document'](row,use_jev=True)
            self.assertEqual(result['decision'],'HUMAN_REVIEW')
        for payload, parser in [(None, lambda value: value.get('decision')), ([], lambda value: value[0])]:
            ns['ask_jev'] = lambda row, payload=payload: payload
            self.assertEqual(ns['route_document'](row,use_jev=True,decision_parser=parser)['decision'],'HUMAN_REVIEW')
        self.assertEqual(ns['route_document'](row)['decision'],'AUTO_PROCESS')
        # This adapter is a test fixture, not a claim about the live API schema.
        for decision in ('AUTO_PROCESS', 'HUMAN_REVIEW', 'ESCALATE'):
            ns['ask_jev'] = lambda row, decision=decision: {'fixture_choice':decision}
            result=ns['route_document'](row,use_jev=True,decision_parser=lambda payload: payload['fixture_choice'])
            self.assertEqual(result['decision'],decision)
        ns['ask_jev'] = lambda row: {}
        def interrupt_parser(payload):
            raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):
            ns['route_document'](row,use_jev=True,decision_parser=interrupt_parser)
        ns['ask_jev'] = lambda row: {'fixture_choice':'UNKNOWN'}
        self.assertEqual(ns['route_document'](row,use_jev=True,decision_parser=lambda payload: payload['fixture_choice'])['decision'],'HUMAN_REVIEW')
        self.assertEqual(ns['route_document'](row,use_jev=True,decision_parser=lambda payload: payload['missing'])['decision'],'HUMAN_REVIEW')

    def test_persisted_profile_matches_monitor_contract(self):
        metrics={'accuracy':1.,'confidence':np.array([.9,.9]),'predictions':np.array([0,1])}
        ns=dict(FEATURES=['f'],X_reference=pd.DataFrame({'f':[0,1]}),reference_accuracy=1.,reference_confidence=np.float64(.9),reference_positive_rate=np.float64(.5),reference_metrics=metrics,ACCURACY_DROP_LIMIT=.05,CONFIDENCE_DROP_LIMIT=.05,PREDICTION_RATE_CHANGE_LIMIT=.1)
        tree=ast.parse(source('ModelData_Drift_Detection.ipynb',22))
        assignment=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='reference_profile' for t in n.targets))
        exec(compile(ast.Module(body=[assignment],type_ignores=[]),'profile','exec'),ns)
        execute('ModelData_Drift_Detection.ipynb',15,ns)
        ns['detect_feature_drift']=lambda *args:pd.DataFrame({'drift_detected':[False],'feature':['f']})
        with tempfile.TemporaryDirectory() as directory:
            artifact = Path(directory) / 'reference_profile.joblib'
            joblib.dump(ns['reference_profile'],artifact)
            profile = joblib.load(artifact)
        result=ns['monitor_batch'](ns['X_reference'],ns['X_reference'],profile,metrics)
        self.assertEqual(result['status'],'HEALTHY')

if __name__ == '__main__':
    unittest.main()
