class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return False

        if position < 0:
            print("Invalid position")
            return False

        if position == 0:
            self.head = self.head.next
            return True

        current = self.head
        for _ in range(position - 1):
            if current.next is None:
                print("Position out of bounds")
                return False
            current = current.next

        if current.next is None:
            print("Position out of bounds")
            return False

        current.next = current.next.next
        return True

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(10)
    ll.head.next = Node(20)
    ll.head.next.next = Node(30)
    ll.head.next.next.next = Node(40)
    ll.head.next.next.next.next = Node(50)

    print("Original list:")
    ll.print_list()

    ll.delete_at_position(2)
    print("After deleting at position 2:")
    ll.print_list()

    ll.delete_at_position(0)
    print("After deleting at position 0 (head):")
    ll.print_list()

    ll.delete_at_position(10)
    print("After trying to delete at position 10:")
    ll.print_list()
