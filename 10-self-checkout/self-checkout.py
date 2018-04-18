def get_items():
    items = []
    stop_input = False
    item_index = 1

    while stop_input == False:
        price = input(f"Enter the price of item {item_index}: ")
        quantity = input(f"Enter the quantity of item {item_index}: ")
        item_index += 1

        if not price:
            stop_input = True
        else:
            items.append([int(quantity), int(price)])

    return items

def get_sub_total(items):
    sub_total = 0

    for item in items:
        sub_total += item[0] * item[1]

    return sub_total

def get_tax(sub_total):
    return sub_total * 0.055

def get_total(sub_total, tax):
    return sub_total + tax

items = get_items()
sub_total = get_sub_total(items)
tax = get_tax(sub_total) 
total = get_total(sub_total, tax)

print("Subtotal: $",sub_total)
print("Tax: $", tax)
print("Total: $", total)