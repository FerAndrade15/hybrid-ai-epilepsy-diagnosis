import unittest
import importlib.util
import numpy as np
from xai_core import predict, occlusion, binary_groups, TorchAdapter, integrated_gradients


class CoreTests(unittest.TestCase):
    def test_occlusion_known_linear_effect(self):
        x = np.array([[1., 2.], [3., 4.]])
        z = np.array([[10.], [20.]])
        score = lambda a, b: a @ np.array([2., -3.]) + b[:, 0]
        drops, base = occlusion(score, (x, z), 0)
        np.testing.assert_allclose(drops, x * [2., -3.])
        np.testing.assert_allclose(base, score(x, z))

    def test_channel_occlusion_and_batches(self):
        x = np.arange(24).reshape(3, 4, 2).astype(float)
        score = lambda a: a.sum(axis=(1, 2))
        drops, base = occlusion(score, (x,), 0, batch_size=2)
        np.testing.assert_allclose(drops, x.sum(axis=1))
        np.testing.assert_allclose(base, predict(score, (x,), batch_size=1))

    def test_reject_multiclass_without_selector(self):
        with self.assertRaises(ValueError):
            predict(lambda a: a, (np.ones((2, 3)),))

    def test_binary_selection(self):
        groups = binary_groups([1, 0, 0, 1], [.9, .8, .1, .2])
        for name, index in zip(['TP', 'FP', 'TN', 'FN'], range(4)):
            np.testing.assert_array_equal(groups[name], [index])

    @unittest.skipUnless(importlib.util.find_spec('shap'), 'shap no instalado')
    def test_shap_preserves_each_sample_context(self):
        from xai_core import kernel_shap
        signal = np.array([[2.], [7.]], dtype=np.float32)
        features = np.array([[3., 4.], [5., 6.]], dtype=np.float32)
        score = lambda s, f: s[:, 0] * f[:, 0] + f[:, 1]
        phi, expected, residual = kernel_shap(score, (signal, features), 1,
                                              np.zeros((1, 2)), nsamples=8)
        np.testing.assert_allclose(phi, [[6, 4], [35, 6]], atol=1e-5)
        np.testing.assert_allclose(residual, 0, atol=1e-5)

    @unittest.skipUnless(importlib.util.find_spec('torch') and
                         importlib.util.find_spec('captum'), 'torch/captum no instalados')
    def test_ig_preserves_pairing_and_completeness(self):
        import torch
        from xai_core import saliency
        class Model(torch.nn.Module):
            def forward(self, s, f):
                return (s[:, 0] * f[:, 0] + f[:, 1])[:, None]
        adapter = TorchAdapter(Model(), lambda out: out[:, 0])
        inputs = (np.array([[2.], [7.]]), np.array([[3., 4.], [5., 6.]]))
        for batch in [None, 2, 4]:
            attrs, delta = integrated_gradients(adapter, inputs, 1, n_steps=10,
                                                internal_batch_size=batch)
            np.testing.assert_allclose(attrs, [[6, 4], [35, 6]], atol=1e-4)
            np.testing.assert_allclose(delta, 0, atol=1e-4)
        np.testing.assert_allclose(saliency(adapter, inputs, 1), [[2, 1], [7, 1]])


if __name__ == '__main__':
    unittest.main()
