from dll_node import DLLNode


def remove_duplicates_sorted(head):
    if head is None:
        return head

    current = head
    while current and current.next:
        if current.data == current.next.data:
            duplicate = current.next
            current.next = duplicate.next
            if duplicate.next:
                duplicate.next.prev = current
        else:
            current = current.next

    return head


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
    head = create_list([1, 1, 2, 2, 3, 4, 4, 5])

    print("Original sorted list: ", end="")
    display_list(head)

    head = remove_duplicates_sorted(head)

    print("After removing duplicates: ", end="")
    display_list(head)

    head = create_list([1, 1, 1, 1])
    print("\nOriginal: ", end="")
    display_list(head)

    head = remove_duplicates_sorted(head)
    print("After removing duplicates: ", end="")
    display_list(head)
