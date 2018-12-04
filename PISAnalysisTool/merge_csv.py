'''
CSE583 Project
This program merges student file or teacher file with school 
file accoding to 'CNTSCHID' and 'SUBNATIO'
'''

import pandas as pd

def merge(file, output):
    '''
    Merges file with school file according to 'CNTSCHID' and 'SUBNATIO',
    and generates a new output csv file
    '''
    school_file = 'Data files/PISA data/schools.csv'
    df = pd.read_csv(file)
    school_df = pd.read_csv(school_file)
    result = pd.merge(df, school_df, how = 'left',
                       on = ['CNTSCHID', 'SUBNATIO'])
    result.to_csv(output, index = False)
    
def main():
    teacher_file = 'Data files/PISA data/teachers.csv'
    teacher_output = 'teascho.csv'
    student_file = 'Data files/PISA data/students.csv'
    student_output = 'stuscho.csv'
    merge(teacher_file, teacher_output)
    merge(student_file, student_output)
    
if __name__ == '__main__':
    main()