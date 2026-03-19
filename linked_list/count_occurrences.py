from linked_list import LinkedList


def count_occurrences(head, key):
    count = 0
    current = head
    while current:
        if current.data == key:
            count += 1
        current = current.next
    return count


if __name__ == "__main__":
    ll = LinkedList()
    for i in [1, 2, 3, 2, 4, 2, 5]:
        ll.append(i)

    print(f"Count of 2: {count_occurrences(ll.head, 2)}")
    print(f"Count of 1: {count_occurrences(ll.head, 1)}")
    print(f"Count of 6: {count_occurrences(ll.head, 6)}")
