import numpy as np


def daily_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""

    pollution = {
        'no': 2,
        'pm10': 3,
        'pm25': 4,
    }
    pol = pollution[pollutant]

    with open(data + '/' + monitoring_station, 'r') as csv_file:
        pol_data = []
        for x in csv_file:
            pol_data.append(x.split(','))

        csv_file.close()

        pol_data.pop(0)

        temp = ''
        all_daily_temps = []
        for x in pol_data:
            if x[0] != temp:
                if temp != '':
                    all_daily_temps.append(np.round_(np.average(daily), 4))
                temp = x[0]
                daily = []
            else:
                if x[pol] != 'No data':
                    daily.append(float(x[pol]))

    return all_daily_temps


def daily_median(data, monitoring_station, pollutant):
    """Your documentation goes here"""

    pollution = {
        'no': 2,
        'pm10': 3,
        'pm25': 4,
    }
    pol = pollution[pollutant]

    with open(data + '/' + monitoring_station, 'r') as csv_file:
        pol_data = []
        for x in csv_file:
            pol_data.append(x.split(','))

        csv_file.close()

        pol_data.pop(0)

        temp = ''
        all_daily_temps = []
        for x in pol_data:
            if x[0] != temp:
                if temp != '':
                    all_daily_temps.append(np.round_(np.median(daily), 4))
                temp = x[0]
                daily = []
            else:
                if x[pol] != 'No data':
                    daily.append(float(x[pol]))

    return all_daily_temps


def hourly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""

    ## Your code goes here


def monthly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""

    ## Your code goes here


def peak_hour_date(data, date, monitoring_station, pollutant):
    """Your documentation goes here"""

    ## Your code goes here


def count_missing_data(data, monitoring_station, pollutant):
    """Your documentation goes here"""

    ## Your code goes here


def fill_missing_data(data, new_value, monitoring_station, pollutant):
    """Your documentation goes here"""

    ## Your code goes here


print(daily_median('data', 'Pollution-London Harlington.csv', 'no'))
