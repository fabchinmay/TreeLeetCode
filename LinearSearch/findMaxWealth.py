def findMaxWealth(arr):
    sum = 0
    ind = 0
    fin = 0


    for rows in arr:
        tmpsm = 0
        for i in rows:
            tmpsm+=i

        if sum<tmpsm:
            fin=ind
            sum = tmpsm

        ind+=1

    print(fin)
    return sum

arr=[[1,2,3],[4,5,6],[3,9,8],[1,1,1]]

print(findMaxWealth(arr))





