class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)

    print("After inserting 10, 20, 30 at beginning:")
    ll.print_list()

    ll.insert_at_beginning(5)
    print("After inserting 5 at beginning:")
    ll.print_list()
