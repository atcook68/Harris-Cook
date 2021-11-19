from players import AI, User
import math
import random

class Game():
    def __init__(self):
        self.board = self.createBoard
        self.victor = None

# establishing the board and the victor.
    def createBoard():     #   creating a board with 9 total places to fill.
        return [' ',' ',' ',' ',' ',' ',' ',' ',' ',]   #for square in range(9)]

    def printBoard(self):                        # the function to print the board. 
        for row in [self.theBoard[i * 3:
            (i + 1) * 3]
            for i in range(3)]:
                print(' '+' | '.join(row)+' ')        # concatenating the pipe strings to make the columns of the board.


    def boardPlaces(self):
        places = [[str(i) for i in range(a * 3, (a + 1)*3)]for a in range(3)]       # assigning numbers to the board places.
        for row in places:
            print('| '+' | '.join(row)+' |')                            # the program displays the 3x3 board in rows

    def playerMoves(self,square,letter):        # making the player choose a space and letter 
        if self.theBoard[square] == ' ':
            self.theBoard[square] == letter
            if self.won(square,letter):
                self.victor = letter
            return True
        return False

#   Are the moves ending the game? this function checks
    def victor(self,square,letter):
        def checkRow(self, square, letter):     # checking the the rows for same letter
            checkRow = math.floor(square/3)
            row = self.theBoard[checkRow * 3: (checkRow + 1) * 3]

            if all([s == letter for s in row]):            # if player has occupied all of the places in the row, they are the victor.
                return True                                 # true means victor

            checkColumn = square % 3
            column = [self.theBoard[checkColumn + i * 3] for i in range()]      # checking the column for the same letters
            if all ([s== letter for s in column]):return True                   # if player has occupied all of the places in the column, they are the victor as well. 

            if square%2 == 0:       # if the squares are even,
                winDiagonally = [self.board[i] for i in [0,4,8]]  # check for a win in from the bottom left to the top right. 
                if all([s== letter for s in winDiagonally]):
                    return True                                     # victory

                winDiagonallyRight = [self.board[i] for i in [0,4,8]]  # check for a win diagonally right. 0,4,8 being from the top left to the bottom right
                if all ([s== letter for s in winDiagonallyRight]):
                    return True                                     # victory
                winDiagonallyLeft = [self.board[i] for i in [2,4,6]]    # checks for a win diagonally left. 2,4,6 being from the top right to the bottom left.
                if all ()([s== letter for s in winDiagonallyLeft]):
                    return True                                     # victory
            return False
                                                    # loss, if not
    def emptySpace(self):
        return ' ' in self.board
    def spacesLeft(self):
        return ' ' in self.board.count(' ')
  #  def spacesLeft(self):
  #      return [i for i, x in enumerate(self.board) if x == ' ']
    def availableMoves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

def current(game,x,o, printGame = True):     # establishing the game, and setting the players
        if printGame:
            game.boardPlaces()
        letter = 'x'
        while game.emptySpace():
            if letter == 'o':
                square = o.get_move(Game)
            else:
                square = x.get_move(Game)
            if game.make_move(square,letter):
                if printGame:
                    print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.victor:
                if printGame:
                    print(letter + ' wins')
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



