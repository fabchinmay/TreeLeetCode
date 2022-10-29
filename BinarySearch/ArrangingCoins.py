def arrangingCoins(num):
    start = 0
    end = num

    while start<=end:
        mid = start+(end-start)//2

        curr = mid*(mid+1)//2

        if curr==num: return mid
        if num<curr:
            end = mid-1
        else:
            start = mid+1

    return start




print(arrangingCoins(3))