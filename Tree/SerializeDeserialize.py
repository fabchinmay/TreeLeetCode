import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solutions:
    def generateSerialize(self,root):
        print("Hi")
        if root is None:
            return
        q = collections.deque()
        q.append(root)
        res = ''
        while q:
            node = q.popleft()

            if node is None:
                res+="n "
                continue

            res+=str(node.data)+" "
            q.append(node.left)
            q.append(node.right)

        print("Hello")
        return str(res)
    def deserialize(self,res):
        values = res.split(" ")
        root = Node(values[0])
        q = collections.deque()
        q.append(root)

        i = 1
        print(values)
        while i<len(values)-1:
            print(i,"-",values[i])

            parent = q.popleft()
            if values[i]!="n":
                left = Node(values[i])
                parent.left = left
                q.append(left)

            i+=1


            if values[i]!="n":
                right = Node(values[i])
                parent.right = right
                q.append(right)

            i+=1

        return root






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
    #root.right.right.right.right = Node(11)
    sol = Solutions()
    res = sol.generateSerialize(root)

    sol.deserialize(res)

if __name__ == "__main__":
    main()
