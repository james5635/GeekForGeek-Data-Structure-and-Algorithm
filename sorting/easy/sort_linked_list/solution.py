"""
Sort a Singly Linked List

Problem Description:
    Given a singly linked list, sort it in non-decreasing order.

Example:
    Input:  10 -> 30 -> 20 -> 5
    Output: 5 -> 10 -> 20 -> 30

Time Complexity: O(n log n) - Merge sort approach
Space Complexity: O(log n) - Due to recursion stack
"""

from typing import Optional


class ListNode:
    """Node for singly linked list."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Sort a singly linked list using merge sort.

    Args:
        head: Head of the linked list

    Returns:
        Head of the sorted linked list
    """
    # Base cases
    if not head or not head.next:
        return head

    # Split the list into two halves
    mid = get_middle(head)
    mid_next = mid.next
    mid.next = None  # Split the list

    # Recursively sort both halves
    left = sort_list(head)
    right = sort_list(mid_next)

    # Merge the sorted halves
    return merge(left, right)


def get_middle(head: ListNode) -> ListNode:
    """
    Find the middle node of a linked list using slow/fast pointer technique.

    Args:
        head: Head of the linked list

    Returns:
        Middle node of the list
    """
    if not head:
        return head

    slow = head
    fast = head

    # Move fast pointer 2 steps and slow pointer 1 step
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists.

    Args:
        left: Head of first sorted list
        right: Head of second sorted list

    Returns:
        Head of merged sorted list
    """
    dummy = ListNode(0)
    tail = dummy

    # Compare and merge
    while left and right:
        if left.val <= right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    # Attach remaining nodes
    if left:
        tail.next = left
    if right:
        tail.next = right

    return dummy.next


def create_linked_list(arr: list) -> Optional[ListNode]:
    """Create a linked list from an array."""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def linked_list_to_array(head: Optional[ListNode]) -> list:
    """Convert linked list to array."""
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


def print_list(head: Optional[ListNode], name: str = "List"):
    """Print a linked list."""
    arr = linked_list_to_array(head)
    print(f"{name}: {' -> '.join(map(str, arr)) if arr else 'Empty'}")


if __name__ == "__main__":
    # Test Case 1: Basic unsorted list
    arr = [10, 30, 20, 5]
    print("Test 1:")
    head = create_linked_list(arr)
    print_list(head, "Before")
    head = sort_list(head)
    print_list(head, "After ")
    print()

    # Test Case 2: Already sorted
    arr = [1, 2, 3, 4, 5]
    print("Test 2:")
    head = create_linked_list(arr)
    print_list(head, "Before")
    head = sort_list(head)
    print_list(head, "After ")
    print()

    # Test Case 3: Reverse sorted
    arr = [5, 4, 3, 2, 1]
    print("Test 3:")
    head = create_linked_list(arr)
    print_list(head, "Before")
    head = sort_list(head)
    print_list(head, "After ")
    print()

    # Test Case 4: Single element
    arr = [42]
    print("Test 4:")
    head = create_linked_list(arr)
    print_list(head, "Before")
    head = sort_list(head)
    print_list(head, "After ")
    print()

    # Test Case 5: Empty list
    arr = []
    print("Test 5:")
    head = create_linked_list(arr)
    print_list(head, "Before")
    head = sort_list(head)
    print_list(head, "After ")
    print()

    # Test Case 6: With duplicates
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Test 6:")
    head = create_linked_list(arr)
    print_list(head, "Before")
    head = sort_list(head)
    print_list(head, "After ")
    print()

    # Test Case 7: Two elements
    arr = [2, 1]
    print("Test 7:")
    head = create_linked_list(arr)
    print_list(head, "Before")
    head = sort_list(head)
    print_list(head, "After ")
