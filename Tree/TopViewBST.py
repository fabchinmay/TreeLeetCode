import collections
from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solutions:
    def generateTopView(self,root,map):
        q = collections.deque()
        q.append([root,0])
        #map = defaultdict(list)

        while q:
            qlen = len(q)
            for _ in range(qlen):
                tmp,axis = q.popleft()
                if tmp :
                    q.append([tmp.left,axis-1])
                    q.append([tmp.right,axis+1])
                    if not map[axis]:
                        map[axis].append(tmp.data)

        return map


def main():
    root = Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left=Node(9)
    root.right.right = Node(10)
    root.left.left.right = Node(6)
    root.left.left.right.right = Node(7)
    res=defaultdict(list)
    chiT = Solutions()
    chiT.generateTopView(root,res)

    print(res)

    for i in sorted(res):
        print( res[i], end=" ")


if __name__=="__main__":
    main()