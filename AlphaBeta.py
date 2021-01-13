import OthelloLogic as ol
import sys

# SIDE: BLACK = 1, WHITE = -1
SIDE = 1
# Board size
SIZE = 8

# Alpha-Beta search
def ab(board, moves, lim, a, b, side):
    # print(moves)
    if lim == 0:
        return calc_eval_score(board)
    """
    if len(moves) == 0:
        pass
        eval = -ab(board)
    """
    for move in moves:
        # print(move)
        nb = get_next_board(board, move, -side)
        enemy_hand = ol.getMoves(nb, -SIDE, SIZE)
        eval = -ab(board, enemy_hand, lim - 1, -b, -a, -side)
        a = max(a, eval)

        if a >= b:
            return a

    return a

def sort(board, moves, lim):
    scores = []
    for move in moves:
        nb = get_next_board(board, move, SIDE)
        eval = -ab(nb, moves, lim - 1, -sys.maxsize, sys.maxsize, SIDE)
        scores.append([move, eval])

    scores.sort(key=lambda x: x[1])
    res = []
    for i in scores:
        res.append(i[0])

    return list(reversed(res))

def calc_eval_score(board):
    board_score = [
        [ 30, -12,  0, -1, -1,  0, -12,  30],
        [-12, -15, -3, -3, -3, -3, -15, -12],
        [  0,  -3,  0, -1, -1,  0,  -3,   0],
        [ -1,  -3, -1,  0,  0, -1,  -3,  -1],
        [ -1,  -3, -1,  0,  0, -1,  -3,  -1],
        [  0,  -3,  0, -1, -1,  0,  -3,   0],
        [-12, -15, -3, -3, -3, -3, -15, -12],
        [ 30, -12,  0, -1, -1,  0, -12,  30]
    ]
    eval_score = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 1:
                eval_score += board_score[x][y]

    return eval_score;

def get_next_board(board, move, side):
    count = 0
    x = move[0]
    y = move[1]

    for p in range(-1, 2):
        for q in range(-1, 2):
            if (p == 0)and(q == 0):
                continue
            count = count_flippable(board, side, x, y, p, q)
            # print(count)
            for i in range(1, count + 1):
                try:
                    board[x + i * p][y + i * q] = side
                except IndexError:
                    continue
    
    board[x][y] = side

    return board

def count_flippable(board, side, x, y, d, e):
    i = 1
    try:
        while(board[x + i * d][y + i * e] == -side):
            i += 1
    except IndexError:
        pass
    # print(i)
    try:
        if board[x + i * d][y + i * e] == side:
            return i - 1
        else:
            return 0
    except IndexError:
        return 0
