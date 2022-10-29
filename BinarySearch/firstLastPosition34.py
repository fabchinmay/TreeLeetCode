def findFirstnLastPosition(arr,target):
    ans=[-1,-1]
    start =searchTarget(arr,target,True)
    end =searchTarget(arr,target,False)
    ans[0]=start
    ans[1]=end

    return ans

def searchTarget(arr,target,isStartIndex):
    ans =-1
    start = 0
    end = len(arr)-1

    while start<=end:
        mid = start+(end-start)//2

        if arr[mid]>target:
            end = mid-1
        elif arr[mid]<target:
            start=mid+1
        else:
            ans=mid
            if isStartIndex:
                end=mid-1
            else:
                start=mid+1
    return ans

arr=[5,7,7,7,7,7,8,8,10]
target=7
print(findFirstnLastPosition(arr,target))