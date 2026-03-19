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

    def reverse_in_groups(self, k):
        if k <= 1 or not self.head:
            return

        prev_group_end = None
        current = self.head

        while current:
            group_start = current
            prev = None
            count = 0

            while current and count < k:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                count += 1

            if prev_group_end:
                prev_group_end.next = prev
            else:
                self.head = prev

            group_start.next = current
            prev_group_end = group_start


if __name__ == "__main__":
    ll = LinkedList()
    for data in [1, 2, 3, 4, 5, 6, 7, 8]:
        ll.append(data)

    print("Original list:", end=" ")
    ll.display()

    ll.reverse_in_groups(3)
    print("Reversed in groups of 3:", end=" ")
    ll.display()

    ll2 = LinkedList()
    for data in [1, 2, 3, 4, 5]:
        ll2.append(data)

    print("\nOriginal list:", end=" ")
    ll2.display()

    ll2.reverse_in_groups(2)
    print("Reversed in groups of 2:", end=" ")
    ll2.display()

    ll3 = LinkedList()
    for data in [1, 2, 3, 4, 5, 6]:
        ll3.append(data)

    print("\nOriginal list:", end=" ")
    ll3.display()

    ll3.reverse_in_groups(4)
    print("Reversed in groups of 4:", end=" ")
    ll3.display()

    ll4 = LinkedList()
    print("\nEmpty list:", end=" ")
    ll4.display()
    ll4.reverse_in_groups(2)
    print("After reverse:", end=" ")
    ll4.display()
