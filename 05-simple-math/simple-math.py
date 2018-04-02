def run():
    first_number = input('What is the first number? ')
    second_number = input('What is the second number? ')
    
    print(first_number + " + " + second_number + " = " + str(plus(first_number, second_number)))
    print(first_number + " - " + second_number + " = " + str(minus(first_number, second_number)))
    print(first_number + " / " + second_number + " = " + str(division(first_number, second_number)))
    print(first_number + " * " + second_number + " = " + str(multiply(first_number, second_number)))
    
    return

def plus (a, b):
    return int(a) + int(b)

def minus(a, b):
    return int(a) - int(b)

def division(a, b):
    return int(a) / int(b)

def multiply(a, b):
    return int(a) * int(b)
    
run()