from random import randrange
board = []

for x in range(5):
    board.append(["O"] * 5)
    
def print_board(board):
    for row in board:
        print(' '.join(row))
        
shipX = randrange(5)
shipY = randrange(5)
counter = 0

print("Let's play battleship!\nTry and sink my battleship in 4 tries!\n")

while (counter < 4):
    print_board(board)
    try:
        row_guess = int(input("\nPlease guess a row: "))
        column_guess = int(input("Please guess a column: "))
    
        if ((row_guess < 0 or row_guess > 4) or (column_guess < 0 or column_guess > 4)):
            print("\nInvalid input--out of board range\n")
            
        elif (board[row_guess][column_guess] == "X"):
            print("\nInvalid input--you have already guessed this coordinate\n")
            
        elif (row_guess != shipX or column_guess != shipY):
            print("\nIncorrect guess")
            board[row_guess][column_guess] = "X"
            counter += 1
            print("You have", 4 - counter, "tries left!\n")
            
        elif (row_guess == shipX and column_guess == shipY):
            counter += 1
            print("\nYou have sunk my battleship in", counter, "tries!")
            break;
            
    except Exception as e:
        print("\nInvalid input--please enter a number\n")

if (row_guess != shipX or column_guess != shipY):
    print("Here was my ship!\n")
    board[shipX][shipY] = "*"
    print_board(board)
    print("\nYou failed to sink my battleship! Please try again!")