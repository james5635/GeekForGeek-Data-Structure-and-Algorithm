from linked_list import LinkedList


def search_recursive(head, key):
    if head is None:
        return -1
    if head.data == key:
        return 0
    result = search_recursive(head.next, key)
    return result + 1 if result != -1 else -1


if __name__ == "__main__":
    ll = LinkedList()
    for i in [10, 20, 30, 40, 50]:
        ll.append(i)

    print(f"Element 30 found at index: {search_recursive(ll.head, 30)}")
    print(f"Element 25 found at index: {search_recursive(ll.head, 25)}")
    print(f"Element 10 found at index: {search_recursive(ll.head, 10)}")
