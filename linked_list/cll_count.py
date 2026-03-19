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


def count_nodes(head):
    if head is None:
        return 0
    count = 1
    current = head
    while current.next != head:
        count += 1
        current = current.next
    return count


if __name__ == "__main__":
    head1 = create_circular_linked_list([1, 2, 3, 4, 5])
    print(f"CLL with 5 nodes: {count_nodes(head1)}")

    head2 = create_circular_linked_list([10, 20])
    print(f"CLL with 2 nodes: {count_nodes(head2)}")

    head3 = create_circular_linked_list([100])
    print(f"CLL with 1 node: {count_nodes(head3)}")

    head4 = create_circular_linked_list([])
    print(f"Empty CLL: {count_nodes(head4)}")

    head5 = create_circular_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"CLL with 10 nodes: {count_nodes(head5)}")
