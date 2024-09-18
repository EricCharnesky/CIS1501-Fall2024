import math
import random

caffeine_content_mg = {
    'Mr. Goodbar chocolate': 122,
    'Red Bull': 33,
    'Monster Hitman Sniper energy drink': 270,
    'Lipton Brisk iced tea - lemon flavor': 2,
    'dark chocolate coated coffee beans': 869,
    'Regular drip or percolated coffee': 60,
    'Buzz Bites Chocolate Chews': 1639
}

caffeine_content_mg.pop('Buzz Bites Chocolate Chews')

caffeine_content_mg['Starbucks tripleshot energy bold mocha'] = 225

print(f'If you eat all this, you\'ll have this much caffeine: {sum(caffeine_content_mg.values())}')


# { for dictionary }
# key : value , separate each pair
grades = {"Eric": "A", 'Jeb': 'B', 'Journey': "C"}


seats = {1: "first place", 2 : 4.2}

# dictionary_value[key] to get the value associated
print(f"Eric's grade is {grades["Eric"]}")

# KeyError: 'jeb' - case sensitive
print(f"Jeb's grade is {grades["Jeb"]}")

# we can change the associated value of a key with =
grades["Jeb"] = 'A'

# if the key doesn't exist, it adds the pair
grades['Jubilee'] = 'C-'

# starts empty
menu = {}

dinner = input("What's for dinner tonight?")

# add key value pair
menu['Wednesday'] = dinner

dinner = input("What's for dinner tomorrow?")
menu['Thursday'] = dinner

day = input("What day do you want to know what is for dinner?")
print(menu[day])

print(menu)

# { } for set or set( )
pokemon = {'Pikachu', 'Squirtle', 'Charmander', "Bulbasaur"}

print(pokemon)

pokemon.add("Evee")

print(pokemon)

pokemon.remove('Charmander')

print(pokemon)

# doesn't crash, but nothing happens
pokemon.add("Pikachu")

print(pokemon)


# [ ] for lists - lists are mutable
foods = ['Apples', 'Bananas', 'Cucumbers', 'Donuts']
# index     0           1           2           3



# first item is at index 0
print(foods[0])

# indexes are assignable - because it's mutable
foods[0] = 'honey crisp apples'

print(foods)

favorite_food = input(f'What is your favorite food? ')

foods.append(favorite_food)

print(foods)

print(f"your random food {foods[random.randint(0, len(foods)-1)]}")
print(f'another random food {random.choice(foods)}')

# pop removes by index ( or the last item if no index given )
foods.pop(1)

print(foods)


# if it's not in the list, it will crash
#    foods.remove("cucumbers")
# ValueError: list.remove(x): x not in list
foods.remove("Cucumbers")



print(foods)


# A is the 'smallest' value for a character, 'a' is bigger
print(min(foods))

lotto_ticket = [ 11, 14, 8, 16, 23, 2]

lotto_ticket[2] = 27

print(min(lotto_ticket))

print(sum(lotto_ticket))

# average
print(sum(lotto_ticket) / len(lotto_ticket ))

# (  ) for tuples
winning_ticket = (1, 2, 3, 4, 5, 6)

# can't change
# winning_ticket[2] = 27


# IndexError: list index out of range - nothing at index 4
# print(foods[4])



# from https://umgpt.umich.edu/
# prompt: how do I get extra left of the decimal digits to show in python in a formatted string
value = 123.456
formatted_value = f"{value:09.3f}"
print(formatted_value)


name = 'Eric'
last_name = input("Enter your last name")

# list with variables
names = [ name, last_name ]

print(names)

names[1] = "you don't get a last name"

print(names)

print(f'{last_name} - last_name')


name = 'Bob'

print(names)

print("your last name has", len(last_name), "letters")

# strings are immutable
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alphabet[4], alphabet[17], alphabet[8], alphabet[2])
alphabet = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

print(alphabet[4], alphabet[17], alphabet[8], alphabet[2])


print( 5 + 4 )
print("5" + "4")

print("Hi " + name + " " + last_name)

favorite_color = input(name + ", what is your favorite color? ")

print(name, ", what is your favorite animal?")
favorite_animal = input()

favorite_number = int(input(f"{name}, what is your favorite number? "))

favorite_season = input(f'{name}, what is your favorite season? ')

print(f'{name}\'s favorite number is {favorite_number}')

# will crash, can't use string concatenation ( + ) with non strings
# print(name + "'s favorite number is " + favorite_number)

some_big_number = int(input("Enter some really big number"))

print(f'{some_big_number: ,d}')

# does round at the last decimal
print(f'{math.pi: .4f}')