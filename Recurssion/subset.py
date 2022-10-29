def findSubset(ch,arr):
    if len(arr)==0:
        print(ch)
        return
    findSubset(ch, arr[1:])
    findSubset(ch+arr[0],arr[1:])


def findSubsetWitoutParameter(ch,arr):

    if len(arr)==0:
        lst = []
        lst.add(ch)
        return lst
    le=[]
    left=findSubset(ch, arr[1:])
    right=findSubset(ch+arr[0],arr[1:])
    le.append(left)
    le.extend(right)

    return le

def subseqRet(p, up):
    if not up:
        list = []
        list.append(p)
        return list
    ch = up[0]
    left = subseqRet(p + ch, up[1:])
    right = subseqRet(p, up[1:])

    left.extend(right)
    return left

def subseqRetAscii(p, arr):
    if len(arr) == 0:
        print(p)
        return
    findSubset(p + arr[0], arr[1:])
    findSubset(p, arr[1:])
    findSubset(str(ord(p)) + str(ord(arr[0])), arr[1:])

def subseqAsciiRet(p, up):
    if not up:
        list = []
        list.append(p)
        return list
    ch = up[0]
    first = subseqAsciiRet(p + ch, up[1:])
    second = subseqAsciiRet(p, up[1:])
    third = subseqAsciiRet(p + str(ch+0), up[1:])

    first.extend(second)
    first.extend(third)
    return first


def subset(arr):
    outer = []
    outer.append([])
    for num in arr:
        n = len(outer)
        for i in range(0, n):
            internal = list(outer[i])
            internal.append(num)
            outer.append(internal)
    return outer

@staticmethod
def subsetDuplicate(arr):
    arr.sort()
    outer = []
    outer.append([])
    start = 0
    end = 0
    i = 0
    while i < len(arr):
        start = 0
        # if current and previous element is same, s = e + 1
        if i > 0 and arr[i] == arr[i-1]:
            start = end + 1
        end = len(outer) - 1
        n = len(outer)
        for j in range(start, n):
            internal = list(outer[j])
            internal.append(arr[i])
            outer.append(internal)
        i += 1
    return outer






arr="abc"

#findSubset("-",arr)
#subseqRetAscii("",arr)

#print(findSubsetWitoutParameter("-",arr))
findSubsetWitoutParameter("-",arr)

#print(subseqRet("",arr))
