class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solutions:

    def buildBinaryTree(self, postOrder, inOrder):
        inMap = {}

        for i in range(len(inOrder)):
            inMap[inOrder[i]]=i

        return self.buildBinaryTreeTraversal(postOrder,0,len(postOrder)-1,inOrder,0,len(inOrder)-1,inMap)


    def buildBinaryTreeTraversal(self,postOrder,postStart,postEnd,inOrder,inStart,inEnd,inMap):
        if postStart>postEnd or inStart>inEnd:
            return

        root = Node(postOrder[postEnd])

        inRoot = inMap[root.data]
        numsLeft = inRoot - inStart

        root.left = self.buildBinaryTreeTraversal(postOrder,postStart,postStart+numsLeft-1,inOrder,inStart,inRoot-1,inMap)
        root.right = self.buildBinaryTreeTraversal(postOrder,postStart+numsLeft,postEnd-1,inOrder,inRoot+1,inEnd,inMap)

        return root


    def Traverse(self,root):
        if root is None:
            return


        self.Traverse(root.left)
        self.Traverse(root.right)
        print(root.data)





def main():

    postOrder=[40,50,20,60,30,10]
    inOrder = [40,20,50,10,60,30]
    chiT = Solutions()
    root=chiT.buildBinaryTree(postOrder,inOrder)
    chiT.Traverse(root)




if __name__=="__main__":
    main()