import pandas as pd
import utils as uti


def daily_average(data, monitoring_station, pollutant):
    """Only Returns the days with data Not the ones with no data"""
    table = data[monitoring_station].values.tolist()
    table.append(['None', 'None'])

    temp_day = None
    daily_temps = []
    all_daily_temps = []

    table.sort(key=lambda elem: elem[0])

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
    table = data[monitoring_station].values.tolist()
    table.append(['None', 'None'])

    temp_day = None
    daily_temps = []
    all_daily_temps = []

    table.sort(key=lambda elem: elem[0])

    for x in table:
        if x[0] == temp_day:
            if x[pollutant] != 'No data':
                daily_temps.append(float(x[pollutant]))
        else:

            temp_day = x[0]
            if len(daily_temps) > 0:
                if len(daily_temps) != 1:
                    daily_temps = sorted(daily_temps)
                    if len(daily_temps) % 2 == 0:
                        a = len(daily_temps) // 2
                        b = a - 1
                    else:
                        a = (len(daily_temps) - 1) // 2
                        b = a + 1

                    all_daily_temps.append(round(((daily_temps[a] + daily_temps[b]) / 2), 4))
                else:
                    all_daily_temps.append(daily_temps[0])
                daily_temps = []

    return all_daily_temps


def hourly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    table = data[monitoring_station].values.tolist()
    table.append(['None', 'None'])

    temp_hour = None
    hourly_temps = []
    all_temps = []

    table.sort(key=lambda elem: elem[1])

    for x in table:
        if x[1] == temp_hour:
            if x[pollutant] != 'No data':
                hourly_temps.append(float(x[pollutant]))
        else:
            temp_hour = x[1]
            if len(hourly_temps) > 0:
                all_temps.append(uti.meannvalue(hourly_temps))
                hourly_temps = []

    return all_temps


def monthly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    table = data[monitoring_station].values.tolist()
    table.append(['NoneNone', 'NoneNone'])

    temp_month = 'None'
    monthly_temps = []
    all_temps = []

    table.sort(key=lambda elem: elem[0])

    for x in table:
        if x[0][0:7] == temp_month:
            if x[pollutant] != 'No data':
                monthly_temps.append(float(x[pollutant]))
        else:
            temp_month = x[0][0:7]
            if len(monthly_temps) > 0:
                all_temps.append(uti.meannvalue(monthly_temps))
                monthly_temps = []

    return all_temps


def peak_hour_date(data, date, monitoring_station, pollutant):
    """Your documentation goes here"""
    table = data[monitoring_station].values.tolist()

    temp_hour = -1000
    temp_table = []
    peak_hour = ''

    for x in table:
        if x[0] == date:
            temp_table.append(x)

    table = temp_table

    check = False
    for x in table:
        if float(x[pollutant]) > temp_hour:
            peak_hour = x[1]
            temp_hour = float(x[pollutant])
            check = True

    return peak_hour, temp_hour, check


def count_missing_data(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    table = data[monitoring_station].values.tolist()

    count = 0
    for x in table:
        if x[pollutant] == 'No data':
            count += 1

    return count


def fill_missing_data(data, new_value, monitoring_station, pollutant):
    """Your documentation goes here"""
    table = data[monitoring_station].values.tolist()
    return_table = []

    for x in table:
        if x[pollutant] == 'No data':
            new_line = x
            new_line[pollutant] = new_value
            return_table.append(new_line)
        else:
            return_table.append(x)

    return return_table

