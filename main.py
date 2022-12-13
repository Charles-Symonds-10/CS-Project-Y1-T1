import reporting as rep
import intelligence as intel
import monitoring as mon
import pandas as pd


def main_menu():
    """Your documentation goes here"""
    run = True
    while run:
        choice = input('''
• R - Access the PR module
• I - Access the MI module
• M - Access the RM module
• A - Print the About text
• Q - Quit the application
: ''')
        print('\n' * 100)
        if type(choice) is str:
            choice = choice.upper()
            if choice == 'R':
                reporting_menu()
            elif choice == 'I':
                intelligence_menu()
            elif choice == 'M':
                monitoring_menu()
            elif choice == 'A':
                about()
            elif choice == 'Q':
                run = quit()
            else:
                input('''That's not one of the options: [Press Enter to Continue]: ''')
        else:
            input('''That's not one of the options: [Press Enter to Continue]: ''')


def reporting_menu():
    data = {'Marylebone Road': pd.read_csv('data/Pollution-London Marylebone Road.csv'), 'N. Kensington': pd.read_csv('data/Pollution-London N Kensington.csv'), 'Harlington': pd.read_csv('data/Pollution-London Harlington.csv')}
    pollutants = {'Nitric Oxide': 2, 'PM10': 3, 'PM2.5': 4}

    while True:
        choice = str(input('''
Where would you like to Report on: 
(1), Marylebone Road, 
(2), N. Kensington, 
(3), Harlington,
(Enter the Number): '''))
        print('\n' * 100)

        if type(choice) is str:
            if choice == '1':
                monitoring_station = 'Marylebone Road'
                break
            elif choice == '2':
                monitoring_station = 'N. Kensington'
                break
            elif choice == '3':
                monitoring_station = 'Harlington'
                break
            else:
                input('''That's not one of the options: [Press Enter to Continue]: ''')
        else:
            input('''That's not one of the options: [Press Enter to Continue]: ''')

    while True:
        choice = str(input('''
Which Pollutant would you like to examine:
(1) Nitric Oxide, 
(2) PM10, 
(3) PM2.5, 
(Enter the Number): '''))
        print('\n' * 100)

        if type(choice) is str:
            if choice == '1':
                pollutant = 'Nitric Oxide'
                break
            elif choice == '2':
                pollutant = 'PM10'
                break
            elif choice == '3':
                pollutant = 'PM2.5'
                break
            else:
                input('''That's not one of the options: [Press Enter to Continue]: ''')
        else:
            input('''That's not one of the options: [Press Enter to Continue]: ''')

    while True:
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
        print('\n' * 100)

        if type(choice) is str:
            if choice == '1':
                daily_average_values = rep.daily_average(data, monitoring_station, pollutants[pollutant])
                print(len(daily_average_values), daily_average_values)
                input('Press Enter to Continue: ')
                break

            elif choice == '2':
                daily_median_values = rep.daily_median(data, monitoring_station, pollutants[pollutant])
                print(len(daily_median_values), daily_median_values)
                input('Press Enter to Continue: ')
                break

            elif choice == '3':
                hourly_average_values = rep.hourly_average(data, monitoring_station, pollutants[pollutant])
                print(len(hourly_average_values), hourly_average_values)
                input('Press Enter to Continue: ')
                break

            elif choice == '4':
                monthly_average_values = rep.monthly_average(data, monitoring_station, pollutants[pollutant])
                print(len(monthly_average_values), monthly_average_values)
                input('Press Enter to Continue: ')
                break

            elif choice == '5':
                while True:
                    date = input('''
Please Enter the Date you would like to have the peak hour for: ('YYYY-MM-DD'): ''')

                    try:
                        peak_hour_data_value = rep.peak_hour_date(data, date, monitoring_station, pollutants[pollutant])
                        if peak_hour_data_value[2]:
                            print(peak_hour_data_value[0:2])
                            input('Press Enter to Continue: ')
                            break
                        else:
                            input("That's Not a Valid Data please try again: ")
                    except:
                        input("That's Not a Valid Data please try again: ")
                break

            elif choice == '6':
                total_missing_data = rep.count_missing_data(data, monitoring_station, pollutants[pollutant])
                print(total_missing_data)
                input('Press Enter to Continue: ')
                break

            elif choice == '7':
                new_value = input('''
Please enter your value to replace all 'No data' values with: (x.y, eg: 2.4): ''')

                filled_missing_data = rep.fill_missing_data(data, new_value, monitoring_station, pollutants[pollutant])
                print(filled_missing_data)
                input('Press Enter to Continue: ')
                break

            else:
                input('''That's not one of the options: [Press Enter to Continue]: ''')
        else:
            input('''That's not one of the options: [Press Enter to Continue]: ''')


def intelligence_menu():
    """Your documentation goes here"""
    while True:
        choice = input('''
What Function would you like to perform: 
(1) Find all of the Red pixels
(2) Find all of the Cyan pixels
(3) Detect the connected components
(4) Detect the connected components sorted : ''')
        print('\n' * 100)
        if type(choice) is str:
            if choice == '1':
                intel.find_red_pixels('map.png')
                break
            elif choice == '2':
                intel.find_cyan_pixels('map.png')
                break
            elif choice == '3':
                intel.detect_connected_components()
                break
            elif choice == '4':
                MARK = intel.detect_connected_components()
                intel.detect_connected_components_sorted(MARK)
                break
            else:
                input('''That's not one of the options: [Press Enter to Continue]: ''')
        else:
            input('''That's not one of the options: [Press Enter to Continue]: ''')


def monitoring_menu():
    """Your documentation goes here"""
    while True:
        choice = input('''
What Function would you like to perform: 
(1) Output all locations data is being Recorded
(2) Output the details of a location
(3) Output all the pollutant types
(4) Output the details of a pollutant 
(5) Output the site codes
(6) Outputs locations that have recent data 
(7) Output a graph of a recent day given Site code and Pollutant ''')
        print('\n' * 100)
        if type(choice) is str:
            if choice == '1':
                mon.get_all_site_locations()
                break
            elif choice == '2':
                row = int(input('''
Please Enter the row of the location that you would like to see: '''))
                mon.get_description_of_location(row)
                break
            elif choice == '3':
                mon.get_all_pollutant_types()
                break
            elif choice == '4':
                row = int(input('''
Please Enter the row of the location that you would like to see: '''))
                mon.get_description_of_pollutant(row)
                break
            elif choice == '5':
                mon.get_site_codes()
                break
            elif choice == '6':
                pollutant = input('''
Please Enter the pollutant that you would like to see: ''')
                mon.find_data(species_code=pollutant)
                break
            elif choice == '7':
                site_code = input('''
Please Enter the Site Code of the place you would like to draw a graph (Recommend: 'BX1'):  ''')
                species_code = input('''
Please Enter the Species Code of the pollutant you would like to draw a graph (Recommend: 'NO2'): ''')
                mon.create_graph_with_data(site_code, species_code)
                break
            else:
                input('''That's not one of the options: [Press Enter to Continue]: ''')
        else:
            input('''That's not one of the options: [Press Enter to Continue]: ''')
    print('\n' * 100)


def about():
    """Your documentation goes here"""
    pass


def quit():
    """Your documentation goes here"""
    return False


if __name__ == '__main__':
    main_menu()
