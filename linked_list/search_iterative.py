from linked_list import LinkedList


def search_iterative(head, key):
    position = 0
    current = head
    while current:
        if current.data == key:
            return position
        position += 1
        current = current.next
    return -1


if __name__ == "__main__":
    ll = LinkedList()
    for i in [10, 20, 30, 40, 50]:
        ll.append(i)

    print(f"Element 30 found at index: {search_iterative(ll.head, 30)}")
    print(f"Element 25 found at index: {search_iterative(ll.head, 25)}")
    print(f"Element 10 found at index: {search_iterative(ll.head, 10)}")
