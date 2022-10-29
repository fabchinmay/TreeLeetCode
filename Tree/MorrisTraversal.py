import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Traversal:
    def inOrderTraversal(self,root):
        preorder = []
        cur = root
        while cur is not None:
            if cur.left is None:
                preorder.append(cur.data)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right is not None and prev.right is not cur:
                    prev = prev.right

                if prev.right is None:
                    prev.right = cur
                    preorder.append(cur.data)
                    cur = cur.left
                else:
                    prev.right = None
                    #preorder.append(cur.data) FOR INoRDER
                    cur = cur.right
        return preorder


def main():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    #root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)

    fun = Traversal()
    print("here")
    print(fun.inOrderTraversal(root))

if __name__ == "__main__":
    main()