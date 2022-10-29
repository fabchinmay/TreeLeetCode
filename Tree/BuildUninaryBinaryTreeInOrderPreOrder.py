class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solutions:

    def buildBinaryTree(self, preOrder, inOrder):
        inMap = {}

        for i in range(len(inOrder)):
            inMap[inOrder[i]]=i

        return self.buildBinaryTreeTraversal(preOrder,0,len(preOrder)-1,inOrder,0,len(inOrder)-1,inMap)


    def buildBinaryTreeTraversal(self,preOrder,preStart,preEnd,inOrder,inStart,inEnd,inMap):
        if preStart>preEnd or inStart>inEnd:
            return

        root = Node(preOrder[preStart])

        inRoot = inMap[root.data]
        numsLeft = inRoot - inStart

        root.left = self.buildBinaryTreeTraversal(preOrder,preStart+1,preStart+numsLeft,inOrder,inStart,inRoot-1,inMap)
        root.right = self.buildBinaryTreeTraversal(preOrder,preStart+numsLeft+1,preEnd,inOrder,inRoot+1,inEnd,inMap)

        return root


    def Traverse(self,root):
        if root is None:
            return


        self.Traverse(root.left)
        self.Traverse(root.right)
        print(root.data)





def main():

    preOrder=[10,20,40,50,30,60]
    inOrder = [40,20,50,10,60,30]
    chiT = Solutions()
    root=chiT.buildBinaryTree(preOrder,inOrder)
    chiT.Traverse(root)




if __name__=="__main__":
    main()