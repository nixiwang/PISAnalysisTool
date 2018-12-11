import unittest
import pandas as pd
import numpy as np
import os
from pisa_analysis_tool.data_cleaning import school_type
from pisa_analysis_tool.data_cleaning import data_cleaning
from pisa_analysis_tool.data_cleaning import small_sample

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class UnitTests(unittest.TestCase):

    def test_valid_school_type(self):
        """ Test for valid variable"""
        self.assertTrue(np.isnan(school_type('.I')))
        self.assertTrue(np.isnan(school_type('.M')))
        self.assertTrue(np.isnan(school_type('8')))
        self.assertTrue(np.isnan(school_type('9')))
        self.assertTrue(np.isnan(school_type('99')))
        self.assertEqual(school_type('1'), 1.0)
        self.assertEqual(school_type('2'), -1.0)

    def test_invalid_school_type(self):
        """ Test for invalid variable"""
        with self.assertRaises(KeyError):
            school_type(10)

    def test_data_cleaning(self):
        df = data_cleaning(os.path.join(
            THIS_DIR, os.pardir, 'data/student_info.csv'))
        self.assertTrue(df['IBTEACH'].dtype == float)
        self.assertTrue(df['WEALTH'].dtype == float)
        self.assertTrue(df['ESCS'].dtype == float)
        self.assertTrue(df['School_type'].dtype == float)
        self.assertTrue(df['Sch_science_resource'].dtype == float)

    def test_small_sample(self):
        # Run on first 100 rows only because it's slow
        df = pd.read_csv(os.path.join(THIS_DIR, os.pardir,
                                      'data/sample data.csv'), header=0)[:100]
        sample_df = small_sample(df)
        self.assertTrue(sample_df['CountryID'].dtype == int)
        self.assertTrue(sample_df['SchoolID'].dtype == int)


if __name__ == '__main__':
    unittest.main()
