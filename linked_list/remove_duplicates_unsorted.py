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

    def remove_duplicates_unsorted(self):
        if not self.head or not self.head.next:
            return

        seen = set()
        current = self.head
        seen.add(current.data)

        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next


if __name__ == "__main__":
    ll = LinkedList()
    for data in [12, 11, 12, 21, 41, 43, 21]:
        ll.append(data)

    print("Original list:", end=" ")
    ll.display()

    ll.remove_duplicates_unsorted()
    print("After removing duplicates:", end=" ")
    ll.display()

    ll2 = LinkedList()
    for data in [5, 3, 5, 3, 10, 15, 10]:
        ll2.append(data)

    print("\nOriginal list:", end=" ")
    ll2.display()

    ll2.remove_duplicates_unsorted()
    print("After removing duplicates:", end=" ")
    ll2.display()

    ll3 = LinkedList()
    for data in [1, 2, 3, 4, 5]:
        ll3.append(data)

    print("\nNo duplicates:", end=" ")
    ll3.display()

    ll3.remove_duplicates_unsorted()
    print("After removing duplicates:", end=" ")
    ll3.display()

    ll4 = LinkedList()
    print("\nEmpty list:", end=" ")
    ll4.display()
    ll4.remove_duplicates_unsorted()
    print("After removing duplicates:", end=" ")
    ll4.display()

    ll5 = LinkedList()
    ll5.append(7)
    print("\nSingle element:", end=" ")
    ll5.display()
    ll5.remove_duplicates_unsorted()
    print("After removing duplicates:", end=" ")
    ll5.display()
