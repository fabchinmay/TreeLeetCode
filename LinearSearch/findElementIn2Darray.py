def findElementIn2Darray(arr,target):
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if target == arr[row][col]:
                return [row,col]

    return [-1,-1]

arr=[[13,14,87],[65,23,67],[63,89,98]]

print(findElementIn2Darray(arr,98))


ab = 5468
cnt = 0

while ab>0:
    cnt +=1
    ab = ab//10


print(cnt)


