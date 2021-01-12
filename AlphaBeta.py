import OthelloLogic
import AuthCheck
import requests

headers = AuthCheck.auth_check("http://tdu-othello.xyz/api")
r = requests.post("http://tdu-othello.xyz/api/where", headers=headers)
data = r.json()
PLAYER = data['player']
ENEMY = PLAYER * -1
SIZE = 8

best_move = []

def execute(board, moves, depth, alpha, beta):
    max_level(board, moves, depth, alpha, beta)
    return self.best_move

def max_level(board, moves, depth, alpha, beta):
    if depth <= 0:
        return calc_eval_score(board);

    score, max_score = 0, 0;
    max_move = []

    for move in moves:
        nb = get_next_board(board, move, ENEMY)
        nm = OthelloLogic.getMoves(nb, PLAYER, SIZE)
        score = min_level(nb, nm, depth, alpha, beta)

        if score >= beta:
            return score

        if score > max_score:
            max_score = score
            alpha = max(max_score, alpha)
            

    depth -= 1

    return max_score

def min_level(board, moves, depth, a, b):
    if depth <= 0:
        return calc_eval_score(board);
            
    score, min_score = 0, 0;

    for move in moves:
        nb = get_next_board(board, move, PLAYER)
        nm = OthelloLogic.getMoves(nb, ENEMY, SIZE)
        score = max_level(nb, nm, depth, alpha, beta)

        if score <= alpha:
            return score

        if score < min_score:
            min_score = score
            beta = min(beta, min_score)

    depth -= 1
    step += 1

    return min_score


def calc_eval_score(board):
    board_score = [
        [ 30, -12,  0, -1, -1,  0, -12,  30],
        [-12, -15, -3, -3, -3, -3, -15, -12],
        [  0,  -3,  0, -1, -1,  0,  -3,   0],
        [ -1,  -3, -1, -1, -1, -1,  -3,  -1],
        [ -1,  -3, -1, -1, -1, -1,  -3,  -1],
        [  0,  -3,  0, -1, -1,  0,  -3,   0],
        [-12, -15, -3, -3, -3, -3, -15, -12],
        [ 30, -12,  0, -1, -1,  0, -12,  30]
    ]
    eval_score = 0
    for x in board:
        for y in board:
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
            count = count_flippable(board, side, x, y, d, e)
            for i in range(1, count + 1):
                board[x + i * d][y + i * e] = side
    
    board[x][y] = side
        
def count_flippable(board, side, x, y, d, e):
    i = 1
    while(board[x + i * d][y + i * e] == ENEMY):
        i += 1
    if board[x + i * d][y + i * e] == PLAYER:
        return i - 1
    else:
        return 0
