#https://www.youtube.com/watch?v=0K0uCMYq5ng&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=5&ab_channel=NeetCode
#o(n) sc:O(logn)
class TreeNode:
    def __init__(self,val,left,right):
        self.val = val
        self.left = None
        self.right = None

    def makeBinarySearch(self,nums):
        def helper(l,r):
            if l>r :
                return None
            mid = (l+r)//2

            root = TreeNode(nums[mid])
            root.left = helper(l,mid-1)
            root.right = helper(mid+1,r)

            return root

        return helper(0,len(nums)-1)