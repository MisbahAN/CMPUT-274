class StackUsingQueue:
    
    def __init__(self):
        self.queue = Queue()

    def push(self, element):
        self.queue.enqueue(element)
        
        for i in range(self.size() - 1):
            self.queue.enqueue(self.queue.pop())

    def pop(self):
        return self.queue.pop()

    def top(self):
        return self.queue.top()

    def is_empty(self):
        return self.queue.is_empty()

    def size(self):
        return len(self.queue.queue)