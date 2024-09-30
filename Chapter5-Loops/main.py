import math
import random


count_of_side_being_rolled = [0, 0, 0, 0, 0, 0]

number_of_rolls = int(input("how many rolls?"))

for roll in range(number_of_rolls):
    number = random.randint(1, 6)
    # subtract 1 to get to the matching index
    count_of_side_being_rolled[number-1] += 1

for index in range(len(count_of_side_being_rolled)):
    print(f'The number {index+1} was rolled {count_of_side_being_rolled[index]} times' +
          f' {count_of_side_being_rolled[index] / number_of_rolls * 100} %')


hours = 0
while hours < 24:
    minutes = 0
    while minutes < 60:
        seconds = 0
        while seconds < 60:
            print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
            seconds += 1
        minutes += 1
    hours += 1



size = int(input("How large of a square should we print?"))

for row in range(size):
    print(' ' * (size - row - 1), end="")
    print('*' * (row+1))

stars = 1

while stars <= size:
    print("*" * stars)
    stars += 1


length = int(input("How long of a rectangle? "))
width = int(input("How wide of a rectangle? "))

row = 1
while row <= length:
    stars = 1
    while stars <= width:
        print("*", end="")
        stars += 1
    row += 1
    print()

for row in range(1,length+1):
    for star in range(width):
        print("*", end="")
    print()




number = int(math.fabs(int(input('What do you want to count down from?'))))

for value in range(number, 0, -1):
    print(value)


# if it's true, it runs
while number > 0:
    #if number % 100_000 == 0:
    print(f'{number:,d}')
    number -= 1
    # number = number - 1
    # at the bottom of the loop, it goes back and checks the condition
print("Blastoff!")

highest_number = int(input("How high of a number do you want to guess?"))

random_number = random.randint(1, highest_number)
number_of_guesses = 1
guess = int(input(f"Guess a number 1-{highest_number}: "))

while guess != random_number:
    if guess < random_number:
        print("too low!")
    else:
        print("too high")
    guess = int(input(f"Guess a number 1-{highest_number}: "))
    number_of_guesses += 1
print(f"You got it in {number_of_guesses} guesses!")

name = input("Enter your name")

# runs once for each item in the collection
# for some_variable_name in some_collection
for letter in name:
    if not letter.isspace():
        print(chr(ord(letter)+1), end="")
    else:
        print(letter, end='')


meals = {'rice and beans': 500, 'chicken': 120, 'tacos': 900, 'ice cream': 700}

# for loops with dictionaries give only the KEYS
for meal in meals:
    print(f'{meal} has {meals[meal]} calories')

classes = ['CIS 1501', 'MAT 115', 'CHEM 110']

# items in for loops are essentially copies
for my_class in classes:
    my_class = my_class.lower()
    print(my_class)

# looping through by index, allows you to change the values stored
for index in range(len(classes)):
    classes[index] = classes[index].lower()
    print(classes[index])

print(classes)

