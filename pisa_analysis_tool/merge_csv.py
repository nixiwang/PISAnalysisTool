"""
CSE583 Project
This program merges student file or teacher file with school
file accoding to 'CNTSCHID' and 'SUBNATIO'
"""

import pandas as pd


def merge(file, output):
    """
    Merges file with school file according to 'CNTSCHID' and 'SUBNATIO',
    and generates a new output csv file
    """
    school_file = 'data_files/schools.csv'
    dataframe = pd.read_csv(file)
    school_df = pd.read_csv(school_file)
    result = pd.merge(dataframe, school_df, how='left',
                      on=['CNTSCHID', 'SUBNATIO'])
    result.to_csv(output, index=False)


def main():
    """
    Merges teacher file with school file and student file with
    school file
    """
    teacher_file = 'data_files/teachers.csv'
    teacher_output = 'teascho.csv'
    student_file = 'data_files/students.csv'
    student_output = 'stuscho.csv'
    merge(teacher_file, teacher_output)
    merge(student_file, student_output)


if __name__ == '__main__':
    main()
