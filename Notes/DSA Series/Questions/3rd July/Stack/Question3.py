class Stack:
    def __init__(self):
        self.stack = []

    def insert(self, data):
        self.stack.append(data)

    def display(self):
        for i in range(len(self.stack)-1, -1, -1):
            print(self.stack[i])
s = Stack()
s.insert(5)
s.insert(10)
s.insert(15)
s.insert(20)
print("Stack from Top to Bottom:")
s.display()