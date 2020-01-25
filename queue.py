class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        return self.queue.pop(0)
    def disply(self):
        return self.queue
queueOperations = Queue()
queueOperations.enqueue(10)
queueOperations.enqueue(20)
queueOperations.enqueue(30)
queueOperations.enqueue(40)
print(queueOperations.disply())
print()
queueOperations.dequeue()
print(queueOperations.disply())

