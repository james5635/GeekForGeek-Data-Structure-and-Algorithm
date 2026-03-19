from dll_node import DLLNode


def rotate_dll(head, n):
    if head is None or n <= 0:
        return head

    current = head
    count = 1

    while count < n and current:
        current = current.next
        count += 1

    if current is None or current.next is None:
        return head

    nth_node = current
    new_head = current.next
    new_head.prev = None

    tail = current
    while tail.next:
        tail = tail.next

    tail.next = head
    head.prev = tail

    nth_node.next = None

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

    print("Original list: ", end="")
    display_list(head)

    head = rotate_dll(head, 3)
    print("After rotating by 3: ", end="")
    display_list(head)

    head = rotate_dll(head, 2)
    print("After rotating by 2: ", end="")
    display_list(head)

    head = create_list([10, 20, 30, 40, 50])
    print("\nOriginal list: ", end="")
    display_list(head)

    head = rotate_dll(head, 5)
    print("After rotating by 5 (same as length): ", end="")
    display_list(head)
