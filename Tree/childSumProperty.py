import collections
from collections import defaultdict

# TC O(N) SC O(H) ~ O(N)
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solutions:
    def getChildSum(self,root):
        if not root:
            return
        child = 0
        if root.left : child+=root.left.data
        if root.right : child+=root.right.data

        if child>=root.data: root.data = child
        else:
            if root.left : root.left.data = root.data
            if root.right : root.right.data = root.data

        self.getChildSum(root.left)
        self.getChildSum(root.right)

        total = 0
        if root.left : total+=root.left.data
        if root.right: total+=root.right.data
        if root.right or root.left: root.data = total

    def getLeft(self,root):
        count=0
        while root:
            count+=1
            root = root.left

        return count

    def getHeight(self,root,cnt):
        if root is None:
            return
        cnt[0]+=1
        self.getHeight(root.left,cnt)
        self.getHeight(root.right,cnt)




def main():
    root = Node(2)
    root.left=Node(35)
    root.right=Node(10)
    root.left.left = Node(2)
    root.left.right = Node(3)
    root.right.left=Node(5)
    root.right.right = Node(2)
    chiT = Solutions()
    chiT.getChildSum(root)

    print(root.data)

    root1 = Node(50)
    root1.left = Node(7)
    root1.right = Node(2)
    root1.left.left = Node(3)
    root1.left.right = Node(5)
    root1.right.left = Node(1)
    root1.right.right = Node(30)
    chiT.getChildSum(root1)
    print(root1.data)

    root2 = Node(40)
    root2.left = Node(10)
    root2.right = Node(20)
    root2.left.left = Node(2)
    root2.left.right = Node(5)
    root2.right.left = Node(30)
    root2.right.right = Node(40)
    chiT.getChildSum(root2)
    print(root2.data)

    print(chiT.getLeft(root2))

    cnt = [0]
    chiT.getHeight(root2,cnt)


    print(cnt[0])




if __name__=="__main__":
    main()