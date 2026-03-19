class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def insertFront(self, x):
        node = Node(x)
        if self.front is None:
            self.front = self.rear = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self._size += 1

    def insertRear(self, x):
        node = Node(x)
        if self.rear is None:
            self.front = self.rear = node
        else:
            node.prev = self.rear
            self.rear.next = node
            self.rear = node
        self._size += 1

    def deleteFront(self):
        if self.front is None:
            return None
        val = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self._size -= 1
        return val

    def deleteRear(self):
        if self.rear is None:
            return None
        val = self.rear.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self._size -= 1
        return val

    def getFront(self):
        if self.front is None:
            return None
        return self.front.data

    def getRear(self):
        if self.rear is None:
            return None
        return self.rear.data

    def isEmpty(self):
        return self.front is None

    def size(self):
        return self._size


class Stack:
    def __init__(self):
        self.dq = Deque()

    def push(self, x):
        self.dq.insertRear(x)

    def pop(self):
        if self.dq.isEmpty():
            print("Stack is Empty")
            return None
        return self.dq.deleteRear()

    def peek(self):
        if self.dq.isEmpty():
            return None
        return self.dq.getRear()

    def isEmpty(self):
        return self.dq.isEmpty()

    def size(self):
        return self.dq.size()


class Queue:
    def __init__(self):
        self.dq = Deque()

    def enqueue(self, x):
        self.dq.insertRear(x)

    def dequeue(self):
        if self.dq.isEmpty():
            print("Queue is Empty")
            return None
        return self.dq.deleteFront()

    def peek(self):
        if self.dq.isEmpty():
            return None
        return self.dq.getFront()

    def isEmpty(self):
        return self.dq.isEmpty()

    def size(self):
        return self.dq.size()


if __name__ == "__main__":
    print("=== Stack Tests ===")
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    print(f"Peek: {st.peek()}")
    print(f"Pop: {st.pop()}")
    print(f"Pop: {st.pop()}")
    print(f"Peek: {st.peek()}")
    print(f"Size: {st.size()}")
    print(f"Pop: {st.pop()}")
    print(f"Is Empty: {st.isEmpty()}")
    st.pop()

    print("\n=== Queue Tests ===")
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(f"Peek: {q.peek()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Peek: {q.peek()}")
    print(f"Size: {q.size()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Is Empty: {q.isEmpty()}")
    q.dequeue()

    print("\n=== Mixed Operations ===")
    st2 = Stack()
    for i in range(1, 6):
        st2.push(i)
    while not st2.isEmpty():
        print(st2.pop(), end=" ")
    print()

    q2 = Queue()
    for i in range(1, 6):
        q2.enqueue(i)
    while not q2.isEmpty():
        print(q2.dequeue(), end=" ")
    print()
    print("All tests passed")
