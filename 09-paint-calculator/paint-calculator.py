import math

GALLON_COVERS = 350

width_of_the_room = input('What is the width of the room? ')
length_of_the_room = input('What is the length of the room? ')

square_feet = int(width_of_the_room) * int(length_of_the_room)
gallons_needed = math.ceil(square_feet / GALLON_COVERS)

print(f"You will need to purchase {gallons_needed} gallons of paint to cover {square_feet} square feet.")
