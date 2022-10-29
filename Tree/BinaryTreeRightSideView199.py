# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
#https://leetcode.com/problems/binary-tree-right-side-view/
#https://www.youtube.com/watch?v=d4zLyf32e3I&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=10&ab_channel=NeetCode
class Solution:
    def rightSideView(self, root):
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            ln = len(q)
            rightSide = None
            for i in range(ln):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                res.append(rightSide.val)

        return res
