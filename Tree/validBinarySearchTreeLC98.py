# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#https://leetcode.com/problems/validate-binary-search-tree/
#https://www.youtube.com/watch?v=s6ATEkipzow&ab_channel=NeetCode
class Solution:
    def isValidBST(self, root):
        def valid(node, left, right):
            if not node:
                return True

            if not (node.val >= right and node.val <= left):
                return False

            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))


class Solution:
    def _checkBST(self, node, min, max):
        if node is None:
            return True
        if node.val <= min or node.val >= max:
            return False

        if self._checkBST(node.left, min, node.val) and self._checkBST(node.right, node.val, max):
            return True
        return False
    def isValidBST(self, root):
        return self._checkBST(root, Long.MIN_VALUE, Long.MAX_VALUE)
