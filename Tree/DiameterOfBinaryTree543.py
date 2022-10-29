# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#https://www.youtube.com/watch?v=Rezetez59Nk&ab_channel=takeUforward
#https://www.youtube.com/watch?v=eD3tmO66aBA&t=190s&ab_channel=takeUforward
#https://leetcode.com/problems/diameter-of-binary-tree/

class Tree:
    def __init__(self,data):
        self.data= data
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        diameter = [0]

        def dfs(root, diameter):
            if not root:
                return 0

            lh = dfs(root.left, diameter)
            rh = dfs(root.right, diameter)
            diameter[0] = max(lh + rh, diameter[0])
            #print(diameter)
            return 1 + max(lh, rh)

        dfs(root, diameter)

        return diameter[0]

    def mat(self,A,B):
        for i in range(5):
            B+=1
        #print(B)
        return B

def main():
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.left = Tree(4)
    root.left.right = Tree(5)
    root.left.right.left = Tree(8)
    root.right.left = Tree(6)
    root.right.right = Tree(7)
    root.right.right.left = Tree(9)
    root.right.right.right = Tree(10)
    s = Solution()
    print(s.diameterOfBinaryTree(root))
    # A=1
    # B=1
    # print(A)
    # print(B)
    # C= s.mat(A,B)
    # print(A)
    # print(B)
    # print(C)

if __name__ == "__main__":
    main()
