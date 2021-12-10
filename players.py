import random
import math

class Player:
    def __init__(self,letter):
        self.letter = letter
    def move(self, game):
        pass
class Random_player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        box = random.choice(game.availableMoves())
        return box

class User(Player):       # The player taking your input as the "human/user"
        def __init__(self,letter):
            self.letter = letter
        def move(self, game):
            valid = False
            val=None
            while val == False:
                box = input(self.letter + '\' turn, where do you choose? (space 0 up to space 9): ')
                try:
                    val = int(box)           # turns the value into an integer
                    if val not in game.spacesLeft():
                        raise ValueError
                    valid = True
                except ValueError:
                    print('Make another selection')
            return val



class AI(Player):             # the AI making moves for the computer
        board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        def __init__(self, letter):
            super().__init__(letter)
        def get_move(self, game):
            if len(game.availableMoves(self)) == 25:        # if the board is empty, make a random choice
                box = random.choice(game.availableMoves())
            else:                                       # this is where the minimax algorithm takes place
                box = self.minimax(game, self.letter)['position']        # the minimax algorithm will choose the best choice given the empty spaces.
            return box
        def minimax(self,state,player):              
            current_player = self.letter
            opposition = 'o' if player == 'x' else 'x'
            if state.victor == opposition:            # if the last move won, return
                return {'position': None, 'score':1* (state.emptySpaces() + 1) 
                if opposition == current_player else -1 * (state.num_empty_boxs() + 1)}
            elif not state.blank_spaces(self):            # if no empty boxes are available
                return {'position':None,'score':0}      # return a score of zero

            if player == current_player:                                    #
                optimal = {'position':None, 'score':-math.inf}              #
            else:
                optimal = {'position': None,'score':math.inf}               #
            for potential_moves in state.availableMoves(self):                   #
                state.make_move(potential_moves,player)                       #
                score = self.minimax(state,opposition)                      #

                state.board[potential_moves] = ' '
                state.victor = None
                score['position'] = potential_moves

                if player == AI:
                    if score['score'] > best['score']:
                        best = score
                else:
                    if score['score'] < best['score']:
                        best = score
            return optimal
