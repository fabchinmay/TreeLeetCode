# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:

        def findSum(curr, num):
            if not curr:
                return 0

            num = (num * 10) + curr.val

            if not curr.left or not curr.right:
                return num

            return findSum(curr.left, num) + findSum(curr.right, num)

        return findSum(root, 0)
