class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def __str__(self):
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        return "Stack(top -> " + " -> ".join(items) + ")"


if __name__ == "__main__":
    s = Stack()
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
