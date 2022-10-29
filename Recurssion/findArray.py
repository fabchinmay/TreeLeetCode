def findArray(arr,target,index):
    flist = []
    if index==len(arr):
        return flist

    if arr[index]==target:
        flist.append(index)

    #flist.append(findArray(arr,target,index+1))
    tlist = findArray(arr,target,index+1)
    flist.append(tlist)
    return flist

arr=[1,2,3,4,4,8]
target=4

#print(findArray(arr,4,0))


def findAllIndex2(arr, target, index):

    list = []

    if index == len(arr):
        return list

    # this will contain answer for that function call only
    if arr[index] == target:
        list.append(index)
    ansFromBelowCalls = findAllIndex2(arr, target, index + 1)

    list.extend(ansFromBelowCalls)

    return list

print(findAllIndex2(arr,4,0))
