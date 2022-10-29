def splitArray(arr,m):
    start=0
    end=0

    for i in range(len(arr)):
        start = max(start,arr[i])
        end +=arr[i]

    print(start)
    print(end)

    while start<end:
        mid = start + (end-start)//2
        sum=0
        pieces =1
        for n in arr:
            if sum+n>mid:
                #you can not add this to this subarray make new one
                sum = n
                pieces+=1
            else:
                sum +=n
        if pieces<=m:
            end = mid
        else:
            start=mid+1


    return end


arr=[7,2,5,10,8 ]

print(splitArray(arr,2))