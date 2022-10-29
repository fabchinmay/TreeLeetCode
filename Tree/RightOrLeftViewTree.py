'''
We can look from rightside or left side of the tree and what do I look that needs to be presented
We will be doing the level order traversal
there are 2 ways one is recursive and other is iterative but the problem is in iterative the space complexity will be the
no of the tree and in recursive it will be the height of the tree
so TC and SC is O(N) and O(H)
in recursive we can select Inorder, preorder, postOrder but here we will select inorder

and if we want to check for the right side then we will check the Preorder from reverse right
basically in PreOrder RootLeftRight but we will do RootRightLeft for right view
and RootLeftRight for Left view
And we will get one list /datastructure if the length is same as the level then insert or else not
'''

import collections
from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solutions:
    def generateRightView(self,root,level,Rightres):
        if not root:
           return
        if level==len(Rightres):
            Rightres.append(root.data)

        self.generateRightView(root.right,level+1,Rightres)
        self.generateRightView(root.left, level + 1, Rightres)

    def generateLeftView(self, root, level, Leftres):
        if not root:
            return

        if level == len(Leftres):
            Leftres.append(root.data)

        self.generateLeftView(root.left, level + 1, Leftres)
        self.generateLeftView(root.right, level + 1, Leftres)




def main():
    root = Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    #root.right.left=Node(9)
    root.right.right = Node(7)
    root.left.right.left = Node(6)
    #root.left.left.right.right = Node(7)
    res=defaultdict(list)
    chiT = Solutions()
    rightRes=[]
    leftRes = []
    chiT.generateRightView(root,0,rightRes)
    chiT.generateLeftView(root, 0, leftRes)

    print(rightRes)
    print(leftRes)




if __name__=="__main__":
    main()