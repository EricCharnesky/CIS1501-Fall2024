import random


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
