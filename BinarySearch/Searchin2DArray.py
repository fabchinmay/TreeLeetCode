def search(arr,target):
    row = 0
    col = len(arr[0])-1

    while row<len(arr) and col >=0:
        if arr[row][col]==target:
            return [row,col]
        elif arr[row][col]>target:
            col-=1
        else:
            row+=1

    return [-1,-1]

arr=[[10,20,30,40],
    [12,25,35,45],
    [28,29,37,49],
    [33,34,38,50]]

print(search(arr,29))