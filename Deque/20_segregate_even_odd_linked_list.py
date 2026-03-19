from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def segregate_even_odd(head):
    dq = deque()
    even_stack = deque()
    odd_stack = deque()
    curr = head
    while curr:
        if curr.val % 2 == 0:
            even_stack.append(curr)
        else:
            odd_stack.append(curr)
        curr = curr.next
    while even_stack:
        dq.appendleft(even_stack.pop())
    while odd_stack:
        dq.append(odd_stack.pop())
    if not dq:
        return None
    head = dq[0]
    for i in range(len(dq) - 1):
        dq[i].next = dq[i + 1]
    dq[-1].next = None
    return head


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def list_to_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head


if __name__ == "__main__":
    head = list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = segregate_even_odd(head)
    assert linked_list_to_list(result) == [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]

    head = list_to_linked_list([1, 3, 5])
    result = segregate_even_odd(head)
    assert linked_list_to_list(result) == [1, 3, 5]

    head = list_to_linked_list([2, 4, 6])
    result = segregate_even_odd(head)
    assert linked_list_to_list(result) == [2, 4, 6]

    head = list_to_linked_list([5])
    result = segregate_even_odd(head)
    assert linked_list_to_list(result) == [5]

    head = list_to_linked_list([])
    result = segregate_even_odd(head)
    assert linked_list_to_list(result) == []

    print("All tests passed!")
