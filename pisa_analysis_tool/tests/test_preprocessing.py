"""
Created on Sat Dec 8 21:37:27 2018

@author: Shenghao Xie
Test module for functions in preprocessing.
"""
import unittest
import pandas as pd
import os
from pisa_analysis_tool.preprocessing import make_country_dict
from pisa_analysis_tool.preprocessing import add_lat_long
from pisa_analysis_tool.preprocessing import remove_country
from pisa_analysis_tool.preprocessing import get_score
from pisa_analysis_tool.preprocessing import sort_by_country_avg


class UnitTests(unittest.TestCase):
    """
    This class is to run all the tests based on preprocessing.
    """
    SUBJECT_LST = ['Mathematics', 'Reading', 'Science']
    LOCAL_DATA_PATH = '../data/visual_data/'
    WB_DATA = LOCAL_DATA_PATH + 'gender_coef.csv'

    MALE_PATH = LOCAL_DATA_PATH + 'world_score_male_avg.csv'
    FEMALE_PATH = LOCAL_DATA_PATH + 'world_score_female_avg.csv'
    COUNT_PATH = LOCAL_DATA_PATH + 'world_score_avg.csv'

    DF_MALE = pd.read_csv(MALE_PATH)
    DF_FEMALE = pd.read_csv(FEMALE_PATH)
    DF_COUNT = pd.read_csv(COUNT_PATH)

    def get_large_dict(self):
        """
        Prepare for the data we used to test
        """
        country_dict = make_country_dict()

        male_avg_dict, _ = add_lat_long(self.MALE_PATH, country_dict)
        female_avg_dict, _ = add_lat_long(self.FEMALE_PATH, country_dict)
        country_avg_dict, _ = add_lat_long(self.COUNT_PATH, country_dict)
        return male_avg_dict, female_avg_dict, country_avg_dict

    # def test_preprocessing(self):
    #     """
    #     Test whether the program has save the files.
    #     """
    #     self.assertTrue(os.path.exists(self.LOCAL_DATA_PATH))
    #     self.assertTrue(os.path.exists(self.LOCAL_DATA_PATH +
    #                                    'world_score_male_avg.csv'))
    #     self.assertTrue(os.path.exists(self.LOCAL_DATA_PATH +
    #                                    'world_score_female_avg.csv'))
    #     self.assertTrue(os.path.exists(self.LOCAL_DATA_PATH +
    #                                    'world_score_avg.csv'))

    # def test_dataframe(self):
    #     """
    #     Test whether the csv file has correct columns
    #     """
    #     self.assertFalse('WEALTH' in self.DF_MALE.columns)
    #     self.assertFalse('StudentID' in self.DF_FEMALE.columns)
    #     self.assertFalse('CountryID' in self.DF_COUNT.columns)
    #
    #     self.assertTrue('CountryName' in self.DF_FEMALE.columns)
    #     self.assertTrue('CountryName' in self.DF_MALE.columns)
    #     self.assertTrue('CountryName' in self.DF_COUNT.columns)
    #
    #     self.assertTrue('Mathematics' in self.DF_FEMALE.columns)
    #     self.assertTrue('Mathematics' in self.DF_MALE.columns)
    #     self.assertTrue('Mathematics' in self.DF_COUNT.columns)
    #
    #     self.assertTrue('Reading' in self.DF_FEMALE.columns)
    #     self.assertTrue('Reading' in self.DF_MALE.columns)
    #     self.assertTrue('Reading' in self.DF_COUNT.columns)
    #
    #     self.assertTrue('Science' in self.DF_FEMALE.columns)
    #     self.assertTrue('Science' in self.DF_MALE.columns)
    #     self.assertTrue('Science' in self.DF_COUNT.columns)
    #
    #     self.assertTrue(len(self.DF_MALE) == 69)
    #     self.assertTrue(len(self.DF_FEMALE) == 69)
    #     self.assertTrue(len(self.DF_COUNT) == 69)
    #
    # def test_make_country_dict(self):
    #     """
    #     Test the Country dict has stored the countries' name with
    #     correct latitude and longitude coordinate.
    #     :return:
    #     """
    #     country_dict = make_country_dict()
    #     self.assertTrue('Algeria' in country_dict.keys())
    #     self.assertTrue(country_dict.get('Brazil') == (-10.772, -53.089))
    #
    def test_add_lat_long(self):
        """
        Test add_lat_long to check each country with its
        correct latitude and longitude coordinate.
        """
        m_avg_dict, f_avg_dict, c_avg_dict = self.get_large_dict()
        self.assertTrue(m_avg_dict['CountryName'][0] == 'Albania' and
                        m_avg_dict['lat'][0] == 41.143)

        self.assertTrue(m_avg_dict['CountryName'][4] == 'Belgium' and
                        m_avg_dict['lon'][4] == 4.664)

        self.assertTrue(f_avg_dict['CountryName'][-1] == 'Uruguay' and
                        f_avg_dict['lat'][-1] == -32.8)

        self.assertTrue(f_avg_dict['CountryName'][-2] == 'United States' and
                        f_avg_dict['lon'][-2] == -98.606)

        self.assertTrue(c_avg_dict['CountryName'][-3] == 'United Kingdom' and
                        c_avg_dict['lat'][-3] == 53)

        self.assertTrue(c_avg_dict['CountryName'][-3] == 'United Kingdom' and
                        c_avg_dict['lon'][-3] == -1.6)
    #
    # def test_wb_data(self):
    #     """
    #     Test the world bank data is correct.
    #     """
    #     df_wb = pd.read_csv(self.WB_DATA)
    #     self.assertTrue(len(df_wb) == 182)
    #     self.assertTrue(df_wb['indicator'].min() > 0)

    def test_remove_country(self):
        """
        Test remove_country in preprocessing to check that
        whether we have extracted the countries only have
        record in wb data.
        """
        df_wb = pd.read_csv(self.WB_DATA)
        country_dict = make_country_dict()
        _, country_lst = add_lat_long(self.MALE_PATH, country_dict)
        needed_country = remove_country(self.WB_DATA,
                                        country_dict, country_lst)

        self.assertTrue(list(needed_country['CountryName'])[28] in
                        list(df_wb['CountryName']))

    # def test_sort_by_country_avg(self):
    #     """
    #     Test sort_by_country_avg funtion. This function returns three
    #     dictionaries, all of them should have four keys with four
    #     values. For the last two dictionaries, the values are in a
    #     descending order.
    #     """
    #     m_avg_dict, f_avg_dict, c_avg_dict = self.get_large_dict()
    #     DF_MALE = pd.DataFrame.from_dict(m_avg_dict)
    #     DF_FEMALE = pd.DataFrame.from_dict(f_avg_dict)
    #     DF_COUNTry_avg = pd.DataFrame.from_dict(c_avg_dict)
    #     male_res, female_res = get_score(DF_MALE, DF_FEMALE, 'Science')
    #     sub_res, m_sub_res, f_sub_res = sort_by_country_avg(DF_COUNTry_avg,
    #                                                         'Science',
    #                                                         male_res,
    #                                                         female_res)
    #     self.assertTrue(list(m_sub_res.values())[0] >= list(m_sub_res.values())[1])
    #     self.assertTrue(list(f_sub_res.values())[0] >= list(f_sub_res.values())[1])
    #     self.assertTrue(len(sub_res) == 4)


if __name__ == '__main__':
    unittest.main()
