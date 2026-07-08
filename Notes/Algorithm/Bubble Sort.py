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
            while current.next:
                current = current.next
            current.next = newNode

    def bubbleSort(self):
        if self.head is None:
            return

        swapped = True

        while swapped:
            swapped = False
            current = self.head

            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next


ll = LinkedList()

ll.insert(10)
ll.insert(9)
ll.insert(100)
ll.insert(20)
ll.insert(5)

print("Original Linked List:")
ll.display()

ll.bubbleSort()

print("\nSorted Linked List:")
ll.display()