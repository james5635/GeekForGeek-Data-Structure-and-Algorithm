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

    def pairwise_swap(self):
        if not self.head or not self.head.next:
            return

        current = self.head
        self.head = current.next

        prev = None
        while current and current.next:
            next_node = current.next
            current.next = next_node.next
            next_node.next = current

            if prev:
                prev.next = next_node

            prev = current
            current = current.next


if __name__ == "__main__":
    ll = LinkedList()
    for data in [1, 2, 3, 4, 5, 6]:
        ll.append(data)

    print("Original list:", end=" ")
    ll.display()

    ll.pairwise_swap()
    print("After pairwise swap:", end=" ")
    ll.display()

    ll2 = LinkedList()
    for data in [1, 2, 3, 4, 5]:
        ll2.append(data)

    print("\nOriginal list (odd length):", end=" ")
    ll2.display()

    ll2.pairwise_swap()
    print("After pairwise swap:", end=" ")
    ll2.display()

    ll3 = LinkedList()
    print("\nEmpty list:", end=" ")
    ll3.display()
    ll3.pairwise_swap()
    print("After pairwise swap:", end=" ")
    ll3.display()

    ll4 = LinkedList()
    ll4.append(10)
    print("\nSingle element:", end=" ")
    ll4.display()
    ll4.pairwise_swap()
    print("After pairwise swap:", end=" ")
    ll4.display()

    ll5 = LinkedList()
    for data in [1, 2]:
        ll5.append(data)

    print("\nTwo elements:", end=" ")
    ll5.display()
    ll5.pairwise_swap()
    print("After pairwise swap:", end=" ")
    ll5.display()
