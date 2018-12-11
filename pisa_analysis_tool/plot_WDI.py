# A grand function that takes as input a list of country codes, then uses our function above WB_country_data to
# get a list of indicators for each country,then plot a line diagram
def plot_indicators(country_list, indicator, start=2000, end=2015):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import wbdata
    import re
    ind = wbdata.get_indicator(indicator, display=False)
    # capture the title which includes the unit after bracket
    title = ind[0]['name']
    # now take entire text from first letter to before opening bracket
    title = title[:title.find('(')-1]
    # this is the patter to match anything between two brackets
    p = re.compile('\((.*?)\)')
    ylab = p.findall(ind[0]['name'])[0]
    sns.set_style('white')
    fig, axis = plt.subplots()
    for c in country_list:
        axis.plot(range(start,end+1), country_data(c,indicator,start,end))
    plt.legend(country_list)
    plt.title(title)
    plt.ylabel(ylab)
    plt.show()