"""
Created on Sat Nov 27 14:15:56 2018

@author: Shenghao Xie
This file is going to wrangle the data before visualization.
"""
import csv
import json
import datetime
import pandas as pd
import numpy as np
import wbdata


FILE_DIR = './data/visual_data/student_info.csv'
SUBJECT_LST = ['Mathematics', 'Reading', 'Science']
GEO_DATA = './data/visual_data/world_ogr.json'


def preprocessing():
    """
    read original student_info data and convert them into 3 new csv file
    world_score_avg.csv: store countries' average subject score
    world_score_male_avg.csv: store countries' male average subject score
    world_score_female_avg.csv: store countries' female average subject score
    :return: none
    """
    df_origin = pd.read_csv(FILE_DIR)
    df_origin.drop(['Unnamed: 0', 'SC013Q01TA', 'SCIERES',
                    'IBTEACH', 'WEALTH', 'ESCS', 'SchoolID',
                    'StudentID', 'CountryID'],
                   axis=1, inplace=True)
    df_avg = df_origin.groupby('CountryName').mean()
    df_avg.to_csv('./data/visual_data/world_score_avg.csv')

    df_male = df_origin[df_origin['Gender'] == 'Male']
    df_male_avg = df_male.groupby('CountryName').mean()
    df_male_avg.to_csv('./data/visual_data/world_score_male_avg.csv')

    df_female = df_origin[df_origin['Gender'] == 'Female']
    df_female_avg = df_female.groupby('CountryName').mean()
    df_female_avg.to_csv('./data/visual_data/world_score_female_avg.csv')


def add_lat_long(filedir, country_dict):
    """
    read a csv file and add countries' latitude and longitude
    data behind the last column.
    :param filedir: directory of csv file
    :param country_dict: a dictionary which keys are country
                         names and values are [lat, lon]
    :return: new csv file and a list of countries which have PISA
             test score
    """
    new_file = dict()
    new_file['CountryName'] = []
    new_file['Mathematics'] = []
    new_file['Reading'] = []
    new_file['Science'] = []
    new_file['lat'] = []
    new_file['lon'] = []
    country_lst = []
    with open(filedir) as csv_file:
        csv_reader = csv.reader(csv_file)
        count = 0
        for row in csv_reader:
            # print(filedir)
            c_name = row[0]
            if filedir == '../data/world_score_male_avg.csv':
                country_lst.append(c_name)
            m_score = row[1]
            r_score = row[2]
            s_score = row[3]
            if count != 0 and c_name in country_dict.keys():
                new_file['CountryName'].append(c_name)
                new_file['Mathematics'].append(float(m_score))
                new_file['Reading'].append(float(r_score))
                new_file['Science'].append(float(s_score))
                new_file['lat'].append(country_dict[c_name][0])
                new_file['lon'].append(country_dict[c_name][1])
            count = 1
    csv_file.close()
    return new_file, country_lst


def wb_country_data(indicator, start=2015, end=2015):
    """
    grab gender parity index data from world bank api
    :param indicator:
    :param start: start year
    :param end: end year
    :return: a dataframe
    """
    data_dates = (datetime.datetime(start, 1, 1), datetime.datetime(end, 1, 1))
    # call the api
    data = wbdata.get_dataframe({indicator: 'indicator'},
                                data_date=data_dates,
                                convert_date=True,
                                keep_levels=False)
    df_wb = data[['indicator']]
    df_wb['CountryName'] = df_wb.index
    df_wb = df_wb.reset_index(drop=True)
    df_wb = df_wb.dropna()
    df_wb.to_csv('../data/gender_coef.csv')
    return df_wb


def make_country_dict():
    """
    extract country name with lat and lon into a dictionary
    :return: a dictionary which keys are country name and value are (lat, lon)
    """
    country_dict = dict()
    with open(GEO_DATA) as json_file:
        data = json.load(json_file)
        for item in data['features']:
            country_name = item['properties']['NAME']
            country_lat = item['properties']['LAT']
            country_lon = item['properties']['LON']
            country_dict[country_name] = (country_lat, country_lon)
    json_file.close()
    return country_dict


def remove_country(csv_dir, country_dict, country_lst):
    """
    extract the countries which have gender parity index
    and also in world country data
    :param csv_dir: a csv file which have gender coefficent.
    :param country_dict: a dictionary which keys are country
                         name and value are (lat, lon)
    :param country_lst: a list of countries which have PISA test score
    :return: a dictionary with country name and gender parity index
    """
    needed_country = dict()
    needed_country['CountryName'] = list()
    needed_country['indicator'] = list()
    with open(csv_dir, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for line in csv_reader:
            if count != 0:
                country = line[1]
                indicator = line[0]
                if line[1] in country_dict.keys() and line[1] in country_lst:
                    needed_country['CountryName'].append(country)
                    needed_country['indicator'].append(float(indicator))
            count = 1
    csv_file.close()
    return needed_country


def get_score(df_male, df_female, subject):
    """
    Get a country's male and female score with respect to a subject.
    :param df_male: a data frame with males average score
    :param df_female: a data frame with females average score
    :param subject: subject name
    :return: two dictionaries
    """
    df_male_new = df_male[['CountryName', subject]]
    df_female_new = df_female[['CountryName', subject]]
    male_res = df_male_new.to_dict('records')
    female_res = df_female_new.to_dict('records')
    return male_res, female_res


def sort_by_country_avg(df_count, subject, m_res, f_res):
    """
    Sort the countries with subject score from high to low.
    Filter the scores into 4 bins, calculate each bin's
    gender coefficient. We also filter male and female mean
    score for each country into 4 bins, and get the average
    for each bin.
    :param df_count: average score for each country
    :param subject: subject name
    :param m_res: average score for male student in each country
    :param f_res: average score for female student in each country
    :return: 3 dictionaries
    """
    df_ctry_subj = df_count[['CountryName', subject]]
    df_ctry_subj_avg_sorted = df_ctry_subj.sort_values(df_ctry_subj.columns[-1],
                                                       ascending=False)
    ctry_subj_avg_lst = df_ctry_subj_avg_sorted.to_dict('split')['data']
    lst_25 = []
    lst_25_male = []
    lst_25_female = []

    lst_50 = []
    lst_50_male = []
    lst_50_female = []

    lst_75 = []
    lst_75_male = []
    lst_75_female = []

    lst_100 = []
    lst_100_male = []
    lst_100_female = []
    for i in range(len(ctry_subj_avg_lst)):
        country_name = ctry_subj_avg_lst[i][0]
        male_score = 0.0
        female_score = 0.0
        for j in range(len(m_res)):
            if m_res[j]['CountryName'] == country_name:
                male_score = m_res[j][subject]
            if f_res[j]['CountryName'] == country_name:
                female_score = f_res[j][subject]
        percent = (male_score - female_score) / male_score
        if i < 15:
            lst_25.append(percent)
            lst_25_male.append(male_score)
            lst_25_female.append(female_score)
        elif i < 30:
            lst_50.append(percent)
            lst_50_male.append(male_score)
            lst_50_female.append(female_score)
        elif i < 45:
            lst_75.append(percent)
            lst_75_male.append(male_score)
            lst_75_female.append(female_score)
        else:
            lst_100.append(percent)
            lst_100_male.append(male_score)
            lst_100_female.append(female_score)
    mean_25 = np.array(lst_25).mean()
    mean_50 = np.array(lst_50).mean()
    mean_75 = np.array(lst_75).mean()
    mean_100 = np.array(lst_100).mean()

    male_mean_25 = np.array(lst_25_male).mean()
    male_mean_50 = np.array(lst_50_male).mean()
    male_mean_75 = np.array(lst_75_male).mean()
    male_mean_100 = np.array(lst_100_male).mean()

    female_mean_25 = np.array(lst_25_female).mean()
    female_mean_50 = np.array(lst_50_female).mean()
    female_mean_75 = np.array(lst_75_female).mean()
    female_mean_100 = np.array(lst_100_female).mean()

    res = dict()
    res['25 percentile'] = mean_25 * 100
    res['50 percentile'] = mean_50 * 100
    res['75 percentile'] = mean_75 * 100
    res['100 percentile'] = mean_100 * 100

    male_res = dict()
    male_res['25 percentile'] = male_mean_25
    male_res['50 percentile'] = male_mean_50
    male_res['75 percentile'] = male_mean_75
    male_res['100 percentile'] = male_mean_100

    female_res = dict()
    female_res['25 percentile'] = female_mean_25
    female_res['50 percentile'] = female_mean_50
    female_res['75 percentile'] = female_mean_75
    female_res['100 percentile'] = female_mean_100

    return res, male_res, female_res
