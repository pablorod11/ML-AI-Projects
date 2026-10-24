"""Exercise real notebook drift functions against invalid monitoring inputs."""
import json
from pathlib import Path
import unittest
import numpy as np
import pandas as pd
from scipy.stats import ks_2samp

class DriftTests(unittest.TestCase):
    def setUp(self):
        cells = json.loads((Path(__file__).resolve().parents[1] / 'ModelData_Drift_Detection.ipynb').read_text())['cells']
        self.ns = dict(np=np, pd=pd, ks_2samp=ks_2samp, ALPHA=.05, ACCURACY_DROP_LIMIT=.05, CONFIDENCE_DROP_LIMIT=.05, PREDICTION_RATE_CHANGE_LIMIT=.1)
        for index in (9, 15):
            exec(''.join(cells[index]['source']), self.ns)
        self.frame = pd.DataFrame({'f': [0., 1.]})
        self.metrics = dict(accuracy=.9, confidence=np.array([.8, .9]), predictions=np.array([0, 1]))

    def test_invalid_features_raise(self):
        for bad in (self.frame.iloc[:0], pd.DataFrame(index=[0, 1]), pd.DataFrame({'f': [np.nan, 1]}), pd.DataFrame({'f': [np.inf, 1]}), pd.DataFrame({'other': [0, 1]})):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                self.ns['detect_feature_drift'](self.frame, bad)
            with self.subTest(reference=bad), self.assertRaises(ValueError):
                self.ns['detect_feature_drift'](bad, self.frame)

    def test_invalid_metrics_raise(self):
        for key, bad in [('accuracy', np.nan), ('accuracy', np.inf), ('confidence', np.array([])), ('confidence', np.array([np.nan, .9])), ('predictions', np.array([0, np.inf])), ('predictions', np.array([0])), ('confidence', np.array([[.8, .9]])), ('accuracy', -.1), ('accuracy', [0.9])]:
            for side in ('reference', 'current'):
                metrics = dict(self.metrics, **{key: bad})
                args = (metrics, self.metrics) if side == 'reference' else (self.metrics, metrics)
                with self.subTest(key=key, side=side, bad=bad), self.assertRaises(ValueError):
                    self.ns['monitor_batch'](self.frame, self.frame, *args)

    def test_unlabeled_healthy_batch_remains_supported(self):
        metrics = dict(self.metrics, accuracy=None)
        result = self.ns['monitor_batch'](self.frame, self.frame, metrics, metrics)
        self.assertEqual(result['status'], 'HEALTHY')
        self.assertIsNone(result['accuracy_drop'])

if __name__ == '__main__':
    unittest.main()
