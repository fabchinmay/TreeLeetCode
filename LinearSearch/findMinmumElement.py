def findMinimumElement(arr):
    min=0
    for i in range(len(arr)):
        if min>arr[i]:
            min=arr[i]
    return min

arr=[18,12,-7,3,14,28]
print(findMinimumElement(arr))
