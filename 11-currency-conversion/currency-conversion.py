from decimal import Decimal

euros = input('How many euros are you exchaging? ')
exchange_rate = input('What is the exchange rate? ')
dollars = round(Decimal(float(euros) * float(exchange_rate) / 100), 2)

print(f"{euros} euros at an exchange rate of {exchange_rate} is {dollars} U.S. dollars.")