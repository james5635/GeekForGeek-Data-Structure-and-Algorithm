from linked_list import LinkedList


def get_nth_node(head, index):
    if index < 0:
        return None
    current = head
    count = 0
    while current:
        if count == index:
            return current.data
        count += 1
        current = current.next
    return None


if __name__ == "__main__":
    ll = LinkedList()
    for i in [10, 20, 30, 40, 50]:
        ll.append(i)

    print(f"0th node: {get_nth_node(ll.head, 0)}")
    print(f"2nd node: {get_nth_node(ll.head, 2)}")
    print(f"4th node: {get_nth_node(ll.head, 4)}")
    print(f"10th node: {get_nth_node(ll.head, 10)}")
