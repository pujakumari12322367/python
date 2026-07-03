class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            self.queue.pop(0)

    def display(self):
        print(self.queue)
q = Queue()
q.insert(5)
q.insert(10)
q.insert(15)
q.insert(20)
q.delete()
q.display()