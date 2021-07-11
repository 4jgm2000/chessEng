import chess
# from tensorflow import keras
import random
class Eng:
    def __init__(self):
        self.board = None
    
    def updateBoard(self, board):
        self.board = board
    
    def makeMove(self): 
        if(self.board == None):
            print("Error: initialize board first")
            return
        # print(self.board.legal_moves(0))
        return random.choice(list(self.board.legal_moves))
        return None