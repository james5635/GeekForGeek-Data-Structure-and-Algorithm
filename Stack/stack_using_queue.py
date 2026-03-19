from collections import deque


class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.queue.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __str__(self):
        return f"Stack({list(self.queue)})"


if __name__ == "__main__":
    s = StackUsingQueue()
    print("Pushing 10, 20, 30")
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"Stack: {s}")
    print(f"Size: {s.size()}")
    print(f"Peek: {s.peek()}")
    print(f"Pop: {s.pop()}")
    print(f"Pop: {s.pop()}")
    print(f"Stack after pops: {s}")
    print(f"Is empty: {s.is_empty()}")
    s.pop()
    print(f"Is empty after popping all: {s.is_empty()}")
