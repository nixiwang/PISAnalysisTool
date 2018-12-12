"""
Created on Sat Dec 7 22:57:07 2018

@author: Shenghao Xie
This file will plot an interactive visualization interface.
"""
from bokeh.plotting import figure
from bokeh.transform import dodge
from bokeh.models import ColumnDataSource
from bokeh.io import show
from bokeh.models import Panel
from bokeh.layouts import gridplot
from bokeh.models.widgets import Tabs
from preprocessing import make_country_dict, \
                          add_lat_long, pd, \
                          get_score, sort_by_country_avg

F_AVG_CSV = './data/visual_data/world_score_female_avg.csv'
M_AVG_CSV = './data/visual_data/world_score_male_avg.csv'
COUNTRY_AVG_CSV = './data/visual_data/world_score_avg.csv'

COUNTRY_DICT = make_country_dict()

M_DICT, _ = add_lat_long(M_AVG_CSV, COUNTRY_DICT)
F_DICT, _ = add_lat_long(F_AVG_CSV, COUNTRY_DICT)
C_DICT, _ = add_lat_long(COUNTRY_AVG_CSV, COUNTRY_DICT)

DF_M_AVG = pd.DataFrame.from_dict(M_DICT)
DF_F_AVG = pd.DataFrame.from_dict(F_DICT)
DF_C_AVG = pd.DataFrame.from_dict(C_DICT)


def prepare_data(df_male_avg, df_female_avg, df_country_avg, subject):
    """
    Return the data we want for each subject
    :param df_male_avg: a data frame which stores all male subjects average
    score from each country
    :param df_female_avg: a data frame which stores all female subjects average
    score from each country
    :param df_country_avg: a data frame which stores all subjects average
    score from each country
    :param subject: subject name
    :return: 3 dictionaries
    """
    male_res, female_res = get_score(df_male_avg, df_female_avg, subject)
    sub_res, m_sub_res, f_sub_res = sort_by_country_avg(df_country_avg,
                                                        subject,
                                                        male_res,
                                                        female_res)
    return sub_res, m_sub_res, f_sub_res


def plot_figure(res, male_res, female_res):
    """
    Plot a line plot and a box plot in each tab
    :param res: a dictionary with mean gender coefficient for each bin
    :param male_res: a dictionary with mean male subject score for each bin
    :param female_res: a dictionary with mean female subject score for each bin
    :return: a grid plot
    """
    x_list = list(res.keys())

    y_list = list(res.values())
    data = {'x': x_list,
            'overall_avg': y_list,
            'female_avg': list(female_res.values()),
            'male_avg': list(male_res.values())
            }
    source1 = ColumnDataSource(data=data)
    tooltips1 = [('Gender test coeff', '@overall_avg')]

    p1_line = figure(x_range=x_list,
                     plot_height=500,
                     tooltips=tooltips1,
                     title='Difference of performance between ' +
                     'male and female students for each country')
    p1_line.line(x_list, y_list, line_width=2)
    p1_line.circle(x='x', y='overall_avg', fill_color="blue",
                   size=8, source=source1)

    tooltips2 = [('Female average score', '@female_avg'),
                 ('Male average score', '@male_avg')]
    p1_bar = figure(x_range=x_list,
                    plot_height=500,
                    tooltips=tooltips2,
                    title='Subject scores by male and female students ' +
                    'for each country')
    p1_bar.vbar(x=dodge('x', -0.15, range=p1_line.x_range),
                top='female_avg',
                source=source1,
                color='#718dbf',
                legend='female average score',
                width=0.3)
    p1_bar.vbar(x=dodge('x', 0.15, range=p1_line.x_range),
                top='male_avg',
                source=source1,
                color='#e84d60',
                legend='male average score',
                width=0.3)

    # change just some things about the y-axes
    p1_line.yaxis.axis_label = "Percentage (%)"
    p1_line.yaxis.major_label_text_color = "black"
    p1_line.yaxis.major_label_orientation = "vertical"

    p1_bar.yaxis.axis_label = "Score"
    p1_bar.yaxis.major_label_text_color = "black"
    p1_bar.yaxis.major_label_orientation = "vertical"

    return gridplot([[p1_bar, p1_line]])


def combine_figures(math_res, male_math_res, female_math_res,
                    read_res, male_read_res, female_read_res,
                    sci_res, male_sci_res, female_sci_res):
    """
    Combine the plot in one html.
    :param math_res: a dict with mean math gender coefficient for each bin
    :param male_math_res: a dict with mean male math score for each bin
    :param female_math_res: a dict with mean female math score for each bin
    :param read_res: a dict with mean reading gender coefficient for each bin
    :param male_read_res: a dict with mean male reading score for each bin
    :param female_read_res: a dict with mean female reading score for each bin
    :param sci_res: a dic with mean science gender coefficient for each bin
    :param male_sci_res: a dict with mean male science score for each bin
    :param female_sci_res: a dict with mean female science score for each bin
    :return: a html file
    """
    math_plot = plot_figure(math_res, male_math_res, female_math_res)
    tab1 = Panel(child=math_plot, title='Math')
    read_plot = plot_figure(read_res, male_read_res, female_read_res)
    tab2 = Panel(child=read_plot, title='Reading')
    sci_plot = plot_figure(sci_res, male_sci_res, female_sci_res)
    tab3 = Panel(child=sci_plot, title='Science')
    tabs = Tabs(tabs=[tab1, tab2, tab3])
    show(tabs)


def main():
    """
    Main function
    """
    math_res, male_math_res, female_math_res = prepare_data(DF_M_AVG,
                                                            DF_F_AVG,
                                                            DF_C_AVG,
                                                            'Mathematics')
    read_res, male_read_res, female_read_res = prepare_data(DF_M_AVG,
                                                            DF_F_AVG,
                                                            DF_C_AVG,
                                                            'Reading')
    sci_res, male_sci_res, female_sci_res = prepare_data(DF_M_AVG,
                                                         DF_F_AVG,
                                                         DF_C_AVG,
                                                         'Science')
    combine_figures(math_res, male_math_res, female_math_res,
                    read_res, male_read_res, female_read_res,
                    sci_res, male_sci_res, female_sci_res)

if __name__ == '__main__':
    main()
