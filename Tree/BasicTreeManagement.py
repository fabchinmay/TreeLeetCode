class ManagementNode:
    def __init__(self,name,designation):
        self.designation = designation
        self.name = name
        self.children = []
        self.parent= None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent

        return level

    def print_management(self,opt):
        space = " "*self.get_level()*3
        prefix = space + "|__" if self.parent else ""
        if opt=="name":
            print(prefix+self.name)
        elif opt=="designation":
            print(prefix+self.designation)
        elif opt=="both":
            print(prefix + self.name+ " ("+self.designation+")")

        if self.children:
            for child in self.children:
                child.print_management(opt)




def build_management_tree():
    ceo = ManagementNode("Nipul","CEO")

    cto = ManagementNode("Chinmay","CTO")
    infhead= ManagementNode("Vishwa","Infrastructure Head")
    infhead.add_child(ManagementNode("Dhaval","Cloud Manager"))
    infhead.add_child(ManagementNode("Abhijit","App Manager"))

    apphead = ManagementNode("Aamir","Application Head")

    cto.add_child(infhead)
    cto.add_child(apphead)

    hrhead = ManagementNode("Gels","HR Head")
    hrhead.add_child(ManagementNode("Peter","Recruitment Manager"))
    hrhead.add_child(ManagementNode("Waqas","Policy Manager"))

    ceo.add_child(cto)
    ceo.add_child(hrhead)

    return ceo

if __name__ == "__main__":
    root = build_management_tree()
    #root.print_management("name")
    #root.print_management("designation")
    root.print_management("both")





