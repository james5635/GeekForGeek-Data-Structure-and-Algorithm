from cll_node import Node


def create_circular_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    current.next = head
    return head


def exchange_first_last(head):
    if head is None or head.next == head:
        return head
    if head.next.next == head:
        second = head.next
        second_next = second.next
        head.next = second_next
        second.next = head
        return second
    first = head
    second = head.next
    current = head
    while current.next != head:
        current = current.next
    last = current
    current = head
    while current.next != last:
        current = current.next
    prev_last = current
    last.next = second
    prev_last.next = first
    first.next = last
    return last


def display_cll(head):
    if head is None:
        print("Empty list")
        return
    elements = []
    current = head
    while True:
        elements.append(str(current.data))
        current = current.next
        if current == head:
            break
    print(" -> ".join(elements) + " -> (back to head)")


if __name__ == "__main__":
    head = create_circular_linked_list([1, 2, 3, 4, 5])
    print("Original CLL:", end=" ")
    display_cll(head)

    head = exchange_first_last(head)
    print("After exchanging first and last:", end=" ")
    display_cll(head)

    head2 = create_circular_linked_list([10, 20, 30])
    print("\nOriginal CLL:", end=" ")
    display_cll(head2)

    head2 = exchange_first_last(head2)
    print("After exchanging first and last:", end=" ")
    display_cll(head2)

    single = create_circular_linked_list([100])
    print("\nSingle node:", end=" ")
    display_cll(single)
    single = exchange_first_last(single)
    print("After exchange:", end=" ")
    display_cll(single)

    two_nodes = create_circular_linked_list([1, 2])
    print("\nTwo nodes:", end=" ")
    display_cll(two_nodes)
    two_nodes = exchange_first_last(two_nodes)
    print("After exchange:", end=" ")
    display_cll(two_nodes)
