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
                square = input(self.letter + '\' turn, where do you choose? (0 up to 0): ')
                try:
                    val = int(square)           # turns the value into an integer
                    if val not in game.spacesLeft():
                        raise ValueError
                    valid = True
                except ValueError:
                    print('Make another selection')
            return val

class AI(Player):             # the AI making moves for the computer
        def __init__(self, letter):
            super().__init__(letter)
        def get_move(self, game):
            if len.game.available_moves() == 9:        # if the board is empty, make a random choice
                square = random.choice(game.available_moves())
            else:                                       # this is where the minimax algorith takes place
                square = self.minimax(game, self.letter)['position']        # the minimax algorithm will choose the best choice given the empty spaces.
            return square
        def minimax(self,state,player):                
            max_player = self.letter
            other_player = 'o' if player == 'x' else 'x'
            if state.current_winner == other_player:            # if the last move won, return
                return {'position': None, 'score':1* (state.emptySpaces() + 1) 
                if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
            elif not state.empty_squares():            # if no empty squares are available
                return {'position':None,'score':0}      # return a score of zero

            if player == max_player:
                optimal = {'position':None, 'score':-math.inf} 
            else:
                optimal = {'position': None,'score':math.inf}
            for possible_move in state.available_moves():
                state.make_move(possible_move,player)
                score = self.minimax(state,other_player)

