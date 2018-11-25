# merge two csv file

import pandas as pd

teacher_file = "Data files/PISA data/csv/teachers.csv"
school_file = "Data files/PISA data/csv/schools.csv"
teacher_df = pd.read_csv(teacher_file)
school_df = pd.read_csv(school_file)
teascho = pd.merge(teacher_df, school_df, how = 'left',
                   on = ['CNTSCHID', 'SUBNATIO'])
teascho.to_csv('teascho.csv', index = False)

student_file = "Data files/PISA data/csv/students.csv"
student_df = pd.read_csv(student_file)
stuscho = pd.merge(student_df, school_df, how = 'left',
                   on = ['CNTSCHID', 'SUBNATIO'])
stuscho.to_csv('stuscho.csv', index = False)