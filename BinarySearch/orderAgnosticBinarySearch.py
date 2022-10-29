def orderAgnostics(arr,target):
    start = 0
    end = len(arr)-1
    orderFlag = "Ascending"

    ind = -1

    if arr[start]>arr[end]:
        orderFlag = "Descending"
        ind = binarySearchDescending(arr, target)
    else:
        orderFlag = "Ascending"
        ind = binarySearchAscending(arr,target)

    return ind

def binarySearchAscending(arr,target):
    start = 0
    end = len(arr)-1

    while start<=end:
        mid = start+(end-start)//2

        if arr[mid]>target:
            end = mid-1
        elif arr[mid]<target:
            start = mid+1
        else:
            return mid

    return -1

def binarySearchDescending(arr,target):
    start = 0
    end = len(arr)-1

    while start<=end:
        mid = start + (end-start)//2
        print(mid)

        if target>arr[mid]:
            end = mid-1
        elif target<arr[mid]:
            start = mid+1
        else:
            return mid

    return -1

#arr =[2,4,6,9,11,12,14,20,36,48]
arr= [67,34,23,12,11,10,8,7,5,4]
print(orderAgnostics(arr,67))