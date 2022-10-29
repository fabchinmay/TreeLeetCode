# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#https://leetcode.com/problems/count-good-nodes-in-binary-tree/
#https://www.youtube.com/watch?v=7cp5imvDzl4&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=2&ab_channel=NeetCode
class Solution:
    def goodNodes(self, root) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0

            res = 1 if root.val >= maxVal else 0
            res += dfs(root.left, max(root.val, maxVal))
            res += dfs(root.right, max(root.val, maxVal))

            return res

        return dfs(root, root.val)

