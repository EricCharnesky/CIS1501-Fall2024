import random

ROCK = 1
PAPER = 2
SCISSORS = 3
LIZARD = 4
SPOCK = 5

computer_throw = random.randint(1,5)

throws = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

print("1 - Rock")
print("2 - Paper")
print("3 - Scissors")
print("4 - Lizard")
print("5 - Spock")

player_throw = int(input())

print(f"Computer picked {throws[computer_throw-1]}")

# if player_throw == ROCK:
#     if computer_throw == SCISSORS or computer_throw == LIZARD:
#         print("You win")
#     elif player_throw == computer_throw:
#         print("Tie")
#     else:
#         print("You lose")

if player_throw == computer_throw:
    print("Tie")
elif (player_throw == ROCK
        and (computer_throw == SCISSORS or computer_throw == LIZARD)) or \
    (player_throw == PAPER
        and (computer_throw == ROCK or computer_throw == SPOCK )) or \
    (player_throw == SCISSORS
        and (computer_throw == PAPER or computer_throw == LIZARD)) or \
    (player_throw == LIZARD
        and (computer_throw == PAPER or computer_throw == SPOCK)) or \
    (player_throw == SPOCK
        and (computer_throw == ROCK or computer_throw == SCISSORS )):
    print("You win!")
else:
    print("You lose!")
