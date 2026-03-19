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


def delete_node(head, key):
    if head is None:
        return None
    if head.data == key:
        if head.next == head:
            return None
        current = head
        while current.next != head:
            current = current.next
        current.next = head.next
        return current.next
    current = head
    while current.next != head and current.next.data != key:
        current = current.next
    if current.next == head:
        return head
    current.next = current.next.next
    return head


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

    head = delete_node(head, 3)
    print("After deleting 3:", end=" ")
    display_cll(head)

    head = delete_node(head, 1)
    print("After deleting 1:", end=" ")
    display_cll(head)

    head = delete_node(head, 5)
    print("After deleting 5:", end=" ")
    display_cll(head)

    head = delete_node(head, 2)
    print("After deleting 2:", end=" ")
    display_cll(head)

    head = delete_node(head, 100)
    print("After deleting 100 (not found):", end=" ")
    display_cll(head)

    single = create_circular_linked_list([10])
    print("Single node:", end=" ")
    display_cll(single)
    single = delete_node(single, 10)
    print("After deleting single node:", end=" ")
    display_cll(single)
