"""
Cleaning data
================
The following module demonstrates data cleaning procedures such as recoding,
missing data handling,
standardization, and subsetting a small sample data for modeling.
"""

import pandas as pd
import numpy as np
from scipy.stats import zscore


def school_type(value):
    """
    In the 'School_type' variable there are multiple responses labeled as
    'Invalid', or 'No response'.
    These will be coded along with system missing code '99' as 'NaN'.
    The 'public' and 'private' school type will be
    recoded as 1 and -1 respectively.
    """
    if value == '8':
        return np.nan
    elif value == '.I':
        return np.nan
    elif value == '9':
        return np.nan
    elif value == '.M':
        return np.nan
    elif value == '99':
        return np.nan
    elif value == '1':
        return 1.0
    elif value == '2':
        return -1.0
    elif value == 'nan':
        return np.nan
    else:
        raise KeyError()


def data_cleaning(filename):
    """
    Function to clean data types, create log_score, effect-coding variables,
    and dealing with NAs.

    :param df: a data frame with student ID, school ID, country ID,
    science, math, reading, and other five selected variables as predictors.
    :return: a dataframe to csv file
    """
    # changing datatype
    df = pd.read_csv(filename, encoding='latin-1',
                     na_values=['', ' '], dtype={'SC013Q01TA': str})
    df['IBTEACH'] = df.IBTEACH.astype(float)
    df['WEALTH'] = df.WEALTH.astype(float)
    df['ESCS'] = df.ESCS.astype(float)
    df['SC013Q01TA'] = df.SC013Q01TA.astype(str)
    df['SCIERES'] = df.SCIERES.astype(float)

    # create log_score for each subject, using log_science for science subject
    df['log_science'] = np.log(df.Science)

    # rename column names
    df.rename(columns={'SC013Q01TA': 'School_type',
                       'SCIERES': 'Sch_science_resource'}, inplace=True)

    # replacing '99' as NaN in all columns
    df.loc[:, 'IBTEACH': 'Sch_science_resource'] = (
        df.loc[:, 'IBTEACH': 'Sch_science_resource'].replace(99, np.NaN))
    df['School_type'] = df['School_type'].apply(school_type).astype(float)
    df.dropna(inplace=True)

    # summarize the number of rows and columns in the dataset
    print(df.shape)
    print(df.isnull().sum())

    # creating "female" variable effect coded for each country,
    # female = 1, male = -1
    df['female'] = df.Gender.map({'Female': 1, 'Male': -1})

    # creating z-scores for selected variables
    df['z_sch_resource'] = zscore(df['Sch_science_resource'])
    df['z_IBTEACH'] = zscore(df['IBTEACH'])
    return df


def small_sample(df):
    """
    output a random sample data csv file for smaller sample analysis
    """
    df_s = df.groupby(['CountryID', 'SchoolID']).apply(
        lambda x: x.sample(frac=0.5, random_state=999)). \
        reset_index(drop=True)
    return df_s


def main():
    """
    Run functions of cleaning and subsetting the data based on multiple levels
     to be used for modeling

        :param df: a data frame with student ID, school ID, country ID,
        science, math, reading, and other five selected variables as
        predictors.
        :return: two csv files, one with complete data, one with subsetted data
    """
    df = data_cleaning("data/student_info.csv")
    sample_df = small_sample(df)
    sample_df.to_csv('sample data.csv', encoding='utf-8')


if __name__ == '__main__':
    main()
