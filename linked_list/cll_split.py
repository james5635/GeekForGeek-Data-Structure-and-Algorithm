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


def split_cll(head):
    if head is None:
        return None, None
    if head.next == head:
        return head, None
    slow = head
    fast = head
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next
    if fast.next.next == head:
        fast = fast.next
    first_head = head
    second_head = slow.next
    slow.next = first_head
    fast.next = second_head
    return first_head, second_head


def display_cll(head):
    if head is None:
        print("Empty list")
        return []
    elements = []
    current = head
    while True:
        elements.append(str(current.data))
        current = current.next
        if current == head:
            break
    print(" -> ".join(elements) + " -> (back to head)")
    return elements


if __name__ == "__main__":
    head = create_circular_linked_list([1, 2, 3, 4, 5, 6])
    print("Original CLL:", end=" ")
    display_cll(head)

    first, second = split_cll(head)
    print("First half:", end=" ")
    display_cll(first)
    print("Second half:", end=" ")
    display_cll(second)

    head2 = create_circular_linked_list([1, 2, 3, 4, 5])
    print("\nOriginal CLL (odd):", end=" ")
    display_cll(head2)

    first2, second2 = split_cll(head2)
    print("First half:", end=" ")
    display_cll(first2)
    print("Second half:", end=" ")
    display_cll(second2)

    head3 = create_circular_linked_list([1, 2])
    print("\nOriginal CLL (2 nodes):", end=" ")
    display_cll(head3)

    first3, second3 = split_cll(head3)
    print("First half:", end=" ")
    display_cll(first3)
    print("Second half:", end=" ")
    display_cll(second3)

    head4 = create_circular_linked_list([1])
    print("\nOriginal CLL (1 node):", end=" ")
    display_cll(head4)

    first4, second4 = split_cll(head4)
    print("First half:", end=" ")
    display_cll(first4)
    print("Second half:", end=" ")
    display_cll(second4)
