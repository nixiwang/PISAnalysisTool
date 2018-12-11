import unittest
import pandas as pd
import csv
from operator import itemgetter
import datetime
import wbdata
import json
import os
from pisa_analysis_tool.preprocessing import *

class UnitTests(unittest.TestCase):
    file_dir = 'sample.csv'
    subject_lst = ['Mathematics', 'Reading', 'Science']
    geo_data = 'Copy of world_ogr.json'

    def test_make_country_dict(self):
        country_dict = make_country_dict()
        self.assertTrue('Algeria' in country_dict.keys())
        self.assertTrue(country_dict.get('Brazil') == (-10.772,-53.089))

    def test_add_lat_long(self):
        country_dict = make_country_dict()
        new_file, country_lst = add_lat_long('Copy of world_score_male_avg.csv', country_dict)
        df = pd.DataFrame.from_dict(new_file)
        df.to_csv('new_file.csv')
        self.assertTrue(len(new_file.get('CountryName')) == 20)
        self.assertTrue(len(country_lst) == 20)

    def test_top_10_cuntries(self):
        math, reading, science = top_10_countries('new_file.csv')
        self.assertTrue(len(math) == 10)
        self.assertTrue(len(reading) == 10)
        self.assertTrue(len(science) == 10)
        self.assertTrue(math[0] == 'Singapore')

if __name__ == '__main__':
    unittest.main()
