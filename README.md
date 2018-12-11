[![Build Status](https://travis-ci.org/nixiwang/PISAnalysisTool.svg?branch=master)](https://travis-ci.org/nixiwang/PISAnalysisTool)
[![Package versioning](https://img.shields.io/pypi/v/PISAnalysisTool.svg)](https://pypi.python.org/pypi?name=PISAnalysisTool&version=0.1.0&:action=display)

PISAnalysisTool
================


PISAnalysisTool is a great source of reference for conducting multi-level modeling in large-scale educational assessment such as PISA (The Programme for International Student Assessment). It provides examplar analysis for conducting quantitative educational inquiry from data cleaning to model summary visualization. This package uses `pymer4` library for modeling in python, which is equivalent to `lmer` package in R. Users can use this package to estimate other interesting variables in the dataset to perform fixed effect, random effect, and mixed effect multi-level modeling.
* Currently for modeling, a selection of variables in PISA 2015 are used in functions. Users can use our formula generator tool to run `Lmer` function
directly. In the future, we can develop more generic functions to facilitate data analysis of large-scale educational assessment data.

## Project structure
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

## PISA and World Bank Educational Data
### Background 
Equity is a fundamental value and guiding principle for education policies, but it is not necessarily equally fulfilled among education systems around the world. In order to investigate educational equity in the difference of academic performance between gender groups, females and males, we collect international education data from PISA and World Bank. 

PISA is an international assessment of 15-year-old students’ capabilities in reading literacy, mathematics literacy, and science literacy as well as measuring a wider range of factors including students’ interest, attitudes and motivation. It is distributed across over 60 countries, and student background questionnaires and teacher questionnaires are collected as part of PISA assessment. Student scores vary greatly for different student subpopulations within a jurisdiction – e.g., gender. 
### Analysis plan
In the current package, it linked different sub-datasets in PISA: student, school, and country level data. The analysis is specifically focused on describing and explaining gender differences in students’ performances scores across countries. We compare different multi-level mixed-effect models and visualize the summary plots. 

The next step is to identify and visualize countries that have “equitable” schooling outcomes and their characteristics in education systems, including student and school culture, teacher educational practices, and societal factors. That said, we caution against simplistic international comparisons of country performances using correlates of higher performance in higher ranking countries for projecting causal generalizations and statements. 

## Documentation
Current documentation for the PISAnalysisTool project can be found at <https://pypi.org/project/PISAnalysisTool/>

## Installation
`PISAnalysisTool` for its first version 0.1.0 is only compatible with Python 3. The installation steps are as below:

### Option 1
Install 'PISAnalysisTool' through: `pip install PISAnalysisTool`

### Option 2
1.For the git approach to install `PISAnalysisTool` you will need to begin by 
cloning `PISAnalysisTool` on your own computer by using the following `git` 
command:

```
git clone https://github.com/nixiwang/PISAnalysisTool
```
2.Next, to install the package you will need to go into the `PISAnalysisTool` 
directory and run the `setup.py` file:

```
cd PISAnalysisTool/
python setup.py install
```

3.To ensure that the dependencies to run `PISAnalysisTool` are installed on
 your computer you will want to both import the conda environment (for one of the R
 package) and pip installed components:

Create an environment from an exported env:
```bash
conda env create -f environment.yml
```
also you will run `pip install` the following command
```
pip install -r requirements.txt
```

You should now be ready to use, run `PISAnalysisTool` example code, and 
import the package on your computer.



## Examples (How to use PISAnalysisTool)
To understand how to use Ax/Wx, please refer to 
the [examples](https://github.com/nixiwang/PISAnalysisTool/tree/master/Examples
) section of this GitHub page where you can find 
examples for doing the following:
    
- How to generate .csv file from .sav file for PISA 2015 data
- How to generate a list of interested variables along with ID info to a 
csv data file for PISA data, including a demo on interactive PISA data generation, auto-scraping a small set of data for analysis
- A demo on generating World Bank data 
- Cleaning the scraped data for the example
- How to generate multi-level models and visualize model summaries
- A demo on interactive model formula generation, for users to create model on their own 
- Creating visualizations with the merged dataset on this example

## Limitations
In its current form, the PISAnalysisTool package serves as a very efficient data scraping and examplar analysis 
tool, but not with customizable model building, though the users can import and call `Lmer` models directly
by using our formula generator tool. 
The package also does not support ad hoc interactive visualization nor longitudinal analysis but can create an analysis
report for gender differences on students' performance for a given time frame.


