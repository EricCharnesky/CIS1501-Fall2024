import math
import random

print(chr(ord("E")+1))
print(chr(ord('r')+1))
print(chr(ord('i')+1))
print(chr(ord('c')+1))

first_letter = input("Enter the first letter to encode")
second_letter = input("Enter the second letter to encode")
third_letter = input("Enter the third letter to encode")

shift_amount = int(input("How far should we shift the letters?"))

value_of_lower_a = 97
first_value = ( ord(first_letter) - value_of_lower_a + shift_amount ) % 26 + value_of_lower_a
second_value = ( ord(second_letter) - value_of_lower_a + shift_amount ) % 26 + value_of_lower_a
third_value = ( ord(third_letter) - value_of_lower_a + shift_amount ) % 26 + value_of_lower_a

print(chr(first_value), chr(second_value), chr(third_value))


print("O'Conner said \"Hi Eric\"")
print('O\'Conner said "Hi Eric"')
print('Eric said "Hi" to Jeb')
print("3\n2\n1\nBlastoff!")



# fixes the pseudo random sequence
random.seed(15)
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

# because random never gives a 1, if I want 1-100, I add 1
print(random.random()*100+1)

first_number = int(input("Enter the first number"))
second_number = int(input("Enter the second number"))

quotient = int(first_number / second_number)

# % is modulus, gives the integer remainder of division
remainder = first_number % second_number

print(first_number, "/", second_number, "=", quotient, "remainder:", remainder)


some_number_with_decimals = 4.2

some_number_with_decimals = some_number_with_decimals + 2

some_number_with_decimals += 2

# be careful with the order +=
some_number_with_decimals =+2
some_number_with_decimals /= 2




print('2.0 to the power of 256 =', 2.0**256)
print('2.0 to the power of 512 = ', 2.0**512)
#print('2.0 to the power of 1024 = ', 2.0**1024)

print(f'{math.pi:.4f}')


print(4 / 2)
print("4 / 2")
print(1/3)
print(math.pi)

first_number = 4
second_number = 2

my_favorite_number = 42

print(first_number / second_number)

first_number = 22

second_number = first_number + my_favorite_number

print(first_number / second_number)

# camel casing
firstNumber = 42

# Please Excuse My Dear Aunt Sally
print(9 / 3*(2+1))

# a is for my first digit of the area code
a = 1
first_digit_of_area_code = 2
c = 3

first_digit_of_area_code = 6

some_number_with_a_decimal = 4.2

print(2 ** -3)


name = input("Enter your name")

print("Hello", name)
print("hello name")

# int( some_value_here ) - tries to convert the value to an integer
age = int(input("enter your age"))

print("You can retire in", 67 - age, "years")
