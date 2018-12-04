import UnitTests
import pandas as pd
import numpy as np
from scipy.stats import zscore
from data_cleaning import *

class UnitTests(unittest.TestCase):
    
    def test_school_type(self):
        ''' Test for valid variable'''
        series1 = pd.Series(['.I', '.M', 8, 9, 99, 1, 2])
        res1 = school_type(series1)
        self.assertTrue(res1 == pd.Series(['NaN', 'NaN', 'NaN', 'NaN', 'NaN', 1, -1]))
        ''' Test for invalid variable'''
        series2 = pd.Series(['invalid', 10])
        with self.assertRaises(KeyError):
            res2 = school_type(series2)

    def smoke_test_data_cleaning(self):
        ''' Smoke test'''
        df = pd.read_csv("student_info.csv", encoding='latin-1', na_values=['', ' '])
        try:
            data_cleaning(df)
        except:
            print('Smoke test failed!')
        print('Smoke test passed!')

    def smoke_test_small_samle(self):
        ''' Smoke test'''
        df = pd.read_csv('data.csv', header=0)
        try:
            small_sample(df)
        except:
            print('Smoke test failed!')
        print('Smoke test passed!')

if __name__ == ‘__main__’:
    unittest.main()
