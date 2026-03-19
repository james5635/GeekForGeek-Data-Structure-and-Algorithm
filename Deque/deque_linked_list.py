class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DequeLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert_front(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

        self.size += 1
        return True

    def insert_rear(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1
        return True

    def delete_front(self):
        if self.is_empty():
            print("Deque is empty")
            return None

        value = self.front.data

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None

        self.size -= 1
        return value

    def delete_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return None

        value = self.rear.data

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None

        self.size -= 1
        return value

    def get_front(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.front.data

    def get_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.rear.data

    def display(self):
        if self.is_empty():
            print("Deque is empty")
            return

        result = []
        curr = self.front
        while curr:
            result.append(str(curr.data))
            curr = curr.next
        print(" ".join(result))

    def display_reverse(self):
        if self.is_empty():
            print("Deque is empty")
            return

        result = []
        curr = self.rear
        while curr:
            result.append(str(curr.data))
            curr = curr.prev
        print(" ".join(result))


def main():
    print("=" * 50)
    print("Deque Implementation using Doubly Linked List")
    print("=" * 50)

    # Test Case 1: Basic operations
    print("\nTest Case 1: Basic Operations")
    dq1 = DequeLinkedList()
    print("insert_front(10):", dq1.insert_front(10))
    print("insert_rear(20):", dq1.insert_rear(20))
    print("insert_front(5):", dq1.insert_front(5))
    print("insert_rear(30):", dq1.insert_rear(30))
    print("insert_front(1):", dq1.insert_front(1))
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

    # Test Case 3: Empty deque operations
    print("Test Case 3: Empty Deque Operations")
    dq2 = DequeLinkedList()
    print("get_front():", dq2.get_front())
    print("get_rear():", dq2.get_rear())
    print("delete_front():", dq2.delete_front())
    print("delete_rear():", dq2.delete_rear())
    print()

    # Test Case 4: Single element
    print("Test Case 4: Single Element Operations")
    dq3 = DequeLinkedList()
    dq3.insert_front(100)
    print("Display after inserting 100: ", end="")
    dq3.display()
    print(f"get_front(): {dq3.get_front()}")
    print(f"get_rear(): {dq3.get_rear()}")
    print("delete_front():", dq3.delete_front())
    print("Display after deleting: ", end="")
    dq3.display()
    print()

    # Test Case 5: Mixed operations
    print("Test Case 5: Mixed Operations")
    dq4 = DequeLinkedList()
    print("insert_rear(1)")
    dq4.insert_rear(1)
    print("insert_rear(2)")
    dq4.insert_rear(2)
    print("insert_front(0)")
    dq4.insert_front(0)
    print("insert_rear(3)")
    dq4.insert_rear(3)
    print("insert_front(-1)")
    dq4.insert_front(-1)
    print("Display: ", end="")
    dq4.display()
    print("Reverse display: ", end="")
    dq4.display_reverse()
    print()

    # Test Case 6: Large deque
    print("Test Case 6: Large Deque Operations")
    dq5 = DequeLinkedList()
    print("Inserting 10 elements at front...")
    for i in range(10, 0, -1):
        dq5.insert_front(i)
    print("Display: ", end="")
    dq5.display()
    print("Inserting 3 elements at rear...")
    for i in range(11, 14):
        dq5.insert_rear(i)
    print("Display: ", end="")
    dq5.display()
    print("Deleting 5 elements from front...")
    for _ in range(5):
        print(f"  delete_front(): {dq5.delete_front()}")
    print("Deleting 3 elements from rear...")
    for _ in range(3):
        print(f"  delete_rear(): {dq5.delete_rear()}")
    print("Final display: ", end="")
    dq5.display()


if __name__ == "__main__":
    main()
