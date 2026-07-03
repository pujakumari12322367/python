class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def checkEdge(self, u, v):
        if v in self.graph[u]:
            print("Edge Exists")
        else:
            print("Edge Does Not Exist")


g = Graph()

g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "D")

g.checkEdge("A", "B")