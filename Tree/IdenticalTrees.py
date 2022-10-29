#TC = O(n) SC= O(n)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def checkIdentical(self,node1,node2):
        if node1 is None or node2 is None:
            return node1==node2

        return  node1.data==node2.data and self.checkIdentical(node1.left,node2.left) and self.checkIdentical(node1.right,node2.right)


def main():
    root = Node(-10)
    root.left=Node(9)
    root.right=Node(20)
    root.right.left=Node(15)
    root.right.right = Node(7)

    root1 = Node(-10)
    root1.left = Node(9)
    root1.right = Node(20)
    root1.right.left = Node(15)
    root1.right.right = Node(7)

    chiT = Solution()
    print(chiT.checkIdentical(root,root1))

if __name__=="__main__":
    main()