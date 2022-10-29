def printOrder(num):
    if num<=0:
        return
    print(num)
    printOrder(num-1)


printOrder(5)


def printNumber(n):
  # check if n is greater than 0
  if n > 0:
    # recursively call the printNumber function
    printNumber(n - 1)
    # print n
    print(n, end = ' ')

# declare the value of n
n = 5
# call the printNumber function
#printNumber(n)

def dispn(n):
    if n == 0:
        return  # Base case
    print(n)
    dispn(n - 1)  # Tail Recursive Call


#dispn(5)

def headr(n):
    if n > 0:
        headr(n - 1)
        print(n, end=" ")


p = 5
headr(5)
