class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def preOrder(self,node):
        if node is None:
            return
        print(node.data)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def deleteNode(self,node,key):
        if node is None:
            return None

        if node.data == key:
            return self.helper(node)

        dummy = node

        while node :
            if node.data >key:
                if node.left is not None and node.left.data == key:
                    node.left = self.helper(node.left)
                    break
                else:
                    node = node.left
            else:
                if node.right is not None and node.right.data==key:
                    node.right = self.helper(node.right)
                    break
                else:
                    node = node.right

        return node

    def getLastRight(self, root):
        if root.right is None:
            return root
        return self.getLastRight(root.right)

    def helper(self,root):

        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            rightNonde = root.right
            lastright = self.getLastRight(root.left)
            lastright.right = rightNonde

        return root.left



class Solution:
    def preOrder(self,node):
        if node is None:
            return
        print(node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def deleteNode(self, root, key):
        if root is None:
            return None
        if root.val == key:
            return self.helper(root)
        dummy = root
        while root is not None:
            if root.val > key:
                if root.left is not None and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right is not None and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
        return dummy
    def helper(self, root):
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            rightChild = root.right
            lastRight = self.findLastRight(root.left)
            lastRight.right = rightChild
            return root.left
    def findLastRight(self, root):
        if root.right is None:
            return root
        return self.findLastRight(root.right)



def main():
    node = Node(9)
    node.left = Node(8)

    node.left.left = Node(5)
    node.left.left.right = Node(7)
    node.left.left.right.left = Node(6)
    node.left.left.right.right = Node(8)

    node.left.left.left = Node(3)
    node.left.left.left.right = Node(4)
    node.left.left.left.left = Node(2)
    node.left.left.left.left.left = Node(1)

    node.right = Node(12)
    node.right.right = Node(13)
    node.right.left = Node(10)
    node.right.left.right = Node(11)

    printTree = Tree()
    #printTree.preOrder(node)

    finalNode = printTree.deleteNode(node,5)
    printTree.preOrder(finalNode)

    #sol = Solution()
    ##dat = sol.deleteNode(node,5)
    #sol.preOrder(dat)

if __name__=="__main__":
    main()
