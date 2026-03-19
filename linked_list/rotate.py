from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")

    def rotate(self, n):
        if n <= 0 or not self.head or not self.head.next:
            return

        current = self.head
        count = 1

        while current.next and count < n:
            current = current.next
            count += 1

        if not current.next:
            return

        new_head = current.next
        current.next = None

        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = self.head

        self.head = new_head


if __name__ == "__main__":
    ll = LinkedList()
    for data in [1, 2, 3, 4, 5]:
        ll.append(data)

    print("Original list:", end=" ")
    ll.display()

    ll.rotate(2)
    print("After rotating by 2:", end=" ")
    ll.display()

    ll2 = LinkedList()
    for data in [2, 4, 7, 9, 1]:
        ll2.append(data)

    print("\nOriginal list:", end=" ")
    ll2.display()

    ll2.rotate(3)
    print("After rotating by 3:", end=" ")
    ll2.display()

    ll3 = LinkedList()
    for data in [10, 20, 30, 40]:
        ll3.append(data)

    print("\nOriginal list:", end=" ")
    ll3.display()

    ll3.rotate(4)
    print("After rotating by 4 (full length):", end=" ")
    ll3.display()

    ll4 = LinkedList()
    ll4.append(5)
    print("\nSingle element:", end=" ")
    ll4.display()
    ll4.rotate(1)
    print("After rotate:", end=" ")
    ll4.display()

    ll5 = LinkedList()
    print("\nEmpty list:", end=" ")
    ll5.display()
    ll5.rotate(2)
    print("After rotate:", end=" ")
    ll5.display()
