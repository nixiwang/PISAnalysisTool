'''
CSE583 Project
Given a student file, extracts useful features and writes
as a csv file
'''

import pandas as pd
from support import infos

# Reads csv files and creates dataframe
df = pd.read_csv('Data files/PISA data/small_stuscho.csv')
country_dict_df = pd.read_csv('Data files/PISA data/nations.csv')

# Dataframe processing
df1 = df[['CNTSTUID', 'ST004D01T']]
df1.columns = ['StudentID', 'Gender']
df1.loc[df1.Gender == 1, 'Gender'] = 'Female'
df1.loc[df1.Gender == 2, 'Gender'] = 'Male'
countryid_list = df['SUBNATIO'].tolist()
df_country = infos(country_dict_df, countryid_list)
df_math = df.iloc[:, 809:819]
df_math['Mathematics'] = df_math.mean(axis=1)
df_read = df.iloc[:, 819:829]
df_read['Reading'] = df_read.mean(axis=1)
df_science = df.iloc[:, 829:839]
df_science['Science'] = df_science.mean(axis=1)

output_df = pd.concat([df1, df_country, df_math['Mathematics'], df_read['Reading'],
                       df_science['Science']], axis=1, sort=False)
output_df.to_csv('student_info.csv', encoding='utf-8')