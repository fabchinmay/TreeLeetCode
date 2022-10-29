class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
class TUF:

    def insertBST(root, val):
        if root is None:
            return Node(val)
        if val<root.data:
            root.left=TUF.insertBST(root.left,val)
        else:
            root.right=TUF.insertBST(root.right,val)
        return root


    def kthlargest(root, k):
        if root is None:
            return None

        right =TUF.kthlargest(root.right,k)
        if right is not None:
            return right
        k[0] -= 1

        if k[0]==0:
            return root

        return TUF.kthlargest(root.left,k)


    def kthsmallest(root, k):
        if root is None:
            return None

        left =TUF.kthsmallest(root.left,k)
        if left is not None:
            return left
        k[0] -= 1
        if k[0]==0:
            return root

        return TUF.kthsmallest(root.right,k)

    def main(args):

        arr = [10, 40, 45, 20, 25, 30, 50]
        i = None

        k =4
        root =None
        for i in range(0, 7):
            root=TUF.insertBST(root,arr[i])
        print()

        p =k
        large =TUF.kthlargest(root,[k])
        k=p
        small =TUF.kthsmallest(root,[k])
        if large is None:
            print("Invalid input")
        else:
            print("kth largest element is  "+str(large.data))

        if small is None:
            print("Invalid input")
        else:
            print("kth smallest element is  "+str(small.data))

# Main function added by Java to Python Converter:

def main():
    TUF.main([])

if __name__ == "__main__":
    main()
