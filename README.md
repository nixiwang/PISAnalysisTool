[![Build Status](https://travis-ci.org/nixiwang/PISAnalysisTool.svg?branch=master)](https://travis-ci.org/nixiwang/PISAnalysisTool)
[![Package versioning](https://img.shields.io/pypi/v/PISAnalysisTool.svg)](https://pypi.python.org/pypi?name=PISAnalysisTool&version=0.1.0&:action=display)

PISAnalysisTool
================


PISAnalysisTool is a great source of reference for conducting multi-level modeling in large-scale educational assessment such as PISA (The Programme for International Student Assessment). It provides examplar analysis for conducting quantitative educational inquiry from data cleaning to model summary visualization. This package uses `pymer4` library for modeling in python, which is equivalent to `lmer` package in R. Users can use this package to estimate other interesting variables in the dataset to perform fixed effect, random effect, and mixed effect multi-level modeling.
* Currently for modeling, a selection of variables in PISA 2015 are used in functions. Users can use our formula generator tool to run `Lmer` function
directly. In the future, we can develop more generic functions to facilitate data analysis of large-scale educational assessment data.

## Project structure
```bash
│   .gitignore
│   .travis.yml
│   CHANGES.txt
│   environment.yml
│   gen_docs.sh
│   LICENSE.md
│   README.md
│   requirements.txt
│   setup.py
│
├───doc
│   │   codebook_snap.png
│   │   Component Specification.md
│   │   Function Specification.md
│   │   In-progress report.pdf
│   │   Technology Review.pdf
│   │
│   ├───gen
│   │   │   .buildinfo
│   │   │   genindex.html
│   │   │   index.html
│   │   │   objects.inv
│   │   │   py-modindex.html
│   │   │   search.html
│   │   │   searchindex.js
│   │   │
│   │   ├───.doctrees
│   │   │   │   environment.pickle
│   │   │   │   index.doctree
│   │   │   │
│   │   │   └───api
│   │   │           modules.doctree
│   │   │           pisa_analysis_tool.doctree
│   │   │
│   │   ├───api
│   │   │       modules.html
│   │   │       pisa_analysis_tool.html
│   │   │
│   │   ├───_sources
│   │   │   │   index.rst.txt
│   │   │   │
│   │   │   └───api
│   │   │           modules.rst.txt
│   │   │           pisa_analysis_tool.rst.txt
│   │   │
│   │   └───_static
│   │           ajax-loader.gif
│   │           alabaster.css
│   │           basic.css
│   │           comment-bright.png
│   │           comment-close.png
│   │           comment.png
│   │           custom.css
│   │           doctools.js
│   │           documentation_options.js
│   │           down-pressed.png
│   │           down.png
│   │           file.png
│   │           jquery-3.2.1.js
│   │           jquery.js
│   │           minus.png
│   │           plus.png
│   │           pygments.css
│   │           searchtools.js
│   │           underscore-1.3.1.js
│   │           underscore.js
│   │           up-pressed.png
│   │           up.png
│   │           websupport.js
│   │
│   ├───sphinx
│   │   │   conf.py
│   │   │   index.rst
│   │   │
│   │   └───api
│   │           modules.rst
│   │           pisa_analysis_tool.rst
│   │
│   └───Updated function specification
│           Function specification.md
│           output_21_2.png
│           output_4_0.png
│           output_4_1.png
│           output_4_2.png
│           output_5_4.png
│           output_5_5.png
│           output_5_6.png
│           output_5_7.png
│           output_5_8.png
│           output_7_4.png
│           output_7_5.png
│
├───Examples
│       bokeh_plot.html
│       demo WB data.ipynb
│       Female_avg_score_country.PNG
│       gender_coeff.PNG
│       get_student_info.ipynb
│       male and female score difference.PNG
│       map_data.html
│
└───pisa_analysis_tool
    │   bokeh_plot.py
    │   correlation.py
    │   data_cleaning.py
    │   formula_creator.py
    │   get_students_info.py
    │   get_WDI_data.py
    │   hlm_pymer4.py
    │   mapdata.py
    │   merge_csv.py
    │   plot_WDI.py
    │   preprocessing.py
    │   students_info_helper.py
    │   version.py
    │   __init__.py
    │
    ├───data
    │   │   Copy of world_ogr.json
    │   │   Copy of world_score_male_avg.csv
    │   │   IDs_sorted_by_student.csv
    │   │   nations.csv
    │   │   sample data.csv
    │   │   sample.csv
    │   │   sample.sav
    │   │   student_info.csv
    │   │   world_ogr.json
    │   │
    │   └───visualization data
    │           gender_coef.csv
    │           world_ogr.json
    │           world_score_avg.csv
    │           world_score_female_avg.csv
    │           world_score_male_avg.csv
    │
    └───tests
            new_file.csv
            test_data_cleaning.py
            test_hlm_pymer4.py
            test_preprocessing.py
            test_students_info_helper.py
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

## Visualization
Figure 1: PISA Score World Distribution
![Image1](https://github.com/nixiwang/PISAnalysisTool/blob/master/Examples/Female_avg_score_country.PNG)

Figure 2: World Bank Gender Parity Indicator Distribution
![Image1](https://github.com/nixiwang/PISAnalysisTool/blob/master/Examples/gender_coeff.PNG)

Figure 3: Average Scores Comparison for Male and Female Students
![Image1](https://github.com/nixiwang/PISAnalysisTool/blob/master/Examples/male%20and%20female%20score%20difference.PNG)

## Limitations
In its current form, the PISAnalysisTool package serves as a very efficient data scraping and examplar analysis 
tool, but not with customizable model building, though the users can import and call `Lmer` models directly
by using our formula generator tool. 
The package also does not support ad hoc interactive visualization nor longitudinal analysis but can create an analysis
report for gender differences on students' performance for a given time frame.


