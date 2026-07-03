class Stack:
    def __init__(self):
        self.stack = []

    def insert(self, data):
        self.stack.append(data)

    def delete(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            self.stack.pop()

    def display(self):
        print(self.stack)

s = Stack()
s.insert(5)
s.insert(10)
s.insert(15)
s.insert(20)
s.delete()
s.display()