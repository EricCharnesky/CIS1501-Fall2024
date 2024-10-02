import math
import random
import statistics


sides_on_a_die = int(input("How many sides are on your dice? "))

how_many_dice = int(input("How many dice are you rolling? "))

list_of_sums = []
for sum in range(sides_on_a_die * how_many_dice + 1):
    list_of_sums.append(0)

how_many_rolls = int(input("How many times do you want to roll those?"))

for count in range(how_many_rolls):
    sum = 0
    for roll in range(how_many_dice):
        sum += random.randint(1, sides_on_a_die)
    list_of_sums[sum] += 1


for roll, count in enumerate(list_of_sums):
    if roll >= how_many_dice:
        percentage = int(count/how_many_rolls*100)
        #print(f'{roll:02d}: {"*" * percentage}')
        print(f'{roll:02d}: {"*" * count}')




foods = ['chicken noodle soup', 'steak sub', 'salad']


for index in range(len(foods)):
    print(f'{index} - {foods[index]}')

for index, value in enumerate(foods):
    print(f'{index} - {value}')
    value = value.upper()

print(foods)


for index in range(len(foods)):
    print(f'{index} - {foods[index]}')
    foods[index] = foods[index].upper()
print(foods)



for number in range(100):
    if number % 3 == 0:
        continue # skip to loop header condition
    print(number)

for number in range(100):
    if not number % 3 == 0:
        print(number)



winning_ticket = [2, 3, 5, 7, 11, 13]

users_ticket = []

while len(users_ticket) != 6:
    users_ticket.append(int(input("Enter a number for your lotto ticket")))

for number in users_ticket:
    if number not in winning_ticket:
        print("you lose!")
        break
else: # else doesn't run if you break
    print("You win!")

won = True

for number in users_ticket:
    if number not in winning_ticket:
        won = False

if won:
    print("You win!")
else:
    print("You lose!")







names = {}
name = input("Enter a name")

while name.upper() != "QUIT":
    score = int(input(f"Enter the score for {name}"))
    names[name] = score
    name = input("Enter a name or QUIT to stop")

print(names)


names = {}
name = input("Enter a name")

while True:
    score = int(input(f"Enter the score for {name}"))
    names[name] = score
    name = input("Enter a name or QUIT to stop")
    if name == "QUIT":
        break

print(names)






# sentinel value to stop a loop
grades = []

grade = int(input("Enter a grade 1-100"))

while grade != -1:
    grades.append(grade)
    grade = int(input("Enter a grade 1-100 or -1 to stop"))

highest_grade = grades[0]
lowest_grade = grades[0]
for grade in grades:
    if grade > highest_grade:
        highest_grade = grade
    if grade < lowest_grade:
        lowest_grade = grade

print(f'Grade Stats: Lowest {lowest_grade} - Average {sum(grades)/len(grades)} - Highest {highest_grade}')
print(f'Standard Deviation {statistics.pstdev(grades)}')

valid_options = ( 'pizza', 'drinks', 'ice cream' )

users_choice = input("Do you want to serve pizza, drinks, or ice cream").lower()

# validation loop
while users_choice not in valid_options:
    users_choice = input("invalid choice, please enter: pizza, drinks, or ice cream")

print(f"you picked {users_choice}")

some_number = int(input("Enter a score 1-100"))
#while not (1 <= some_number <= 100):
#    some_number = int(input("Invalid number, Enter a score 1-100"))

while some_number < 1 or some_number > 100:
    some_number = int(input("Invalid number, Enter a score 1-100"))







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



import random
play_again = 'y'

while play_again == 'y':

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

    play_again = input("Do you want to play again? y/n").lower()

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

