def findPair(arr,tar):
    tempDict = dict()
    res=[]
    for i in range(len(arr)):
        diff = tar-arr[i]
        if diff in tempDict:
            res.append([i,tempDict.get(diff)])
        else:
            tempDict[arr[i]]=i

    return res

arr =[1,2,3,4,5,6,7,8,9]
tar=10

print(findPair(arr,tar))