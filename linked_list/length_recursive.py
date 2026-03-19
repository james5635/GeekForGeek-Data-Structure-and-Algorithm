from linked_list import LinkedList


def length_recursive(head):
    if head is None:
        return 0
    return 1 + length_recursive(head.next)


if __name__ == "__main__":
    ll = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        ll.append(i)

    print(f"Length of list: {length_recursive(ll.head)}")

    ll2 = LinkedList()
    print(f"Empty list length: {length_recursive(ll2.head)}")
