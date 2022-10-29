def getRange(arr,target):
    start=0
    end=1
    ans=0
    while target>arr[end]:
        newStart = end+1
        end = (end-start+1)*2+end
        start= newStart

    ans=getBinarySearch(arr,start,end,target)

    return ans


def getBinarySearch(arr,start,end,target):
    while start<=end:
        mid = start + (end-start)//2

        if arr[mid]>target:
            end = mid-1
        elif arr[mid]<target:
            start = mid+1
        else:
            return mid
    return -1

arr=[3,5,7,9,10,90,100,130,140,160,170,200,201,202,203,204,205,207,209,210]
target=130

print(getRange(arr,target))