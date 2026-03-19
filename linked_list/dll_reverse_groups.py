from dll_node import DLLNode


def reverse_in_groups(head, k):
    if head is None or k <= 1:
        return head

    current = head
    new_head = None
    tail_of_prev_group = None

    while current:
        prev_group_tail = tail_of_prev_group
        group_start = current

        i = 0
        while current and i < k:
            i += 1
            current = current.next

        next_group_head = current
        group_end = current.prev if current else None

        current = group_start
        prev_node = None
        count = 0

        while current and count < k:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
            count += 1

        if prev_group_tail:
            prev_group_tail.next = prev_node
            prev_node.prev = prev_group_tail
        else:
            new_head = prev_node

        if group_end:
            group_end.next = next_group_head
            if next_group_head:
                next_group_head.prev = group_end

        tail_of_prev_group = group_end if group_end else group_start
        current = next_group_head

    return new_head


def display_list(head):
    elements = []
    current = head
    while current:
        elements.append(str(current.data))
        current = current.next
    print(" <-> ".join(elements) if elements else "Empty list")


def create_list(values):
    if not values:
        return None
    head = DLLNode(values[0])
    current = head
    for val in values[1:]:
        current.next = DLLNode(val)
        current.next.prev = current
        current = current.next
    return head


if __name__ == "__main__":
    head = create_list([1, 2, 3, 4, 5, 6, 7, 8])

    print("Original: ", end="")
    display_list(head)

    head = reverse_in_groups(head, 3)

    print("Reversed in groups of 3: ", end="")
    display_list(head)

    head = create_list([1, 2, 3, 4, 5])
    print("\nOriginal: ", end="")
    display_list(head)

    head = reverse_in_groups(head, 2)
    print("Reversed in groups of 2: ", end="")
    display_list(head)
