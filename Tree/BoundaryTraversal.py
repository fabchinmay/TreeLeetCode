import collections
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def isleafNode(self,root):
        print("hellp")
        return root.left is None and root.right is None

    def addLeft(self,root,res):
        curr = root.left
        while curr:
            print(curr.data)
            if not self.isleafNode(curr):
                res.append(curr.data)
            print("dddd")
            if not curr.left:
                curr = curr.left
            else :
                curr = curr.right

    def addleaves(self,root,res):
        if not root:
            return

        print("Here in this ")
        if self.isleafNode(root):
            res.append(root.data)

        if root.left:
            self.addleaves(root.left,res)

        if root.right:
            self.addleaves(root.right,res)

    def addRight(self,root,res):
        curr = root.right
        tmp = []
        while curr:
            if not self.isleafNode(curr):
                tmp.append(curr.data)
            if curr.right:
                curr=curr.right
            else:
                curr= curr.left

        tmpLen = len(tmp)

        for i in range(tmpLen-1,-1,-1):
            res.append(tmp[i])

    def printBoundaryTree(self,root,res):
        res.append(root.data)
        self.addLeft(root,res)
        self.addleaves(root,res)
        self.addRight(root,res)

        return res




def main():
    root = Node(-10)
    root.left=Node(9)
    root.right=Node(20)
    root.right.left=Node(15)
    root.right.right = Node(7)
    res=[]
    chiT = Solution()
    print(chiT.printBoundaryTree(root,res))
    print(res)

if __name__=="__main__":
    main()