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

    def reverse_iterative(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


if __name__ == "__main__":
    ll = LinkedList()
    for data in [1, 2, 3, 4, 5]:
        ll.append(data)

    print("Original list:", end=" ")
    ll.display()

    ll.reverse_iterative()
    print("Reversed list:", end=" ")
    ll.display()

    ll2 = LinkedList()
    ll2.append(10)
    print("\nSingle element list:", end=" ")
    ll2.display()
    ll2.reverse_iterative()
    print("After reverse:", end=" ")
    ll2.display()

    ll3 = LinkedList()
    print("\nEmpty list:", end=" ")
    ll3.display()
    ll3.reverse_iterative()
    print("After reverse:", end=" ")
    ll3.display()
