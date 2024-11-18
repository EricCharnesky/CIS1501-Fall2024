games_files = open('games/games.txt')

games = games_files.readlines()

for game in games:
    print(game, end="")

for index in range(0, len(games), 2):
    print(f"Name: {games[index].strip()} - Players: {games[index+1].strip()}")

players = int(input("How many players are playing tonight?"))

for index in range(0, len(games), 2):
    player_minimum = int(games[index+1].strip().split("-")[0])
    player_maximum = int(games[index + 1].strip().split("-")[1])
    if player_minimum <= players <= player_maximum:
        print(f"Name: {games[index].strip()}")

games_to_add = input("Do you want to add games to your library? (y/n)").lower()

while games_to_add == 'y':
    game_name = input("Enter the name of the game")
    minimum_number_of_players = input("Enter the minimum number of players")
    maximum_number_of_players = input("Enter the maximum number of players")

    games_file = open('games/games.txt', 'a')
    games_file.write(f'{game_name}\n')
    games_file.write(f'{minimum_number_of_players}-{maximum_number_of_players}\n')

    games_to_add = input("Do you want to add more games to your library? (y/n)").lower()

import os

# full path is generally bad, no one else's computer will have this path
path = r"C:\Users\EricC\Documents\GitHub\CIS1501-Fall2024"

for dirname, subdirs, files in os.walk(path):
    # get the last subdirectory, first character
    has_hidden_folder = False
    for subdirectory in dirname.split("\\"):
        if subdirectory[0] == '.':
            has_hidden_folder = True

    if not has_hidden_folder:
        print(dirname, 'contains subdirectories:', subdirs, end=' ')
        print('and the files:', files)