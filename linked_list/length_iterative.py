from linked_list import LinkedList


def length_iterative(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count


if __name__ == "__main__":
    ll = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        ll.append(i)

    print(f"Length of list: {length_iterative(ll.head)}")

    ll2 = LinkedList()
    print(f"Empty list length: {length_iterative(ll2.head)}")
