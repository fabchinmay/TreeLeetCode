def Queen(board,row):
    if row==len(board):
        display(board)
        return 1

    col = 0
    cnt = 0

    while col<len(board):
        if isSafe(board,row,col):
            board[row][col]=True
            cnt+=Queen(board,row+1)
            board[row][col]=False

        col+=1

    return cnt

def isSafe(board,row,col):
    for i in range(0,row):
        if board[i][col]:
            return False

    minRight = min(row,len(board)-col-1)

    for i in range(minRight+1):
        if board[row-i][col+i]:
            return False

    minLeft = min(row,col)

    for i in range(minLeft+1):
        if board[row-i][col-i]:
            return False

    return True


def display(board):
    for row in board:
        for element in row:
            if element:
                print("Q ",end=' ')
            else:
                print("X ",end=' ')
        print()



n=5
board = [[False for _ in range(n)] for _ in range(n)]

print(Queen(board,0))