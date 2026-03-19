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


def traverse_cll(head):
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
    head = create_circular_linked_list([1, 2, 3, 4, 5])
    print("Circular Linked List:", end=" ")
    traverse_cll(head)

    head2 = create_circular_linked_list([10, 20, 30])
    print("Another Circular Linked List:", end=" ")
    traverse_cll(head2)

    head3 = create_circular_linked_list([])
    print("Empty List:", end=" ")
    traverse_cll(head3)

    head4 = create_circular_linked_list([100])
    print("Single Node Circular List:", end=" ")
    traverse_cll(head4)
