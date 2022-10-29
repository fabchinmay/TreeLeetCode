class BSTIterator:

    def __init__(self, root):
        #instance fields found by Java to Python Converter:
        self._stack = Stack()

        self._pushAll(root)

    #* @return whether we have a next smallest number
    def hasNext(self):
        return not self._stack.isEmpty()

    #* @return the next smallest number
    def next(self):
        tmpNode = self._stack.pop()
        self._pushAll(tmpNode.right)
        return tmpNode.val

    def _pushAll(self, node):
        while node is not None:
            pass
            stack.push(node)
            node = node.left
