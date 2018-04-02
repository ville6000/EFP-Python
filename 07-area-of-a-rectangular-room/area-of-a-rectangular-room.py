CONVERSION_FACTOR = 0.09290304

length = input('What is the length of the room in feet? ')
width = input('What is the width of the room in feet? ')

square_feet = int(length) * int(width)
square_meters = square_feet * CONVERSION_FACTOR

print(f"You entered dimensions of {length} feet by {width} feet.")
print(f"The area is  \n{square_feet} square feet \n{square_meters} square meters")
