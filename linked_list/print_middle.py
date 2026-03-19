from linked_list import LinkedList


def print_middle(head):
    if head is None:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data


if __name__ == "__main__":
    ll = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        ll.append(i)
    print(f"Middle of [1,2,3,4,5]: {print_middle(ll.head)}")

    ll2 = LinkedList()
    for i in [1, 2, 3, 4, 5, 6]:
        ll2.append(i)
    print(f"Middle of [1,2,3,4,5,6]: {print_middle(ll2.head)}")

    ll3 = LinkedList()
    print(f"Middle of empty list: {print_middle(ll3.head)}")
