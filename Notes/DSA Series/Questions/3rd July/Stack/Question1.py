class Stack:
    def __init__(self):
        self.stack = []

    def insert(self, data):
        self.stack.append(data)

    def top(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Top Element:", self.stack[-1])

    def display(self):
        print(self.stack)


s = Stack()

s.insert(10)
s.insert(20)
s.insert(30)

s.display()
s.top()