class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                raise IndexError("dequeue from empty queue")
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            if not self.stack1:
                raise IndexError("peek from empty queue")
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def size(self):
        return len(self.stack1) + len(self.stack2)


if __name__ == "__main__":
    q = QueueUsingStacks()
    print("Enqueue: 1, 2, 3, 4")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(f"Size: {q.size()}")
    print(f"Peek: {q.peek()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Size after dequeues: {q.size()}")
    print(f"Peek: {q.peek()}")
    q.enqueue(5)
    print(f"Enqueue 5, then dequeue: {q.dequeue()}")
    print(f"Is empty: {q.is_empty()}")
