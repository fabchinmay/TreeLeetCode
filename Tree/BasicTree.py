class TreeNode:
    def __init__(self,data):
        self.data= data
        self.children = []
        self.parent = None

    def add_Child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p=p.parent

        return level


    def print_Tree(self):
        space = " "*self.get_level()*2
        prefix = space+ "|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_Tree()

def build_root():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    root.add_Child(laptop)

    laptop.add_Child(TreeNode("Mac"))
    laptop.add_Child(TreeNode("Windows"))
    laptop.add_Child(TreeNode("Thinkpad"))

    tv = TreeNode("Tv")
    root.add_Child(tv)

    tv.add_Child(TreeNode("Onida"))
    tv.add_Child(TreeNode("Samsung"))
    tv.add_Child(TreeNode("LG"))

    mobile = TreeNode("Mobile")
    root.add_Child(mobile)

    mobile.add_Child(TreeNode("Nokia"))
    mobile.add_Child(TreeNode("Nexus"))
    mobile.add_Child(TreeNode("iPhone"))





    return root




if __name__ == "__main__":
    root = build_root()
    root.print_Tree()
    #print(root.get_level())