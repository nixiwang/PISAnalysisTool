"""
CSE583 Project
Processing map data
"""

import pandas as pd
import folium
from pisa_analysis_tool.preprocessing import make_country_dict
from pisa_analysis_tool.preprocessing import add_lat_long
from pisa_analysis_tool.preprocessing import remove_country

# json file with countries' name and their geographical data
country_geo = '../../data/world_ogr.json'
# gender coefficient data for countries
gender_coeff = '../../data/gender_coef.csv'

# preprocessing raw data
female_avg_csv = '../../data/world_score_female_avg.csv'
male_avg_csv = '../../data/world_score_male_avg.csv'
country_avg_csv = '../../data/world_score_avg.csv'

country_dict = make_country_dict()

male_avg_dict, country_lst = add_lat_long(male_avg_csv, country_dict)
female_avg_dict, country_lst1 = add_lat_long(female_avg_csv, country_dict)
country_avg_dict, country_lst2 = add_lat_long(country_avg_csv, country_dict)

df_male_avg = pd.DataFrame.from_dict(male_avg_dict)
df_female_avg = pd.DataFrame.from_dict(female_avg_dict)
df_country_avg = pd.DataFrame.from_dict(country_avg_dict)

needed_country = remove_country(gender_coeff, country_dict, country_lst)
indicator_data = pd.DataFrame.from_dict(needed_country)

# initalize the position when the html file is open
m1 = folium.Map(location=[50, 15], zoom_start=1.5)

# Add the color for the chloropleth:
m1.choropleth(
    geo_data=country_geo,
    name='Male Average Mathematics Score for Each Country',
    data=df_male_avg,
    columns=['CountryName', 'Mathematics'],
    key_on='properties.NAME',
    fill_color='YlOrBr',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='Male Average Mathematics Score'
)  # Male Average Mathematics Score distribution layer
m1.choropleth(
    geo_data=country_geo,
    name='Male Average Science Score for Each Country',
    data=df_male_avg,
    columns=['CountryName', 'Reading'],
    key_on='properties.NAME',
    fill_color='PuBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='Male Average Science Score'
)  # Male Average Science Score distribution layer
m1.choropleth(
    geo_data=country_geo,
    name='Male Average Reading Score for Each Country',
    data=df_male_avg,
    columns=['CountryName', 'Science'],
    key_on='properties.NAME',
    fill_color='GnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='Male Average Reading Score'
)  # Male Average Reading Score distribution layer
m1.choropleth(
    geo_data=country_geo,
    name='Female Average Mathematics Score for Each Country',
    data=df_female_avg,
    columns=['CountryName', 'Mathematics'],
    key_on='properties.NAME',
    fill_color='YlOrBr',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='Female Average Mathematics Score'
)  # Female Average Mathematics Score distribution layer
m1.choropleth(
    geo_data=country_geo,
    name='Female Average Science Score for Each Country',
    data=df_female_avg,
    columns=['CountryName', 'Reading'],
    key_on='properties.NAME',
    fill_color='PuRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='Female Average Science Score'
)  # Female Average Science Score distribution layer
m1.choropleth(
    geo_data=country_geo,
    name='Female Average Reading Score for Each Country',
    data=df_female_avg,
    columns=['CountryName', 'Science'],
    key_on='properties.NAME',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='Female Average Reading Score'
)  # Female Average Reading Score distribution layer
m1.choropleth(
    geo_data=country_geo,
    name='Countries\' indicator score',
    data=indicator_data,
    columns=['CountryName', 'indicator'],
    key_on='properties.NAME',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='World Bank gender parity index(GPI)'
)  # World Bank gender parity index(GPI) layer

# add markers for each country in the csv file
for i in range(0, len(df_female_avg)):
    folium.Marker([df_female_avg.iloc[i]['lat'],
                   df_female_avg.iloc[i]['lon']],
                  popup=df_female_avg.iloc[i]['CountryName']).add_to(m1)

folium.LayerControl().add_to(m1)

# Save to html
m1.save('map_data.html')
