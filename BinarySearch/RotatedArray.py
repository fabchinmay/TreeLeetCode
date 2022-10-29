def BinarySearch(arr,target,start,end):
    while start<=end:
        mid = start+(end-start)//2
        if arr[mid]>target:
            end=mid-1
        elif arr[mid]<target:
            start=mid+1
        else:
            return mid
    return -1
def findPivot(arr):
    start=0
    end =len(arr)-1

    while start<=end:
        mid = start + (end-start)//2

        if mid<end and arr[mid] > arr[mid+1]:
            return mid
        elif mid>start and arr[mid]<arr[mid-1]:
            return mid-1
        elif arr[start]>arr[mid]:
            end = mid-1
        else:
            start=mid+1

    return -1

def findPivotWithDuplicateArray(arr):
    start=0
    end= len(arr)-1

    while start<=end:
        mid = start + (end-start)//2
        if arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid-1]>arr[mid]:
            return mid-1

        if arr[start]==arr[mid] and arr[mid]==arr[end]:
            if arr[start]>arr[start+1]:
                return start
            start+=1

            if arr[end]<arr[end-1]:
                return end-1
            end-=1
        elif (arr[start]<arr[mid] or (arr[mid]>arr[end] and arr[start]==arr[mid])):
            start=mid+1
        else:
            end=mid-1

    return -1


def search(arr,target):
    pivot = findPivot(arr)
    print(pivot)
    start=0
    end = len(arr)-1

    if pivot==-1:
        return BinarySearch(arr,target,start,end)

    if arr[pivot]==target:
        return pivot
    elif arr[start]<=target:
        return BinarySearch(arr, target,start,pivot-1)


    return BinarySearch(arr, target,pivot+1,end)

arr = [6,7,8,0,1,2,3,4,5]

print(search(arr,7))
