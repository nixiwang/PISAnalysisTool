import pandas as pd
import csv
from operator import itemgetter
import datetime
import wbdata
import json
import os

cwd = os.getcwd()

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_DIR = os.path.join(THIS_DIR, 'data/student_info.csv')
GEO_DATA = os.path.join(THIS_DIR, 'data/world_ogr.json')


def preprocessing():
    """
    read original student_info data and convert them into 3 new csv file
    world_score_avg.csv: store countries' average subject score
    world_score_male_avg.csv: store countries' male average subject score
    world_score_female_avg.csv: store countries' female average subject score
    :return: none
    """
    df = pd.read_csv(FILE_DIR)
    df.drop(['Unnamed: 0', 'SC013Q01TA', 'SCIERES', 'IBTEACH', 'WEALTH',
             'ESCS', 'SchoolID', 'StudentID', 'CountryID'],
            axis=1, inplace=True)
    df_avg = df.groupby('CountryName').mean()
    df_avg.to_csv('../../data/world_score_avg.csv')

    df_male = df[df['Gender'] == 'Male']
    df_male_avg = df_male.groupby('CountryName').mean()
    df_male_avg.to_csv('../../data/world_score_male_avg.csv')

    df_female = df[df['Gender'] == 'Female']
    df_female_avg = df_female.groupby('CountryName').mean()
    df_female_avg.to_csv('../../data/world_score_female_avg.csv')


def add_lat_long(filedir, country_dict):
    """
    read a csv file and add countries' latitude and longitude data behind the
    last column.
    :param filedir: directory of csv file
    :param country_dict: a dictionary which keys are country names and values
    are [lat, lon]
    :return: new csv file and a list of countries which have PISA test score
    """
    new_file = dict()
    new_file['CountryName'] = []
    new_file['Mathematics'] = []
    new_file['Reading'] = []
    new_file['Science'] = []
    new_file['lat'] = []
    new_file['lon'] = []
    country_lst = []
    with open(filedir) as f:
        csv_reader = csv.reader(f)
        count = 0
        for row in csv_reader:
            # print(filedir)
            c_name = row[0]
            if filedir == '../../data/world_score_male_avg.csv':
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
    f.close()
    return new_file, country_lst


def top_10_countries(csv_dir):
    """
    for each csv file, sort the countries by different subject average scores
    from high to low
    :param csv_dir: directory of the csv file
    :return: top 10 countries with three different subjects.
    """
    top_10_math = set()
    top_10_reading = set()
    top_10_science = set()
    with open(csv_dir) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            if count != 0:
                top_10_math.add((row[0], row[1]))
                top_10_reading.add((row[0], row[2]))
                top_10_science.add((row[0], row[3]))
            count = 1
    csv_file.close()
    sorted_top_10_math = sorted(
        top_10_math, key=itemgetter(1), reverse=True)[0:10]
    sorted_top_10_reading = sorted(
        top_10_reading, key=itemgetter(1), reverse=True)[0:10]
    sorted_top_10_science = sorted(
        top_10_science, key=itemgetter(1), reverse=True)[0:10]
    return sorted_top_10_math, sorted_top_10_reading, sorted_top_10_science


def WB_country_data(indicator, start=2015, end=2015):
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
    df = data[['indicator']]
    df['CountryName'] = df.index
    df = df.reset_index(drop=True)
    df = df.dropna()
    df.to_csv('../../data/gender_coef.csv')
    return df


def make_country_dict():
    """
    extract country name with lat and lon into a dictionary
    :return: a dictionary which keys are country name and value are (lat, lon)
    """
    country_dict = dict()
    with open(GEO_DATA) as f:
        data = json.load(f)
        for item in data['features']:
            country_name = item['properties']['NAME']
            country_lat = item['properties']['LAT']
            country_lon = item['properties']['LON']
            country_dict[country_name] = (country_lat, country_lon)
    f.close()
    return country_dict


def remove_country(csv_dir, country_dict, country_lst):
    """
    extract the countries which have gender parity index and also in world
    country data
    :param csv_dir: a csv file which have gender coefficent.
    :param country_dict: a dictionary which keys are country name and value
    are (lat, lon)
    :param country_lst: a list of countries which have PISA test score
    :return: a dictionary with country name and gender parity index
    """
    needed_country = dict()
    needed_country['CountryName'] = list()
    needed_country['indicator'] = list()
    with open(csv_dir, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        count = 0
        for line in csv_reader:
            if count != 0:
                country = line[1]
                indicator = line[0]
                if line[1] in country_dict.keys() and line[1] in country_lst:
                    needed_country['CountryName'].append(country)
                    needed_country['indicator'].append(float(indicator))
            count = 1
    f.close()
    return needed_country
