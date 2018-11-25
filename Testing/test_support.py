import UnitTests
import pandas as pd
from support import *

class UnitTests(unittest.TestCase):

    def test_sav_to_dataframe(self):
        ''' Test for file not existing'''
        with self.assertRaises(FileNotFoundError):
            sav_to_dataframe('123.sav')
        ''' Test for file with a wrong type'''
        with self.assertRaises(FileNotFoundError):
            sav_to_dataframe('sample.txt')
        ''' Test for a valid file'''
        file = 'sample.sav'
        df = sav_to_dataframe(file)
        self.assertTrue(len(df) == 3)

    def test_student2school(selßf):
        df = pd.read_csv('IDs_sorted_by_student.csv')
        ''' Test for invalid student id'''
        with self.assertRaises(KeyError):
            student2school(df, 0)
        with self.assertRaises(KeyError):ß
            student2school(df, 99999999)
        ''' Test for valid student id'''
        nID = student2school(df, 800001)
        self.assertTrue(nID == 80000)

    def test_info(self):
        df = pd.read_csv('nations.csv')
        ''' Test for invalid nation id'''
        with self.assertRaises(KeyError):
            info(df, 0)
        ''' Test for valid nation id'''
        res = info(df, 360000)
        self.assertTrue(res == ('AUS', 'AP'))

if _name_ == '_main_':
    unittest.main()
