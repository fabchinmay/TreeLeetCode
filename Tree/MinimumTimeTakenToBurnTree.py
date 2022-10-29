import collections
from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solutions:
    def buildParentVisit(self,root,parent,visited):
        q= collections.deque()
        q.append(root)
        visited[root]=False
        while q:
            qsize = len(q)

            for _ in range(qsize):
                current = q.popleft()
                if current.left :
                    q.append(current.left)
                    parent[current.left]=current
                    visited[current.left]=False

                if current.right:
                    q.append(current.right)
                    parent[current.right] = current
                    visited[current.right] = False


    def burnAllNodes(self,root,target):
        parent,visited = {},{}
        self.buildParentVisit(root,parent,visited)

        q = collections.deque()
        q.append(target)
        visited[target]=True
        maxi = 0


        while q:
            qsize = len(q)
            f1 = 0

            for _ in range(qsize):
                current = q.popleft()

                if current.left is not None and not visited[current.left]:
                    q.append(current.left)
                    visited[current.left]=True
                    f1 = 1

                if current.right is not None and not visited[current.right]:
                    q.append(current.right)
                    visited[current.right]=True
                    f1 = 1

                if current in parent:
                    if parent[current] is not None and not visited [parent[current]]:
                        q.append(parent[current])
                        visited[parent[current]] = True
                        f1=1

            if f1==1 :
                maxi+=1

        return maxi



def main():
    root = Node(1)
    target=root.left=Node(2)
    root.right=Node(3)
    root.left.left = Node(4)
    root.left.left.right = Node(7)
    root.right.left=Node(5)
    root.right.right = Node(6)
    chiT = Solutions()
    print(chiT.burnAllNodes(root,target))




if __name__=="__main__":
    main()