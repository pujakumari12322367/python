class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node

    def insert_betw(self, data, prev):
            new_node = Node(data)
            new_node.ref = prev.ref
            prev.ref = new_node

    def insert_end(self, data):
            new_node = Node(data)
            if self.head is None:
             self.head = new_node
            return
    
    def del_start(self):
         del_node = self.head
         self.head = self.head.ref
         del_node.ref = None

    def del_betw(self, prev):
         prev.ref = prev.ref.ref
         prev.ref.ref = None

  
    def del_end(self):
                if self.head is None:
                        return
                if self.head.ref is None:
                        self.head = None
                        return
                