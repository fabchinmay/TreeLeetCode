#TC = O(n) SC= O(n)
import collections
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def printZigZag(self,root):
        q = collections.deque()
        q.append(root)
        leftToRight=True
        result = []


        while q:
            size = len(q)
            tmp = [0]*size
            for i in range(size):
                tmp1 = q.popleft()

                index = i if leftToRight else size - 1 - i
                # print(index)
                # print(tmp1.data)
                tmp[index] = tmp1.data

                if tmp1.left:
                    q.append(tmp1.left)
                if tmp1.right:
                    q.append(tmp1.right)

            leftToRight = not leftToRight
            result.append(tmp)

        return result





def main():
    root = Node(-10)
    root.left=Node(9)
    root.right=Node(20)
    root.right.left=Node(15)
    root.right.right = Node(7)

    chiT = Solution()
    print(chiT.printZigZag(root))

if __name__=="__main__":
    main()