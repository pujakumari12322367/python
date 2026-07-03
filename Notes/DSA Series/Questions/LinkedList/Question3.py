class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def delete(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

ll = LinkedList()
ll.insert(8)
ll.insert(16)
ll.insert(24)
ll.insert(32)
ll.delete(24)
ll.display()