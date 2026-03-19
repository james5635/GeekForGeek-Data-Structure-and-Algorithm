class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MergableStack:
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

    def merge(self, other):
        if other.is_empty():
            return
        current = other.top
        last = None
        while current:
            last = current
            current = current.next
        last.next = self.top
        self.top = other.top
        self._size += other._size
        other.top = None
        other._size = 0

    def __str__(self):
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        return "Stack(top -> " + " -> ".join(items) + ")"


if __name__ == "__main__":
    s1 = MergableStack()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    print(f"Stack 1: {s1}")

    s2 = MergableStack()
    s2.push(4)
    s2.push(5)
    s2.push(6)
    print(f"Stack 2: {s2}")

    print(f"\nMerging stack 2 into stack 1")
    s1.merge(s2)
    print(f"Stack 1 after merge: {s1}")
    print(f"Stack 2 after merge: {s2}")
    print(f"Stack 1 size: {s1.size()}")
    print(f"Stack 2 size: {s2.size()}")

    print(f"\nPopping from merged stack:")
    while not s1.is_empty():
        print(f"Pop: {s1.pop()}")
