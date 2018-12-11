"""
CSE583 Project
Given a student file, extracts useful features and writes
as a csv file
"""

import pandas as pd
from students_info_helper import interface, extract_basic_df

def get_student_info(input_file):
    """
    Takes a list of interested attributes, computes and extracts
    useful data from student-school datafile, stores data into a
    new csv file.
    """
    # Reads csv files and creates dataframe
    df = pd.read_csv(input_file)
    country_dict_df = pd.read_csv('data_files/nations.csv')

    # Generates basic dataframe
    df_basic = extract_basic_df(df, country_dict_df)

    # Reads user's inputs in to a dataframe
    attributes_list, name = interface(df)
    df_att = df[attributes_list]

    output_df = pd.concat([df_basic, df_att], axis=1, sort=False)
    output_df.loc[df_basic['Gender'] == 1, 'Gender'] = 'Female'
    output_df.loc[df_basic['Gender'] == 2, 'Gender'] = 'Male'

    # Generates output file
    output_df.to_csv(name, encoding='utf-8')

def main():
    """
    Extracts student infomation and generates a output csv file
    """
    get_student_info('data_files/small_stuscho.csv')

if __name__ == '__main__':
    main()
