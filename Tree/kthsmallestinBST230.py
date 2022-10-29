#https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://www.youtube.com/watch?v=9TJYWh0adfk&ab_channel=takeUforward
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        n = 0
        stack = []

        curr = root
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val

            curr = curr.right

