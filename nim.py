from operator import xor

def choose_move(board):
    xor_all = reduce(xor, board)
    for i, x in enumerate(board):
        if x >= xor_all ^ x:
            return (i, x - (xor_all ^ x))
    return (0, 1)
