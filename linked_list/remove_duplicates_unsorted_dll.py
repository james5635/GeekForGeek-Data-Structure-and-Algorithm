from dll_node import DLLNode


def remove_duplicates_unsorted(head):
    if head is None:
        return head

    seen = set()
    current = head
    seen.add(current.data)

    while current and current.next:
        if current.next.data in seen:
            duplicate = current.next
            current.next = duplicate.next
            if duplicate.next:
                duplicate.next.prev = current
        else:
            seen.add(current.next.data)
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
    head = create_list([12, 11, 12, 21, 41, 43, 21])

    print("Original unsorted list: ", end="")
    display_list(head)

    head = remove_duplicates_unsorted(head)

    print("After removing duplicates: ", end="")
    display_list(head)

    head = create_list([1, 2, 3, 2, 4, 1, 5])
    print("\nOriginal: ", end="")
    display_list(head)

    head = remove_duplicates_unsorted(head)
    print("After removing duplicates: ", end="")
    display_list(head)
