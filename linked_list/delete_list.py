class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def delete_list(self):
        while self.head:
            temp = self.head
            self.head = self.head.next
            del temp
        print("Linked list deleted successfully")

    def print_list(self):
        if self.head is None:
            print("Empty list")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def is_empty(self):
        return self.head is None


if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(10)
    ll.head.next = Node(20)
    ll.head.next.next = Node(30)
    ll.head.next.next.next = Node(40)

    print("Original list:")
    ll.print_list()

    ll.delete_list()

    print("After deleting list:")
    print(f"Is empty: {ll.is_empty()}")
    ll.print_list()

    ll.head = Node(100)
    ll.head.next = Node(200)
    print("New list created:")
    ll.print_list()
