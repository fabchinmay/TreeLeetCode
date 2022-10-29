#Find smallest letter getter than Target lC#744
def binarySearch(arr,target,isCeil):
    start = 0
    end = len(arr)-1
    if arr[end]<target or arr[start]>end:
        return -1
    while start<=end:
        mid = start+(end-start)//2

        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]>target:
            end=mid-1
        elif arr[mid]<target:
            start=mid+1

    return arr[start] if isCeil  else  arr[end]

def binarySearchCharacter(arr,target,isCeil):
    start = 0
    end = len(arr)-1
    if arr[end]<target or arr[start]>end:
        return -1
    while start<=end:
        mid = start+(end-start)//2

        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]>target:
            end=mid-1
        elif arr[mid]<target:
            start=mid+1

    return arr[start] if isCeil  else  arr[end]

def nextGreatestLetter(letters,target) -> str:
    start = 0
    end = len(letters) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if letters[mid] < target:
            start = mid + 1
        elif letters[mid] > target:
            end = mid - 1

    return letters[start % len(letters)]

arr =[2,3,5,9,14,16,18]
letters = ["c","f","j"]
target = "a"
print(nextGreatestLetter(letters,target))
print(binarySearch(arr,15,False))
            
