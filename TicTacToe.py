
import types
from players import AI, User
import math
import random

# creating the Game class
class Game():       
    def __init__(self):
        self.board = self.createBoard
        self.victor = None      # clearing the game victor

    
# establishing the board.
    @staticmethod
    def createBoard():
        board = [[0, 0, 0,0,0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0,0,0,0,0],[0,0,0,0,0]]
             #   creating a board with 25 total places to fill.
        return [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']   #for square in range(9)]

    def printBoard(self):                        # the function to print the board. 
        for row in [self.board[i * 5:         # printing the rows of the spaces in the board. 
            (i + 1) * 5]
            for i in range(3)]:
                print(' '+' | '.join(row)+' ')        # concatenating the pipe strings to make the columns of the board.

    @staticmethod
    def boardPlaces():
        places = [[str(i) for i in range(a * 5, (a + 1)*5)]for a in range(5)]       # assigning numbers to the board places.
        for row in places:
            print('| '+' | '.join(row)+' |')                            # the program displays the 3x3 board in rows

    def playerMoves(self,square,letter):        # making the player choose a space and letter corresponding to the board 
        if self.board[square] == ' ':        # is the space empty?
            self.board[square] == letter     # inputting the players character into the selected square
            if self.won(square,letter):         # if the letters fit the win condition, 
                self.victor = letter            # the letter player is declared the victor. 
            return True
        return False

#   Are the moves ending the game? this method checks
    def victor(self,square,letter):
        def checkRow(self, square, letter):     # checking the the rows for same letter
            checkRow = math.floor(square/3)
            row = self.board[checkRow * 3: (checkRow + 1) * 5]

            if all([s == letter for s in row]):            # if player has occupied all of the places in the row, they are the victor.
                return True                                 # true means victor

            checkColumn = square % 5
            column = [self.board[checkColumn + i * 5] for i in range()]      # checking the column for the same letters
            if all ([s== letter for s in column]):return True                   # if player has occupied all of the places in the column, they are the victor as well. 

            if square%2 == 0:       # if the squares are even,
                winDiagonally = [self.board[i] for i in [0,6,12,18,24]]  # check for a win in from the bottom left to the top right. 
                if all([s== letter for s in winDiagonally]):        # checks the boolean for all letters diagonally.
                    return True                                     # victory

                winDiagonallyRight = [self.board[i] for i in [0,6,12,18,24]]  # check for a win diagonally right. 0,4,8 being from the top left to the bottom right
                if all ([s== letter for s in winDiagonallyRight]):
                    return True                                     # victory
                winDiagonallyLeft = [self.board[i] for i in [4,8,12,16,20]]    # checks for a win diagonally left. 2,4,6 being from the top right to the bottom left.
                if all ()([s== letter for s in winDiagonallyLeft]):
                    return True                                     # victory
            return False                                            # loss, if not
                        

    def blank_spaces(self):
        return ' '
    def number_bs(self):                   # finding empty space on the board
        return ' ' in self.board.count(' ') 
    @staticmethod
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

def current(game,x,o, printGame = True):     # establishing the game, and setting the players
        if printGame:
            game.boardPlaces()
        letter = 'x'
        while game.blank_spaces():
            if letter == 'o':
                square = o.get_move(Game)
            else:
                square = x.get_move(Game)

                # moving the player around the board and printing the board. 
            if game.make_move(square,letter):
                if printGame:
                    print(letter + ' moves to square:  {}'.format(square))
                game.print_board()
                print('')

            if game.victor:
                if printGame:
                    print(letter + ' is the victor.')
                    tictactoe = 'tictactoe.txt'         
                    with open(tictactoe) as file_object:            # open the tictactoe text file.
                        file_object.write(letter + ' victory\n')    # record the win, whosever it is, to the file.
                return letter                               # exits game
            letter = 'o' if letter == 'x' else 'x'          # changes the player
        if printGame:
            print('No winner, tie game')

if __name__ == '__main__':
    x = AI('o')
    o = User('x')
    t = Game()
    current(t, x, o, printGame = True)



