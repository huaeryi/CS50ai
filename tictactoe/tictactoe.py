"""
Tic Tac Toe Player
"""
import copy
import math

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
    """
    Returns player who has the next turn on a board.
    """
    numX = 0
    numO = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                numX += 1
            elif board[i][j] == O:
                numO += 1
    if numX == numO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ret = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                ret.append((i, j))
    return ret

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = copy.deepcopy(board)
    i,j = action
    if player(board) == X:
        newboard[i][j] = X
    else:
        newboard[i][j] = O
    return newboard
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def isWin(player):
        for i in range(3):
            count = 0
            for j in range(3):
                if board[i][j] == player:
                    count += 1
            if count == 3:
                return True
                
        for j in range(3):
            count = 0
            for i in range(3):
                if board[i][j] == player:
                    count += 1
            if count == 3:
                return True
        i = 0
        j = 0
        count = 0
        while i < 3 and j < 3:
            if board[i][j] == player:
                count += 1 
            i += 1
            j += 1
        if count == 3:
            return True

        i = 2
        j = 0
        count = 0
        while i >= 0 and j < 3:
            if board[i][j] == player:
                count += 1
            i -= 1
            j += 1
        if count == 3:
            return True
        return False
    
    if isWin(X):
        return X
    elif isWin(O):
        return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if not board[i][j] is EMPTY:
                count += 1
    if count == 9:
        return True
    if winner(board) == X or winner(board) == O:
        return True
    else:
        return False

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

def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    return v

def minvalue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    X : Max
    O : Min
    """
    if terminal(board):
        return None

    L = []
    acts = actions(board)
    turn = player(board)
    if turn == X:
        for act in acts:
            L.append(minvalue(result(board, act)))
        tar = L.index(max(L))
        return acts[tar]
    else:
        for act in acts:
            L.append(maxvalue(result(board, act)))
        tar = L.index(min(L))
        return acts[tar]



