from collections import defaultdict

class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        print(d,"<Before visited_vertex>",visited_vertex)
        visited_vertex[d] = True
        print(d, "<After visited_vertex>", visited_vertex)
        print(self.graph[d])
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        #print(d,"<<The Stack is >>",stack,"<visited_vertex>",visited_vertex)
        for i in self.graph[d]:
            #print(d,"<>",i)
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        #print(d, "<<Before append The Stack is >>", stack)
        stack = stack.append(d)
        #print(d, "<<After append The Stack is >>", stack)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)
        print(self.graph)

        for i in range(self.V):
            #print(i)
            #print(visited_vertex)
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        #print(visited_vertex)
        #print("Here the stack is")
        print(stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)
        print(gr.graph)
        while stack:
            i = stack.pop()
            print(i)
            if not visited_vertex[i]:
                print("inside>>",i)
                gr.dfs(i, visited_vertex)
                print("---")


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_scc()