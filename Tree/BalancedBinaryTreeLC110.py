# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#https://leetcode.com/problems/balanced-binary-tree/
#https://www.youtube.com/watch?v=QfJsau0ItOY&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&ab_channel=NeetCode
class Solution:
    def isBalanced(self, root) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]  # Empty tree is Balanced

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, max(left[1], right[1]) + 1]

        return dfs(root)[0]

