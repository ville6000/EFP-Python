def ask_int(question):
    answer = ''

    while answer.isdigit() == False:
        answer = input(question)

    return answer

people = ask_int('How many people? ')
pizza_count = ask_int('How many pizzas do you have? ')
slices_per_pizza = ask_int('How many slices per pizza? ')

slice_count = int(pizza_count) * int(slices_per_pizza)
slices_per_person = slice_count // int(people)
leftover_slices = slice_count - slices_per_person * int(people) 

print(str(people), 'people with', str(pizza_count), 'pizzas')
print(f"Each person gets {slices_per_person} pieces of pizza.")
print(f"There are {leftover_slices} leftover pieces.")
