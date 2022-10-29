def findFrequency(arr):
    freqDict=dict()
    for i in arr.split():
        if i in freqDict:
            freqDict[i]=freqDict.get(i)+1
        else:
            freqDict[i]=1

    return freqDict

arr="Apple Mango Orange Mango Guava Guava Mango"

print(findFrequency(arr))
