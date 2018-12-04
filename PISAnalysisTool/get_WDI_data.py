# function for specific country lookup

def country_data(country_code, indicator, start=2015, end=2015):
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


# function for getting gender indicator data for all countries
def WB_country_data(indicator, start=2015, end=2015):
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
