from linked_list import LinkedList


def nth_node_from_end(head, n):
    if head is None:
        return None
    first = head
    second = head

    for _ in range(n):
        if first is None:
            return None
        first = first.next

    while first:
        first = first.next
        second = second.next

    return second.data if second else None


if __name__ == "__main__":
    ll = LinkedList()
    for i in [10, 20, 30, 40, 50]:
        ll.append(i)

    print(f"1st from end: {nth_node_from_end(ll.head, 1)}")
    print(f"2nd from end: {nth_node_from_end(ll.head, 2)}")
    print(f"5th from end: {nth_node_from_end(ll.head, 5)}")
    print(f"6th from end: {nth_node_from_end(ll.head, 6)}")
