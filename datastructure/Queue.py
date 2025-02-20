class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        new_queue = [0] * (len(self.queue) + 1)
        for i in range(len(self.queue)):
            new_queue[i] = self.queue[i]
        new_queue[len(self.queue)] = value
        self.queue = new_queue

    def dequeue(self):
        if len(self.queue) == 0:
            raise IndexError("dequeue from empty queue")
        value = self.queue[0]
        new_queue = [0] * (len(self.queue) - 1)
        for i in range(1, len(self.queue)):
            new_queue[i - 1] = self.queue[i]
        self.queue = new_queue
        return value

    def peek(self):
        if len(self.queue) == 0:
            raise IndexError("peek from empty queue")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        count = 0
        for _ in self.queue:
            count += 1
        return count


