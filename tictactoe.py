"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count_X = 0
    count_O = 0
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board [row] [col] == X:
                count_X += 1
            if board [row][col] == O:
                count_O += 1
    
    if count_X > count_O:
        return O
    else:
        return X


def actions(board):
    available_actions = set()
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                available_actions.add((i, j))
    
    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('Invalid Action')
    
    i, j = action
    board_copy = copy.deepcopy(board)
    
    board_copy[i][j] = player(board)
    
    return board_copy

def checkRow(board, player):
    for row in range(len(board)):
        if board [row] [0] == player and board [row] [1] == player and board [row] [2] == player:
            return True
    return False

def checkCol(board, player):
    for col in range(len(board)):
       if board [0] [col] == player and board [1] [col] == player and board [2] [col] == player:
            return True
    return False 
            
def checkFirstDiag(board, player):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return True
    return False

def checkSecondDiag(board, player):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[0][2] == player and board[1][1] == player and board[2][0] == player:
                return True
    return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board, X) or checkCol(board, X) or checkFirstDiag(board, X) or checkSecondDiag(board, X):
        return X
    elif checkRow(board, O) or checkCol(board, O) or checkFirstDiag(board, O) or checkSecondDiag(board, O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    
def max_val(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_val(result(board, action)))
    return v

def min_val(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_val(result(board, action)))
    return v
        
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_val(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_val(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]
