"""
Sort Numbers Stored on Different Machines

Problem Description:
    Given n machines in the form of linked lists. Each machine contains
    some numbers in sorted form. The amount of numbers each machine has
    is not fixed. Output the numbers from all machines in sorted non-decreasing form.

Example:
    Input: Machine 1: [30, 40, 50]
           Machine 2: [35, 45]
           Machine 3: [10, 60, 70, 80, 100]
    Output: [10, 30, 35, 40, 45, 50, 60, 70, 80, 100]

Time Complexity: O(N log k) - Where N is total elements, k is number of machines
Space Complexity: O(k) - For the min-heap
"""

import heapq
from typing import List, Optional


class ListNode:
    """Node for linked list."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        """For heap comparison."""
        return self.val < other.val


def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists using a min-heap.

    Args:
        lists: List of head nodes of sorted linked lists

    Returns:
        Head of the merged sorted linked list
    """
    # Min heap to store (value, list_index, node)
    min_heap = []

    # Push the first node of each list into the heap
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))

    # Dummy head for result list
    dummy = ListNode(0)
    current = dummy

    # Process until heap is empty
    while min_heap:
        val, idx, node = heapq.heappop(min_heap)

        # Add the smallest element to result
        current.next = ListNode(val)
        current = current.next

        # Push next node from the same list if exists
        if node.next:
            heapq.heappush(min_heap, (node.next.val, idx, node.next))

    return dummy.next


def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Create a linked list from an array."""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def linked_list_to_array(head: Optional[ListNode]) -> List[int]:
    """Convert linked list to array."""
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


if __name__ == "__main__":
    # Test Case 1: Basic case
    machines = [[30, 40, 50], [35, 45], [10, 60, 70, 80, 100]]
    print("Test 1:")
    print("Machines:", machines)
    lists = [create_linked_list(m) for m in machines]
    merged = merge_k_sorted_lists(lists)
    result = linked_list_to_array(merged)
    print(f"Merged: {result}")
    print()

    # Test Case 2: Different sizes
    machines = [[1, 5, 10], [35, 45], [30, 90, 130]]
    print("Test 2:")
    print("Machines:", machines)
    lists = [create_linked_list(m) for m in machines]
    merged = merge_k_sorted_lists(lists)
    result = linked_list_to_array(merged)
    print(f"Merged: {result}")
    print()

    # Test Case 3: Single machine
    machines = [[1, 2, 3, 4, 5]]
    print("Test 3:")
    print("Machines:", machines)
    lists = [create_linked_list(m) for m in machines]
    merged = merge_k_sorted_lists(lists)
    result = linked_list_to_array(merged)
    print(f"Merged: {result}")
    print()

    # Test Case 4: Empty machines
    machines = [[], [1, 2, 3], []]
    print("Test 4:")
    print("Machines:", machines)
    lists = [create_linked_list(m) for m in machines]
    merged = merge_k_sorted_lists(lists)
    result = linked_list_to_array(merged)
    print(f"Merged: {result}")
    print()

    # Test Case 5: All single element machines
    machines = [[5], [1], [3], [2], [4]]
    print("Test 5:")
    print("Machines:", machines)
    lists = [create_linked_list(m) for m in machines]
    merged = merge_k_sorted_lists(lists)
    result = linked_list_to_array(merged)
    print(f"Merged: {result}")
    print()

    # Test Case 6: With negative numbers
    machines = [[-10, 0, 10], [-5, 5], [-20, 20]]
    print("Test 6:")
    print("Machines:", machines)
    lists = [create_linked_list(m) for m in machines]
    merged = merge_k_sorted_lists(lists)
    result = linked_list_to_array(merged)
    print(f"Merged: {result}")
