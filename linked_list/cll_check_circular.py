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


def create_singly_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


def is_circular(head):
    if head is None or head.next is None:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    cll = create_circular_linked_list([1, 2, 3, 4, 5])
    print(f"Circular Linked List: {is_circular(cll)}")

    sll = create_singly_linked_list([1, 2, 3, 4, 5])
    print(f"Singly Linked List: {is_circular(sll)}")

    single_node = Node(10)
    single_node.next = single_node
    print(f"Single node (pointing to itself): {is_circular(single_node)}")

    single_node_regular = Node(10)
    print(f"Single node (not pointing to itself): {is_circular(single_node_regular)}")

    empty_list = None
    print(f"Empty list: {is_circular(empty_list)}")
