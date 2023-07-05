"""
AI player for TicTacToe game
"""

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns the initial state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn based on the given board status.
    """
    Itr = 0
    for row in board:
        Itr += row.count(X) + row.count(O)
    if Itr % 2 == 0:
        return X
    return O


def actions(board):
    """
    Returns all possible set of actions (i, j) available on the given board status.
    """
    moves = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                moves.append((i, j))
    return moves


def result(board, action):
    """
    Returns the board status that results from an action / move (i, j) on the board.
    """
    import copy
    if action not in actions(board):
        raise Exception("Invalid action")
    resultant_board = copy.deepcopy(board)
    resultant_board[action[0]][action[1]] = player(board)
    return resultant_board


def winner(board):
    """
    Returns the winner of the game.
    """
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    for col in zip(*board):
        if col[0] == col[1] == col[2]:
            return col[0]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def terminal(board):
    """
    check if there is a winner, and if yes, Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    best_move = None
    best_val = None
    for move in actions(board):
        new_board = result(board, move)
        val = minimax_value(new_board)
        if best_val is None or (player(board) == X and val > best_val) or (player(board) == O and val < best_val):
            best_val = val
            best_move = move
    return best_move

def minimax_value(board):
    if terminal(board):
        return utility(board)
    best_val = None
    for move in actions(board):
        val = minimax_value(result(board, move))
        if best_val is None or (player(board) == X and val > best_val) or (player(board) == O and val < best_val):
            best_val = val
    return best_val