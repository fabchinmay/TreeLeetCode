def findPeak(arr):
    start = 0
    end = len(arr)
    while start<=end:
        mid = start+(end-start)//2

        if arr[mid-1]<arr[mid]<arr[mid+1]:
            start = mid
        elif arr[mid-1]>arr[mid]>arr[mid+1]:
            end = mid
        else:
            if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
                return arr[mid]

    return -1
#https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/blob/main/lectures/10-binary%20search/code/src/com/kunal/Mountain.java

def findPeakElement(arr):
    start = 0
    end = len(arr)-1

    while start<end:
        mid= start+(end-start)//2

        if arr[mid]>arr[mid+1]:
            end = mid
        else:
            start = mid+1



    return arr[start]


def findPeakElementinRotatedArray(arr):
    start = 0
    end = len(arr)-1

    while start<end:
        mid= start+(end-start)//2

        if arr[mid]>arr[mid+1]:
            start = mid + 1
        else:
            end = mid




    return arr[start]

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


arr=[1,2,3,5,7,8,9,7,6,5,4,3,2]
arr1=[1,2,3,5,7,6,5,4,3,2]
arr2=[6,7,8,1,2,3,4,5]
arr3= [6,7,8,0,1,2,3,4,5]
arr4=[10, 20, 15, 2, 23, 90, 67]
print(findPeak(arr))
print(findPeakElement(arr1))
print(findPeakElementinRotatedArray(arr2))
print(findPeakElementinRotatedArray(arr3))
print(findPeakElementinRotatedArray(arr4))
print("Pivot-----------")
print(arr[findPivot(arr)])
print(arr1[findPivot(arr1)])
print(arr2[findPivot(arr2)])
print(arr3[findPivot(arr3)])
print(arr4[findPivot(arr4)])