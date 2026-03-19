class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def delete_node(self, value):
        if self.head is None:
            print("List is empty")
            return False

        if self.head.data == value:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next

        print(f"Value {value} not found in the list")
        return False

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

    print("Original list:")
    ll.print_list()

    ll.delete_node(20)
    print("After deleting 20:")
    ll.print_list()

    ll.delete_node(10)
    print("After deleting 10 (head):")
    ll.print_list()

    ll.delete_node(100)
    print("After trying to delete 100:")
    ll.print_list()
