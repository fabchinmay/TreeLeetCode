def aggressiveCow(arr,k):
    arr.sort()
    left = 0
    right = max(arr)- min(arr)
    ans=0

    while left<=right:
        mid = left + (right-left)//2

        if isPossible :
            ans= mid
            left = mid+1
        else:
            right = mid-1

    return ans



def isPossible(arr,mid,k):
    cntCow=1
    lastPos = arr[0]
    for i in range(len(arr)):
        if arr[i]-lastPos>=mid:
            cntCow+=1
            if cntCow==k:
                return True
            lastPos=arr[i]

    return False

arr = [4,2,1,3,6]
k=2

print(aggressiveCow(arr,k))


