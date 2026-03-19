class myDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0
        self.size = 0

    def insertFront(self, x):
        if self.isFull():
            print("Deque is Full")
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = x
        self.size += 1
        return True

    def insertRear(self, x):
        if self.isFull():
            print("Deque is Full")
            return False
        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = x
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            print("Deque is Empty")
            return None
        val = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val

    def deleteRear(self):
        if self.isEmpty():
            print("Deque is Empty")
            return None
        rear = (self.front + self.size - 1) % self.capacity
        val = self.arr[rear]
        self.size -= 1
        return val

    def frontEle(self):
        if self.isEmpty():
            return None
        return self.arr[self.front]

    def rearEle(self):
        if self.isEmpty():
            return None
        return self.arr[(self.front + self.size - 1) % self.capacity]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


if __name__ == "__main__":
    dq = myDeque(5)

    print("=== Insert at Rear ===")
    dq.insertRear(10)
    dq.insertRear(20)
    dq.insertRear(30)
    print(f"Front: {dq.frontEle()}, Rear: {dq.rearEle()}")

    print("\n=== Insert at Front ===")
    dq.insertFront(5)
    dq.insertFront(1)
    print(f"Front: {dq.frontEle()}, Rear: {dq.rearEle()}")

    print(f"\nIs Full: {dq.isFull()}")
    dq.insertFront(0)

    print("\n=== Delete from Front ===")
    print(f"Deleted: {dq.deleteFront()}")
    print(f"Deleted: {dq.deleteFront()}")
    print(f"Front: {dq.frontEle()}, Rear: {dq.rearEle()}")

    print("\n=== Delete from Rear ===")
    print(f"Deleted: {dq.deleteRear()}")
    print(f"Front: {dq.frontEle()}, Rear: {dq.rearEle()}")

    print("\n=== Drain Remaining ===")
    while not dq.isEmpty():
        print(f"Deleted: {dq.deleteFront()}")
    print(f"Is Empty: {dq.isEmpty()}")

    print("\n=== Edge Cases ===")
    dq.deleteFront()
    dq.deleteRear()
    print("All tests passed")
