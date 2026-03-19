class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)

    print("After inserting 10, 20, 30 at end:")
    ll.print_list()

    ll.insert_at_end(40)
    print("After inserting 40 at end:")
    ll.print_list()
