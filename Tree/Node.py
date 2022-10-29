import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class TUF:

    @staticmethod
    def preOrderTrav(curr, inOrder):
        if curr is None:
            return

        inOrder.append(curr.data)
        TUF.preOrderTrav(curr.left, inOrder)
        TUF.preOrderTrav(curr.right, inOrder)

    def preOrder_tra(root):
        if root is None:
            return
        res = []
        stack =[]
        stack.append(root)
        while stack:
            tmp = stack.pop()
            res.append(tmp.data)

            if tmp.right:
                stack.append(tmp.right)

            if tmp.left:
                stack.append(tmp.left)

        return res

    def inOrder_Itr(root):
        inord = []
        stack = []
        while True:
            if root is not None:
                stack.append(root)
                root=root.left
            else:
                if len(stack)==0:
                    break

                root = stack.pop()
                inord.append(root.data)
                root = root.right

        return inord


    def inOrderTrav(curr, inOrder):
        if curr is None:
            return
        TUF.inOrderTrav(curr.left, inOrder)
        inOrder.append(curr.data)
        TUF.inOrderTrav(curr.right, inOrder)

    def postOrderTrav(curr, postOrder):
        if curr is None:
            return
        TUF.postOrderTrav(curr.left, postOrder)
        TUF.postOrderTrav(curr.right, postOrder)
        postOrder.append(curr.data)

    def postOrder_Itr(root):
        postOrd = []
        stack = []
        stack.append(root)
        res = []

        while stack:
            tmp = stack.pop()
            if tmp :
                res.append(tmp.data)
                stack.append(tmp.left)
                stack.append(tmp.right)

        while res:
            stack.append(res.pop())

        return stack




    def bfs(root):
        queue = collections.deque()
        res = []
        queue.append(root)

        while queue:
            qlen = len(queue)
            level = []
            #print("outside-"+str(qlen)+"-"+str(len(queue)))
            # print(queue)
            # print(qlen)
            for i in range(qlen):
                #print("inside-" + str(qlen )+ "-" + str(len(queue)))
                tmp = queue.popleft()

                if tmp:
                    level.append(tmp.data)
                    if tmp.data==4:
                        print(tmp.left)
                    queue.append(tmp.left)
                    queue.append(tmp.right)

            if level:
                res.append(level)

        return res





    @staticmethod
    def main():

        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.left.right.left = Node(8)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.right.right.left = Node(9)
        root.right.right.right = Node(10)

        #print(TUF.bfs(root))

        inOrder = []
        #TUF.preOrderTrav(root, inOrder)
        #TUF.inOrderTrav(root, inOrder)
        TUF.postOrderTrav(root, inOrder)

        #print(TUF.preOrder_tra(root))
        #print(TUF.inOrder_Itr(root))
        print(TUF.postOrder_Itr(root))

        print("The Pre/in/Post-Order Traversal is : ")
        i = 0
        print(inOrder)
        while i < len(inOrder):
            print(str(inOrder[i]) + " ", end = '')
            i += 1

# Main function added by Java to Python Converter:

if __name__ == "__main__":
    tf = TUF()
    tf.main()
