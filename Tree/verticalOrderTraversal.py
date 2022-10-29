import collections
from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solutions:
    def printVerticalOrder(self,root):
        q= collections.deque()
        q.append([root,0,0])
        map = defaultdict(list)

        while q:
            qlen=len(q)
            print(qlen,"->")
            for i in range(qlen):

                tmp,Node,level = q.popleft()
                #print(i,"----",tmp.data)

                if tmp:
                    #if tmp.left:
                    q.append([tmp.left,Node-1,level+1 ])
                    #if tmp.right:
                    q.append([tmp.right,Node+1,level+1 ])
                    map[Node].append(tmp.data)

        return map

    def preOrderVerticalTraversal(self,root,premap,axis):
        if not root:
            return
        premap[axis].append(root.data)
        if root.left:
            self.preOrderVerticalTraversal(root.left,premap,axis-1)
        if root.right:
            self.preOrderVerticalTraversal(root.right, premap,axis+1)




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
    res=[]
    chiT = Solutions()
    fmap = chiT.printVerticalOrder(root)
    for i in sorted(fmap):
        print( fmap[i], end=" ")

    prmap = defaultdict(list)
    chiT.preOrderVerticalTraversal(root,prmap,0)

    print(prmap)


if __name__=="__main__":
    main()