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


def merge_sorted(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    dummy = Node(0)
    current = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1:
        current.next = head1
    if head2:
        current.next = head2

    return dummy.next


if __name__ == "__main__":
    ll1 = LinkedList()
    for val in [1, 3, 5, 7, 9]:
        ll1.insert_at_end(val)

    ll2 = LinkedList()
    for val in [2, 4, 6, 8, 10]:
        ll2.insert_at_end(val)

    print("List 1:")
    ll1.print_list()
    print("List 2:")
    ll2.print_list()

    merged = merge_sorted(ll1.head, ll2.head)
    print("Merged List:")
    current = merged
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll3 = LinkedList()
    for val in [1, 2, 4]:
        ll3.insert_at_end(val)

    ll4 = LinkedList()
    for val in [3, 5, 6]:
        ll4.insert_at_end(val)

    print("List 1:", end=" ")
    ll3.print_list()
    print("List 2:", end=" ")
    ll4.print_list()

    merged2 = merge_sorted(ll3.head, ll4.head)
    print("Merged List:")
    current = merged2
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("\n" + "=" * 40 + "\n")

    ll5 = LinkedList()
    for val in [1, 2, 3]:
        ll5.insert_at_end(val)

    ll6 = LinkedList()
    merged3 = merge_sorted(ll5.head, ll6.head)
    print("List 1:", end=" ")
    ll5.print_list()
    print("List 2: Empty")
    print("Merged List:")
    current = merged3
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
