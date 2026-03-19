"""
Merge K Sorted Linked Lists
URL: https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
Source: GeeksforGeeks

Problem:
Given k sorted linked lists of different sizes, merge them into a single
list while maintaining their sorted order.

Examples:
Input:
List 1: 1 -> 3 -> 5 -> 7
List 2: 2 -> 4 -> 6 -> 8
List 3: 0 -> 9 -> 10 -> 11
Output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11

Approaches:
1. Naive - Merge one by one: O(n*k²)
2. Repeated Min Selection: O(n*k²) but O(1) space
3. Min Heap: O(n*k*log k) - Best for unequal sized lists
4. Divide and Conquer: O(n*k*log k) - Best for equal sized lists

where n is average size of lists, k is number of lists
"""

import heapq


class ListNode:
    """
    Node class for linked list.
    """

    def __init__(self, x):
        self.data = x
        self.next = None

    def __repr__(self):
        return f"ListNode({self.data})"

    def __str__(self):
        values = []
        current = self
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values)


def merge_two_lists(head1, head2):
    """
    Merge two sorted linked lists.

    Args:
        head1: Head of first sorted linked list
        head2: Head of second sorted linked list

    Returns:
        Head of merged sorted linked list
    """
    dummy = ListNode(-1)
    current = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1:
        current.next = head1
    else:
        current.next = head2

    return dummy.next


def merge_k_lists_one_by_one(arr):
    """
    Merge one by one approach.

    Time: O(n*k²)
    Space: O(1)
    """
    result = None

    for node in arr:
        result = merge_two_lists(result, node)

    return result


def get_min_node(arr):
    """
    Get the node with minimum value from array of heads.

    Returns:
        Tuple of (minimum node, index of list it came from)
    """
    mini = None
    index = -1

    for i in range(len(arr)):
        if arr[i] is None:
            continue

        if mini is None or arr[i].data < mini.data:
            index = i
            mini = arr[i]

    if index != -1:
        arr[index] = arr[index].next

    return mini


def merge_k_lists_repeated_min(arr):
    """
    Repeatedly select minimum - O(n*k²) time, O(1) space.
    """
    dummy = ListNode(-1)
    tail = dummy

    while True:
        mini = get_min_node(arr)
        if mini is None:
            break
        tail.next = mini
        tail = mini

    return dummy.next


def merge_k_lists_heap(arr):
    """
    Min Heap approach - works better for unequal sized lists.

    Algorithm:
    1. Insert first node of each list into min heap
    2. Extract minimum node
    3. Add its next node to heap (if exists)
    4. Repeat until heap is empty

    Time: O(n*k*log k)
    Space: O(k)
    """
    if not arr:
        return None

    heap = []

    for i, node in enumerate(arr):
        if node:
            heapq.heappush(heap, (node.data, i, node))

    dummy = ListNode(-1)
    tail = dummy

    while heap:
        data, list_idx, node = heapq.heappop(heap)
        tail.next = node
        tail = node

        if node.next:
            heapq.heappush(heap, (node.next.data, list_idx, node.next))

    return dummy.next


def merge_k_lists_divide_conquer(arr):
    """
    Divide and Conquer approach - works better for equal sized lists.

    Algorithm:
    1. Divide k lists into two halves
    2. Recursively merge left half
    3. Recursively merge right half
    4. Merge the two results

    Time: O(n*k*log k)
    Space: O(log k) for recursion stack
    """
    if not arr:
        return None

    def merge_helper(lo, hi):
        if lo == hi:
            return arr[lo]

        mid = lo + (hi - lo) // 2

        left = merge_helper(lo, mid)
        right = merge_helper(mid + 1, hi)

        return merge_two_lists(left, right)

    return merge_helper(0, len(arr) - 1)


class HeapNode:
    """
    Custom heap node for linked list merging.
    """

    def __init__(self, node, list_index):
        self.node = node
        self.list_index = list_index

    def __lt__(self, other):
        return self.node.data < other.node.data


def merge_k_lists_optimized(arr):
    """
    Optimized version with custom heap node.
    """
    if not arr:
        return None

    heap = []

    for idx, node in enumerate(arr):
        if node:
            heapq.heappush(heap, HeapNode(node, idx))

    dummy = ListNode(0)
    current = dummy

    while heap:
        heap_node = heapq.heappop(heap)
        current.next = heap_node.node
        current = current.next

        if heap_node.node.next:
            new_node = ListNode(heap_node.node.next.data)
            heapq.heappush(heap, HeapNode(heap_node.node.next, heap_node.list_index))

    return dummy.next


def create_linked_list(values):
    """
    Create linked list from list of values.
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def print_list(node):
    """
    Print linked list in readable format.
    """
    if node is None:
        print("Empty list")
        return

    values = []
    while node:
        values.append(str(node.data))
        node = node.next
    print(" -> ".join(values))


if __name__ == "__main__":
    print("=" * 60)
    print("MERGE K SORTED LINKED LISTS")
    print("=" * 60)

    print("\n" + "-" * 60)
    print("TEST CASE 1: Standard Case")
    print("-" * 60)

    lists = [
        create_linked_list([1, 3, 5, 7]),
        create_linked_list([2, 4, 6, 8]),
        create_linked_list([0, 9, 10, 11]),
    ]

    print("\nInput lists:")
    for i, lst in enumerate(lists):
        print(f"  List {i}: ", end="")
        print_list(lst)

    print("\nUsing merge_k_lists_heap:")
    result1 = merge_k_lists_heap(lists)
    print("  ", end="")
    print_list(result1)

    lists = [
        create_linked_list([1, 3, 5, 7]),
        create_linked_list([2, 4, 6, 8]),
        create_linked_list([0, 9, 10, 11]),
    ]
    print("\nUsing merge_k_lists_divide_conquer:")
    result2 = merge_k_lists_divide_conquer(lists)
    print("  ", end="")
    print_list(result2)

    lists = [
        create_linked_list([1, 3, 5, 7]),
        create_linked_list([2, 4, 6, 8]),
        create_linked_list([0, 9, 10, 11]),
    ]
    print("\nUsing merge_k_lists_one_by_one:")
    result3 = merge_k_lists_one_by_one(lists)
    print("  ", end="")
    print_list(result3)

    print("\n" + "-" * 60)
    print("TEST CASE 2: Different Sized Lists")
    print("-" * 60)

    lists = [
        create_linked_list([1, 4, 7, 10, 15]),
        create_linked_list([2, 5]),
        create_linked_list([3, 6, 9, 12]),
    ]

    print("\nInput lists:")
    for i, lst in enumerate(lists):
        print(f"  List {i}: ", end="")
        print_list(lst)

    result = merge_k_lists_heap(lists)
    print("\nMerged result:")
    print("  ", end="")
    print_list(result)

    print("\n" + "-" * 60)
    print("TEST CASE 3: Empty Lists")
    print("-" * 60)

    lists = [create_linked_list([1]), None, create_linked_list([2])]

    print("\nInput lists:")
    for i, lst in enumerate(lists):
        print(f"  List {i}: ", end="")
        print_list(lst)

    result = merge_k_lists_heap(lists)
    print("\nMerged result:")
    print("  ", end="")
    print_list(result)

    print("\n" + "-" * 60)
    print("TEST CASE 4: Single List")
    print("-" * 60)

    lists = [create_linked_list([1, 2, 3, 4, 5])]

    print("\nInput lists:")
    print("  List 0: ", end="")
    print_list(lists[0])

    result = merge_k_lists_heap(lists)
    print("\nMerged result:")
    print("  ", end="")
    print_list(result)

    print("\n" + "=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)
    print("\n1. Merge One by One:")
    print("   Time:  O(n*k²)")
    print("   Space: O(1)")
    print("\n2. Repeated Min Selection:")
    print("   Time:  O(n*k²)")
    print("   Space: O(1)")
    print("\n3. Min Heap:")
    print("   Time:  O(n*k*log k)")
    print("   Space: O(k)")
    print("\n4. Divide and Conquer:")
    print("   Time:  O(n*k*log k)")
    print("   Space: O(log k)")
    print("\nWhere n = avg size per list, k = number of lists")
