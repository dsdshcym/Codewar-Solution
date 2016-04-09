def wins(lines, value):
    for line in lines:
        if not any([ele != value for ele in line]):
            return True
    return False

def isSolved(board):
    board_size = len(board)

    rows = board
    columns = zip(*board)
    diagonal = [board[i][i] for i in range(board_size)]
    anti_diagonal = [board[i][board_size-i-1] for i in range(board_size)]

    lines = rows + columns + [diagonal, anti_diagonal]

    for i in (1, 2):
        if wins(lines, i):
            return i

    if any((0 in row) for row in board):
        return -1

    return 0

print(isSolved([[1,1,1],
                [0,2,2],
                [0,0,0]]))
