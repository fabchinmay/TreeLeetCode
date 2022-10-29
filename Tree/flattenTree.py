import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class flatten:
    def flattenTree(self,root):
        return root


def main():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    #root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)

    fun = flatten()
    fun.flattenTree()
    print("here")
    print(fun.inOrderTraversal(root))

if __name__ == "__main__":
    main()