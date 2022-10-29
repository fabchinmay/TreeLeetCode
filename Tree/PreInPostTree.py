class TreeNode:

    def _initialize_instance_fields(self):
        #instance fields found by Java to Python Converter:
        self.val = 0
        self.left = None
        self.right = None

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: TreeNode()
    def __init__(self):
        self._initialize_instance_fields()

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: TreeNode(int val)
    def __init__(self, val):
        self._initialize_instance_fields()

        self.val = val
class Pair:
    def __init__(self, _node, _num):
        #instance fields found by Java to Python Converter:
        self.node = None
        self.num = 0

        self.num = _num
        self.node = _node
class TUF:
    @staticmethod
    def allTraversal(root, pre, in_, post):
        st = Stack()
        st.push(Pair(root, 1))

        if root is None:
            return

        while not st.isEmpty():
            it = st.pop()

            # this is part of pre
            # increment 1 to 2
            # push the left side of the tree
            if it.num == 1:
                pre.append(it.node.val)
                it.num += 1
                st.push(it)

                if it.node.left is not None:
                    st.push(Pair(it.node.left, 1))

            # this is a part of in
            # increment 2 to 3
            # push right
            elif it.num == 2:
                in_.append(it.node.val)
                it.num += 1
                st.push(it)

                if it.node.right is not None:
                    st.push(Pair(it.node.right, 1))
            # don't push it back again
            else:
                post.append(it.node.val)


    @staticmethod
    def main(args):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        pre = []
        in_ = []
        post = []
        TUF.allTraversal(root, pre, in_, post)

        print("The preorder Traversal is : ")
        for nodeVal in pre:
            print(str(nodeVal) + " ", end = '')
        print()
        print("The inorder Traversal is : ")
        for nodeVal in in_:
            print(str(nodeVal) + " ", end = '')
        print()
        print("The postorder Traversal is : ")
        for nodeVal in post:
            print(str(nodeVal) + " ", end = '')
        print()

# Main function added by Java to Python Converter:

def main():
    TUF.main([])

if __name__ == "__main__":
    main()
