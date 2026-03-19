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


def reorder_list(head):
    if not head:
        return head

    dq = deque()
    curr = head
    while curr:
        dq.append(curr)
        curr = curr.next

    head = dq.popleft()
    curr = head
    use_back = True

    while dq:
        if use_back:
            node = dq.pop()
        else:
            node = dq.popleft()
        curr.next = node
        curr = node
        use_back = not use_back

    curr.next = None
    return head


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    result = reorder_list(head)
    print(linked_list_to_list(result))

    head = build_linked_list([1, 2, 3, 4])
    result = reorder_list(head)
    print(linked_list_to_list(result))

    head = build_linked_list([1])
    result = reorder_list(head)
    print(linked_list_to_list(result))

    head = build_linked_list([])
    result = reorder_list(head)
    print(linked_list_to_list(result))

    head = build_linked_list([1, 2, 3, 4, 5, 6, 7])
    result = reorder_list(head)
    print(linked_list_to_list(result))
