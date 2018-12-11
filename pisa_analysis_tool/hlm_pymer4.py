"""
Fitting and plotting multi-level models
=======================================
This module runs models through pymer4 package for the examplar inquiry,
which is to investigate the school-level and country-level factors that predict
students' science performance in the PISA 2015 data set, and mediate
gender differences in science performance.
Here each model category is exemplified with a selection of variables
and we will show a demonstration of model fitting with regard to
gender (female) and a group of other interested factors. The results show the
model coefficients for each model.
"""

import pandas as pd
import seaborn as sns
from pymer4.models import Lmer


#################################################
# Fitting hierarchical level mixed effects models
# -----------------------------------------------
#
def random_intercept_3level_model(dataframe):
    """
    Multi-level model_0_sci includes grand-mean intercept and setting outcome
    of log science
    scores as random.

        :param dataframe: a data frame with student ID, school ID, country ID,
        science, math, reading, and other five selected variables as
        predictors.
        :return: the model results
    """
    # Random Intercept-only three-level model
    model_0_sci = Lmer('log_science ~ 1 | SchoolID/CountryID',
                       data=dataframe)
    # model must be fitted in order to get estimate results
    model_0_sci.fit(REML=False)
    # print summary since auto-generated result doesn't include fixed effects
    print(model_0_sci.summary())
    # plot summary
    model_0_sci.plot_summary()
    # Inspecting overall fit
    sns.regplot(x='fits',
                y='log_science',
                units='CountryID',
                data=model_0_sci.data,
                fit_reg=True
                )
    return model_0_sci


# Calculating ICC

def random_effect_2level_model(dataframe):
    """
    Multi-level model_1_sci includes intercept, variable as fixed and the
    interaction term
    random on country level.

        :param dataframe: a data frame with student ID, school ID, country ID,
        science, math, reading, and other five selected variables as
        predictors.
        :return: the model results
    """
    # Random intercept and slope two-level model:
    model_1_sci = Lmer('Science ~ female + (female*ESCS | CountryID)',
                       data=dataframe)
    # model must be fitted in order to get estimate results
    model_1_sci.fit(REML=False)
    # print summary since auto-generated result doesn't include fixed effects
    print(model_1_sci.summary())
    model_1_sci.plot_summary()
    # Visualizing random effect of a predictor
    model_1_sci.plot('female',
                     plot_ci=True,
                     ylabel='Predicted log_science')

    sns.regplot(x='female',
                y='residuals',
                data=model_1_sci.data,
                fit_reg=False
                )
    # Inspecting overall fit
    sns.regplot(x='fits',
                y='log_science',
                units='CountryID',
                data=model_1_sci.data,
                fit_reg=True
                )
    return model_1_sci


def fixed_effect_3level_model(dataframe):
    """
    Multi-level model_2_sci includes intercept, variables as fixed effect.

        :param dataframe: a data frame with student ID, school ID, country ID,
        science, math, reading, and other five selected variables as
        predictors.
        :return: the model results
    """
    # Fixed effects three-level model
    model_2_sci = Lmer('log_science ~ IBTEACH + WEALTH '
                       '+ ESCS + female + Sch_science_resource '
                       '+ (1 | SchoolID/CountryID)',
                       data=dataframe)
    # model must be fitted in order to get estimate results
    model_2_sci.fit(REML=False)
    # print summary since auto-generated result doesn't include fixed effects
    print(model_2_sci.summary())
    model_2_sci.plot_summary()
    sns.regplot(x='Sch_science_resource',
                y='residuals',
                data=model_2_sci.data,
                fit_reg=False
                )
    # Inspecting overall fit
    sns.regplot(x='fits',
                y='log_science',
                units='CountryID',
                data=model_2_sci.data,
                fit_reg=True
                )

    return model_2_sci


def fixeff_interaction_3level_model(dataframe):
    """
    Multi-level model_3_sci includes intercept, variables as fixed, and an
    interaction term.

        :param dataframe: a data frame with student ID, school ID, country ID,
        science, math, reading, and other five selected variables as
        predictors.
        :return: the model results
    """
    # Fixed effects plus interaction three-level model
    model_3_sci = Lmer('log_science ~ IBTEACH + WEALTH '
                       '+ ESCS + female + Sch_science_resource'
                       ' + female*ESCS '
                       '+ (1 | SchoolID/CountryID)',
                       data=dataframe)
    # model must be fitted in order to get estimate results
    model_3_sci.fit(REML=False)
    # print summary since auto-generated result doesn't include fixed effects
    print(model_3_sci.summary())
    model_3_sci.plot_summary()
    # Visualizing the residual of a predictor
    sns.regplot(x='WEALTH',
                y='residuals',
                data=model_3_sci.data,
                fit_reg=False
                )
    # Inspecting overall fit
    sns.regplot(x='fits',
                y='log_science',
                units='CountryID',
                data=model_3_sci.data,
                fit_reg=True
                )
    return model_3_sci


def mixeff_interaction_3level_model(dataframe):
    """
    Multi-level model_4_sci includes intercept, school resource as random,
    others as fixed including
     interaction.

        :param dataframe: a data frame with student ID, school ID, country ID,
        science, math, reading, and other five selected variables as
        predictors.
        :return: the model results
    """
    # Mixed effects plus interaction three-level model
    model_4_sci = Lmer('log_science ~ IBTEACH + WEALTH '
                       '+ ESCS + female + Sch_science_resource '
                       '+ female*ESCS '
                       '+ (ESCS | CountryID) '
                       '+ (1 | SchoolID/CountryID)',
                       data=dataframe)
    # model must be fitted in order to get estimate results
    model_4_sci.fit(REML=False)
    # print summary since auto-generated result doesn't include fixed effects
    print(model_4_sci.summary())
    model_4_sci.plot_summary()
    # Visualizing the residual of a predictor
    sns.regplot(x='IBTEACH',
                y='residuals',
                data=model_4_sci.data,
                fit_reg=False
                )
    # Inspecting overall fit
    sns.regplot(x='fits',
                y='log_science',
                units='CountryID',
                data=model_4_sci.data,
                fit_reg=True
                )
    return model_4_sci


def mixeff_multinteraction2level_model(dataframe):
    """
    Multi-level model_5_sci includes intercept, multiple interactions and
    fixed effects,
     and setting ESCS as random on country level.

        :param dataframe: a data frame with student ID, school ID, country ID,
        science, math, reading, and other five selected variables as
        predictors.
        :return: the model results
    """
    # one random effect and multiple interactions between gender and factors
    model_5_sci = Lmer(
        'log_science ~ IBTEACH + WEALTH + ESCS + female + '
        'Sch_science_resource '
        '+ female*ESCS '
        '+ female*WEALTH + female*IBTEACH + (ESCS | CountryID)',
        data=dataframe)
    # model must be fitted in order to get estimate results
    model_5_sci.fit(REML=False)
    # print summary since auto-generated result doesn't include fixed effects
    print(model_5_sci.summary())
    model_5_sci.plot_summary()
    # Visualizing random effect of a predictor
    model_5_sci.plot('ESCS',
                     plot_ci=True,
                     ylabel='Predicted log_science')

    sns.regplot(x='ESCS',
                y='residuals',
                data=model_5_sci.data,
                fit_reg=False
                )
    # Inspecting overall fit
    sns.regplot(x='fits',
                y='log_science',
                units='CountryID',
                data=model_5_sci.data,
                fit_reg=True
                )
    return model_5_sci


# Model fit
# BIC change (of main effects combined M0 to M1
# BIC change (of main effects combined M1 to M2
# Using a likelihood ratio test (LRT) to test the difference between
# any two models
# Calculate the change in approximate variance explained (approximate R2) M0
# to M1, to M2.

#####################
# Visualizing results
# -------------------
#
# Visualize model summary
def model_sum_visual(model_x_sci, predictor, outcome):
    """
    A general function of plotting model results, including the coefficients
    with 95% confidence
    intervals, and cluster level estimates overlaid, as well as fit and
    residuals.

            :param model_x_sci: a list of lists of model results assigned to
            a name
            :param predictor: a string of predictor indicator
            :param outcome: a string of outcome variable
    """
    model_x_sci.plot_summary()
    # Visualizing random effect of a predictor
    model_x_sci.plot(predictor,
                     plot_ci=True,
                     ylabel=outcome)

    sns.regplot(x=predictor,
                y='residuals',
                data=model_x_sci.data,
                fit_reg=False
                )
    # Inspecting overall fit
    sns.regplot(x='fits',
                y=outcome,
                units='CountryID',
                data=model_x_sci.data,
                fit_reg=True
                )


####################
# Main: Loading data
# ------------------
#


def main():
    """
    Run the function of intercept-only model, gradually adding in predictors,
    and interactions, with
    focal interest variable of female and science outcome.
    """
    # Reading PISA csv file
    # df = pd.read_csv('data.csv')
    dataframe = pd.read_csv('data/sample data.csv')
    random_effect_2level_model(dataframe)
    fixed_effect_3level_model(dataframe)
    mixeff_multinteraction2level_model(dataframe)


if __name__ == '__main__':
    main()
