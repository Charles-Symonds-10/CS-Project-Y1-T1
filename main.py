import reporting as rep
import intelligence as intel
import monitoring as mon
import pandas as pd


# This is the Function for the main menu it will display all the various options
# This main function also links all the other functions
def main_menu():
    """This function takes user input to run all the different functions across all the different files

    Args:
        No Arguments

    returns:
        Returns Nothing

        """

    # While Run is true,  the program is running
    run = True
    # This is the main loop for the whole program
    while run:
        # This input is the first menu that is displayed and allows the user to decide what module they would like
        # to use, Choice is the response from the user it should be a single letter, but there is error checking
        choice = input('''
• R - Access the PR module
• I - Access the MI module
• M - Access the RM module
• A - Print the About text
• Q - Quit the application
: ''')
        # printing 100 blank lines just neatens up the text output making it easier to read
        print('\n' * 100)
        # This is if statement checks that it was a string that was input as if it isn't an error would be raised
        if type(choice) is str:
            # This sets what ever the string was to the upper case so the lower or upper case could be input
            choice = choice.upper()
            # This if statement checks to see if the user input R or r as they want to access the reporting menu
            if choice == 'R':
                # This function runs the reporting menu
                reporting_menu()
            # This if statement checks to see if the user input I or i as they want to access the intelligence menu
            elif choice == 'I':
                # This function runs the intelligence menu
                intelligence_menu()
            # This if statement checks to see if the user input M or m as they want to access the monitoring menu
            elif choice == 'M':
                # This function runs the monitoring menu
                monitoring_menu()
            # This if statement checks to see if the user input A or a as they want to access the about function
            elif choice == 'A':
                # This function returns information about the candidate and the course
                about()
            # This if statement checks to see if the user input Q or q as they want to quit the program
            elif choice == 'Q':
                # This quit function returns False setting run to false means that the next time that the main
                # loop is checked the program is closed
                run = quit()
            # if the string is not any of the options above then this statement is printed to inform the user
            else:
                # I use input rater then print as it gives the user time to read the problem
                input('''That's not one of the options: [Press Enter to Continue]: ''')
        # If the input isn't a string then this else statement is used
        else:
            # I use input rater then print as it gives the user time to read the problem
            input('''That's not one of the options: [Press Enter to Continue]: ''')


# This is the function that is called when the user selects the reporting menu in the main menu function above
# This menu allows access to all the functions in the reporting module
def reporting_menu():
    """ This function takes no args and doesn't return any values, it takes user inputs to navigate the reporting
    functions and displace data

    Args:
        No Arguments

    returns:
        Returns Nothing
        """

    # Data is a dictionary linking the name of the location that data was recorded from and a pandas
    # data frame that is formed from the given csv files
    data = {'Marylebone Road': pd.read_csv('data/Pollution-London Marylebone Road.csv'),
            'N. Kensington': pd.read_csv('data/Pollution-London N Kensington.csv'),
            'Harlington': pd.read_csv('data/Pollution-London Harlington.csv')}
    # pollutants is a dictionary linking the names of the pollutants to their index within the pandas data frame
    pollutants = {'Nitric Oxide': 2, 'PM10': 3, 'PM2.5': 4}

    # This is the loop to find the monitoring station the user wants to see it uses while True,
    # which can only be broken by the break or break point statements that is implement bellow
    while True:
        # printing 100 blank lines just neatens up the text output making it easier to read
        print('\n' * 100)
        # This is the first choice for the user, of which location the user would like to see the data from
        # The expected output is a number 1 - 3 that is used bellow
        choice = str(input('''
Where would you like to Report on: 
(1), Marylebone Road, 
(2), N. Kensington, 
(3), Harlington,
(Enter the Number): '''))
        # printing 100 blank lines just neatens up the text output making it easier to read
        print('\n' * 100)

        # The input is checked to be a string as a form of error checking
        if type(choice) is str:
            # If the user inputs 1 then the user wants to see the data from 'Marylebone Road'
            if choice == '1':
                # The monitoring station is set to 'Marylebone Road' for later use
                monitoring_station = 'Marylebone Road'
                # The While loop above is then broken here
                break
            # If the user inputs 2 then the user wants to see the data from 'N. Kensington'
            elif choice == '2':
                # The monitoring station is set to 'N. Kensington'' for later use
                monitoring_station = 'N. Kensington'
                # The While loop above is then broken here
                break
            # If the user inputs 3 then the user wants to see the data from 'Harlington'
            elif choice == '3':
                # The monitoring station is set to 'Harlington' for later use
                monitoring_station = 'Harlington'
                # The While loop above is then broken here
                break
            # This statement is input if none of the if statements are satisfied above
            else:
                input('''That's not one of the options: [Press Enter to Continue]: ''')
        # This statement is input if what was inout was not a string
        else:
            input('''That's not one of the options: [Press Enter to Continue]: ''')

    # This the loop to find the pollutant that the user wants the data from it uses while True,
    # which can only be broken by the break or break point statements that is implement bellow
    while True:
        # This is the second choice for the user, of which pollutant the user would like to see the data from
        # The expected output is a number 1 - 3 that is used bellow
        choice = str(input('''
Which Pollutant would you like to examine:
(1) Nitric Oxide, 
(2) PM10, 
(3) PM2.5, 
(Enter the Number): '''))
        # printing 100 blank lines just neatens up the text output making it easier to read
        print('\n' * 100)

        # The input is checked to be a string as a form of error checking
        if type(choice) is str:
            # If the user inputs 1 then the user wants to see the data from 'Nitric Oxide'
            if choice == '1':
                # pollutant is set to 'Nitric Oxide' for later use
                pollutant = 'Nitric Oxide'
                # The While loop above is then broken here
                break
            # If the user inputs 2 then the user wants to see the data from 'PM10'
            elif choice == '2':
                # pollutant is set to 'PM10' for later use
                pollutant = 'PM10'
                # The While loop above is then broken here
                break
            # If the user inputs 3 then the user wants to see the data from 'PM2.5'
            elif choice == '3':
                # pollutant is set to 'PM2.5' for later use
                pollutant = 'PM2.5'
                # The While loop above is then broken here
                break
            # This statement is input if none of the if statements are satisfied above
            else:
                input('''That's not one of the options: [Press Enter to Continue]: ''')
        # This statement is input if what was inout was not a string
        else:
            input('''That's not one of the options: [Press Enter to Continue]: ''')

    # This is the while loop that is used to find what function the user would like to do, it uses while True,
    # which can only be broken by the break or break point statements that is implement bellow
    while True:
        # This is the Third choice for the user, of which function the user would like to complete with the data
        # The expected output is a number 1 - 7 that is used bellow
        choice = str(input('''
What Function Would you like to Apply:
(1) daily_average
(2) daily_median
(3) hourly_average
(4) monthly_average
(5) peak_hour_date
(6) count_missing_data
(7) fill_missing_data
(Enter the Number): '''))
        # printing 100 blank lines just neatens up the text output making it easier to read
        print('\n' * 100)

        # The input is checked to be a string as a form of error checking
        if type(choice) is str:
            # If the user inputs 1 then they want to find daily_average of the monitoring station and
            # pollutant they selected
            if choice == '1':
                # The daily_average function returns a list of values
                daily_average_values = rep.daily_average(data, monitoring_station, pollutants[pollutant])
                # I then print out the amount of the values and the values themselves
                print(len(daily_average_values), daily_average_values)
                # I have an input to allow the user time to read the values they requested
                input('Press Enter to Continue: ')
                # The While loop above is then broken here
                break

            # If the user inputs 2 then they want to find daily_median of the monitoring station and
            # pollutant they selected
            elif choice == '2':
                # The daily_median function returns a list of values
                daily_median_values = rep.daily_median(data, monitoring_station, pollutants[pollutant])
                # I then print out the amount of the values and the values themselves
                print(len(daily_median_values), daily_median_values)
                # I have an input to allow the user time to read the values they requested
                input('Press Enter to Continue: ')
                # The While loop above is then broken here
                break

            # If the user inputs 3 then they want to find hourly_average of the monitoring station and
            # pollutant they selected
            elif choice == '3':
                # The hourly_average function returns a list of values
                hourly_average_values = rep.hourly_average(data, monitoring_station, pollutants[pollutant])
                # I then print out the amount of the values and the values themselves
                print(len(hourly_average_values), hourly_average_values)
                # I have an input to allow the user time to read the values they requested
                input('Press Enter to Continue: ')
                # The While loop above is then broken here
                break

            # If the user inputs 4 then they want to find monthly_average of the monitoring station and
            # pollutant they selected
            elif choice == '4':
                # The monthly_average function returns a list of values
                monthly_average_values = rep.monthly_average(data, monitoring_station, pollutants[pollutant])
                # I then print out the amount of the values and the values themselves
                print(len(monthly_average_values), monthly_average_values)
                # I have an input to allow the user time to read the values they requested
                input('Press Enter to Continue: ')
                # The While loop above is then broken here
                break

            # If the user inputs 5 then they want to find peak_hour_date of the monitoring station and
            # pollutant they selected
            elif choice == '5':
                # This loop is to make sre that an accepted date is input
                while True:
                    # This takes the users input for the date and assigns it to the date variable
                    date = input('''
Please Enter the Date you would like to have the peak hour for: ('YYYY-MM-DD'): ''')

                    # a try function is used as a error could be brought up if the date is invalid
                    try:
                        # The peak_hour_date function returns a list of values
                        peak_hour_data_value = rep.peak_hour_date(data, date, monitoring_station, pollutants[pollutant])
                        if peak_hour_data_value[2]:
                            # I then print out the peak hour and the hour itself
                            print(peak_hour_data_value[0:2])
                            # I have an input to allow the user time to read the values they requested
                            input('Press Enter to Continue: ')
                            # The While loop above is then broken here
                            break
                        # If the function check is false: there is no data at the input date
                        else:
                            # This message is output if there is no data for that date
                            input("That's Not a Valid Data please try again: ")
                    # If the date wasn't a valid date and causes this error then:
                    except:
                        # This message is output if the input was invalid
                        input("That's Not a Valid Data please try again: ")
                # The While loop above is then broken here
                break

            # If the user inputs 6 then they want to find count_missing_data of the monitoring station and
            # pollutant they selected
            elif choice == '6':
                # The count_missing_data function returns a list of values
                total_missing_data = rep.count_missing_data(data, monitoring_station, pollutants[pollutant])
                # I then print out the amount of missing values
                print(total_missing_data)
                # I have an input to allow the user time to read the values they requested
                input('Press Enter to Continue: ')
                # The While loop above is then broken here
                break

            # If the user inputs 7 then they want to find fill_missing_data of the monitoring station and
            # pollutant they selected
            elif choice == '7':
                # The user is requested to input a new value witch thanks to pythons list flexibility can be
                # almost anything
                new_value = input('''
Please enter your value to replace all 'No data' values with: (x.y, eg: 2.4): ''')
                # The _ function returns a list of values
                filled_missing_data = rep.fill_missing_data(data, new_value, monitoring_station, pollutants[pollutant])
                # I then print out the table with the missing data values filled with the new value
                print(filled_missing_data)
                # I have an input to allow the user time to read the values they requested
                input('Press Enter to Continue: ')
                # The While loop above is then broken here
                break

            # This statement is input if none of the if statements are satisfied above
            else:
                input('''That's not one of the options: [Press Enter to Continue]: ''')
        # This statement is input if what was inout was not a string
        else:
            input('''That's not one of the options: [Press Enter to Continue]: ''')

    # printing 100 blank lines just neatens up the text output making it easier to read
    print('\n' * 100)


# This function is called when the user selects the intelligence menu in the main menu function above
# This menu allows access to all the functions in the intelligence module
def intelligence_menu():
    """This function takes no args and returns nothing, it uses user input to navigate the intelligence functions
    Args:
        No Arguments

    returns:
        Returns Nothing
         """

    # This is the main menu function of the intelligence menu, it uses while True,
    # which can only be broken by the break or break point statements that is implement bellow
    while True:
        # This input allows the user to select witch function they would like to perform from the intelligence module
        # This input should be a number 1 - 4 but there is error checking
        choice = input('''
What Function would you like to perform: 
(1) Find all of the Red pixels
(2) Find all of the Cyan pixels
(3) Detect the connected components
(4) Detect the connected components sorted : ''')
        # printing 100 blank lines just neatens up the text output making it easier to read
        print('\n' * 100)
        # This is if statement checks that it was a string that was input as if it isn't an error would be raised
        if type(choice) is str:
            # If the user inputs 1 then they are looking to do the find_red_pixels function
            if choice == '1':
                # This function takes an image stored in an adjacent file and manipulates it to only contain the
                # red pixels the new image is then saved
                intel.find_red_pixels('map.png')
                # The While loop above is then broken here
                break
            # If the user inputs 2 then they are looking to do the find_cyan_pixels function
            elif choice == '2':
                # This function takes an image stored in an adjacent file and manipulates it to only contain the
                # cyan pixels the new image is then saved
                intel.find_cyan_pixels('map.png')
                # The While loop above is then broken here
                break
            # If the user inputs 3 then they are looking to do the detect_connected_components function
            elif choice == '3':
                # This function takes an image stored in an adjacent file and manipulates it to find all the
                # connected pixels and then saves a list of the connected components to a text file
                intel.detect_connected_components()
                # The While loop above is then broken here
                break
            # If the user inputs 4 then they are looking to do the detect_connected_components_sorted function
            elif choice == '4':
                # MARK is a 2d array that is returned when the detect_connected_components is run this can then be used
                # to display the 2 largest connected components
                MARK = intel.detect_connected_components()
                # This function takes MARK and then sorts the connected components and stores them to a new txt file
                # It also saves an image of the two largest connected components
                intel.detect_connected_components_sorted(MARK)
                # The While loop above is then broken here
                break

            # if the string is not any of the options above then this statement is printed to inform the user
            else:
                # I use input rater then print as it gives the user time to read the problem
                input('''That's not one of the options: [Press Enter to Continue]: ''')
        # If the input isn't a string then this else statement is used
        else:
            # I use input rater then print as it gives the user time to read the problem
            input('''That's not one of the options: [Press Enter to Continue]: ''')

    # printing 100 blank lines just neatens up the text output making it easier to read
    print('\n' * 100)


# This function is called when the user selects the monitoring menu in the main menu function above
# This menu allows access to all the functions in the monitoring module
def monitoring_menu():
    """This function takes no args and returns nothing, it uses user input to navigate the monitoring functions
    Args:
        No Arguments

    returns:
        Returns Nothing
         """

    # This is the main menu function of the monitoring menu, it uses while True,
    # which can only be broken by the break or break point statements that is implement bellow
    while True:
        # This input allows the user to select witch function they would like to perform from the monitoring module
        # This input should be a number 1 - 7 but there is error checking
        choice = input('''
What Function would you like to perform: 
(1) Output all locations data is being Recorded
(2) Output the details of a location
(3) Output all the pollutant types
(4) Output the details of a pollutant 
(5) Output the site codes
(6) Outputs locations that have recent data 
(7) Output a graph of a recent day given Site code and Pollutant ''')
        # printing 100 blank lines just neatens up the text output making it easier to read
        print('\n' * 100)

        # This is if statement checks that it was a string that was input as if it isn't an error would be raised
        if type(choice) is str:
            # If the user inputs 1 then they are looking to see all the site locations displayed
            if choice == '1':
                # This function makes a call to the API and then displays all the site locations
                mon.get_all_site_locations()
                # The While loop above is then broken here
                break

            # if the user inputs 2 then they are looking to see the description of a particular site
            elif choice == '2':
                # The row is the row corresponding to the site that the user would like to see the details on
                row = int(input('''
Please Enter the row of the location that you would like to see: '''))
                # This function displays just the row of the site that was requested and its details
                mon.get_description_of_location(row)
                # The While loop above is then broken here
                break

            # If the user inputs 3 then they are looking to display all the types of pollutants and their codes
            elif choice == '3':
                # This function displays all the pollutants including there codes
                mon.get_all_pollutant_types()
                # The While loop above is then broken here
                break

            # If the user inputs 4 then they are looking to see the description of a particular pollutant
            elif choice == '4':
                # The row is the row corresponding to the pollutant that the user would like to see the details on
                row = int(input('''
Please Enter the row of the location that you would like to see: '''))
                # This function displays the description of a specific pollutant given the row
                mon.get_description_of_pollutant(row)
                # The While loop above is then broken here
                break

            # If the user inputs 5 they are looking to see all the site codes, so they can be used later on
            elif choice == '5':
                # This function displays all the site codes for the user
                mon.get_site_codes()
                # The While loop above is then broken here
                break

            #  If the user inputs 6 they are looking for a  site location that has recent data
            # given a pollutant
            elif choice == '6':
                # The pollutant is set here by the user and used in the function bellow
                pollutant = input('''
Please Enter the pollutant that you would like to see: ''')
                # This function will return site codes given a pollutant code
                # This function is used in tandem with the display function bellow
                mon.find_data(species_code=pollutant)
                # The While loop above is then broken here
                break

            # If the user inputs 7 they are looking for the data of a recent day to be displayed on a text
            # based scatter graph for a clear variation of the selected pollutant over a day
            elif choice == '7':
                # The selected site is input here to be used in the function bellow
                site_code = input('''
Please Enter the Site Code of the place you would like to draw a graph (Recommend: 'BX1'):  ''')
                # The selected pollutant code is input here to be used bellow
                species_code = input('''
Please Enter the Species Code of the pollutant you would like to draw a graph (Recommend: 'NO2'): ''')
                # This function takes site code and a pollutant code (species code)
                # and displays a graph of a recent day of the data
                mon.create_graph_with_data(site_code, species_code)
                # The While loop above is then broken here
                break

            # if the string is not any of the options above then this statement is printed to inform the user
            else:
                # I use input rater then print as it gives the user time to read the problem
                input('''That's not one of the options: [Press Enter to Continue]: ''')
        # If the input isn't a string then this else statement is used
        else:
            # I use input rater then print as it gives the user time to read the problem
            input('''That's not one of the options: [Press Enter to Continue]: ''')

    # printing 100 blank lines just neatens up the text output making it easier to read
    print('\n' * 100)


# This is a simple function that when called displays the course code and my candidate number
def about():
    """Takes no input and returns None, Displays the course code and my candidate number

    Args:
        No Arguments

    returns:
        Returns Nothing
    """
    print('ECM1400')
    print('Candidate Number: 234342')
    input('Press Enter to Continue')


#  This is a very simple function that returns false used to set run too false to stop the main loop
def quit():
    """Takes no input just returns false used to set run too false to stop the main loop

    Args:
        No Arguments

    returns:
        False: 'Bool'
    """
    return False


# Runs the main menu function so run the whole program
if __name__ == '__main__':
    main_menu()
