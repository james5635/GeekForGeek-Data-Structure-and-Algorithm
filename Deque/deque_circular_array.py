class DequeCircularArray:
    def __init__(self, size):
        self.size = size
        self.deque = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def insert_front(self, value):
        if self.is_full():
            print("Deque is full")
            return False

        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.deque[self.front] = value
        else:
            self.front = (self.front - 1 + self.size) % self.size
            self.deque[self.front] = value

        return True

    def insert_rear(self, value):
        if self.is_full():
            print("Deque is full")
            return False

        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.deque[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.deque[self.rear] = value

        return True

    def delete_front(self):
        if self.is_empty():
            print("Deque is empty")
            return None

        value = self.deque[self.front]
        self.deque[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return value

    def delete_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return None

        value = self.deque[self.rear]
        self.deque[self.rear] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size

        return value

    def get_front(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.deque[self.front]

    def get_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.deque[self.rear]

    def display(self):
        if self.is_empty():
            print("Deque is empty")
            return

        result = []
        i = self.front
        while True:
            result.append(str(self.deque[i]))
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print(" ".join(result))


def main():
    print("=" * 50)
    print("Deque Implementation using Circular Array")
    print("=" * 50)

    # Test Case 1: Basic operations
    print("\nTest Case 1: Basic Operations")
    dq1 = DequeCircularArray(10)
    print("insert_rear(10): ", end="")
    dq1.insert_rear(10)
    print("insert_rear(20): ", end="")
    dq1.insert_rear(20)
    print("insert_front(5): ", end="")
    dq1.insert_front(5)
    print("insert_rear(30): ", end="")
    dq1.insert_rear(30)
    print("insert_front(1): ", end="")
    dq1.insert_front(1)
    print("Display: ", end="")
    dq1.display()
    print(f"get_front(): {dq1.get_front()}")
    print(f"get_rear(): {dq1.get_rear()}")
    print()

    # Test Case 2: Delete operations
    print("Test Case 2: Delete Operations")
    print("delete_front():", dq1.delete_front())
    print("delete_rear():", dq1.delete_rear())
    print("Display after deletions: ", end="")
    dq1.display()
    print()

    # Test Case 3: Fill and empty
    print("Test Case 3: Fill and Empty Deque")
    dq2 = DequeCircularArray(5)
    print("Inserting 5 elements...")
    for i in range(1, 6):
        dq2.insert_rear(i * 10)
    print("Display: ", end="")
    dq2.display()
    print("Deleting all elements:")
    while not dq2.is_empty():
        print(f"  delete_front(): {dq2.delete_front()}")
    print()

    # Test Case 4: Empty deque operations
    print("Test Case 4: Empty Deque Operations")
    dq3 = DequeCircularArray(5)
    print("get_front():", dq3.get_front())
    print("get_rear():", dq3.get_rear())
    print("delete_front():", dq3.delete_front())
    print("delete_rear():", dq3.delete_rear())
    print()

    # Test Case 5: Full deque
    print("Test Case 5: Full Deque")
    dq4 = DequeCircularArray(3)
    print("Inserting 3 elements...")
    dq4.insert_rear(100)
    dq4.insert_rear(200)
    dq4.insert_rear(300)
    print("Display: ", end="")
    dq4.display()
    print("Trying to insert 4th element:")
    dq4.insert_rear(400)
    print()

    # Test Case 6: Mixed operations
    print("Test Case 6: Mixed Operations")
    dq5 = DequeCircularArray(8)
    operations = [
        ("insert_rear", 1),
        ("insert_rear", 2),
        ("insert_front", 0),
        ("insert_rear", 3),
        ("insert_front", -1),
        ("delete_front", None),
        ("delete_rear", None),
        ("insert_front", 10),
        ("insert_rear", 20),
    ]

    for op, val in operations:
        if op == "insert_front":
            dq5.insert_front(val)
            print(f"insert_front({val})")
        elif op == "insert_rear":
            dq5.insert_rear(val)
            print(f"insert_rear({val})")
        elif op == "delete_front":
            result = dq5.delete_front()
            print(f"delete_front() -> {result}")
        elif op == "delete_rear":
            result = dq5.delete_rear()
            print(f"delete_rear() -> {result}")

    print("Final display: ", end="")
    dq5.display()


if __name__ == "__main__":
    main()
