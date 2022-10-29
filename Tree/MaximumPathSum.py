class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def findmaxSum(self,root,maxi):
        if root is None:
            return 0
        lhm = max(0,self.findmaxSum(root.left,maxi))
        rhm = max(0,self.findmaxSum(root.right,maxi))
        maxi[0] = max(maxi[0],root.data+lhm+rhm)

        return root.data+max(lhm,rhm)


def main():
    root = Node(-10)
    root.left=Node(9)
    root.right=Node(20)
    root.right.left=Node(15)
    root.right.right = Node(7)
    maxi=[0]
    fs = Solution()
    fs.findmaxSum(root,maxi)

    print(maxi[0])

if __name__ == "__main__":
    main()