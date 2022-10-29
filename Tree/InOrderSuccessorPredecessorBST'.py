class Solution:

    def inorderSuccessor(self, root, p):

        successor = None

        while root is not None:

            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor
