"""
=======================================
Fitting and plotting multi-level models
=======================================
This module runs pymer4 package which mimics functionality of lmer4 in R.
Here each model category is exemplified with a selection of variables in
the PISA 2015 dataset and we will show a demonstration of model fitting with regard to
gender (female) and a group of other interested factors. The results show the model
coefficients for each model.
"""


import os
import pandas as pd
import seaborn as sns
from pymer4.models import Lmer
from pymer4.utils import get_resource_path

###############################################################################
# Fitting hierarchical level mixed effects models
# ---------------
#
def random_intercept_3level_model(df):
    # Random Intercept-only three-level model
    model_0_sci = Lmer('log_science ~ 1 | SchoolID/CountryID', data=df)
    model_0_sci.fit(REML=False)
    m0_list=model_0_sci.fit(REML=False)
    model_0_sci.coefs


# Calculating ICC

def random_effect_2level_model(df):
    # Random intercept and slop two-level model:
    model_1_sci = Lmer('Science ~ female + (female*ESCS | CountryID)', data=df)
    model_1_sci.fit(REML=False)
    m1_list = model_1_sci.fit(REML=False)
    model_1_sci.coefs


def fixed_effect_3level_model(df):
    # Fixed effects three-level model
    model_2_sci = Lmer('log_science ~ IBTEACH + WEALTH '
                       '+ ESCS + female + Sch_science_resource '
                       '+ (1 | SchoolID/CountryID)',
                       data=df)
    model_2_sci.fit(REML=False)
    m2_list = model_2_sci.fit(REML=False)


def fixeff_interaction_3level_model(df):
    # Fixed effects plus interaction three-level model
    model_3_sci = Lmer('log_science ~ IBTEACH + WEALTH '
                       '+ ESCS + female + Sch_science_resource'
                       ' + female*ESCS '
                       '+ (1 | SchoolID/CountryID)',
                       data=df)
    model_3_sci.fit(REML=False)
    m3_list = model_3_sci.fit(REML=False)


def mixeff_interaction_3level_model(df):
    # Mixed effects plus interaction three-level model
    model_4_sci = Lmer('log_science ~ IBTEACH + WEALTH '
                       '+ ESCS + female + Sch_science_resource '
                       '+ female*ESCS '
                       '+ (ESCS | CountryID) '
                       '+ (Sch_science_resource | SchoolID/CountryID) '
                       '+ (1 | SchoolID/CountryID)',
                       data=df)
    model_4_sci.fit(REML=False)
    m4_list = model_4_sci.fit(REML=False)


def random_effect_multinteraction_model(df):
    # one random effect and multiple interactions between gender and factors
    model_5_sci = Lmer('log_science ~ IBTEACH + WEALTH + ESCS + female + Sch_science_resource + female*ESCS '
                       '+ female*WEALTH + female*IBTEACH + (ESCS | CountryID)',
                       data=df)
    model_5_sci.fit(REML=False)
    m5_list = model_5_sci.fit(REML=False)


# Model fit
# BIC change (of main effects combined M0 to M1
# BIC change (of main effects combined M1 to M2
# Using a likelihood ratio test (LRT) to test the difference between any two models
# Calculate the change in approximate variance explained (approximate R2) from M0 to M1, and M1 to M2.

###############################################################################
# Visualizing results
# -------------------
#
# Visualize model summary
def model_sum_visual(model_x_sci, predictor):
    model_x_sci.plot_summary()
    # Visualizing random effect of a predictor
    model_x_sci.plot('predictor',
               plot_ci=True,
               ylabel='Predicted log_science')

    sns.regplot(x='predictor',
                y='residuals',
                data=model_x_sci.data,
                fit_reg= False
                )
    # Inspecting overall fit
    sns.regplot(x='fits',
                y='log_science',
                units='CountryID',
                data=model_x_sci.data,
                fit_reg=True
                )

###############################################################################
# Main: Loading data
# ------------
#
def main():
    # Reading PISA csv file
    # df = pd.read_csv('data.csv')
    df = pd.read_csv('sample data.csv')
    random_effect_multinteraction_model(df)
    model_sum_visual(model_5_sci, ESCS)


if __name__ == '__main__':
    main()
