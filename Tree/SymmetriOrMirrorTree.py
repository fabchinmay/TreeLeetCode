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
    def CheckSymmetric(self,root):
       return root is None or self.isSymmetric(root.left,root.right)

    def isSymmetric(self, left, right):
        if left is None or right is None:
            return left==right

        if left.data != right.data:
            return False

        return self.isSymmetric(left.left,right.right) and self.isSymmetric(left.right,right.left)





def main():
    root = Node(1)
    root.left=Node(2)
    root.right=Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left=Node(4)
    root.right.right = Node(3)
    #root.left.right.left = Node(6)
    #root.left.left.right.right = Node(7)
    chiT = Solutions()
    print(chiT.CheckSymmetric(root))



if __name__=="__main__":
    main()