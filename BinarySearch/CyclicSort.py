def sortArray(arr):
    i=0
    while i < len(arr):
        correctIndex = arr[i]-1

        if arr[i]!=arr[correctIndex]:
            temp = arr[i]
            arr[i]= arr[correctIndex]
            arr[correctIndex]=temp
        else:
            i+=1

    #print(arr)
    return arr


arr=[3,5,2,1,4]
print(sortArray(arr))


def missingArray(nums):
    i = 0
    while i < len(nums):
        correctIndex = nums[i]  # [3,0,1]
        if nums[i] < len(nums) and nums[i] != nums[correctIndex]:
            temp = nums[i]
            nums[i] = nums[correctIndex]
            nums[correctIndex] = temp
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return len(nums)

nums=[3,0,1]
print(missingArray(nums))
