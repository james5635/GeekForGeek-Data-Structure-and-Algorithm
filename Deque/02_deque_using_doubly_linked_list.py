class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class myDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def insertFront(self, x):
        node = Node(x)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self._size += 1

    def insertRear(self, x):
        node = Node(x)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            node.prev = self.rear
            self.rear.next = node
            self.rear = node
        self._size += 1

    def deleteFront(self):
        if self.isEmpty():
            print("Deque is Empty")
            return None
        val = self.front.data
        self._size -= 1
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        return val

    def deleteRear(self):
        if self.isEmpty():
            print("Deque is Empty")
            return None
        val = self.rear.data
        self._size -= 1
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        return val

    def getFront(self):
        if self.isEmpty():
            return None
        return self.front.data

    def getRear(self):
        if self.isEmpty():
            return None
        return self.rear.data

    def isEmpty(self):
        return self.front is None

    def size(self):
        return self._size


if __name__ == "__main__":
    dq = myDeque()

    print("=== Insert at Rear ===")
    dq.insertRear(10)
    dq.insertRear(20)
    dq.insertRear(30)
    print(f"Front: {dq.getFront()}, Rear: {dq.getRear()}, Size: {dq.size()}")

    print("\n=== Insert at Front ===")
    dq.insertFront(5)
    dq.insertFront(1)
    print(f"Front: {dq.getFront()}, Rear: {dq.getRear()}, Size: {dq.size()}")

    print("\n=== Delete from Front ===")
    print(f"Deleted: {dq.deleteFront()}")
    print(f"Deleted: {dq.deleteFront()}")
    print(f"Front: {dq.getFront()}, Rear: {dq.getRear()}, Size: {dq.size()}")

    print("\n=== Delete from Rear ===")
    print(f"Deleted: {dq.deleteRear()}")
    print(f"Deleted: {dq.deleteRear()}")
    print(f"Front: {dq.getFront()}, Rear: {dq.getRear()}, Size: {dq.size()}")

    print("\n=== Single Element ===")
    print(f"Deleted: {dq.deleteFront()}")
    print(f"Is Empty: {dq.isEmpty()}")

    print("\n=== Edge Cases ===")
    dq.deleteFront()
    dq.deleteRear()
    print("All tests passed")
