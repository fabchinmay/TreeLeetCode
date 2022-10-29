class TreeNode:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

class Solution:
    def preOrderTraversal(self,node):
        if node is None:
            return None
        print(node.val)
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)

    def bstFromPreorderF(self, A):
        return self.bstFromPreorder(A, float("inf"), [0])

    def bstFromPreorder(self, A, bound, i):
        if i[0] == len(A) or A[i[0]] > bound:
            return None
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: TreeNode root = new TreeNode(A[i[0]++]);
        root = TreeNode(A[i[0]])
        i[0] += 1
        root.left = self.bstFromPreorder(A, root.val, i)
        root.right = self.bstFromPreorder(A, bound, i)
        return root

def main():
    A = [8,5,1,7,10,12]
    s = Solution()
    tree = s.bstFromPreorderF(A)
    s.preOrderTraversal(tree)



if __name__=="__main__":
    main()

