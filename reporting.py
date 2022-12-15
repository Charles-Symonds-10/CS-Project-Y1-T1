import pandas as pd
import utils as uti


def daily_average(data, monitoring_station, pollutant):
    """Takes data a monitoring station and a pollutant and returns all the daily averages in a list for the year,
    if there is data present for the given day.

    args:
        data: A 'dictionary' linking the monitoring stations to data frames of their given data
        monitoring_station: A 'string' of the chosen monitoring station
        pollutant: A 'integer' That corresponds to a given pollutant (defined in the menu)

    returns:
        A 'List' of average pollutant amounts for every day in the data frame"""

    # Creates a list of lists from the chosen monitoring station and the data dictionary
    table = data[monitoring_station].values.tolist()
    # Adds a null value to the end of the list of lists as a end point, to be used later.
    table.append(['None', 'None'])

    # Temporary Day a placeholder to allow me to compare the date between days to gain all the values for a given day
    temp_day = None
    # The list of all the values for a given day so the average can be calculated
    daily_values = []
    # The final list that contains all the daily average values, will be returned
    all_daily_ave_values = []

    # This functions sorts the table so that all values of a given day will be adjacent to one another
    # This is a security feature as if the data is already in order it has no effect
    # It uses a lambda function to sort by the second element (day)
    table.sort(key=lambda elem: elem[0])

    # For loop to navigate through the table of data
    for row in table:
        # Checks if the days are the same from the temporary day value to the value in the table
        if row[0] == temp_day:
            # If the day is the same then there is a check to see if there is a value in the table
            if row[pollutant] != 'No data':
                # If there is a value present then the value is added to the daily values list in float form
                # The pollutant acts as an index within in the row in the table
                daily_values.append(float(row[pollutant]))
        # If the day is not the same as the temporary value then:
        else:
            # The temporary days is updated with the new day
            temp_day = row[0]
            # Checking if daily values is empty as if it is there is no data to average and no data to add to the list
            # Removes days with no data
            if len(daily_values) > 0:
                # Adds the average of the daily data to the overall list
                # The average is found using the utils functions
                all_daily_ave_values.append(uti.meannvalue(daily_values))
                # Resets the list of daily values so there is no leak of values from day to day
                daily_values = []

    # returns all the daily values
    return all_daily_ave_values


def daily_median(data, monitoring_station, pollutant):
    """Takes data a monitoring station and a pollutant and returns all the daily medians in a list for the year,
    if there is data present for the given day.

    args:
        data: A 'dictionary' linking the monitoring stations to data frames of their given data
        monitoring_station: A 'string' of the chosen monitoring station
        pollutant: A 'integer' That corresponds to a given pollutant (defined in the menu)

    returns:
        A 'List' of median pollutant amounts for every day in the data frame"""

    # Creates a list of lists from the chosen monitoring station and the data dictionary
    table = data[monitoring_station].values.tolist()
    # Adds a null value to the end of the list of lists as a end point, to be used later.
    table.append(['None', 'None'])

    # Temporary Day a placeholder to allow me to compare the date between days to gain all the values for a given day
    temp_day = None
    # The list of all the values for a given day so the average can be calculated
    daily_values = []
    # The final list that contains all the daily average values, will be returned
    all_daily_med_values = []

    # This functions sorts the table so that all values of a given day will be adjacent to one another
    # This is a security feature as if the data is already in order it has no effect
    # It uses a lambda function to sort by the second element (day)
    table.sort(key=lambda elem: elem[0])

    #
    # For loop to navigate through the table of data
    for row in table:
        # Checks if the days are the same from the temporary day value to the value in the table
        if row[0] == temp_day:
            # If the day is the same then there is a check to see if there is a value in the table
            if row[pollutant] != 'No data':
                # If there is a value present then the value is added to the daily values list in float form
                # The pollutant acts as an index within in the row in the table
                daily_values.append(float(row[pollutant]))
        # If the day is not the same as the temporary value then:
        else:
            # The temporary days is updated with the new day
            temp_day = row[0]
            # Checking if daily values is empty as if it is there is no data to average and no data to add to the list
            # Removes days with no data
            if len(daily_values) > 0:
                # Checks to see if there is only one value in the daily temps as this value would be the median
                if len(daily_values) != 1:
                    # The daily values are then sorted so that the median is easier to find
                    daily_values = sorted(daily_values)
                    # Checks to see if there is an even number of values in the list
                    if len(daily_values) % 2 == 0:
                        # If there is an even amount then the indexes of the two middle values are found
                        a = len(daily_values) // 2
                        # As python has a 0 start point index the other middle value would be one less
                        b = a - 1
                    # If there is an odd number of values then:
                    else:
                        # The middle index value is found then the other middle index is the same.
                        a = (len(daily_values) - 1) // 2
                        b = a
                    # The median is then found by either adding the two even values together and dividing by 2
                    # or by adding two of the same nuber together and dividing by 2 to get the original number
                    # The value is also rounded to 4 decimal places for simplicity, it is also done at this stage to
                    # not lose value
                    all_daily_med_values.append(round(((daily_values[a] + daily_values[b]) / 2), 4))
                # If there is only one value then that value is the median
                else:
                    # Adding the only value to the list.
                    all_daily_med_values.append(daily_values[0])
                # Finally resetting the daily values
                daily_values = []

    # Returning the list of all of the daily values
    return all_daily_med_values


def hourly_average(data, monitoring_station, pollutant):
    """Takes data a monitoring station and a pollutant and returns all the hourly averages in a list for the year,
    if there is data present for the given hour.

    args:
        data: A 'dictionary' linking the monitoring stations to data frames of their given data
        monitoring_station: A 'string' of the chosen monitoring station
        pollutant: A 'integer' That corresponds to a given pollutant (defined in the menu)

    returns:
        A 'List' of average pollutant amounts for every hour in the data frame"""

    # Creates a list of lists from the chosen monitoring station and the data dictionary
    table = data[monitoring_station].values.tolist()
    # Adds a null value to the end of the list of lists as a end point, to be used later.
    table.append(['None', 'None'])

    # Temporary hour allows the comparison between different rows in the tabel
    temp_hour = None
    # A list of all the hourly values used to find the average
    hourly_values = []
    # A list of all the hourly values in the year that is given in the data frame
    all_hourly_values = []

    # Sorts all the data by the hour so that the rows of the same hour are adjacent to one another simplifying the
    # code. The Lambda function makes it so that the second value in the row is the value that is being sorted
    table.sort(key=lambda elem: elem[1])

    # For loop to navigate through the table of data
    for row in table:
        # Checks if the hours are the same from the temporary hour value to the value in the table
        if row[1] == temp_hour:
            # If the hour is the same then there is a check to see if there is a value in the table
            if row[pollutant] != 'No data':
                # If there is a value present then the value is added to the hourly values list in float form
                # The pollutant acts as an index within in the row in the table
                hourly_values.append(float(row[pollutant]))
        # If the hour is not the same as the temporary value then:
        else:
            # The temporary hour is updated with the new hour
            temp_hour = row[1]
            # Checking if hourly values is empty as if it is there is no data to average and no data to add to the list
            # Removes hours with no data
            if len(hourly_values) > 0:
                # Adds the average of the hourly data to the overall list
                # The average is found using the utils functions
                all_hourly_values.append(uti.meannvalue(hourly_values))
                # Resets the list of hourly values so there is no leak of values from hour to hour
                hourly_values = []

    # returns all the hourly values
    return all_hourly_values


def monthly_average(data, monitoring_station, pollutant):
    """Takes data a monitoring station and a pollutant and returns all the monthly averages in a list for the year,
    if there is data present for the given month.

    args:
        data: A 'dictionary' linking the monitoring stations to data frames of their given data
        monitoring_station: A 'string' of the chosen monitoring station
        pollutant: A 'integer' That corresponds to a given pollutant (defined in the menu)

    returns:
        A 'List' of average pollutant amounts for every month in the data frame"""

    # Creates a list of lists from the chosen monitoring station and the data dictionary
    table = data[monitoring_station].values.tolist()
    # Adds a null value to the end of the list of lists as an end point, to be used later.
    table.append(['None', 'None'])

    # Temporary month a placeholder to allow me to compare the date between months to gain all
    # the values for a given month.
    temp_month = None
    # The list of all the values for a given month so the average can be calculated
    monthly_values = []
    # The final list that contains all the monthly average values, will be returned
    all_monthly_ave_values = []

    # This functions sorts the table so that all values of a given day will be adjacent to one another
    # This is a security feature as if the data is already in order it has no effect
    # It uses a lambda function to sort by the second element (month)
    table.sort(key=lambda elem: elem[0])

    # For loop to navigate through the table of data
    for row in table:
        # Comparison between the temp month and the month in the row being looked at
        # The [0:7] allows me to look at just the year and the month and not the day
        if row[0][0:7] == temp_month:
            # If the month is the same then there is a check to see if there is a value in the table
            if row[pollutant] != 'No data':
                # If there is a value present then the value is added to the monthly values list in float form
                # The pollutant acts as an index within in the row in the table
                monthly_values.append(float(row[pollutant]))
        # If the day is not the same as the temporary value then:
        else:
            # The temporary month is updated with the new month
            temp_month = row[0][0:7]
            # Checking if monthly values is empty as if it is there is no data to average and no data to add to the list
            # Removes months with no data
            if len(monthly_values) > 0:
                # Adds the average of the monthly data to the overall list
                # The average is found using the utils functions
                all_monthly_ave_values.append(uti.meannvalue(monthly_values))
                # Monthly values is reset
                monthly_values = []

    # all the monthly values are returned in a list
    return all_monthly_ave_values


def peak_hour_date(data, date, monitoring_station, pollutant):
    """Takes the data dictionary and a monitoring_station and a pollutant and returns the peak hour in a day and returns
    the peak hour the max_pollutant and weather the data selected is within the data as (check)

    args:
        data: A 'dictionary' linking the monitoring stations to data frames of their given data
        date: A 'string' containing the chosen date in the form YYYY-MM-DD
        monitoring_station: A 'string' of the chosen monitoring station
        pollutant: A 'integer' That corresponds to a given pollutant (defined in the menu)

    returns:
        A 'string' of the peak hour
        A 'integer' of the max pollutant value
        A 'bool' in the form of check which is a check of weather the date is within the data
    """

    # Creates a list of lists from the chosen monitoring station and the data dictionary
    table = data[monitoring_station].values.tolist()

    # Setting the max pollution to a low value so that any value in the hour should be larger
    max_pollutant_value = -1000
    # Creates a temporary table so that all the values with the same date as that is input can be added to it.
    temp_table = []
    # Peak hour is the string of the YYYY-MM-DD witch is updated when max pollutant is
    peak_hour = ''

    # For loop to go through the table list of lists to find all the rows with the same date as is required
    for row in table:
        if row[0] == date:
            # if the row is of the required date then it is added to the temporary table
            temp_table.append(row)

    # The Check is set to false so that if it is unchanged then it will always be false
    check = False
    # For loop to go through all the rows in temp table to find which hour has the largest pollution value
    for row in temp_table:
        # Check to see if the pollution value of the row is greater than the max pollutant value
        if float(row[pollutant]) > max_pollutant_value:
            # If it is the case then the peak hour, max_pollutant_value, check is updated
            peak_hour = row[1]
            max_pollutant_value = float(row[pollutant])
            # Check needs only to be updated once for the chosen date to be valid
            check = True

    # The peak hour, max pollutant value and the check is returned
    return peak_hour, max_pollutant_value, check


def count_missing_data(data, monitoring_station, pollutant):
    """Takes data a monitoring station and a pollutant and returns a number witch corresponds to the total number of
       missing values for a given data set.

    args:
        data: A 'dictionary' linking the monitoring stations to data frames of their given data
        monitoring_station: A 'string' of the chosen monitoring station
        pollutant: A 'integer' That corresponds to a given pollutant (defined in the menu)

    returns:
        A 'integer' of the total number of missing data values """

    # Creates a list of lists from the chosen monitoring station and the data dictionary
    table = data[monitoring_station].values.tolist()

    # sets the count to 0 at the start
    count = 0
    # For loop that goes through all the rows of the table so that they can be check to
    # see if it contains a data value
    for row in table:
        # if the row contains no data count is incremented by 1
        if row[pollutant] == 'No data':
            count += 1

    # the count of no data is returned
    return count


def fill_missing_data(data, new_value, monitoring_station, pollutant):
    """Takes data,  monitoring station, pollutant and a new value, returns a list of lists with the new value
    replacing any empty values in the table.

    args:
        data: A 'dictionary' linking the monitoring stations to data frames of their given data
        monitoring_station: A 'string' of the chosen monitoring station
        pollutant: A 'integer' That corresponds to a given pollutant (defined in the menu)
        new_value: anything used to replace any data holes

    returns:
        A list of lists with the new value replacing any empty values in the table.  """

    # Creates a list of lists from the chosen monitoring station and the data dictionary
    table = data[monitoring_station].values.tolist()
    # A new table will be filled and if there is missing data then it will be replaced with the input value
    return_table = []

    # For loop to go through each row in the table
    for row in table:
        # Checks to see if the row has no value
        if row[pollutant] == 'No data':
            # If there is no data a new line is created then the value of the pollutant is updated
            new_line = row
            new_line[pollutant] = new_value
            # The new line is then added to the return table
            return_table.append(new_line)
        else:
            # if there is data then the original row is added to the return table
            return_table.append(row)

    # The return table is then returned
    return return_table

