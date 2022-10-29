class Solutions:
    def findLCA(self,root,p,q):
        if root is None:
            return None

        curr = root.val

        if curr<p.val and curr< q.val:
            self.findLCA(root.right,p,q)

        if curr > p.val and curr > q.val:
            self.findLCA(root.left,p,q)

        return root