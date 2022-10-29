
#TC = O(N) SC = O(H)
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solutions:
    def getPath(self,root,arr,target):
        if root is None:
            return False
        #print(arr)
        arr.append(root.data)

        if root.data==target:
            return True

        if (self.getPath(root.left,arr,target) or self.getPath(root.right,arr,target)):
            return True

        arr.pop()
        return False







def main():
    root = Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left=Node(9)
    root.right.right = Node(10)
    root.left.left.right = Node(6)
    root.left.left.right.right = Node(7)
    res=[]
    chiT = Solutions()
    chiT.getPath(root,res,5)
    print(res)


if __name__=="__main__":
    main()