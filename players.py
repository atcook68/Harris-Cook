import random
import math

class Player:
        def __init__(self,letter):
            self.letter = letter
        def move(self, game):
            pass

class User(Player):       # The player taking your input as the "human/user"
        def __init__(self,letter):
            self.letter = letter
        def move(self, game):
            valid = False
            val=None
            while val == False:
                square = input(self.letter + '\' turn, where do you choose? (space 0 up to space 9): ')
                try:
                    val = int(square)           # turns the value into an integer
                    if val not in game.spacesLeft():
                        raise ValueError
                    valid = True
                except ValueError:
                    print('Make another selection')
            return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class AI(Player):             # the AI making moves for the computer
        def __init__(self, letter):
            super().__init__(letter)
        def get_move(self, game):
            if len(game.available_moves(self)) == 9:        # if the board is empty, make a random choice   ---------alterrrrr
                square = random.choice(game.availableMoves())
            else:                                       # this is where the minimax algorith takes place
                square = self.minimax(game, self.letter)['position']        # the minimax algorithm will choose the best choice given the empty spaces.
            return square
        def minimax(self,state,player):              
            current_player = self.letter
            opposition = 'o' if player == 'x' else 'x'
            if state.current_winner == opposition:            # if the last move won, return
                return {'position': None, 'score':1* (state.emptySpaces() + 1) 
                if opposition == current_player else -1 * (state.num_empty_squares() + 1)}
            elif not state.empty_squares():            # if no empty squares are available
                return {'position':None,'score':0}      # return a score of zero

            if player == current_player:                                    #
                optimal = {'position':None, 'score':-math.inf}              #
            else:
                optimal = {'position': None,'score':math.inf}               #
            for possible_move in state.availableMoves():                   #
                state.make_move(possible_move,player)                       #
                score = self.minimax(state,opposition)                      #

                state.board[possible_move] = ' '
                state.victor = None
                score['position'] = possible_move

                if player == AI:
                    if score['score'] > best['score']:
                        best = score
                else:
                    if score['score'] < best['score']:
                        best = score
            return best
