#https://leetcode.com/problems/count-complete-tree-nodes/
#https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
import collections
from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solutions:

    def getHeight(self, root, cnt):
        if not root:
            return

        cnt += 1
        self.getHeight(root.left)
        self.getHeight(root.right)

    '''we could to DFS or BFS to get the no of nodes but if I will calclulate the left and right tree separately 
    then this will help me in binding the binary tree rules where if left===right means total heiht = 2**left -1 
    else 1+ height in left + height in right recursion'''
    def getLeftHeight(self, root):
        cnt = 0
        while root:
            cnt += 1
            root = root.left
        return cnt



    def getRightHeight(self, root):
        cnt = 0
        while root:
            cnt += 1
            root = root.right

        return cnt

    def countNodes(self, root):
        if not root:
            return 0

        left = self.getLeftHeight(root)
        right = self.getRightHeight(root)

        if left == right:
            return 2 ** left - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


def main():
    root = Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left=Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    chiT = Solutions()
    print(chiT.countNodes(root))




if __name__=="__main__":
    main()