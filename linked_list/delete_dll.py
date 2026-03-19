from dll_node import DLLNode


def delete_node(head, node):
    if head is None or node is None:
        return head

    if node.prev:
        node.prev.next = node.next
    else:
        head = node.next
        if head:
            head.prev = None

    if node.next:
        node.next.prev = node.prev

    return head


def delete_at_position(head, position):
    if head is None:
        return head

    if position <= 0:
        return head

    current = head
    for _ in range(position - 1):
        if current is None:
            return head
        current = current.next

    if current is None:
        return head

    return delete_node(head, current)


def delete_by_value(head, value):
    current = head
    while current:
        if current.data == value:
            temp = current
            head = delete_node(head, current)
            current = temp.next
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
    head = create_list([10, 20, 30, 40, 50])

    print("Original: ", end="")
    display_list(head)

    node_to_delete = head.next.next
    head = delete_node(head, node_to_delete)
    print("After deleting node with data 30: ", end="")
    display_list(head)

    head = create_list([10, 20, 30, 40, 50])
    print("\nOriginal: ", end="")
    display_list(head)

    head = delete_at_position(head, 2)
    print("After deleting at position 2: ", end="")
    display_list(head)

    head = delete_by_value(head, 20)
    print("After deleting value 20: ", end="")
    display_list(head)
