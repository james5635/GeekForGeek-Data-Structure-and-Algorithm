from cll_node import Node


def create_singly_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


def singly_to_circular(head):
    if head is None:
        return None
    current = head
    while current.next:
        current = current.next
    current.next = head
    return head


def display_singly(head):
    if head is None:
        print("Empty list")
        return
    elements = []
    current = head
    while current:
        elements.append(str(current.data))
        current = current.next
    print(" -> ".join(elements))


def display_circular(head):
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
    sll = create_singly_linked_list([1, 2, 3, 4, 5])
    print("Singly Linked List:", end=" ")
    display_singly(sll)

    cll = singly_to_circular(sll)
    print("Converted to Circular:", end=" ")
    display_circular(cll)

    sll2 = create_singly_linked_list([10, 20, 30])
    print("\nAnother Singly Linked List:", end=" ")
    display_singly(sll2)

    cll2 = singly_to_circular(sll2)
    print("Converted to Circular:", end=" ")
    display_circular(cll2)

    empty = singly_to_circular(None)
    print("\nEmpty list conversion:", end=" ")
    display_circular(empty)

    single = create_singly_linked_list([100])
    print("Single node singly:", end=" ")
    display_singly(single)

    single_circ = singly_to_circular(single)
    print("Single node circular:", end=" ")
    display_circular(single_circ)
