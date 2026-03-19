"""
Implement Stack and Queue using Deque

Approach:
- Deque provides O(1) operations at both ends
- Stack: Use one end for both push and pop
- Queue: Use one end for enqueue, other for dequeue

Classes:
- Node: Basic linked list node for deque implementation
- Deque: Full deque with O(1) operations at both ends
- Stack: LIFO structure using deque
- Queue: FIFO structure using deque
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    """Doubly linked list based Deque with O(1) operations at both ends."""

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def add_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def remove_front(self):
        if self.is_empty():
            return None
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return data

    def remove_rear(self):
        if self.is_empty():
            return None
        data = self.rear.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1
        return data

    def get_front(self):
        return self.front.data if self.front else None

    def get_rear(self):
        return self.rear.data if self.rear else None

    def display(self):
        result = []
        curr = self.front
        while curr:
            result.append(str(curr.data))
            curr = curr.next
        return " <-> ".join(result) if result else "Empty"


class Stack:
    """LIFO Stack implemented using Deque."""

    def __init__(self):
        self.deque = Deque()

    def push(self, data):
        self.deque.add_rear(data)

    def pop(self):
        return self.deque.remove_rear()

    def peek(self):
        return self.deque.get_rear()

    def is_empty(self):
        return self.deque.is_empty()

    def size(self):
        return self.deque.size

    def display(self):
        return self.deque.display()


class Queue:
    """FIFO Queue implemented using Deque."""

    def __init__(self):
        self.deque = Deque()

    def enqueue(self, data):
        self.deque.add_rear(data)

    def dequeue(self):
        return self.deque.remove_front()

    def front(self):
        return self.deque.get_front()

    def rear(self):
        return self.deque.get_rear()

    def is_empty(self):
        return self.deque.is_empty()

    def size(self):
        return self.deque.size

    def display(self):
        return self.deque.display()


def main():
    print("=== Stack and Queue Implementation using Deque ===\n")

    print("--- Testing Stack ---")
    stack = Stack()

    print("\nPush 10, 20, 30:")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Stack: {stack.display()}")

    print("\nPop twice:")
    print(f"Popped: {stack.pop()}")
    print(f"Stack: {stack.display()}")
    print(f"Popped: {stack.pop()}")
    print(f"Stack: {stack.display()}")

    print("\nPeek:", stack.peek())
    print(f"Is empty: {stack.is_empty()}")
    print(f"Size: {stack.size()}")

    print("\nPush 40, 50, then pop all:")
    stack.push(40)
    stack.push(50)
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}")

    print("\n--- Testing Queue ---")
    queue = Queue()

    print("\nEnqueue 1, 2, 3, 4, 5:")
    for i in range(1, 6):
        queue.enqueue(i)
    print(f"Queue: {queue.display()}")

    print("\nDequeue twice:")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Queue: {queue.display()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Queue: {queue.display()}")

    print("\nFront:", queue.front())
    print("Rear:", queue.rear())
    print(f"Is empty: {queue.is_empty()}")
    print(f"Size: {queue.size()}")

    print("\nEnqueue 6, 7, then dequeue all:")
    queue.enqueue(6)
    queue.enqueue(7)
    while not queue.is_empty():
        print(f"Dequeued: {queue.dequeue()}")

    print("\n--- Edge Cases ---")
    print("\nPop from empty stack:", Stack().pop())
    print("Dequeue from empty queue:", Queue().dequeue())


if __name__ == "__main__":
    main()
