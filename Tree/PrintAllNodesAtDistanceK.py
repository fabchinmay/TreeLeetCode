#https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
import collections
from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solutions:
    def buildParent(self,root,parent,visited):
        q = collections.deque()
        q.append(root)
        visited[root]=False
        while q:
            current = q.popleft()
            if current.left:
                q.append(current.left)
                visited[current.left]=False
                parent[current.left]=current

            if current.right :
                visited[current.right] = False
                q.append(current.right)
                parent[current.right]=current
    def print_AllNodes(self,root,target,k):
        if not root:
            return
        parent = {}
        visited = {}

        self.buildParent(root,parent,visited)
        visited[target] = True
        # for i in parent:
        #     print(i.data,"->",parent[i].data)

        q = collections.deque()
        q.append(target)
        curr_level = 0
        res = list()

        while q:
            qlen=len(q)
            if curr_level==k:
                break
            curr_level+=1

            for i in range(qlen):
                current=q.popleft()

                if current.left is not None and not visited[current.left]:
                    q.append(current.left)
                    visited[current.left] = True
                if current.right is not None and not visited[current.right]:
                    q.append(current.right)
                    visited[current.right] = True
                if current in parent:
                    if parent[current] is not None and not visited[parent[current]]:
                        q.append(parent[current])
                        visited[parent[current]] = True

                #print(current.data)

        result = []
        while q:
            current = q.pop()
            result.append(current.data)

        print(result)


def main():
    root = Node(3)
    target=root.left=Node(5)
    root.right=Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.right.left=Node(0)
    root.right.right = Node(8)
    root.right.right.right = Node(11)
    root.left.right.right = Node(4)
    root.left.right.left = Node(7)
    chiT = Solutions()
    chiT.print_AllNodes(root,target,2)




if __name__=="__main__":
    main()