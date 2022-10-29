def squareRoot(x):
    start = 1
    end = x
    ans = 0

    while start<=end:
        mid = start+ (end - start)//2

        if mid <= x/mid:
            start = mid+1
            ans = mid
        else:
            end = mid-1

    return ans


def sqrt(x):
    left = 0
    right = x+1

    while left<right:
        mid = left + (right-left)//2
        if mid*mid>x:
            right=mid
        else:
            left=mid+1

    return left-1


def bsearch(arr,target):
    left=0
    right=len(arr)

    while left<right:
        mid = left+ (right-left)//2

        if arr[mid]>=target:
            right=mid
        else:
            left=mid+1

    return left

arr =[1,3,5,6]
target=2

print(bsearch(arr,target))



print(squareRoot(20))
print(sqrt(20))