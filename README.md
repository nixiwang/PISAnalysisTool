[![Build Status](https://travis-ci.org/nixiwang/PISAnalysisTool.svg?branch=master)](https://travis-ci.org/nixiwang/PISAnalysisTool)
[![Package versioning](https://img.shields.io/pypi/v/PISAnalysisTool.svg)](https://pypi.python.org/pypi?name=PISAnalysisTool&version=0.1.0&:action=display)

PISAnalysisTool
================


PISAnalysisTool is a great source of reference for conducting multi-level modeling in large-scale educational assessment such as PISA (The Programme for International Student Assessment). It provides examplar analysis for conducting quantitative educational inquiry from data cleaning to model summary visualization. This package uses `pymer4` library for modeling in python, which is equivalent to `lmer` package in R. Users can use this package to estimate other interesting variables in the dataset to perform fixed effect, random effect, and mixed effect multi-level modeling.
* Currently for modeling, a selection of variables in PISA 2015 are used in functions. In the future, we can extend them to more generic functions to facilitate data analysis of large-scale educational assessment data.

## PISA and World Bank Educational Data
### Background 
Equity is a fundamental value and guiding principle for education policies, but it is not necessarily equally fulfilled among education systems around the world. In order to investigate educational equity in the difference of academic performance between gender groups, females and males, we collect international education data from PISA and World Bank. PISA is an international assessment of 15-year-old students’ capabilities in reading literacy, mathematics literacy, and science literacy as well as measuring a wider range of factors including students’ interest, attitudes and motivation. It is distributed across over 60 countries, and student background questionnaires and teacher questionnaires are collected as part of PISA assessment. Student scores vary greatly for different student subpopulations within a jurisdiction – e.g., gender. In this PISA analysis, we linked different small datasets in PISA: student, school, and country level files. We are specifically interested in describing and explaining gender differences in students’ performances scores across countries. We will visualize the differences and hope to identify countries that have “equitable” schooling outcomes and their characteristics in education systems, including student and school culture, teacher educational practices, and societal factors. That said, we caution against simplistic international comparisons of country performances using correlates of higher performance in higher ranking countries for projecting causal generalizations and statements. 

```bash
│   .DS_Store
│   .gitignore
│   CHANGES.txt
│   LICENSE.md
│   README.md
│   requirements.txt
│
├───Data_
│       .DS_Store
│       sample data.csv
│       student_info.csv
│
├───Doc
│   │   .DS_Store
│   │   codebook_snap.png
│   │   Component Specification.md
│   │   Function Specification.md
│   │   Technology Review.pdf
│   │
│   └───.ipynb_checkpoints
│           Function Specification-checkpoint.ipynb
│
├───Examples
│       .DS_Store
│       demo WB data.ipynb
│       get_student_info.ipynb
│
└───PISAnalysisTool
    │   .DS_Store
    │   correlation.py
    │   data_cleaning.py
    │   get_WDI_data.py
    │   hlm_pymer4.py
    │   merge_csv.py
    │   plot_WDI.py
    │   students.py
    │   support.py
    │   version.py
    │   __init__.py
    │
    └───tests
            sample.sav
            test_correlation.py
            test_data_cleaning.py
            test_hlm_pymer4.py
            test_support.py
            __init__.py
```
