class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, data):
        new_node = Node(data)

        if self.head is None or self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data < data:
            current = current.next

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

    values = [30, 10, 50, 20, 40]
    for val in values:
        ll.insert_sorted(val)
        print(f"After inserting {val}:")
        ll.print_list()
