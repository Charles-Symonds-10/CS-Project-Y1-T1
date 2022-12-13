import requests
import datetime
import pandas as pd


def get_all_site_locations(information_type='@GroupName', Print=True):
    """Your documentation goes here"""
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Information/Groups/Json"
    url = endpoint
    res = requests.get(url)
    locations = pd.DataFrame.from_dict(res.json()['Groups']['Group'])

    if Print:
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
            print(locations[information_type])
            input('Press Enter to Continue')

    return locations


def get_description_of_location(row=0):
    """Your documentation goes here"""
    locations = get_all_site_locations(Print=False)
    if row >= len(locations):
        print('This row does not exist')
        input('Press Enter to Continue')
    else:
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
            print(locations.iloc[row])
        input('Press Enter to Continue')


def get_all_pollutant_types(information_type=None, Print=True):
    """Your documentation goes here"""
    if information_type is None:
        information_type = ['@SpeciesCode', '@SpeciesName']

    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Information/Species/Json"
    url = endpoint
    res = requests.get(url)
    pollutants = pd.DataFrame.from_dict(res.json()['AirQualitySpecies']['Species'])

    if Print:
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
            print(pollutants[information_type])
            input('Press Enter to Continue')

    return pollutants


def get_description_of_pollutant(row=0):
    pollutants = get_all_pollutant_types(Print=False)
    if row >= len(pollutants):
        print('This row does not exist')
        input('Press Enter to Continue')
    else:
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
            print(pollutants.iloc[row])
        input('Press Enter to Continue')


def get_site_codes(Print=True, group_name='All', information_type=None):
    if information_type is None:
        information_type = ['@SiteCode', '@SiteName']

    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSites/GroupName={GroupName}/Json"

    url = endpoint.format(
        GroupName=group_name
    )

    res = requests.get(url)
    site_codes = pd.DataFrame.from_dict(res.json()['Sites']['Site'])

    if Print:
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None):
            print(site_codes[information_type])
            input('Press Enter to Continue')
    return site_codes


def get_data_of_certain_day(start_date=None, end_date=None, site_code='BX1', species_code='NO2'):
    start_date = datetime.date.today() - datetime.timedelta(days=3) if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date

    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={SiteCode}/SpeciesCode={SpeciesCode}/StartDate={StartDate}/EndDate={EndDate}/Json"

    url = endpoint.format(
        SiteCode=site_code,
        SpeciesCode=species_code,
        StartDate=start_date,
        EndDate=end_date
    )

    res = requests.get(url)

    data = []
    max_value = -1000
    for x in res.json()['RawAQData']['Data']:
        data.append(x['@Value'])
        try:
            temp = float(x['@Value'])
            if temp > max_value:
                max_value = temp
        except:
            pass

    return data, max_value


def create_scatter_graph(height=15, width=24):
    graph = []
    for x in range(height):
        temp = []
        for y in range(width):
            temp.append('  ')
        graph.append(temp)

    for x in range(1, height - 1):
        if len(str(x)) == 1:
            graph[x + 1][0] = '0' + str(x)
        else:
            graph[x + 1][0] = str(x)

    for x in range(1, height):
        graph[x][1] = '| '

    for y in range(width - 1, 1, -1):
        graph[1][y] = '--'

    for y in range(1, width - 1):
        if len(str(y)) == 1:
            graph[0][y + 1] = '0' + str(y)
        else:
            graph[0][y + 1] = str(y)

    graph[1][0] = graph[0][1] = '  '
    graph[1][1] = '+ '

    return graph


def create_graph_with_data(site_code, species_code):
    data, max_value = get_data_of_certain_day(site_code=site_code, species_code=species_code)
    graph = create_scatter_graph(width=(2 + len(data)))

    if max_value == -1000:
        print('There are no value of data for this time and location')
        input('Press Enter to Continue: ')
    else:
        for x in range(len(data)):
            temp = int(round(float(data[x]), 0))
            y_val = int(((temp * 13) // max_value) + 2)
            graph[y_val][x + 2] = 'xx'

    for x in range(len(graph) - 1, -1, -1):
        print(' '.join(graph[x]))


def find_data(species_code='NO2'):
    codes = get_site_codes(Print=False)
    for x in codes['@SiteCode']:
        data, max_values = get_data_of_certain_day(site_code=x, species_code=species_code)
        if max_values > 0:
            print(x)
            print(data)
            print(max_values)
            option = input('Press Enter to Continue or (q) to Quit: ')
            if option == 'q':
                break


