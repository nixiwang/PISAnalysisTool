"""
Processing map data
"""

import pandas as pd
import folium
from pisa_analysis_tool.preprocessing import make_country_dict, add_lat_long, remove_country


# json file with countries' name and their geographical data
COUNTRY_GEO = './data/world_ogr.json'
# gender coefficient data for countries
GENDER_COEFF = './data/gender_coef.csv'

# preprocessing raw data
F_AVG_CSV = './data/world_score_female_avg.csv'
M_AVG_CSV = './data/world_score_male_avg.csv'
C_AVG_CSV = './data/world_score_avg.csv'

COUNTRY_DICT = make_country_dict()


M_AVG_DICT, COUNTRY_LST = add_lat_long(M_AVG_CSV, COUNTRY_DICT)
F_AVG_DICT, COUNTRY_LST1 = add_lat_long(F_AVG_CSV, COUNTRY_DICT)
C_AVG_DICT, COUNTRY_LST2 = add_lat_long(C_AVG_CSV, COUNTRY_DICT)

DF_M_AVG = pd.DataFrame.from_dict(M_AVG_DICT)
DF_F_AVG = pd.DataFrame.from_dict(F_AVG_DICT)
DF_C_AVG = pd.DataFrame.from_dict(C_AVG_DICT)

NEED_COUNTRY = remove_country(GENDER_COEFF, COUNTRY_DICT, COUNTRY_LST)
DF_INDICATOR = pd.DataFrame.from_dict(NEED_COUNTRY)


# initalize the position when the html file is open
M1 = folium.Map(location=[50, 15], zoom_start=1.5)


# Add the color for the chloropleth:
M1.choropleth(
    geo_data=COUNTRY_GEO,
    name='Male Average Mathematics Score for Each Country',
    data=DF_M_AVG,
    columns=['CountryName', 'Mathematics'],
    key_on='properties.NAME',
    fill_color='YlOrBr',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='Male Average Mathematics Score'
)  # Male Average Mathematics Score distribution layer
M1.choropleth(
    geo_data=COUNTRY_GEO,
    name='Male Average Science Score for Each Country',
    data=DF_M_AVG,
    columns=['CountryName', 'Reading'],
    key_on='properties.NAME',
    fill_color='PuBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='Male Average Science Score'
)  # Male Average Science Score distribution layer
M1.choropleth(
    geo_data=COUNTRY_GEO,
    name='Male Average Reading Score for Each Country',
    data=DF_M_AVG,
    columns=['CountryName', 'Science'],
    key_on='properties.NAME',
    fill_color='GnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='Male Average Reading Score'
)  # Male Average Reading Score distribution layer
M1.choropleth(
    geo_data=COUNTRY_GEO,
    name='Female Average Mathematics Score for Each Country',
    data=DF_F_AVG,
    columns=['CountryName', 'Mathematics'],
    key_on='properties.NAME',
    fill_color='YlOrBr',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='Female Average Mathematics Score'
)  # Female Average Mathematics Score distribution layer
M1.choropleth(
    geo_data=COUNTRY_GEO,
    name='Female Average Science Score for Each Country',
    data=DF_F_AVG,
    columns=['CountryName', 'Reading'],
    key_on='properties.NAME',
    fill_color='PuRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='Female Average Science Score'
)  # Female Average Science Score distribution layer
M1.choropleth(
    geo_data=COUNTRY_GEO,
    name='Female Average Reading Score for Each Country',
    data=DF_F_AVG,
    columns=['CountryName', 'Science'],
    key_on='properties.NAME',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='Female Average Reading Score'
)  # Female Average Reading Score distribution layer
M1.choropleth(
    geo_data=COUNTRY_GEO,
    name='Countries\' indicator score',
    data=DF_INDICATOR,
    columns=['CountryName', 'indicator'],
    key_on='properties.NAME',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='#8c8c8c',
    legend_name='World Bank gender parity index(GPI)'
)  # World Bank gender parity index(GPI) layer


# add markers for each country in the csv file
for i in range(0, len(DF_F_AVG)):
    folium.Marker([DF_F_AVG.iloc[i]['lat'],
                   DF_F_AVG.iloc[i]['lon']],
                  popup=DF_F_AVG.iloc[i]['CountryName']).add_to(M1)

folium.LayerControl().add_to(M1)

# Save to html
M1.save('map_data.html')
