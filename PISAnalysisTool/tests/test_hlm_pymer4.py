import UnitTests
from pymer4.models import Lmer
from pymer4.utils import get_resource_path
import pandas as pd
import numpy as np
import os
from pymer4 import *

class UnitTests(unittest.TestCase):
    def test_hlm_m0():

        df = pd.read_csv(os.path.join(get_resource_path(), 'sample data.csv'))
        model_0_sci = Lmer('log_science ~ 1 | SchoolID/CountryID', data=df)
        model_0_sci.fit(summarize=False, REML=False)

        # Test results against r output
        assert model_0_sci.coefs.shape == (1, 8)
        estimates = np.array([6.138196])
        assert np.allclose(model_0_sci.coefs['Estimate'], estimates, atol=.001)

        assert isinstance(model_0_sci.fixef, list)
        assert model_0_sci.fixef[0].shape == (14419, 1)
        assert model_0_sci.fixef[1].shape == (14419, 1)

        assert isinstance(model_0_sci.ranef, list)
        assert model_0_sci.ranef[0].shape == (14419, 1)
        assert model_0_sci.ranef[1].shape == (14419, 1)

        assert model_0_sci.ranef_var.shape == (3, 3)

        variance = np.array([0.008007, 0.014925, 0.021602])
        assert np.allclose(
            model_0_sci.ranef_var.loc[:, 'Var'], variance, atol=.01)


    def test_hlm_m1():

        df = pd.read_csv(os.path.join(get_resource_path(), 'sample data.csv'))
        model_1_sci = Lmer('Science ~ female + (female*ESCS | CountryID)',
                           data=df)
        model_1_sci.fit(summarize=False, REML=False)

        # Test results against r output
        assert model_1_sci.coefs.shape == (2, 8)
        estimates = np.array([412.298572, 6.220405])
        assert np.allclose(model_1_sci.coefs['Estimate'], estimates, atol=.001)

        assert model_1_sci.ranef_var.shape == (5, 3)

    def test_hlm_m2():

        df = pd.read_csv(os.path.join(get_resource_path(), 'sample data.csv'))
        model_2_sci = Lmer('log_science ~ IBTEACH + WEALTH '
                           '+ ESCS + female + Sch_science_resource '
                           '+ (1 | SchoolID/CountryID)',
                           data=df)
        model_2_sci.fit(summarize=False, REML=False)

        # Test results against r output
        assert model_2_sci.coefs.shape == (6, 8)
        estimates = np.array([6.074618, -0.015097, 0.010710, 0.042099, -0.006254, 0.016298])
        assert np.allclose(model_2_sci.coefs['Estimate'], estimates, atol=.001)

        assert isinstance(model_2_sci.fixef, list)
        assert model_2_sci.fixef[0].shape == (14419, 6)
        assert model_2_sci.fixef[1].shape == (14419, 6)

        assert isinstance(model_2_sci.ranef, list)
        assert model_2_sci.ranef[0].shape == (14419, 1)
        assert model_2_sci.ranef[1].shape == (14419, 1)

        assert model_2_sci.ranef_var.shape == (3, 3)

        assert np.allclose(
            model_2_sci.coefs.loc[:, 'Estimate'], model_2_sci.fixef[0].mean(), atol=.01)


    def test_hlm_m3():

        df = pd.read_csv(os.path.join(get_resource_path(), 'sample data.csv'))
        model_3_sci = Lmer('log_science ~ IBTEACH + WEALTH '
                           '+ ESCS + female + Sch_science_resource '
                           '+ female*ESCS '
                           '+ (1 | SchoolID/CountryID)',
                           data=df)
        model_3_sci.fit(summarize=False, REML=False)

        # Test results against r output
        assert model_3_sci.coefs.shape == (3, 8)
        estimates = np.array([6.074593, -0.015087, -0.010693, 0.042019, -0.006004, 0.016301, 0.000859])
        assert np.allclose(model_3_sci.coefs['Estimate'], estimates, atol=.001)

        assert isinstance(model_3_sci.fixef, list)
        assert model_3_sci.fixef[0].shape == (14419, 7)
        assert model_3_sci.fixef[1].shape == (14419, 7)

        assert isinstance(model_3_sci.ranef, list)
        assert model_3_sci.ranef[0].shape == (14419, 1)
        assert model_3_sci.ranef[1].shape == (14419, 1)

        assert model_3_sci.ranef_var.shape == (3, 3)

        assert np.allclose(
            model_3_sci.coefs.loc[:, 'Estimate'], model_3_sci.fixef[0].mean(), atol=.01)


    def test_hlm_m4():

        df = pd.read_csv(os.path.join(get_resource_path(), 'sample data.csv'))
        model_4_sci = Lmer('log_science ~ IBTEACH + WEALTH '
                           '+ ESCS + female + Sch_science_resource '
                           '+ female*ESCS '
                           '+ (Sch_science_resource | SchoolID/CountryID) '
                           '+ (ESCS | CountryID) '
                           '+ (1| SchoolID/CountryID)',
                           data=df)
        model_4_sci.fit(summarize=False, REML=False)

        # Test results against r output
        assert model_4_sci.coefs.shape == (7, 8)
        estimates = np.array([6.079710, -0.013440, -0.012672, 0.046351,
                              -0.005399, 0.013502, 0.000887])
        assert np.allclose(model_4_sci.coefs['Estimate'], estimates, atol=.001)

        assert isinstance(model_4_sci.fixef, list)
        assert model_4_sci.fixef[0].shape == (14419, 7)
        assert model_4_sci.fixef[1].shape == (14419, 7)

        assert isinstance(model_4_sci.ranef, list)
        assert model_4_sci.ranef[0].shape == (14419, 3)
        assert model_4_sci.ranef[1].shape == (14419, 3)

        assert model_4_sci.ranef_corr.shape == (3, 3)
        assert model_4_sci.ranef_var.shape == (9, 3)

        assert np.allclose(
            model_4_sci.coefs.loc[:, 'Estimate'], model_4_sci.fixef[0].mean(), atol=.01)


    def test_hlm_m5():

        df = pd.read_csv(os.path.join(get_resource_path(), 'sample data.csv'))
        model_5_sci = Lmer('log_science ~ IBTEACH + WEALTH '
                           '+ ESCS + female + Sch_science_resource '
                           '+ female*ESCS + female*WEALTH + female*IBTEACH '
                           '+ (ESCS | CountryID)',
                   data=df)
        model_5_sci.fit(summarize=False, REML=False)

        # Test results against r output
        assert model_5_sci.coefs.shape == (9, 8)
        estimates = np.array([6.108262, -0.016521, -0.013483, 0.074545,
                              0.000658, 0.010694,
                              -0.000788, 0.001784, 0.003985])
        assert np.allclose(model_5_sci.coefs['Estimate'], estimates, atol=.001)

        assert isinstance(model_5_sci.fixef, list)
        assert model_5_sci.fixef.shape == (64, 9)

        assert isinstance(model_5_sci.ranef, list)
        assert model_5_sci.ranef.shape == (64, 2)

        assert model_5_sci.ranef_corr.shape == (1, 3)
        assert model_5_sci.ranef_var.shape == (3, 3)

        assert np.allclose(
            model_5_sci.coefs.loc['(Intercept)', 'Estimate'], model_5_sci.fixef['(Intercept)'].mean(), atol=.01)


if __name__ == ‘__main__’:
    unittest.main()