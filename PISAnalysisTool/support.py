'''
    CSE583 Project
    Supporting functions
'''
import pandas as pd
import savReaderWriter as spss
from pathlib import Path

def sav_to_dataframe(file):
    if not os.path.isfile(file):
        print('File not exists!')
        raise FileNotFoundError()
    
    if not file.endswith('.sav'):
        print('It is not a sav file!')
        raise FileNotFoundError()

    records = []
    with spss.SavReader(file) as reader:
        print("Reading file:",file, "...")
        for line in reader:
            records.append(line)

    df = pd.DataFrame(records)
    return df


def student2school(df, id):
    '''
        Takes the 'IDs_sorted_by_student.csv' dataframe and student id, returns school id of the student.
        '''
    return student2schoolHelper(df, id, 0, len(df))


def student2schoolHelper(df, id, start, end):
    if start > end:
        print('Student ID:' + id + ' not exists!')
        raise KeyError()
    elif start == end:
        if id == student2schoolHelper['CNTSCHID'][start]:
            return student2schoolHelper['SUBNATIO'][start]
        else:
            print('Student ID:' + id + ' not exists!')
            raise KeyError()
    index = (end + start) // 2
    mid_value = df['CNTSCHID'][index]
    if mid_value == id:
        return df['SUBNATIO'][index]
    elif mid_value > id:
        return student2schoolHelper(df, id, start, index)
    else:
        return student2schoolHelper(df, id, index, end)


def school2nation(id):
    '''
        Takes school id, returns nation id of the school.
        '''
    if id < 97100000:
        return id // 100000 * 10000
    if id < 97200000:
        return 7240000
    if id < 97400000:
        return 8400000
    return 320100

def student2nation(id):
    '''
        Takes student id, returns nation id of the student.
        '''
    return school2nation(id)


def info(df, id):
    '''
    :param df: the dataframe of 'nations.csv'
    :param id: the id of nation
    :return: a tuple - (string country name, string country code, string continent)
    '''
    try:
        target = df[df['nationID'] == id]
    except KeyError:
        print('Nation ID:' + id + ' not exists!')
        raise KeyError()

    name = target['nationName'].tolist()
    code = target.nationCode.tolist()
    continent = target.continent.tolist()

    return (name[0], code[0], continent[0])


def infos(country_df, id_list):
    '''
    :param country_df: the dataframe of 'nations.csv'
    :param id_df: the dataframe of country id
    :return: a dataframe - (string country name, string country code, string continent)
    '''

    name_list = []
    continent_list = []
    code_list = []

    for i in range(len(id_list)):
        t = info(country_df, id_list[i])
        name_list.append(t[0])
        code_list.append(t[1])
        continent_list.append(t[2])

    dict = {'CountryName':name_list, 'CountryCode': code_list, 'Continent':continent_list}
    res = pd.DataFrame(dict)

    return res
