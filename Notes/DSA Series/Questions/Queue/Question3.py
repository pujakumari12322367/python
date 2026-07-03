class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)

    def display(self):
        for i in self.queue:
            print(i)


q = Queue()

q.insert(5)
q.insert(10)
q.insert(15)
q.insert(20)

print("Queue Elements:")
q.display()