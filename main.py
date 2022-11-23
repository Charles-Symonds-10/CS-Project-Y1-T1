import reporting
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
    : 
    ''')
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
    choice = input('''

''')

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
