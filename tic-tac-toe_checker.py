def check(to_check, value):
    return any((set(row) == set([value])) for row in to_check)

def isSolved(board):
    board_size = len(board)
    to_check = board + zip(*board)
    to_check.append([board[i][i] for i in range(board_size)])
    to_check.append([board[i][board_size-i-1] for i in range(board_size)])

    x_won = check(to_check, 1)
    o_won = check(to_check, 2)
    if x_won and o_won:
        return 0
    elif x_won:
        return 1
    elif o_won:
        return 2
    elif any((0 in row) for row in board):
        return -1
    else:
        return 0

print(isSolved([[1,1,1],
                [0,2,2],
                [0,0,0]]))
