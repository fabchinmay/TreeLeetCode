def findPathBackTrack(p,maze,r,c):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        print(p)
        return

    if not maze[r][c]:
        return

    maze[r][c]=False



    if r<len(maze)-1:
        findPathBackTrack(p+"D",maze,r+1,c)
    if c<len(maze[0])-1:
        findPathBackTrack(p+"R",maze,r,c+1)

    if r>0:
        findPathBackTrack(p+"U",maze,r-1,c)

    if c>0:
        findPathBackTrack(p+"L",maze,r,c-1)

    maze[r][c] = True


#board=[[True,True,True],[True,True,True],[True,True,True]]

#findPathBackTrack("",board,0,0)



def allPathPrint(p, maze, r, c, path, step):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        path[r][c] = step
        for arr in path:
            print(arr)
        print(p)
        print()
        return

    if not maze[r][c]:
        return

    # i am considering this block in my path
    maze[r][c] = False
    path[r][c] = step
    if r < len(maze) - 1:
        allPathPrint(p + 'D', maze, r+1, c, path, step+1)

    if c < len(maze[0]) - 1:
        allPathPrint(p + 'R', maze, r, c+1, path, step+1)

    if r > 0:
        allPathPrint(p + 'U', maze, r-1, c, path, step+1)

    if c > 0:
        allPathPrint(p + 'L', maze, r, c-1, path, step+1)

    # this line is where the function will be over
    # so before the function gets removed, also remove the changes that were made by that function
    maze[r][c] = True
    path[r][c] = 0

board = [[True, True, True], [True, True, True], [True, True, True]]
path = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
allPathPrint("", board, 0, 0, path, 1)


path = [["" for _ in range(5)] for _ in range(5)]



