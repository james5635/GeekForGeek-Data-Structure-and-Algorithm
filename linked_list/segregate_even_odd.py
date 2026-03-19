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

    def segregate_even_odd(self):
        if not self.head or not self.head.next:
            return

        even_start = even_end = odd_start = odd_end = None

        current = self.head
        while current:
            val = current.data
            if val % 2 == 0:
                if not even_start:
                    even_start = even_end = current
                else:
                    even_end.next = current
                    even_end = current
            else:
                if not odd_start:
                    odd_start = odd_end = current
                else:
                    odd_end.next = current
                    odd_end = current
            current = current.next

        if not even_start:
            self.head = odd_start
            if odd_end:
                odd_end.next = None
            return

        if not odd_start:
            self.head = even_start
            if even_end:
                even_end.next = None
            return

        self.head = even_start
        even_end.next = odd_start
        odd_end.next = None


if __name__ == "__main__":
    ll = LinkedList()
    for data in [1, 2, 3, 4, 5, 6]:
        ll.append(data)

    print("Original list:", end=" ")
    ll.display()

    ll.segregate_even_odd()
    print("After segregation:", end=" ")
    ll.display()

    ll2 = LinkedList()
    for data in [8, 12, 10, 7, 6, 9, 11]:
        ll2.append(data)

    print("\nOriginal list:", end=" ")
    ll2.display()

    ll2.segregate_even_odd()
    print("After segregation:", end=" ")
    ll2.display()

    ll3 = LinkedList()
    print("\nEmpty list:", end=" ")
    ll3.display()
    ll3.segregate_even_odd()
    print("After segregation:", end=" ")
    ll3.display()

    ll4 = LinkedList()
    ll4.append(5)
    print("\nSingle odd element:", end=" ")
    ll4.display()
    ll4.segregate_even_odd()
    print("After segregation:", end=" ")
    ll4.display()

    ll5 = LinkedList()
    for data in [2, 4, 6, 8]:
        ll5.append(data)

    print("\nAll even:", end=" ")
    ll5.display()
    ll5.segregate_even_odd()
    print("After segregation:", end=" ")
    ll5.display()
