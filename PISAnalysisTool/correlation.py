# Scatterplot Matrix
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix


def calculate_correlation(df, colnames):
    # dataframe for plotting
    df_plot = df.loc[:, list(colnames)]
    correlations = df_plot.corr()
    # plot correlation matrix
    names = colnames
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(correlations, vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = np.arange(0,9,1)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(names)
    ax.set_yticklabels(names)
    plt.show()

def visual_scatterplot(df, colnames):
    # Scatterplot Matrix
    df_plot = df.loc[:, list(colnames)]
    scatter_matrix(df_plot)
    plt.show()

def visual_histplot(df, colnames):
    # histogram plot
    df_plot = df.loc[:, list(colnames)]
    df_plot.hist()
    plt.show()

def visual_densityplot(df, colnames):
    # Univariate density plot, as a way to look at distribution
    df_plot = df.loc[:, list(colnames)]
    df_plot.plot(kind='density', subplots=True, layout=(4,4), sharex=False)
    plt.show()


def main():
    df = pd.read_csv('sample data.csv', header=0)
    colnames = ('Science', 'IBTEACH', 'WEALTH', 'ESCS', 'School_type',
                'Sch_science_resource', 'log_science', 'female')
    calculate_correlation(df, colnames)
    visual_histplot(df, colnames)
    visual_densityplot(df, colnames)

if __name__ == '__main__':
    main()