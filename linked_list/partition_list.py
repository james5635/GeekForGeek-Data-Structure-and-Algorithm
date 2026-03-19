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

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
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


def partition_list(head, x):
    before_head = before_tail = None
    after_head = after_tail = None

    current = head
    while current:
        if current.data < x:
            if not before_head:
                before_head = before_tail = current
            else:
                before_tail.next = current
                before_tail = current
        else:
            if not after_head:
                after_head = after_tail = current
            else:
                after_tail.next = current
                after_tail = current
        current = current.next

    if after_tail:
        after_tail.next = None

    if not before_head:
        return after_head

    before_tail.next = after_head
    return before_head


if __name__ == "__main__":
    ll = LinkedList()
    for val in [3, 8, 5, 10, 2, 1]:
        ll.insert_at_end(val)

    print("Original list:")
    ll.print_list()

    ll.head = partition_list(ll.head, 5)
    print("After partitioning around 5:")
    ll.print_list()

    print("\n" + "=" * 40)

    ll2 = LinkedList()
    for val in [1, 4, 3, 2, 5, 2]:
        ll2.insert_at_end(val)

    print("Original list:")
    ll2.print_list()

    ll2.head = partition_list(ll2.head, 3)
    print("After partitioning around 3:")
    ll2.print_list()

    print("\n" + "=" * 40)

    ll3 = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll3.insert_at_end(val)

    print("Original list (all smaller than pivot):")
    ll3.print_list()

    ll3.head = partition_list(ll3.head, 10)
    print("After partitioning around 10:")
    ll3.print_list()

    print("\n" + "=" * 40)

    ll4 = LinkedList()
    for val in [5, 5, 5, 5, 5]:
        ll4.insert_at_end(val)

    print("Original list (all equal to pivot):")
    ll4.print_list()

    ll4.head = partition_list(ll4.head, 5)
    print("After partitioning around 5:")
    ll4.print_list()
