"""Focused regression tests against notebook cell source."""
import json
import unittest
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
ROOT = Path(__file__).resolve().parents[1]
def cell(name, index):
    return ''.join(json.loads((ROOT / (name + '.ipynb')).read_text())['cells'][index]['source'])
class OpsTests(unittest.TestCase):
    def test_group_disjoint_splits(self):
        for name in ['Enterprise_Autocoding_MLOps_Platform', 'HITL_Review_Pipeline']:
            ns = dict(np=np, pd=pd, train_test_split=train_test_split, RANDOM_STATE=42, rng=np.random.default_rng(42))
            for i in [2,3,4]: exec(cell(name,i),ns)
            a,b,c = [set(ns[k]['source_id']) for k in ['train_data','validation_data','test_data']]
            self.assertFalse(a & b or a & c or b & c)
    def test_calibration_failure_routes_to_review(self):
        ns = dict(pd=pd, threshold_analysis=pd.DataFrame({'accuracy':[0.2], 'coverage':[1.], 'threshold':[0.4]}), TARGET_AUTO_ACCEPT_ACCURACY=.9, DEFAULT_AUTO_ACCEPT_THRESHOLD=.7, ESCALATE_THRESHOLD=.4)
        exec(cell('Enterprise_Autocoding_MLOps_Platform',20),ns)
        exec(cell('Enterprise_Autocoding_MLOps_Platform',23),ns)
        self.assertNotEqual(ns['route_prediction'](1.),'AUTO_ACCEPT')
    def test_empty_review_schema(self):
        ns = dict(pd=pd, review_queue=pd.DataFrame({'record_id':[]}), human_labels={})
        exec(cell('HITL_Review_Pipeline',24),ns)
        exec(cell('HITL_Review_Pipeline',28),ns)
        self.assertIn('human_label',ns['feedback_data'])
    def test_cost_comparison_uses_successful_cohort(self):
        ns = dict(pd=pd, demo_requests=['different prompt', 'another'], successful=pd.DataFrame({'prompt':['short']}), total_cost=.001, premium_model={'input_cost_per_million':8.,'output_cost_per_million':30.}, estimate_tokens=lambda p:1,estimate_output_tokens=lambda p:100)
        exec(cell('LLM_cost_Autopilot',7),ns)
        # Suppress plotting through a tiny no-op facade.
        class Plot:
            def __getattr__(self,name): return lambda *a,**k:None
        ns['plt']=Plot()
        exec(cell('LLM_cost_Autopilot',26),ns)
        self.assertAlmostEqual(ns['always_premium_cost'],.003008)
    def test_completed_queue_status(self):
        for name,index in [('Enterprise_Autocoding_MLOps_Platform',31),('HITL_Review_Pipeline',25)]:
            ns=dict(pd=pd, production_results=pd.DataFrame([{'record_id':'A','route':'HUMAN_REVIEW','prediction':'X'}]),
                    review_queue=pd.DataFrame([{'record_id':'A','review_status':'PENDING'}]),
                    review_log=pd.DataFrame([{'record_id':'A','reviewer_label':'Y'}]))
            exec(cell(name,index),ns)
            self.assertEqual(ns['review_queue'].iloc[0]['review_status'],'COMPLETED')
            self.assertEqual(ns['final_results'].iloc[0]['final_label'],'Y')
    def test_output_tokens_in_dashboard(self):
        ns=dict(successful=pd.DataFrame([{'model':'tiny','input_tokens':3,'output_tokens':100,'cost':.1,'latency_ms':2}]))
        exec(cell('LLM_cost_Autopilot',35),ns)
        self.assertEqual(ns['dashboard'].iloc[0]['total_tokens'],103)
    def test_session_budget_label(self):
        source=''.join(cell('LLM_cost_Autopilot',i) for i in range(37))
        self.assertNotIn('DAILY_BUDGET',source)
        self.assertNotIn('Daily budget',source)
        ns=dict(SESSION_BUDGET=1.,spent_this_session=.3,llm_autopilot=lambda p:None)
        exec(cell('LLM_cost_Autopilot',15),ns)
        self.assertAlmostEqual(ns['budget_remaining'](),.7)
    def test_regression_probability_gate(self):
        from sklearn.metrics import accuracy_score,f1_score,log_loss
        class Model:
            def __init__(self, prob): self.prob=prob
        ns=dict(predict=lambda m,x:(np.array([0,1]),np.array([[m.prob,1-m.prob],[1-m.prob,m.prob]]),0),accuracy_score=accuracy_score,f1_score=f1_score,log_loss=log_loss,LOG_LOSS_MAX_INCREASE=.05)
        exec(cell('Copy_of_Model_Regression_Detection_System',27),ns)
        outcome=ns['detect_regression'](Model(.99),Model(.51),None,np.array([0,1]))
        self.assertEqual(outcome['decision'],'FAIL')
if __name__=='__main__': unittest.main()
