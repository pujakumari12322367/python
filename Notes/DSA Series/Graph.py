# Node Class
class Node:
    def __init__(self, data):
        self.data = data


# Graph Class
class Graph:
    def __init__(self):
        self.graph = {}

    # Insert Node
    def insertNode(self, data):
        newNode = Node(data)
        self.graph[newNode.data] = []

    # Insert Directed Edge
    def insertEdge(self, source, destination):
        self.graph[source].append(destination)

    # Display Graph
    def display(self): 
        for node in self.graph:
            print(node, "->", self.graph[node])


# Driver Code
g = Graph()

# Insert Nodes
g.insertNode("A")
g.insertNode("B")
g.insertNode("C")

# Insert Edges
g.insertEdge("A", "B")
g.insertEdge("B", "C")

# Display Graph
g.display()