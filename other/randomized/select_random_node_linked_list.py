import random


class ListNode:
    """Node in a singly linked list."""

    def __init__(self, val: int, next_node: "ListNode | None" = None):
        self.val = val
        self.next = next_node


def select_random_node(head: ListNode) -> int:
    """Select a random node from a singly linked list with equal probability (reservoir sampling)."""
    result = head.val
    current = head.next
    i = 2

    while current:
        if random.randint(1, i) == 1:
            result = current.val
        current = current.next
        i += 1

    return result


if __name__ == "__main__":
    values = [10, 20, 30, 40, 50]
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next

    counts = {v: 0 for v in values}
    for _ in range(10000):
        selected = select_random_node(head)
        counts[selected] += 1

    print("Linked list:", values)
    print("Selection distribution:")
    for v in values:
        print(f"  {v}: {counts[v]:4d} ({counts[v] / 100:.2f}%)")
