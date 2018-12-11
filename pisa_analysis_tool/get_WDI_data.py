"""
CSE583 Project
===========================================
Getting World Bank data from wbdata pakcage
===========================================
This module searches the indicators in the World Bank data and get a dataframe accordingly.
"""


def country_data(country_code, indicator, start=2015, end=2015):
    """
    A function for specific country lookup.

    :param country_code: a string of three letters indicatoring country name
    :param indicator: the indicator of database, a string
    :param start: start date of the year
    :param end: end year
    :return: a dataframe of this indicator
    """
    import datetime
    import wbdata
    data_dates = (datetime.datetime(start, 1, 1), datetime.datetime(end, 1, 1))
    # call the api
    data = wbdata.get_dataframe({indicator: 'indicator'},
                                country=country_code,
                                data_date=data_dates,
                                convert_date=True,
                                keep_levels=False)

    data = data.reset_index()
    # data = data.dropna() #if I want I can drop the na's
    return data[['indicator']]


def WB_country_data(indicator, start=2015, end=2015):
    """
    A function for for getting gender indicator data for all countries

    :param country_code: a string of three letters indicatoring country name
    :param indicator: the indicator of database, a string
    :param start: start date of the year
    :param end: end year
    :return: a dataframe of this indicator
    """
    import datetime
    import wbdata
    data_dates = (datetime.datetime(start, 1, 1), datetime.datetime(end, 1, 1))
    # call the api
    data = wbdata.get_dataframe({indicator: 'indicator'},
                                data_date=data_dates,
                                convert_date=True,
                                keep_levels=False)

    data = data.reset_index()
    # data = data.dropna() #if I want I can drop the na's
    return data[['indicator']]


def main():
    """
    Run to get gender equity indicator/coefficient for all countries
    """
    df_wb = WB_country_data('SE.ENR.SECO.FM.ZS')
    df_wb['CountryName'] = df_wb.index
    return df_wb


if __name__ == '__main__':
    main()
