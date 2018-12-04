import UnitTests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix
from correlation import *

class UnitTests(unittest.TestCase):
    df = pd.read_csv('sample data.csv', header=0)
    colnames = ('Science', 'IBTEACH', 'WEALTH', 'ESCS', 'School_type',
                'Sch_science_resource', 'log_science', 'female')
                
    def smoke_test_calculate_correlation(self):
        ''' Smoke test'''
        try:
            calculate_correlation(df, colnames)
        except:
            print('Smoke test failed!')
        print('Smoke test passed!')

    def smoke_test_visual_scatterplot(self):
        ''' Smoke test'''
        try:
                visual_scatterplot(df, colnames)
        except:
            print('Smoke test failed!')
        print('Smoke test passed!')

    def smoke_test_visual_histplot(self):
        ''' Smoke test'''
        try:
            visual_histplot(df, colnames)
        except:
            print('Smoke test failed!')
        print('Smoke test passed!')

    def smoke_test_visual_densityplot(self):
        ''' Smoke test'''
        try:
            visual_densityplot(df, colnames)
        except:
            print('Smoke test failed!')
        print('Smoke test passed!')

if __name__ == ‘__main__’:
    unittest.main()
