class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next

        if current is None:
            print("Position out of bounds")
            return

        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end = lambda data: None

    ll.head = Node(10)
    ll.head.next = Node(20)
    ll.head.next.next = Node(30)

    print("Original list:")
    ll.print_list()

    ll.insert_at_position(15, 1)
    print("After inserting 15 at position 1:")
    ll.print_list()

    ll.insert_at_position(5, 0)
    print("After inserting 5 at position 0:")
    ll.print_list()

    ll.insert_at_position(40, 5)
    print("After inserting 40 at position 5:")
    ll.print_list()
