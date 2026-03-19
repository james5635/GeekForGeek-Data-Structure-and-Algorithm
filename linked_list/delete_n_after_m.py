class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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


def delete_n_after_m(head, m, n):
    if not head or m <= 0 or n <= 0:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy
    current = head

    while current:
        skip_count = 0
        while current and skip_count < m:
            prev = current
            current = current.next
            skip_count += 1

        delete_count = 0
        while current and delete_count < n:
            temp = current
            current = current.next
            delete_count += 1
            del temp

        prev.next = current

    return dummy.next


if __name__ == "__main__":
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        ll.insert_at_end(val)

    print("Original List:")
    ll.print_list()

    result = delete_n_after_m(ll.head, 2, 3)
    print("After deleting 3 nodes after every 2 nodes:")
    current = result
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll2 = LinkedList()
    for val in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        ll2.insert_at_end(val)

    print("Original List:")
    ll2.print_list()

    result2 = delete_n_after_m(ll2.head, 1, 1)
    print("After deleting 1 node after every 1 node (alternating):")
    current = result2
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll3 = LinkedList()
    for val in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        ll3.insert_at_end(val)

    print("Original List:")
    ll3.print_list()

    result3 = delete_n_after_m(ll3.head, 3, 2)
    print("After deleting 2 nodes after every 3 nodes:")
    current = result3
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll4 = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll4.insert_at_end(val)

    print("Original List:")
    ll4.print_list()

    result4 = delete_n_after_m(ll4.head, 5, 10)
    print("After deleting 10 nodes after every 5 nodes (delete remaining):")
    current = result4
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
