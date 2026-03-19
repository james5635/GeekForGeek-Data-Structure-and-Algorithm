from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head


def linked_list_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result


def reverse_k_group(head, k):
    if not head or k <= 1:
        return head

    dummy = Node(0)
    dummy.next = head
    prev_group = dummy

    while True:
        dq = deque()
        curr = prev_group.next

        for _ in range(k):
            if not curr:
                break
            dq.append(curr)
            curr = curr.next

        if len(dq) < k:
            break

        last_node = None
        while dq:
            node = dq.pop()
            if last_node is None:
                prev_group.next = node
            else:
                last_node.next = node
            last_node = node

        last_node.next = curr
        prev_group = last_node

    return dummy.next


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5, 6])
    result = reverse_k_group(head, 3)
    print(linked_list_to_list(result))

    head = build_linked_list([1, 2, 3, 4, 5])
    result = reverse_k_group(head, 3)
    print(linked_list_to_list(result))

    head = build_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    result = reverse_k_group(head, 3)
    print(linked_list_to_list(result))

    head = build_linked_list([1, 2])
    result = reverse_k_group(head, 3)
    print(linked_list_to_list(result))

    head = build_linked_list([1, 2, 3, 4])
    result = reverse_k_group(head, 2)
    print(linked_list_to_list(result))

    head = build_linked_list([1])
    result = reverse_k_group(head, 1)
    print(linked_list_to_list(result))
