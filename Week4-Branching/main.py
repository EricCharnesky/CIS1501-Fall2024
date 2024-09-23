age = int(input("Enter your age: "))

car_insurance_monthly_rate = 100

if age < 26:
    car_insurance_monthly_rate += 50

print(f"Your insurance will cost ${car_insurance_monthly_rate} per month")


money = int(input("Enter how much money you have for lunch: "))

if money >= 10:
    print("You can go to picasso for lunch")
    print("They don't give change")
    print("You can have lots of stuff here")
else:
    print("You can have ramen noodles")

guess = int(input("Guess a number"))


    # equals
if guess == 42:
    print("You guessed it!")
else:
    print("Wrong!")

    # does not equal
if guess != 42:
    print("Wrong!")
else:
    print("You guessed it!")

name = input("Enter your name: ")

# checking strings is case sensitive
# can use lower to make sure we don't worry about casing
if name.lower() == "eric":
    print(f"Howdy {name}")
else:
    print(f"{name}, who are you?")

print("Welcome to Eric's coffee shop, enter your order")
print("1 - Coffee")
print("2 - Espresso")
print("3 - Americano")
print("4 - Latte")
print("5 - Tea")

#order = int(input("Welcome to Eric's coffee shop, enter your order\n1 - coffee\n"))
order = int(input())

if order == 1:
    print("$1.00 for coffee")
elif order == 2:
    print("$2.00 for espresso")
elif order == 3:
    print("$1.50 for americano")
elif order == 4:
    print("$3.00 for a latte")
elif order == 5:
    print("$1.50 for tea")
else:
    print("We don't serve that")



# modified from https://learn.zybooks.com/zybook/UMDEARBORNCIS1501CharneskyFall2024/chapter/4/section/4
user_age = int(input('Enter your age: '))

if user_age < 16:          # Age 15 and under
  print('Too young.')
  insurance_price = 0

# explicit
elif 16 <= user_age < 25:        # Age 16 - 24
  insurance_price = 4800

elif 25 <= user_age < 40:         # Age 25 - 39
  insurance_price = 2350

else:                      # Age 40 and up
  insurance_price = 2100

print(f'Annual price: ${insurance_price}')


temperature_in_celsius = int(input("Enter the temperature in celsius: "))

weather = input("Enter the weather (sunny, rainy, snowy): ")

if temperature_in_celsius > 20:

    if weather != "sunny":
        print("Don't forget your umbrella")
        if age < 25:
            print("Forget the umbrella, you're invincible")
    else:
        print("It's nice out, wear shorts")

else:
    print("You'll want pants")


if weather != "sunny" and temperature_in_celsius > 20:
    print("Don't forget your umbrella")
elif temperature_in_celsius > 20:
    print("Wear shorts")
else:
    print("wear pants")

dinners = ['Ramen', 'Noodles', "Pizza", "tacos"]

dinner_choice = input("What sounds good for dinner? ")

if dinner_choice in dinners:
    print("We've got that")
else:
    print("You'll have to run to Meijer to get that")

grades = {"Eric" : "A", "Jeb" : "B"}

# with dictionaries, in, only checks keys
if 'Eric' in grades:
    print("Eric is in the class")


if dinner_choice.lower() == 'ramen':
    cost = .33
else:
    cost = 2

cost = .33 if dinner_choice.lower() == 'ramen' else 2

# logical operators
# and
# true and false == false
# false and true == false
# false and false == false
# true and true == true

# or
# true or false == true
# false or true == true
# true or true == true
# false or false == false

# not
# not true == false
# not false == true

number1 = int(input("Enter your first lotto number: "))
number2 = int(input("Enter your first lotto number: "))
number3 = int(input("Enter your first lotto number: "))

cheating = input("Do you want to cheat? (y/n) ")

if ( number1 == 7 and number2 == 2 and number3 == 5 ) or cheating == 'y':
    print("you win the lotto")
else:
    print("You lost your money")
