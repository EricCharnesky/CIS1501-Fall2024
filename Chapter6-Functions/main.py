import random



def lucky_numbers_with_explict_tuple():
    return (42, 7)

def lucky_numbers():
    return 42, 7 # automatically packs into a tuple


def generate_citation(author, title, publisher="", year_published=2024):
    print(f"{author}, {title}. {publisher}, {year_published}")



# lists are mutable and can be changed in functions
def upper_case_list(some_list):
    for index in range(len(some_list)):
        some_list[index] = some_list[index].upper()

# strings are immutable and cannot be changed in functions
def scream_in_internet(some_string):
    some_string = some_string.upper()
    return some_string

# passing by value - not the location in memory
def add_to(value):
    value += 10

def add_to_and_return(value):
    value += 10
    return value


# automatic unpacking of a tuple returned
lucky_number1, luck_number2 = lucky_numbers()

# shortcut for doing it the long way
tuple_lucky_numbers = lucky_numbers_with_explict_tuple()
lucky_number3 = tuple_lucky_numbers[0]
lucky_number4 = tuple_lucky_numbers[1]

value = 12

print(value)
add_to(value)
print(value)

value = add_to_and_return(value)

print(value)


hello = "Happy Wednesday"
scream_in_internet(hello)
print(hello)


drinks = ['Coffee', 'water', 'coke zero', 'matcha']

print(drinks)
upper_case_list(drinks)
print(drinks)



generate_citation("Eric", "some code", "myself", 2024)
generate_citation(title="Some code", author="Eric Charnesky", year_published=2024, publisher="myself")
generate_citation("eric", "some code", "myself")
range(10, 20, 2)



# try not to do this
global some_number

some_number = 20

def wednesday():
    some_number = 10 # local scope version
    print("Print happy wednesday" * some_number)
    print(some_number)

print(some_number)

print(wednesday())

name = "Eric"

print(len)

print(len(name))

#len = 10

print(len)

my_number = 42

print(globals())



wednesday()
print(my_number)

def finish_this_later(x, y, z):
    print("FIXME")

def call_me_third(name):
    print(f"Hi there {name}, third here")


def call_me_second(name):
    print(f"Hi {name}, I'm second")
    call_me_third(name)

def call_me_first(name):
    print(f'Hi {name}')
    call_me_second(name)

def add_two_things(thing_one, thing_two):
    return thing_one + thing_two

def print_too_high_or_too_low(guess, number_to_guess):
    if guess < number_to_guess:
        print('too low')
    else:
        print('too high')

def print_happy_monday():
    print("Happy Monday!")
    print("Happy Monday!")
    print("Happy Monday!")

def get_integer_in_range(lowest_possible, highest_possible):

    value = int(input(f"enter a number {lowest_possible}-{highest_possible}"))
    while not (lowest_possible <= value <= highest_possible):
        print("Invalid, please try again")
        value = int(input(f"enter a number {lowest_possible}-{highest_possible}"))
    #while value < lowest_possible or value > highest_possible:

    return value

def get_integer_input(prompt):
    value = int(input(prompt))
    return value

def get_valid_value(prompt, list_of_valid_values):
    value = input(prompt)
    while value not in list_of_valid_values:
        print(f"Invalid choice, please pick from: {list_of_valid_values}")
        value = input(prompt)
    return value


call_me_first("Eric")

print(add_two_things("thing one", "thing two"))
print(add_two_things(10, 12))
print(add_two_things("thing one", 2))


print_happy_monday()
valid_colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']
favorite_color = get_valid_value("Enter your favorite color", valid_colors)

lowest_possible = get_integer_input("Enter the lowest possible value")
highest_possible = get_integer_input("Enter the highest possible value")

number_of_guesses = 1
# number_of_guesses = "ten"
guess = get_integer_in_range(lowest_possible, highest_possible)
number_to_guess = random.randint(lowest_possible, highest_possible)

while guess != number_to_guess:
    print_too_high_or_too_low(guess, number_to_guess)
    guess = get_integer_in_range(lowest_possible, highest_possible)
    number_of_guesses += 1

print(f"You got it in {number_of_guesses}!")
