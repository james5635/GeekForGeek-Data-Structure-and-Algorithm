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


def intersection_sorted(head1, head2):
    result = None
    result_tail = None

    while head1 and head2:
        if head1.data == head2.data:
            new_node = Node(head1.data)
            if not result:
                result = result_tail = new_node
            else:
                result_tail.next = new_node
                result_tail = new_node
            head1 = head1.next
            head2 = head2.next
        elif head1.data < head2.data:
            head1 = head1.next
        else:
            head2 = head2.next

    return result


if __name__ == "__main__":
    ll1 = LinkedList()
    for val in [1, 2, 3, 4, 6]:
        ll1.insert_at_end(val)

    ll2 = LinkedList()
    for val in [2, 4, 6, 8]:
        ll2.insert_at_end(val)

    print("List 1:")
    ll1.print_list()
    print("List 2:")
    ll2.print_list()

    result = intersection_sorted(ll1.head, ll2.head)
    result_list = LinkedList()
    result_list.head = result
    print("Intersection:")
    result_list.print_list()

    print("\n" + "=" * 40)

    ll3 = LinkedList()
    for val in [1, 3, 5, 7, 9]:
        ll3.insert_at_end(val)

    ll4 = LinkedList()
    for val in [2, 4, 6, 8, 10]:
        ll4.insert_at_end(val)

    print("List 1:")
    ll3.print_list()
    print("List 2:")
    ll4.print_list()

    result = intersection_sorted(ll3.head, ll4.head)
    result_list = LinkedList()
    result_list.head = result
    print("Intersection:")
    result_list.print_list()

    print("\n" + "=" * 40)

    ll5 = LinkedList()
    for val in [1, 2, 2, 3, 4]:
        ll5.insert_at_end(val)

    ll6 = LinkedList()
    for val in [2, 2, 5, 6]:
        ll6.insert_at_end(val)

    print("List 1:")
    ll5.print_list()
    print("List 2:")
    ll6.print_list()

    result = intersection_sorted(ll5.head, ll6.head)
    result_list = LinkedList()
    result_list.head = result
    print("Intersection (with duplicates):")
    result_list.print_list()
