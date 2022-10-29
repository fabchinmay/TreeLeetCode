import collections
class Tree:
    def __init__(self,data):
        self.data= data
        self.left = None
        self.right = None

    def bfs(self,root):
        q = collections.deque()

class Solution:
    def maxDepth(self, root):
        #dfs
        #print("Hi")
        if root is None:
            return 0

        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        return 1 + max(lh, rh)

    def maxDepth_Iter(self,root):
        res= 0
        stack = [[root,1]]
        while stack:
            node,depth = stack.pop()
            if node:
                res = max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])

        return res



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
    print(s.maxDepth(root))
    print(s.maxDepth_Iter(root))

if __name__ == "__main__":
    main()