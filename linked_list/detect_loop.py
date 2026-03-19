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

    def create_loop(self, pos):
        if pos == -1:
            return
        loop_node = self.head
        for _ in range(pos):
            loop_node = loop_node.next
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = loop_node


def detect_loop(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)
    ll.insert_at_beginning(40)
    ll.insert_at_beginning(50)

    print("List without loop:")
    ll.print_list()
    print(f"Has loop: {detect_loop(ll.head)}")

    ll2 = LinkedList()
    ll2.insert_at_beginning(10)
    ll2.insert_at_beginning(20)
    ll2.insert_at_beginning(30)
    ll2.insert_at_beginning(40)
    ll2.insert_at_beginning(50)
    ll2.create_loop(2)

    print("\nList with loop (at position 2):")
    ll2.print_list()
    print(f"Has loop: {detect_loop(ll2.head)}")
