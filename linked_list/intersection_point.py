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


def get_intersection_point(head1, head2):
    if not head1 or not head2:
        return None

    def get_length(head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    len1 = get_length(head1)
    len2 = get_length(head2)

    diff = abs(len1 - len2)

    longer = head1 if len1 > len2 else head2
    shorter = head2 if len1 > len2 else head1

    for _ in range(diff):
        longer = longer.next

    while longer and shorter:
        if longer == shorter:
            return longer
        longer = longer.next
        shorter = shorter.next

    return None


def get_intersection_point_hash(head1, head2):
    if not head1 or not head2:
        return None

    visited = set()

    current = head1
    while current:
        visited.add(id(current))
        current = current.next

    current = head2
    while current:
        if id(current) in visited:
            return current
        current = current.next

    return None


if __name__ == "__main__":
    head1 = Node(10)
    head2 = Node(20)

    shared = Node(30)
    shared.next = Node(40)
    shared.next.next = Node(50)

    head1.next = Node(15)
    head1.next.next = Node(25)
    head1.next.next.next = shared

    head2.next = shared

    print("List 1:")
    current = head1
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("List 2:")
    current = head2
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    intersection = get_intersection_point(head1, head2)
    print(
        f"\nIntersection point (Method 1 - Length Diff): {intersection.data if intersection else 'None'}"
    )

    intersection2 = get_intersection_point_hash(head1, head2)
    print(
        f"Intersection point (Method 2 - Hashing): {intersection2.data if intersection2 else 'None'}"
    )

    print("\n" + "=" * 40 + "\n")

    ll1 = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll1.insert_at_end(val)

    ll2 = LinkedList()
    for val in [6, 7]:
        ll2.insert_at_end(val)

    print("List 1 (no intersection):")
    ll1.print_list()
    print("List 2 (no intersection):")
    ll2.print_list()

    intersection3 = get_intersection_point(ll1.head, ll2.head)
    print(f"\nIntersection point: {intersection3.data if intersection3 else 'None'}")

    print("\n" + "=" * 40 + "\n")

    ll3 = LinkedList()
    head3 = Node(100)
    ll3.head = head3
    for val in [200, 300]:
        head3.next = Node(val)
        head3 = head3.next

    ll4 = LinkedList()
    ll4.head = Node(400)

    intersection_node = Node(500)
    ll4.head.next = intersection_node
    intersection_node.next = Node(600)
    head3.next = intersection_node

    print("List 1:")
    current = ll3.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("List 2:")
    current = ll4.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    intersection4 = get_intersection_point(ll3.head, ll4.head)
    print(f"\nIntersection point: {intersection4.data if intersection4 else 'None'}")
