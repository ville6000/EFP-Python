import datetime

age = input('What is your current age? ')
retirement_age = input('At what age would you like to retire? ' )

years_left = int(retirement_age) - int(age)
current_year = datetime.date.today().strftime("%Y")
retirement_year = int(current_year) + years_left

print(f"You have {years_left} years left until you can retire.")
print(f"Is's {current_year}, so you can retire in {retirement_year}.")
