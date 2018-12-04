'''
CSE583 Project
Given a student file, extracts useful features and writes
as a csv file
'''

import pandas as pd
from support import infos, student2nation

def get_student_info():
    '''
    Computes and extracts useful data from student-school datafile,
    stores data into a new csv file
    '''
    # Reads csv files and creates dataframe
    df = pd.read_csv('Data files/PISA data/small_stuscho.csv')
    country_dict_df = pd.read_csv('Data files/PISA data/nations.csv')
    
    # Dataframe processing
    df1 = df[['CNTRYID', 'CNTSCHID', 'CNTSTUID', 'ST004D01T']]
    df1.columns = ['CountryID', 'SchoolID', 'StudentID', 'Gender']
    stuid_list = df1['StudentID'].tolist()
    countryid_list = []
    for stuid in stuid_list:
        countryid_list.append(student2nation(stuid))
    df_country = infos(country_dict_df, countryid_list)
    df_math = df.iloc[:, 809:819]
    df_math['Mathematics'] = df_math.mean(axis=1)
    df_read = df.iloc[:, 819:829]
    df_read['Reading'] = df_read.mean(axis=1)
    df_science = df.iloc[:, 829:839]
    df_science['Science'] = df_science.mean(axis=1)
    df_hlm = df[['IBTEACH', 'WEALTH', 'ESCS', 'SC013Q01TA', 'SCIERES']]
    
    output_df = pd.concat([df1, df_country, df_math['Mathematics'],
                           df_read['Reading'], df_science['Science'],
                           df_hlm], axis=1, sort=False)
    output_df.loc[df1['Gender'] == 1, 'Gender'] = 'Female'
    output_df.loc[df1['Gender'] == 2, 'Gender'] = 'Male'
    output_df.to_csv('small_student_info.csv', encoding='utf-8')
    
def main():
    get_student_info()
    
if __name__ == '__main__':
    main()
