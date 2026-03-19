from dll_node import DLLNode


def merge_sorted_dll(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        head1.next = merge_sorted_dll(head1.next, head2)
        if head1.next:
            head1.next.prev = head1
        head1.prev = None
        return head1
    else:
        head2.next = merge_sorted_dll(head1, head2.next)
        if head2.next:
            head2.next.prev = head2
        head2.prev = None
        return head2


def merge_sorted_dll_iterative(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    dummy = DLLNode(0)
    current = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1.prev = current
            head1 = head1.next
        else:
            current.next = head2
            head2.prev = current
            head2 = head2.next
        current = current.next

    if head1:
        current.next = head1
        head1.prev = current
    else:
        current.next = head2
        if head2:
            head2.prev = current

    result = dummy.next
    if result:
        result.prev = None
    return result


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
    head1 = create_list([1, 3, 5, 7, 9])
    head2 = create_list([2, 4, 6, 8, 10])

    print("First sorted list: ", end="")
    display_list(head1)

    print("Second sorted list: ", end="")
    display_list(head2)

    merged = merge_sorted_dll(head1, head2)
    print("Merged list: ", end="")
    display_list(merged)

    head1 = create_list([1, 2, 3])
    head2 = create_list([4, 5, 6])
    print("\nFirst list: ", end="")
    display_list(head1)
    print("Second list: ", end="")
    display_list(head2)

    merged = merge_sorted_dll(head1, head2)
    print("Merged list: ", end="")
    display_list(merged)
