from random import randrange

board = []

for x in range(5):
    board.append(["O"] * 5)
    
def print_board(board):
    for row in board:
        print(' '.join(row))
        
kang_row = randrange(5)
kang_column = randrange(5)
board[kang_row][kang_column] = "K"

flow_row = randrange(5)
flow_column = randrange(5)
board[flow_row][flow_column] = "F"

moveX = kang_row - flow_row
moveY = kang_column - flow_column
print("Let's play Pick & Pluck!")

while(kang_row != flow_row or kang_column != flow_column):
    print_board(board)
    if (moveX < 0):
        board[kang_row][kang_column] = "O"
        kang_row += 1
        board[kang_row][kang_column] = "K"
        moveX += 1
    elif (moveX > 0):
        board[kang_row][kang_column] = "O"
        kang_row -= 1
        board[kang_row][kang_column] = "K"
        moveX -= 1
    elif (moveY < 0):
        board[kang_row][kang_column] = "O"
        kang_column += 1
        board[kang_row][kang_column] = "K"
        moveY += 1
    elif (moveY > 0):
        board[kang_row][kang_column] = "O"
        kang_column -= 1
        board[kang_row][kang_column] = "K"
        moveY-= 1
    print("\n")

board[flow_row][flow_column] = "*"
print_board(board)
print("Flower was plucked!")
