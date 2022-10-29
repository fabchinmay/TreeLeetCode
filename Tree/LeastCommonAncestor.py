
#TC = O(N) SC = O(N) Auxilary space
#https://takeuforward.org/data-structure/lowest-common-ancestor-for-two-given-nodes/
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solutions:
    def getLCA(self,root,p,q):
        if root is None or root==p or root==q:
            return root

        left = self.getLCA(root.left,p,q)
        right = self.getLCA(root.right,p,q)

        if left is None:
            return right
        elif right is None:
            return left
        else: #if left right both not found return root
            return root






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