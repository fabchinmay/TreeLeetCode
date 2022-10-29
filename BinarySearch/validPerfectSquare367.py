def findPerfectSquare(x):
    start =1
    end = x

    while start <=end:
        mid = start + (end-start)//2
        if mid*mid < x:
            start = mid+1
        elif mid*mid >x:
            end = mid-1
        else:
            return True

    return False

print(findPerfectSquare(64))