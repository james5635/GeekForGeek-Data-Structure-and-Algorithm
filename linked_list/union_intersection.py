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

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


def union_intersection(head1, head2):
    s = set()
    temp1 = head1
    while temp1:
        s.add(temp1.data)
        temp1 = temp1.next

    union_head = union_tail = None
    intersection_head = intersection_tail = None

    temp2 = head2
    while temp2:
        if temp2.data not in s:
            new_node = Node(temp2.data)
            if not union_head:
                union_head = union_tail = new_node
            else:
                union_tail.next = new_node
                union_tail = new_node
        else:
            if not intersection_head:
                intersection_head = intersection_tail = Node(temp2.data)
            else:
                intersection_tail.next = Node(temp2.data)
                intersection_tail = intersection_tail.next
        temp2 = temp2.next

    temp1 = head1
    while temp1:
        new_node = Node(temp1.data)
        if not union_head:
            union_head = union_tail = new_node
        else:
            union_tail.next = new_node
            union_tail = new_node
        temp1 = temp1.next

    return union_head, intersection_head


def union_intersection_sorted(head1, head2):
    union_head = union_tail = None
    intersection_head = intersection_tail = None

    while head1 and head2:
        if head1.data == head2.data:
            if not union_head:
                union_head = union_tail = Node(head1.data)
            else:
                union_tail.next = Node(head1.data)
                union_tail = union_tail.next
            if not intersection_head:
                intersection_head = intersection_tail = Node(head1.data)
            else:
                intersection_tail.next = Node(head1.data)
                intersection_tail = intersection_tail.next
            head1 = head1.next
            head2 = head2.next
        elif head1.data < head2.data:
            if not union_head:
                union_head = union_tail = Node(head1.data)
            else:
                union_tail.next = Node(head1.data)
                union_tail = union_tail.next
            head1 = head1.next
        else:
            if not union_head:
                union_head = union_tail = Node(head2.data)
            else:
                union_tail.next = Node(head2.data)
                union_tail = union_tail.next
            head2 = head2.next

    while head1:
        if not union_head:
            union_head = union_tail = Node(head1.data)
        else:
            union_tail.next = Node(head1.data)
            union_tail = union_tail.next
        head1 = head1.next

    while head2:
        if not union_head:
            union_head = union_tail = Node(head2.data)
        else:
            union_tail.next = Node(head2.data)
            union_tail = union_tail.next
        head2 = head2.next

    return union_head, intersection_head


if __name__ == "__main__":
    print("Using Hashing approach:")
    print("=" * 40)

    ll1 = LinkedList()
    for val in [10, 20, 30, 40]:
        ll1.insert_at_end(val)

    ll2 = LinkedList()
    for val in [30, 40, 50, 60]:
        ll2.insert_at_end(val)

    print("List 1:")
    ll1.print_list()
    print("List 2:")
    ll2.print_list()

    union_head, intersection_head = union_intersection(ll1.head, ll2.head)

    union_list = LinkedList()
    union_list.head = union_head
    print("Union:")
    union_list.print_list()

    intersection_list = LinkedList()
    intersection_list.head = intersection_head
    print("Intersection:")
    intersection_list.print_list()

    print("\n" + "=" * 40)
    print("Using Sorted Lists approach:")
    print("=" * 40)

    ll3 = LinkedList()
    for val in [1, 3, 5, 7, 9]:
        ll3.insert_at_end(val)

    ll4 = LinkedList()
    for val in [2, 3, 5, 7, 10]:
        ll4.insert_at_end(val)

    print("List 1:")
    ll3.print_list()
    print("List 2:")
    ll4.print_list()

    union_head, intersection_head = union_intersection_sorted(ll3.head, ll4.head)

    union_list = LinkedList()
    union_list.head = union_head
    print("Union:")
    union_list.print_list()

    intersection_list = LinkedList()
    intersection_list.head = intersection_head
    print("Intersection:")
    intersection_list.print_list()
