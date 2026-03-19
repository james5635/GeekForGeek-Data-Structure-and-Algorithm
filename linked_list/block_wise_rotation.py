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


def rotate_right(head, k):
    if not head or k <= 0:
        return head

    current = head
    length = 1

    while current.next:
        current = current.next
        length += 1

    current.next = head

    k = k % length
    skip = length - k

    prev = None
    current = head
    for _ in range(skip):
        prev = current
        current = current.next

    prev.next = None
    return current


def block_wise_rotation(head, k):
    if not head or k <= 1:
        return head

    dummy = Node(0)
    dummy.next = head
    prev_group_end = dummy
    current = head

    while current:
        group_start = current
        count = 1

        while count < k and current.next:
            current = current.next
            count += 1

        if count < k:
            prev_group_end.next = group_start
            break

        next_group_start = current.next
        current.next = None

        rotated = rotate_right(group_start, k)

        prev_group_end.next = rotated

        while prev_group_end.next:
            prev_group_end = prev_group_end.next

        current = next_group_start

    return dummy.next


def block_wise_rotation_reverse(head, k):
    if not head or k <= 1:
        return head

    dummy = Node(0)
    dummy.next = head
    current = dummy

    while True:
        group_start = current.next
        if not group_start:
            break

        group_end = group_start
        count = 1

        while count < k and group_end.next:
            group_end = group_end.next
            count += 1

        if count < k:
            break

        next_group = group_end.next
        group_end.next = None

        prev = None
        temp = group_start
        while temp:
            next_temp = temp.next
            temp.next = prev
            prev = temp
            temp = next_temp

        current.next = prev
        group_start.next = next_group
        current = group_start

    return dummy.next


if __name__ == "__main__":
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        ll.insert_at_end(val)

    print("Original List:")
    ll.print_list()

    result = block_wise_rotation(ll.head, 3)
    print("After block-wise rotation (k=3):")
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

    result2 = block_wise_rotation_reverse(ll2.head, 4)
    print("After block-wise reverse rotation (k=4):")
    current = result2
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll3 = LinkedList()
    for val in [1, 2, 3, 4, 5, 6]:
        ll3.insert_at_end(val)

    print("Original List:")
    ll3.print_list()

    result3 = block_wise_rotation(ll3.head, 2)
    print("After block-wise rotation (k=2):")
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

    result4 = block_wise_rotation_reverse(ll4.head, 3)
    print("After block-wise reverse rotation (k=3):")
    current = result4
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
