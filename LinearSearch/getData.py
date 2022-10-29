def getData(arr,target):
    if len(arr)==0:
        return -1
    
    for i in range(len(arr)):
        if target==arr[i]:
            return i

    return -1

arr=[10,32,77,4,2]
target=2

print(getData(arr,target))