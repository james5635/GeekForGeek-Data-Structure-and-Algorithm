"""
Rearrange Linked List in Alternate First-Last Order

Approach:
1. Collect all values from linked list
2. Sort values in descending order
3. Use deque: take from front and back alternately to create zigzag pattern
4. Rebuild linked list with rearranged values

Pattern: smallest, largest, 2nd smallest, 2nd largest, ...

Time Complexity: O(n log n) for sorting
Space Complexity: O(n) for deque storage
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        result = []
        curr = self.head
        while curr:
            result.append(str(curr.data))
            curr = curr.next
        return " -> ".join(result)

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result


def rearrange_alternate_first_last(head):
    """
    Rearrange linked list: smallest, largest, 2nd smallest, 2nd largest, ...
    """
    from collections import deque

    if not head or not head.next:
        return head

    values = []
    curr = head
    while curr:
        values.append(curr.data)
        curr = curr.next

    values.sort()
    dq = deque()

    left, right = 0, len(values) - 1
    take_from_left = True

    while left <= right:
        if take_from_left:
            dq.append(values[left])
            left += 1
        else:
            dq.append(values[right])
            right -= 1
        take_from_left = not take_from_left

    curr = head
    while curr:
        curr.data = dq.popleft()
        curr = curr.next

    return head


def rearrange_alternate_first_last_v2(head):
    """
    Alternative: 1st, last, 2nd, 2nd-last pattern keeping original order.
    """
    from collections import deque

    if not head:
        return None

    values = []
    curr = head
    while curr:
        values.append(curr.data)
        curr = curr.next

    n = len(values)
    dq = deque()

    i, j = 0, n - 1
    take_from_i = True

    while i <= j:
        if take_from_i:
            dq.append(values[i])
            i += 1
        else:
            dq.append(values[j])
            j -= 1
        take_from_i = not take_from_i

    curr = head
    while curr:
        curr.data = dq.popleft()
        curr = curr.next

    return head


def main():
    print("=== Rearrange Linked List Alternate First-Last ===\n")

    test_cases = [
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2], [1, 2]),
        ([1], [1]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    ]

    for input_vals, expected in test_cases:
        ll = LinkedList()
        for val in input_vals:
            ll.append(val)

        print(f"Input: {ll.display()}")
        rearrange_alternate_first_last(ll.head)
        result = ll.to_list()
        status = "PASS" if result == expected else "FAIL"
        print(f"Output: {' -> '.join(map(str, result))}")
        print(f"Expected: {' -> '.join(map(str, expected))}")
        print(f"Status: {status}\n")


if __name__ == "__main__":
    main()
