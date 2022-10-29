import collections
from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solutions:
    def getMaxWidth(self,root):
        q = collections.deque()
        q.append([root,0])
        ans =0

        while q:
            mmin = q[0][1]
            qlen = len(q)

            first = 0
            last = 0
            for i in range(qlen):
                node = q.popleft()
                cur_id = node[1] - mmin

                if i == 0:
                    first = cur_id
                if i == qlen - 1:
                    last = cur_id
                if node[0].left is not None:
                    q.append([node[0].left, cur_id * 2 + 1])
                if node[0].right is not None:
                    q.append([node[0].right, cur_id * 2 + 2])
            ans = max(ans, last - first + 1)
        return ans


def main():
    root = Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left=Node(9)
    root.right.right = Node(10)
    root.right.right.right = Node(11)
    root.left.left.right = Node(6)
    root.left.left.left = Node(12)
    root.left.left.right.right = Node(7)
    res=0
    chiT = Solutions()
    print(chiT.getMaxWidth(root))

    print(res)




if __name__=="__main__":
    main()