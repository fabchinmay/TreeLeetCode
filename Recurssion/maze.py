def count(r,c):
    if r==1 or c==1:
        return 1
    left = count(r-1,c)
    right = count(r,c-1)

    return left+right

#print(count(2,2))


def FindPath(p,r,c):
    if r==1 and c==1:
        print(p)
        return

    # if r>1:
    #     FindPath(p+'D',r-1,c)
    # if c>1:
    #     FindPath(p+'R',r,c-1)
    # Diagonal ----
    if r>1 and c>1:
        FindPath(p + 'D', r-1, c - 1) # Diagonal path move
    if r > 1:
        FindPath(p + 'V', r - 1, c)
    if c > 1:
        FindPath(p + 'H', r, c - 1)


#FindPath("",3,3)

def findRestrictedPath(p,maze,r,c):
    #print("hello")
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(p)
        return

    if not maze[r][c]:
        return

    if r<len(maze)-1 :
        findRestrictedPath(p+"D",maze,r+1,c)
    if c<len(maze[0])-1 :
        findRestrictedPath(p+"R",maze,r,c+1)

board=[[True,True,True],[True,False,True],[True,True,True]]

findRestrictedPath("",board,0,0)

