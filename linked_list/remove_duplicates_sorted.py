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

    def remove_duplicates_sorted(self):
        if not self.head or not self.head.next:
            return

        current = self.head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next


if __name__ == "__main__":
    ll = LinkedList()
    for data in [11, 11, 11, 21, 43, 43, 60]:
        ll.append(data)

    print("Original sorted list:", end=" ")
    ll.display()

    ll.remove_duplicates_sorted()
    print("After removing duplicates:", end=" ")
    ll.display()

    ll2 = LinkedList()
    for data in [1, 2, 2, 3, 3, 3, 4, 5, 5]:
        ll2.append(data)

    print("\nOriginal sorted list:", end=" ")
    ll2.display()

    ll2.remove_duplicates_sorted()
    print("After removing duplicates:", end=" ")
    ll2.display()

    ll3 = LinkedList()
    for data in [1, 2, 3, 4, 5]:
        ll3.append(data)

    print("\nNo duplicates:", end=" ")
    ll3.display()

    ll3.remove_duplicates_sorted()
    print("After removing duplicates:", end=" ")
    ll3.display()

    ll4 = LinkedList()
    print("\nEmpty list:", end=" ")
    ll4.display()
    ll4.remove_duplicates_sorted()
    print("After removing duplicates:", end=" ")
    ll4.display()

    ll5 = LinkedList()
    ll5.append(10)
    print("\nSingle element:", end=" ")
    ll5.display()
    ll5.remove_duplicates_sorted()
    print("After removing duplicates:", end=" ")
    ll5.display()
