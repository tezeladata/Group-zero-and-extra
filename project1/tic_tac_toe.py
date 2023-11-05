board=[" " for x in range(9)]
def game_board():
    row1=" | {} | {} | {} |".format(board[0], board[1], board[2])
    row2=" | {} | {} | {} |".format(board[3], board[4], board[5])
    row3=" | {} | {} | {} |".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
def move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn player {}".format(number))
    choice=int(input("Enter your choice (1-9): ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = icon

def victory(icon):
    if  (board[0]==icon and board[1]==icon and board[2]==icon) or \
        (board[3]==icon and board[4]==icon and board[5]==icon) or \
        (board[6]==icon and board[7]==icon and board[8]==icon) or \
        (board[0]==icon and board[3]==icon and board[6]==icon) or \
        (board[1]==icon and board[4]==icon and board[7]==icon) or \
        (board[2]==icon and board[5]==icon and board[8]==icon) or \
        (board[0]==icon and board[4]==icon and board[8]==icon) or \
        (board[2]==icon and board[4]==icon and board[6]==icon):
        return True
    else:
        return False

def draw():
    if " " not in board:
        return True
    else:
        return False
while True:
    game_board()
    move("X")
    game_board()
    if victory("X"):
        print("X wins! Congratulations!")
        break
    elif draw():
        print("It's a draw!")
        break
    move("O")
    if victory("O"):
        game_board()
        print("O wins! Congratulations!")
        break
    elif draw():
        print("It's a draw!")
        break