import math


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