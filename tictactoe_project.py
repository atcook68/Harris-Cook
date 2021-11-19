#Creating game board

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

user = True # when true it refers to x, otherwise o
turns = 0
#creatingarrays to house the info in the tic tac toe structure

def print_board(board): #printing board in terminal
    for row in board: #telling system to check each row in board
        for slot in row: #telling system to more specifically go row by row in board
            print(f"{slot} " + " ", end="") #using f function to print in each slot
        print()

def quit(user_input): #telling system when to quit or if player would like to quit, they can select q
   if user_input.lower() == "q": 
       print("Thank you for playing!")
       return True
   else: return False

def check_input(user_input): #used to check if the number is 1-9
    if not isnum(user_input): return False
    user_input = int(user_input)
    if not bounds(user_input): return False

    return True

def isnum(user_input): #used to note when a number is not valid as a value
    if not user_input.isnumeric():
        print("Not valid number.")
        return False
    else: return True

def bounds(user_input): #setting boundaries on numbers outside of 1 and 9
    if user_input > 9 or user_input < 1:
        print("Number is not valid.")
        return False
    else: return True

def istaken(coords, board): #used to show when a position is already taken
    row = coords[0]
    col = coords [1]
    if board[row][col] != "-":
        print("This position is already full.")
        return True
    else: return False

def coordinates(user_input): #used to input numbers in range in the chart
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(col % 3)
    return (row, col)

def add_to_board(coords, board, active_user): #allows users to input the numbers in
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(user): #telling the program to return x and if use o if x is not selected
    if user: return "x"
    else: return "o"

def iswin(user, board): #telling the program to check the rows, columns, and diagonals for tictactoe sequence
    if check_row(user, board): return True
    if check_col(user, board): return True
    if check_diag(user, board): return True
    return False

def check_row(user, board): #checking rows foe user inputs
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row: return True
    return False

def check_col(user, board): #checking columns for user inputs
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
            if complete_col: return True
        return False

def check_diag(user, board): #checking diagonaly for winner by user inputs
    if board[0][1] == user and board[1][1] == user and board[2][2] == user: return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
    else: return False

while turns < 9:
    active_user = current_user(user) #created sequence for the game prompts to start playing and allowing a q for quit
    print_board(board)
    user_input = input("Enter a position 1 through 9 or enter \"q\" to quit:")
    if quit(user_input): break
    if not check_input(user_input):
        print("Please enter again.") #error messages if user does not input values correctly
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Please enter again.")
        continue
    add_to_board(coords, board, active_user) #winning message for user
    if iswin(active_user, board):
        print(f"{active_user.upper()} Win!")
        break

    turns += 1 #telling system to show tie message if both users do not win
    if turns == 9: print("Tie!")
    user = not user