import unittest
from pymer4.models import Lmer
import pandas as pd
import numpy as np
import os
from pisa_analysis_tool.hlm_pymer4 import *

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class UnitTests(unittest.TestCase):
    def test_hlm_m0(self):
        """Run on a much smaller random sample of 273 rows only because
        it's slow to run even the sample data"""
        df = pd.read_csv(
            os.path.join(THIS_DIR, os.pardir, 'data/sample data.csv')) \
            .groupby(['CountryID', 'SchoolID']).apply(
            lambda x: x.sample(frac=0.02, random_state=999)) \
            .reset_index(drop=True)
        model_0_sci = random_intercept_3level_model(df)

        # Test results against r output
        assert model_0_sci.coefs.shape == (1, 8)
        estimates = np.array([6.113608])
        assert np.allclose(model_0_sci.coefs['Estimate'], estimates, atol=.001)

        assert isinstance(model_0_sci.fixef, list)
        assert model_0_sci.fixef[0].shape == (224, 1)
        assert model_0_sci.fixef[1].shape == (224, 1)

        assert isinstance(model_0_sci.ranef, list)
        assert model_0_sci.ranef[0].shape == (224, 1)
        assert model_0_sci.ranef[1].shape == (224, 1)

        assert model_0_sci.ranef_var.shape == (3, 3)

        variance = np.array([0.014718, 0.008542, 0.027549])
        assert np.allclose(
            model_0_sci.ranef_var.loc[:, 'Var'], variance, atol=.01)

    def test_hlm_m1(self):
        """Run on a much smaller random sample of 273 rows only because
        it's slow to run even the sample data"""
        df = pd.read_csv(
            os.path.join(THIS_DIR, os.pardir, 'data/sample data.csv')) \
            .groupby(['CountryID', 'SchoolID']).apply(
            lambda x: x.sample(frac=0.02, random_state=999)) \
            .reset_index(drop=True)
        model_1_sci = random_effect_2level_model(df)

        # Test results against r output
        assert model_1_sci.coefs.shape == (2, 8)
        estimates = np.array([417.005530, -1.403671])
        assert np.allclose(model_1_sci.coefs['Estimate'], estimates, atol=.001)

        assert model_1_sci.ranef_var.shape == (5, 3)

    def test_hlm_m2(self):
        """Run on a much smaller random sample of 273 rows only because
        it's slow to run even the sample data"""
        df = pd.read_csv(
            os.path.join(THIS_DIR, os.pardir, 'data/sample data.csv')) \
            .groupby(['CountryID', 'SchoolID']).apply(
            lambda x: x.sample(frac=0.02, random_state=999)) \
            .reset_index(drop=True)
        model_2_sci = fixed_effect_3level_model(df)

        # Test results against r output
        assert model_2_sci.coefs.shape == (6, 8)
        estimates = np.array([5.989285, -0.016045, -0.053171, 0.071663,
                              -0.012513, 0.022523])
        assert np.allclose(model_2_sci.coefs['Estimate'], estimates, atol=.001)

        assert isinstance(model_2_sci.fixef, list)
        assert model_2_sci.fixef[0].shape == (224, 6)
        assert model_2_sci.fixef[1].shape == (224, 6)

        assert isinstance(model_2_sci.ranef, list)
        assert model_2_sci.ranef[0].shape == (224, 1)
        assert model_2_sci.ranef[1].shape == (224, 1)

        assert model_2_sci.ranef_var.shape == (3, 3)

        assert np.allclose(
            model_2_sci.coefs.loc[:, 'Estimate'], model_2_sci.fixef[0].mean(),
            atol=.01)

    def test_hlm_m3(self):
        """Run on a much smaller random sample of 273 rows only because
        it's slow to run even the sample data"""
        df = pd.read_csv(
            os.path.join(THIS_DIR, os.pardir, 'data/sample data.csv')) \
            .groupby(['CountryID', 'SchoolID']).apply(
            lambda x: x.sample(frac=0.02, random_state=999)) \
            .reset_index(drop=True)
        model_3_sci = fixeff_interaction_3level_model(df)

        # Test results against r output
        assert model_3_sci.coefs.shape == (7, 8)
        estimates = np.array([5.992273, -0.017844, -0.049827, 0.069809,
                              -0.014507, 0.022053, 0.014162])
        assert np.allclose(model_3_sci.coefs['Estimate'], estimates, atol=.001)

        assert isinstance(model_3_sci.fixef, list)
        assert model_3_sci.fixef[0].shape == (224, 7)
        assert model_3_sci.fixef[1].shape == (224, 7)

        assert isinstance(model_3_sci.ranef, list)
        assert model_3_sci.ranef[0].shape == (224, 1)
        assert model_3_sci.ranef[1].shape == (224, 1)

        assert model_3_sci.ranef_var.shape == (3, 3)

        assert np.allclose(
            model_3_sci.coefs.loc[:, 'Estimate'], model_3_sci.fixef[0].mean(),
            atol=.01)

    def test_hlm_m4(self):
        """Run on a much smaller random sample of 273 rows only because
        it's slow to run even the sample data"""
        df = pd.read_csv(
            os.path.join(THIS_DIR, os.pardir, 'data/sample data.csv')) \
            .groupby(['CountryID', 'SchoolID']).apply(
            lambda x: x.sample(frac=0.02, random_state=999)) \
            .reset_index(drop=True)
        model_4_sci = mixeff_interaction_3level_model(df)

        # Test results against r output
        assert model_4_sci.coefs.shape == (7, 8)
        estimates = np.array([6.022373, -0.011295, -0.049406, 0.090477,
                              -0.001867, 0.015878, 0.010068])
        assert np.allclose(model_4_sci.coefs['Estimate'], estimates, atol=.001)

        assert isinstance(model_4_sci.fixef, list)
        assert model_4_sci.fixef[0].shape == (224, 7)
        assert model_4_sci.fixef[1].shape == (224, 7)

        assert isinstance(model_4_sci.ranef, list)
        assert model_4_sci.ranef[0].shape == (224, 1)
        assert model_4_sci.ranef[1].shape == (224, 1)

        assert model_4_sci.ranef_corr.shape == (1, 3)
        assert model_4_sci.ranef_var.shape == (5, 3)

        assert np.allclose(
            model_4_sci.coefs.loc[:, 'Estimate'], model_4_sci.fixef[0].mean(),
            atol=.01)

    def test_hlm_m5(self):
        """Run on a much smaller random sample of 273 rows only because
        it's slow to run even the sample data"""
        df = pd.read_csv(
            os.path.join(THIS_DIR, os.pardir, 'data/sample data.csv')) \
            .groupby(['CountryID', 'SchoolID']).apply(
            lambda x: x.sample(frac=0.02, random_state=999)) \
            .reset_index(drop=True)
        model_5_sci = mixeff_multinteraction2level_model(df)

        # Test results against r output
        assert model_5_sci.coefs.shape == (9, 8)
        estimates = np.array([6.022526, -0.010283, -0.051110, 0.088622,
                              -0.002294, 0.016113,
                              0.018638, -0.009444, 0.003725])
        assert np.allclose(model_5_sci.coefs['Estimate'], estimates, atol=.001)

        assert model_5_sci.fixef.shape == (10, 9)
        assert model_5_sci.ranef.shape == (10, 2)

        assert model_5_sci.ranef_corr.shape == (1, 3)
        assert model_5_sci.ranef_var.shape == (3, 3)

        assert np.allclose(
            model_5_sci.coefs.loc['(Intercept)', 'Estimate'],
            model_5_sci.fixef['(Intercept)'].mean(), atol=.01)


if __name__ == '__main__':
    unittest.main()
