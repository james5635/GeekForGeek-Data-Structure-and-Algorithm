from dll_node import DLLNode


def pairs_with_sum(head, target_sum):
    pairs = []
    if head is None:
        return pairs

    first = head
    last = head

    while last.next:
        last = last.next

    while first and last and first != last and first.prev != last:
        current_sum = first.data + last.data

        if current_sum == target_sum:
            pairs.append((first.data, last.data))
            first = first.next
            last = last.prev
        elif current_sum < target_sum:
            first = first.next
        else:
            last = last.prev

    return pairs


def display_list(head):
    elements = []
    current = head
    while current:
        elements.append(str(current.data))
        current = current.next
    print(" <-> ".join(elements) if elements else "Empty list")


def create_list(values):
    if not values:
        return None
    head = DLLNode(values[0])
    current = head
    for val in values[1:]:
        current.next = DLLNode(val)
        current.next.prev = current
        current = current.next
    return head


if __name__ == "__main__":
    head = create_list([1, 2, 3, 4, 5, 6])

    print("DLL: ", end="")
    display_list(head)

    pairs = pairs_with_sum(head, 7)
    print(f"\nPairs with sum 7: {pairs}")

    pairs = pairs_with_sum(head, 5)
    print(f"Pairs with sum 5: {pairs}")

    head = create_list([1, 2, 3, 4, 5])
    print("\nDLL: ", end="")
    display_list(head)

    pairs = pairs_with_sum(head, 6)
    print(f"Pairs with sum 6: {pairs}")
