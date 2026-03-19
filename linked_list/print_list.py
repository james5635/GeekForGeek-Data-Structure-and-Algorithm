from linked_list import LinkedList


def print_list(head):
    if head is None:
        print("Empty list")
        return
    elements = []
    current = head
    while current:
        elements.append(str(current.data))
        current = current.next
    print(" -> ".join(elements))


if __name__ == "__main__":
    ll = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        ll.append(i)

    print("Linked List:", end=" ")
    print_list(ll.head)

    ll2 = LinkedList()
    print("Empty List:", end=" ")
    print_list(ll2.head)
