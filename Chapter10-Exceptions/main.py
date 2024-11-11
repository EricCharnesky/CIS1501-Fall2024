from random import randint

# import Cup

import containers.cup
import containers.mug




coffee = containers.cup.Cup(700)
coffee.fill(100)
coffee.drink(15)

while True:
    try:
        number = int(input("Please enter a number"))
        result = number / number
        print("that is a valid number")
        break
    # be careful using a broad Exception handler
    #except Exception as e:
    #    print(e)
    except:
        print("Error, try again")

print(number)
print(randint(1, 10))
#random.sample()