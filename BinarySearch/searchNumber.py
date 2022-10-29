def findElement(arr,target):
    start = 0
    end = len(arr)-1

    while start<=end:
        mid = start + (end-start)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end = mid-1
        elif arr[mid]<target:
            start=mid+1

    return -1
def bsearch(arr,target):
    left ,right = 0,len(arr)
    while left<right:
        mid = left + (right-left)//2
        if arr[mid]>=target:
            right = mid
        else:
            left = mid+1

    return left

arr =[2,4,6,9,11,12,14,20,36,48]

print(findElement(arr,48))

print(bsearch(arr,50))