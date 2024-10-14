import random

def get_random_tilt():
    return random.randint(-10, 10)

def get_command():
    print("Enter one of the following commands:")
    print("x+")
    print("x-")
    print("y+")
    print("y-")
    print("thrusters")
    print("self destruct")
    print("nothing")
    command = input("What command do you want to send to the lander?")
    return command.lower()

play_again = 'y'

while play_again == "y":

    x_tilt = get_random_tilt()
    y_tilt = get_random_tilt()

    distance_from_surface = 10

    while distance_from_surface != 0:

        print(f'Distance from surface: {distance_from_surface}')
        print(f'X Tilt: {x_tilt}')
        print(f'Y Tilt: {y_tilt}')

        command = get_command()
        distance_from_surface -= 1

        if command == "x+":
            x_tilt += 1
        elif command == "x-":
            x_tilt -= 1
        elif command == "y+":
            y_tilt += 1
        elif command == "y-":
            y_tilt -= 1
        elif command == "thrusters":
            distance_from_surface += 2
        elif command == "self destruct":
            print("Self destruct sequence activated!")
            cancel_code = ""

            while cancel_code != "cancel":
                cancel_code = input("Please enter cancellation code")
            print("Self destruct sequence deactivated")
        elif command == "nothing":
            pass
        else:
            print("invalid command, please try again")
            distance_from_surface += 1

    if x_tilt or y_tilt: # silly shortcut - 0 is false
        print("You crashed!")
    else:
        print("Congratulations you landed the lander")

    play_again = input("Do you want to play again? y/n").lower()