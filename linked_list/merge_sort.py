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


def get_middle(head):
    if not head:
        return head
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)
    return result


def merge_sort(head):
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next

    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = merge(left, right)
    return sorted_list


if __name__ == "__main__":
    ll = LinkedList()
    for val in [64, 34, 25, 12, 22, 11, 90]:
        ll.insert_at_end(val)

    print("Original list:")
    ll.print_list()

    ll.head = merge_sort(ll.head)
    print("Sorted list (MergeSort):")
    ll.print_list()

    print("\n" + "=" * 40)

    ll2 = LinkedList()
    for val in [38, 27, 43, 3, 9, 82, 10]:
        ll2.insert_at_end(val)

    print("Original list:")
    ll2.print_list()

    ll2.head = merge_sort(ll2.head)
    print("Sorted list (MergeSort):")
    ll2.print_list()

    print("\n" + "=" * 40)

    ll3 = LinkedList()
    ll3.insert_at_end(1)
    print("Single element list:")
    ll3.print_list()
    ll3.head = merge_sort(ll3.head)
    print("Sorted list:")
    ll3.print_list()
