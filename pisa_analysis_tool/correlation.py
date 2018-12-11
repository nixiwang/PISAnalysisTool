"""
Running descriptive visuals
============================
The following module offers visualization for descriptive statistics such as
correlation plot, scatter plot,
density plot, and histograms.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix


def calculate_correlation(df, colnames):
    """
    A general function to calculate and visualize correlations
    between selected variables

    :param df: a data frame with student ID, school ID, country ID,
    science, math, reading, and other five selected variables as predictors.

    :param colnames: a list of focal variables
    :return: a plot of correlations
    """
    # dataframe for plotting
    df_plot = df.loc[:, list(colnames)]
    correlations = df_plot.corr()
    # plot correlation matrix
    names = colnames
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(correlations, vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = np.arange(0, 9, 1)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(names)
    ax.set_yticklabels(names)
    plt.show()


def visual_scatterplot(df, colnames):
    """
    scatter plot
    :param df: a data frame with student ID, school ID, country ID,
    science, math, reading, and other five selected variables as predictors.
    :param colnames: a list of focal variables
    :return: a scatter plot
    """
    # Scatterplot Matrix
    df_plot = df.loc[:, list(colnames)]
    scatter_matrix(df_plot)
    plt.show()


def visual_histplot(df, colnames):
    """
    histogram plot
    :param df: a data frame with student ID, school ID, country ID,
    science, math, reading, and other five selected variables as predictors.
    :param colnames: a list of focal variables
    :return: a histogram plot
    """
    # histogram plot
    df_plot = df.loc[:, list(colnames)]
    df_plot.hist()
    plt.show()


def visual_densityplot(df, colnames):
    """
    Univariate density plot, as a way to look at distribution

    :param df: a data frame with student ID, school ID, country ID,
    science, math, reading, and other five selected variables as predictors.
    :param colnames: a list of focal variables
    :return: a density plot
    """
    df_plot = df.loc[:, list(colnames)]
    df_plot.plot(kind='density', subplots=True, layout=(4, 4), sharex=False)
    plt.show()


def main():
    """
    Run functions for correlations and visuals
    """
    df = pd.read_csv('data/sample data.csv', header=0)
    colnames = ('Science', 'IBTEACH', 'WEALTH', 'ESCS', 'School_type',
                'Sch_science_resource', 'log_science', 'female')
    calculate_correlation(df, colnames)
    visual_histplot(df, colnames)
    visual_densityplot(df, colnames)
    df.Science.apply(lambda x: np.log(x + 0.1)).hist(bins=25)
    df.Sch_science_resource.hist(bins=25)


if __name__ == '__main__':
    main()
