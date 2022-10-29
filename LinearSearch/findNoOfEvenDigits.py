def findNoOfEvenDigits(arr):
    cnt = 0
    for num in arr:
        if even(num):
            cnt+=1

    return cnt

def even(num):
    cnt=0
    while num>0:
        cnt+=1
        num=num//10

    if cnt%2==0:
        return True

    return False

arr=[12,345,2,6,7896]

print(findNoOfEvenDigits(arr))