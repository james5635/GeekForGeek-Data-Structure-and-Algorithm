from dll_node import DLLNode


def get_length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count


def get_length_recursive(head):
    if head is None:
        return 0
    return 1 + get_length_recursive(head.next)


if __name__ == "__main__":
    head = DLLNode(10)
    head.next = DLLNode(20)
    head.next.prev = head
    head.next.next = DLLNode(30)
    head.next.next.prev = head.next
    head.next.next.next = DLLNode(40)
    head.next.next.next.prev = head.next.next

    print(f"Iterative length: {get_length(head)}")
    print(f"Recursive length: {get_length_recursive(head)}")
