import reporting as rep
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
                monitoring_menu()
            elif choice == 'M':
                intelligence_menu()
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
                pass
            elif choice == '3':
                pass
            elif choice == '4':
                pass
            elif choice == '5':
                pass
            elif choice == '6':
                pass
            elif choice == '7':
                pass
            else:
                input('''That's not one of the options: [Press Enter to Continue]: ''')
        else:
            input('''That's not one of the options: [Press Enter to Continue]: ''')


def monitoring_menu():
    """Your documentation goes here"""
    pass


def intelligence_menu():
    """Your documentation goes here"""
    pass


def about():
    """Your documentation goes here"""
    pass


def quit():
    """Your documentation goes here"""
    return False


if __name__ == '__main__':
    main_menu()
