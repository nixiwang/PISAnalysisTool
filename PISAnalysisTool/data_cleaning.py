"""
================
Cleaning data
================
The following module demonstrates data cleaning procedures such as recoding, missing data handling,
standardization, and subsetting a small sample data for modeling.
"""


import pandas as pd
import numpy as np
from scipy.stats import zscore

def school_type(series):
    """In the 'School_type' variable there are multiple responses labeled as 'Invalid', or 'No response'.
    These will be coded along with system missing code '99' as 'NaN'. The 'public' and 'private' school type will be
    recoded as 1 and -1 respectively."""
    if series == 8:
        return 'NaN'
    elif series == '.I':
        return 'NaN'
    elif series == 9:
        return 'NaN'
    elif series == '.M':
        return 'NaN'
    elif series == 99:
        return 'NaN'
    elif series == 1:
        return 1
    elif series == 2:
        return -1
    else:
        raise KeyError()


def data_cleaning(df):
    # changing datatype
    df['IBTEACH'] = df.IBTEACH.astype(float)

    df['IBTEACH'] = df.IBTEACH.astype(float)
    df['WEALTH'] = df.WEALTH.astype(float)
    df['ESCS'] = df.ESCS.astype(float)
    df['SC013Q01TA'] = df.SC013Q01TA.astype(float)
    df['SCIERES'] = df.SCIERES.astype(float)

    # create log_score for each subject, using log_science for science subject
    df['log_science'] = np.log(df.Science)

    # rename column names
    df.rename(columns={'SC013Q01TA': 'School_type', 'SCIERES': 'Sch_science_resource'}, inplace=True)

    # replacing '99' as NaN in all columns
    df.loc[:, 'IBTEACH': 'Sch_science_resource'] = df.loc[:, 'IBTEACH': 'Sch_science_resource'].replace(99, np.NaN)
    df['School_type'] = df['School_type'].apply(school_type)
    df.dropna(inplace=True)
    # summarize the number of rows and columns in the dataset
    print(df.shape)
    print(df.isnull().sum())

    # creating "female" variable effect coded for each country, female = 1, male = -1
    df['female'] = df.Gender.map({'Female': 1, 'Male': -1})

    # creating z-scores for selected variables
    df['z_sch_resource'] = zscore(df['Sch_science_resource'])
    df['z_IBTEACH'] = zscore(df['IBTEACH'])
    return df.to_csv('data.csv', encoding='utf-8')


def small_sample(df):
    """output a random sample data csv file for smaller sample analysis"""
    df_s = df.groupby(['CountryID', 'SchoolID']).apply(lambda x: x.sample(frac=0.5, random_state=999)).\
        reset_index(drop=True)
    return df_s.to_csv('sample data.csv', encoding='utf-8')


def main():
    # df = pd.read_csv("data/student_info.csv", encoding='latin-1', na_values=['', ' '])
    df = pd.read_csv("student_info.csv", encoding='latin-1', na_values=['', ' '])
    data_cleaning(df)

    # df = pd.read_csv('data/data.csv', header=0)
    df = pd.read_csv('data.csv', header=0)
    small_sample(df)

if __name__ == '__main__':
    main()