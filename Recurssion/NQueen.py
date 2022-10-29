def queens(board, row):
    if row == len(board):
        _display(board)
        print()
        return 1

    count = 0

    # placing the queen and checking for every row and col
    col = 0
    while col < len(board):
        # place the queen if it is safe
        if _isSafe(board, row, col):
            board[row][col] = True
            count += queens(board, row + 1)
            board[row][col] = False
        col += 1

    return count

@staticmethod
def _isSafe(board, row, col):
    # check vertical row
    for i in range(0, row):
        if board[i][col]:
            return False

    # diagonal left
    maxLeft =min(row, col)
    for i in range(1, maxLeft + 1):
        if board[row-i][col-i]:
            return False

    # diagonal right
    maxRight =min(row, len(board) - col - 1)
    for i in range(1, maxRight + 1):
        if board[row-i][col+i]:
            return False

    return True

@staticmethod
def _display(board):
    for row in board:
        for element in row:
            if element:
                print("Q ", end = '')
            else:
                print("X ", end = '')
        print()

n = 5
board = [[ False for _ in range(n)] for _ in range(n)]
print(queens(board, 0))
