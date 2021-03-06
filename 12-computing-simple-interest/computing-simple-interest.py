import locale
locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )

def calculate_simple_interest(principal, rate_of_interest, years):
    return int(principal) * (1 + (float(rate_of_interest) / 100) * int(years))

principal = input('Enter the principal: ')
rate_of_interest = input('Enter the rate of interest: ')
years = input('Enter the number of years: ')
worth = calculate_simple_interest(principal, rate_of_interest, years)

print(locale.currency(worth))