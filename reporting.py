import pandas as pd
import utils as uti


def daily_average(data, monitoring_station, pollutant):
    """Only Returns the days with data Not the ones with no data"""
    table = data[monitoring_station].values.tolist()

    temp_day = None
    daily_temps = []
    all_daily_temps = []
    for x in table:
        if x[0] == temp_day:
            if x[pollutant] != 'No data':
                daily_temps.append(float(x[pollutant]))
        else:

            temp_day = x[0]
            if len(daily_temps) > 0:
                all_daily_temps.append(uti.meannvalue(daily_temps))
                daily_temps = []

    return all_daily_temps


def daily_median(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    pass


def hourly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    pass


def monthly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    pass


def peak_hour_date(data, date, monitoring_station, pollutant):
    """Your documentation goes here"""
    pass


def count_missing_data(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    pass


def fill_missing_data(data, new_value, monitoring_station, pollutant):
    """Your documentation goes here"""
    pass
