"""
Reverse Linked List in groups of given size k
Uses deque for efficient node collection and reversal
"""

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result


def reverse_groups(head, k):
    """
    Reverse linked list in groups of k nodes
    Uses deque to collect nodes for reversal
    Incomplete groups at the end are not reversed
    """
    if not head or k <= 1:
        return head

    dummy = Node(0)
    dummy.next = head
    prev_tail = dummy

    while True:
        group_head = prev_tail.next
        if not group_head:
            break

        dq = deque()
        curr = group_head
        count = 0
        while curr and count < k:
            dq.append(curr)
            curr = curr.next
            count += 1

        if count < k:
            break

        prev_tail.next = None
        new_head = None
        while dq:
            node = dq.popleft()
            if new_head is None:
                new_head = node
                node.next = None
            else:
                node.next = new_head
                new_head = node

        prev_tail.next = new_head
        prev_tail = group_head
        prev_tail.next = curr

    return dummy.next


def main():
    print("=" * 60)
    print("Reverse Linked List in Groups of Size K")
    print("=" * 60)

    print("\n--- Test Case 1 ---")
    head = build_linked_list([1, 2, 3, 4, 5, 6])
    k = 2
    result_head = reverse_groups(head, k)
    result = linked_list_to_list(result_head)
    print(f"Input: 1->2->3->4->5->6, k={k}")
    print(f"Output: {' -> '.join(map(str, result))}")
    print(f"Expected: 2 -> 1 -> 4 -> 3 -> 6 -> 5")
    print(f"Pass: {result == [2, 1, 4, 3, 6, 5]}")

    print("\n--- Test Case 2 ---")
    head = build_linked_list([1, 2, 3, 4, 5, 6])
    k = 4
    result_head = reverse_groups(head, k)
    result = linked_list_to_list(result_head)
    print(f"Input: 1->2->3->4->5->6, k={k}")
    print(f"Output: {' -> '.join(map(str, result))}")
    print(f"Expected: 4 -> 3 -> 2 -> 1 -> 6 -> 5")
    print(f"Pass: {result == [4, 3, 2, 1, 6, 5]}")

    print("\n--- Test Case 3 ---")
    head = build_linked_list([1, 2, 3, 4, 5])
    k = 3
    result_head = reverse_groups(head, k)
    result = linked_list_to_list(result_head)
    print(f"Input: 1->2->3->4->5, k={k}")
    print(f"Output: {' -> '.join(map(str, result))}")
    print(f"Expected: 3 -> 2 -> 1 -> 4 -> 5")
    print(f"Pass: {result == [3, 2, 1, 4, 5]}")

    print("\n--- Test Case 4 ---")
    head = build_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    k = 3
    result_head = reverse_groups(head, k)
    result = linked_list_to_list(result_head)
    print(f"Input: 1->2->3->4->5->6->7->8, k={k}")
    print(f"Output: {' -> '.join(map(str, result))}")
    print(f"Expected: 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7")
    print(f"Pass: {result == [3, 2, 1, 6, 5, 4, 8, 7]}")

    print("\n--- Test Case 5 ---")
    head = build_linked_list([1])
    k = 2
    result_head = reverse_groups(head, k)
    result = linked_list_to_list(result_head)
    print(f"Input: 1, k={k}")
    print(f"Output: {result}")
    print(f"Expected: [1]")
    print(f"Pass: {result == [1]}")


if __name__ == "__main__":
    main()
