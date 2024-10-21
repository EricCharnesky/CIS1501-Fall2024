import sys

print(sys.argv)

def print_board(board):
    for index, row in enumerate(board):
        print("|".join(row))
        if index != 2:
            print("-----")

def place_mark(board, current_player):
    print_board(board)
    print(f"{current_player}'s turn")
    row_and_column = input("Please enter the row and column you want to mark ( 1 1 )")
    row = int(row_and_column.split()[0])
    column = int(row_and_column.split()[1])
    while board[row][column] != " ":
        print("there's already a mark there, try again")
        row_and_column = input("Please enter the row and column you want to mark ( 1 1 )")
        row = int(row_and_column.split()[0])
        column = int(row_and_column.split()[1])
    board[row][column] = current_player

def did_someone_win_horizontally(board):
    for row in board:
        if row[0] != ' ' and row[0] == row[1] and row[0] == row[2]   :
            return True
    return False

def did_someone_win_vertically(board):
    for column_index in range(len(board)):
        if board[0][column_index] != ' ' \
                and (board[0][column_index] == board[1][column_index] \
                and board[0][column_index] == board[2][column_index]):
            return True
    return False

def did_someone_win_diagonally(board):
    return board[1][1] != ' ' and ( ( board[1][1] == board[0][0] and board[1][1] == board[2][2] ) or \
            (board[0][2] == board[1][1] and board[2][0] == board[1][1] ) )


def cats_game(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def is_game_over(board):
    return did_someone_win_horizontally(board) or did_someone_win_vertically(board) or \
            did_someone_win_diagonally(board) or cats_game(board)


numbers = [2, 4, 6, 8, 42, 73]

halved_numbers = [ number / 2 for number in numbers if number % 2 == 0 ]
print(halved_numbers)
halved_numbers = []
for number in numbers:
    if number % 2 == 0:
        halved_numbers.append(number / 2)
print(halved_numbers)




items_in_our_pockets = [
    ['wallet'],
    [1, 2, 3, 4, 5, 6, 7],
    ['car keys', 'air pods', 'change']
]

print(items_in_our_pockets)

ingredients = ['rice', 'Beans', 'veggies', 'corn salsa', 'green salsa', 'guac' ]

ingredients.remove('corn salsa')
ingredients.pop(2)

print(ingredients)

sorted_ingredients = sorted(ingredients)

another_sorted = ingredients[:]
#ingredients.sort()

print(sorted_ingredients)
print(another_sorted)
print(ingredients)

# index will cause an error and crash if the value isn't present
if "chicken" in ingredients:
    print(ingredients.index("chicken"))

print(ingredients.count("chicken"))

# getting a copy of each - read only
for ingredient in ingredients:
    print(ingredient)

# you can modify the list at a given index
for index in range(len(ingredients)):
    print(f'{index}: {ingredients[index]}')

for index, ingredient in enumerate(ingredients):
    print(f'{index}: {ingredient}')



board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

current_player = 'X'
while not is_game_over(board):
    place_mark(board, current_player)
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    #current_player = 'X' if current_player == "O" else "O"
print_board(board)

