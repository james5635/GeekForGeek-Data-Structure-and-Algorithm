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


def remove_kth_node(head, k):
    if not head or k <= 0:
        return head

    dummy = Node(0)
    dummy.next = head

    current = dummy
    count = 0

    while current and current.next:
        count += 1
        if count % k == 0:
            to_delete = current.next
            current.next = to_delete.next
            del to_delete
            count = 0
        current = current.next

    return dummy.next


def remove_kth_node_single_pass(head, k):
    if not head or k <= 0:
        return head

    dummy = Node(0)
    dummy.next = head

    first = dummy
    second = dummy

    for _ in range(k):
        if first:
            first = first.next

    if not first:
        return head

    while first.next:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next


def remove_every_kth_node(head, k):
    if not head or k <= 1:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy
    count = 1

    current = head
    while current:
        if count % k == 0:
            prev.next = current.next
            temp = current
            current = current.next
            del temp
        else:
            prev = current
            current = current.next
        count += 1

    return dummy.next


if __name__ == "__main__":
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        ll.insert_at_end(val)

    print("Original List:")
    ll.print_list()

    result = remove_kth_node(ll.head, 3)
    print("After removing every 3rd node:")
    current = result
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll2 = LinkedList()
    for val in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        ll2.insert_at_end(val)

    print("Original List:")
    ll2.print_list()

    result2 = remove_kth_node_single_pass(ll2.head, 4)
    print("After removing 4th node (single pass):")
    current = result2
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll3 = LinkedList()
    for val in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        ll3.insert_at_end(val)

    print("Original List:")
    ll3.print_list()

    result3 = remove_every_kth_node(ll3.head, 5)
    print("After removing every 5th node:")
    current = result3
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll4 = LinkedList()
    for val in [10, 20, 30, 40]:
        ll4.insert_at_end(val)

    print("Original List:")
    ll4.print_list()

    result4 = remove_every_kth_node(ll4.head, 2)
    print("After removing every 2nd node:")
    current = result4
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
