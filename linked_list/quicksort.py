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

    def get_tail(self):
        if not self.head:
            return None
        tail = self.head
        while tail.next:
            tail = tail.next
        return tail

    def partition(self, x):
        before_head = before_tail = None
        after_head = after_tail = None

        current = self.head
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
            self.head = after_head
        else:
            before_tail.next = after_head
            self.head = before_head


def quicksort(head):
    if not head or not head.next:
        return head

    pivot = head
    less_head = less_tail = None
    greater_head = greater_tail = None
    equal_head = equal_tail = None

    current = head.next
    while current:
        if current.data < pivot.data:
            if not less_head:
                less_head = less_tail = current
            else:
                less_tail.next = current
                less_tail = current
        elif current.data == pivot.data:
            if not equal_head:
                equal_head = equal_tail = current
            else:
                equal_tail.next = current
                equal_tail = current
        else:
            if not greater_head:
                greater_head = greater_tail = current
            else:
                greater_tail.next = current
                greater_tail = current
        current = current.next

    if greater_tail:
        greater_tail.next = None
    if equal_tail:
        equal_tail.next = None
    if less_tail:
        less_tail.next = None

    less_sorted = quicksort(less_head)
    greater_sorted = quicksort(greater_head)

    result_head = less_sorted
    if not result_head:
        result_head = equal_head
    else:
        tail = result_head
        while tail.next:
            tail = tail.next
        tail.next = equal_head

    if result_head and equal_head:
        tail = result_head
        while tail.next != equal_head:
            tail = tail.next
        tail.next = greater_sorted
    elif equal_head:
        equal_tail.next = greater_sorted
        result_head = equal_head
    else:
        result_head = greater_sorted

    return result_head


if __name__ == "__main__":
    ll = LinkedList()
    for val in [30, 5, 20, 10, 40, 15, 25]:
        ll.insert_at_end(val)

    print("Original list:")
    ll.print_list()

    ll.head = quicksort(ll.head)
    print("Sorted list (QuickSort):")
    ll.print_list()

    print("\n" + "=" * 40)

    ll2 = LinkedList()
    for val in [9, 3, 7, 1, 5, 2, 8]:
        ll2.insert_at_end(val)

    print("Original list:")
    ll2.print_list()

    ll2.head = quicksort(ll2.head)
    print("Sorted list (QuickSort):")
    ll2.print_list()
