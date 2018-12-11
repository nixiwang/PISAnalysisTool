'''
CSE583 Project
get_student_info helper functions
'''

import os
import pandas as pd
import savReaderWriter as spss

def sav_to_dataframe(file):
    '''
    Converts a sav file to a pandas dataframe
    '''
    if not os.path.isfile(file):
        print('File not exists!')
        raise FileNotFoundError()

    if not file.endswith('.sav'):
        print('It is not a sav file!')
        raise FileNotFoundError()

    records = []
    with spss.SavReader(file) as reader:
        print("Reading file:", file, "...")
        for line in reader:
            records.append(line)

    df = pd.DataFrame(records)
    return df


def student2school(df, id_num):
    '''
    Takes the 'IDs_sorted_by_student.csv' dataframe
    and student id, returns school id of the student.
    '''
    return student2school_helper(df, id_num, 0, len(df))


def student2school_helper(df, id_num, start, end):
    '''
    student2school's helper function
    '''
    if start > end:
        print('Student ID:' + id_num + ' not exists!')
        raise KeyError()
    elif start == end:
        if id_num == df['CNTSCHID'][start]:
            return df['SUBNATIO'][start]
        print('Student ID:' + id_num + ' not exists!')
        raise KeyError()
    index = (end + start) // 2
    mid_value = df['CNTSCHID'][index]
    if mid_value == id_num:
        return df['SUBNATIO'][index]
    if mid_value > id_num:
        return student2school_helper(df, id_num, start, index)
    return student2school_helper(df, id_num, index, end)


def school2nation(id_num):
    '''
    Takes school id, returns nation id of the school.
    '''
    if id_num < 97100000:
        return id_num // 100000 * 10000
    if id_num < 97200000:
        return 7240000
    if id_num < 97400000:
        return 8400000
    return 320100


def student2nation(id_num):
    '''
    Takes student id, returns nation id of the student.
    '''
    return school2nation(id_num)


def info(df, id_num):
    '''
    :param df: the dataframe of 'nations.csv'
    :param id: the id of nation
    :return: a tuple - (string country name, string country
    code, string continent)
    '''
    try:
        target = df[df['nationID'] == id_num]
    except KeyError:
        print('Nation ID:' + id_num + ' not exists!')
        raise KeyError()

    name = target['nationName'].tolist()
    code = target.nationCode.tolist()
    continent = target.continent.tolist()

    return (name[0], code[0], continent[0])


def infos(country_df, id_list):
    '''
    :param country_df: the dataframe of 'nations.csv'
    :param id_df: the dataframe of country id
    :return: a dataframe - (string country name, string
    country code, string continent)
    '''

    name_list = []
    continent_list = []
    code_list = []

    for i in range(len(id_list)):
        tpl = info(country_df, id_list[i])
        name_list.append(tpl[0])
        code_list.append(tpl[1])
        continent_list.append(tpl[2])

    dictionary = {'CountryName':name_list, 'CountryCode': code_list, 'Continent':continent_list}
    res = pd.DataFrame(dictionary)

    return res

def extract_basic_df(df, country_dict_df):
    '''
    Takes 2 dataframes df and country_dict_df, extract basic
    student information, returns a new dataframe
    '''
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
    output_df = pd.concat([df1, df_country, df_math['Mathematics'],
                           df_read['Reading'], df_science['Science']],
                          axis=1, sort=False)
    return output_df



def interface(df):
    '''
    Takes a dataframe as parameter, gets variable names
    and output file name, returns a list with the given
    variables
    '''
    attributes_list = []
    print('Default attributes are: "IBTEACH", "WEALTH", '
          '"ESCS", "SC013Q01TA", "SCIERES"')
    print('Default output name is: student_info.csv')
    user_input = input('Using default settings?(y/n): ')
    if user_input == 'y':
        attributes_list = ['IBTEACH', 'WEALTH', 'ESCS',
                           'SC013Q01TA', 'SCIERES']
        name = 'student_info.csv'
    elif user_input == 'n':
        print('Input attribute name, "s" to stop:')
        attribute = input()
        while attribute != 's':
            if attribute not in df.columns.values:
                print('No attribute:', attribute)
                print('Please input again.')
            else:
                attributes_list.append(attribute)
            attribute = input()
        name = input('Input output file name:')
    else:
        raise ValueError('Invalid Input!')
    return attributes_list, name
