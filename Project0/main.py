import math

name = input("Welcome to the party planning program, what's your name friend? ")

number_of_people = int(input(f'{name}, how many guests are you expecting? ')) + 1

serving = input(f'{name}, what are you serving? Pizza, Drinks, or Ice Cream? ').lower()

if serving == 'pizza':
    slices_per_guest = int(input(f"{name}, How many slices will the average guest eat? "))
    total_slices_needed = slices_per_guest * number_of_people
    slices_per_pizza = int(input(f"{name}, How many slices per pizza? "))
    pizzas_needed = math.ceil(total_slices_needed / slices_per_pizza )
    cost_per_pizza = float(input(f"{name}, How much does each pizza cost?"))
    print(f"{name}You need to buy {pizzas_needed} pizzas, it will cost ${cost_per_pizza*pizzas_needed}")

elif serving == 'drinks':
    OUNCES_PER_GALLON = 128
    ounces_per_guest = int(input(f"{name}, How many ounces will the average guest drink? "))
    gallons_needed = math.ceil(ounces_per_guest * number_of_people / OUNCES_PER_GALLON)
    cost_of_gallon = float(input(f"{name}, How much does a gallon of drink cost? " ))
    print(f"{name}, you need to buy {gallons_needed} of drink, it will cost ${cost_of_gallon * gallons_needed}")

elif serving == 'ice cream':
    scoops_per_guest = int(input(f'{name}, how much scoops will each guest eat? '))
    scoops_needed = scoops_per_guest * number_of_people
    scoops_per_container = int(input(f"{name}, how many scoops come in a container? "))
    containers_needed = math.ceil(scoops_needed / scoops_per_container)
    cost_per_container = float(input(f"{name}, how much does a container cost? "))
    print(f'{name}, you need to buy {containers_needed} containers, it will cost ${cost_per_container * containers_needed}')

else:
    print("I can't help you, please try again")