from dll_node import DLLNode


def insert_sorted(head, data):
    new_node = DLLNode(data)

    if head is None:
        return new_node

    if data <= head.data:
        new_node.next = head
        head.prev = new_node
        return new_node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    if current.next:
        current.next.prev = new_node
    current.next = new_node
    new_node.prev = current

    return head


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

    print("Original sorted list: ", end="")
    display_list(head)

    head = insert_sorted(head, 25)
    print("After inserting 25: ", end="")
    display_list(head)

    head = insert_sorted(head, 5)
    print("After inserting 5: ", end="")
    display_list(head)

    head = insert_sorted(head, 40)
    print("After inserting 40: ", end="")
    display_list(head)
