import unittest
import pandas as pd
import os
from pisa_analysis_tool.preprocessing import make_country_dict
from pisa_analysis_tool.preprocessing import add_lat_long
from pisa_analysis_tool.preprocessing import top_10_countries

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class UnitTests(unittest.TestCase):
    subject_lst = ['Mathematics', 'Reading', 'Science']

    def test_make_country_dict(self):
        country_dict = make_country_dict()
        self.assertTrue('Algeria' in country_dict.keys())
        self.assertTrue(country_dict.get('Brazil') == (-10.772, -53.089))

    def test_add_lat_long(self):
        country_dict = make_country_dict()
        new_file, country_lst = add_lat_long(
            os.path.join(THIS_DIR, os.pardir,
                         'data/Copy of world_score_male_avg.csv'),
            country_dict)
        df = pd.DataFrame.from_dict(new_file)
        df.to_csv('new_file.csv')
        self.assertEqual(61, len(new_file.get('CountryName')))
        self.assertEqual(0, len(country_lst))

    def test_top_10_cuntries(self):
        math, reading, science = top_10_countries('new_file.csv')
        self.assertTrue(len(math) == 10)
        self.assertTrue(len(reading) == 10)
        self.assertTrue(len(science) == 10)
        self.assertEqual('Uruguay', math[0][1])


if __name__ == '__main__':
    unittest.main()
