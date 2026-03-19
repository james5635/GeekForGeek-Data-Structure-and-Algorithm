from dll_node import DLLNode


def reverse_dll(head):
    if head is None:
        return None

    current = head
    new_tail = head

    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev

    if new_tail:
        new_tail.prev = None

    return temp.prev if temp else head


def reverse_dll_v2(head):
    if head is None:
        return None

    current = head
    prev_node = None

    while current:
        next_node = current.next
        current.next = prev_node
        current.prev = next_node
        prev_node = current
        current = next_node

    return prev_node


def display_list(head):
    elements = []
    current = head
    while current:
        elements.append(str(current.data))
        current = current.next
    print(" <-> ".join(elements) if elements else "Empty list")


if __name__ == "__main__":
    head = DLLNode(10)
    head.next = DLLNode(20)
    head.next.prev = head
    head.next.next = DLLNode(30)
    head.next.next.prev = head.next
    head.next.next.next = DLLNode(40)
    head.next.next.next.prev = head.next.next

    print("Original: ", end="")
    display_list(head)

    head = reverse_dll_v2(head)

    print("Reversed: ", end="")
    display_list(head)
