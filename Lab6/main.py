
def drop_piece(board, current_player):
    column_index = int(input("Enter the column you want to drop a piece in"))
    while board[0][column_index] != ' ':
        print("that column is full")
        column_index = int(input("Enter the column you want to drop a piece in"))

    # row_index = 5
    # while row_index >= 0:
    #
    #     row_index -= 1

    for row_index in range(5, -1, -1):
        if board[row_index][column_index] == ' ':
            board[row_index][column_index] = current_player
            return
            # break

def did_someone_win_diagonally_down(board):
    for row_index in range(3):
        for column_index in range(4):
            if board[row_index][column_index] != ' ' and \
                    board[row_index][column_index] == board[row_index + 1][column_index + 1] and \
                    board[row_index][column_index] == board[row_index + 2][column_index + 2] and \
                    board[row_index][column_index] == board[row_index + 3][column_index + 3]:
                return True
    return False

def print_board(board):
    for row in board:
        print(row)

board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

# don't do this
while True:
    print_board(board)
    drop_piece(board, "X")