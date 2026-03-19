"""
Merge K Sorted Arrays
URL: https://www.geeksforgeeks.org/merge-k-sorted-arrays/
Source: GeeksforGeeks

Problem:
Given a 2D matrix mat[][] where each row is sorted in non-decreasing order,
find a single sorted array that contains all the elements from the matrix.

Examples:
Input: mat[][] = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Approaches:
1. Naive: Concatenate all and sort - O(n log n)
2. Merge Sort: Divide and conquer merge - O(n log k)
3. Min Heap: Optimal for different sized arrays - O(n log k)

where k = number of arrays, n = total elements
"""

import heapq


def merge_arrays_naive(mat):
    """
    Naive approach: Concatenate all and sort.

    Time: O(n log n)
    Space: O(n)
    """
    result = []
    for row in mat:
        result.extend(row)
    result.sort()
    return result


def merge_two_arrays(a, b):
    """
    Merge two sorted arrays into one sorted array.

    Args:
        a: First sorted array
        b: Second sorted array

    Returns:
        Merged sorted array
    """
    i, j = 0, 0
    n1, n2 = len(a), len(b)
    result = []

    while i < n1 and j < n2:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    while i < n1:
        result.append(a[i])
        i += 1

    while j < n2:
        result.append(b[j])
        j += 1

    return result


def merge_arrays_divide_conquer(mat):
    """
    Divide and conquer approach - works better for equal sized arrays.

    Time: O(n log k)
    Space: O(n)

    Args:
        mat: 2D matrix where each row is sorted

    Returns:
        Single sorted array
    """
    k = len(mat)
    if k == 0:
        return []

    def merge(lo, hi):
        if lo == hi:
            return mat[lo]

        mid = (lo + hi) // 2
        left = merge(lo, mid)
        right = merge(mid + 1, hi)

        return merge_two_arrays(left, right)

    return merge(0, k - 1)


def merge_arrays_heap(mat):
    """
    Min Heap approach - works better for different sized arrays.

    Algorithm:
    1. Push first element of each array into min heap
    2. Extract minimum, add to result
    3. Push next element from same array
    4. Repeat until heap is empty

    Time: O(n log k)
    Space: O(k)

    Args:
        mat: 2D matrix where each row is sorted

    Returns:
        Single sorted array
    """
    k = len(mat)
    if k == 0:
        return []

    output = []
    min_heap = []

    for i in range(k):
        if len(mat[i]) > 0:
            heapq.heappush(min_heap, (mat[i][0], i, 0))

    while min_heap:
        val, i, j = heapq.heappop(min_heap)
        output.append(val)

        if j + 1 < len(mat[i]):
            heapq.heappush(min_heap, (mat[i][j + 1], i, j + 1))

    return output


def merge_arrays_heap_with_list(mat):
    """
    Alternative heap implementation with custom Node class.
    """

    class Node:
        def __init__(self, val, row, col):
            self.val = val
            self.row = row
            self.col = col

        def __lt__(self, other):
            return self.val < other.val

    k = len(mat)
    if k == 0:
        return []

    result = []
    heap = []

    for i in range(k):
        if len(mat[i]) > 0:
            heapq.heappush(heap, Node(mat[i][0], i, 0))

    while heap:
        node = heapq.heappop(heap)
        result.append(node.val)

        if node.col + 1 < len(mat[node.row]):
            next_node = Node(mat[node.row][node.col + 1], node.row, node.col + 1)
            heapq.heappush(heap, next_node)

    return result


class MinHeapNode:
    """
    Custom min heap node for merge operations.
    """

    def __init__(self, val, array_index, element_index):
        self.val = val
        self.array_index = array_index
        self.element_index = element_index

    def __repr__(self):
        return f"Node({self.val}, arr={self.array_index}, idx={self.element_index})"

    def __lt__(self, other):
        return self.val < other.val


def merge_k_arrays(arrays):
    """
    Main function to merge k sorted arrays.

    Args:
        arrays: List of sorted arrays

    Returns:
        Single merged sorted array
    """
    if not arrays:
        return []

    k = len(arrays)
    result = []
    heap = []

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, MinHeapNode(arr[0], i, 0))

    while heap:
        node = heapq.heappop(heap)
        result.append(node.val)

        if node.element_index + 1 < len(arrays[node.array_index]):
            next_val = arrays[node.array_index][node.element_index + 1]
            heapq.heappush(
                heap, MinHeapNode(next_val, node.array_index, node.element_index + 1)
            )

    return result


if __name__ == "__main__":
    print("=" * 60)
    print("MERGE K SORTED ARRAYS")
    print("=" * 60)

    test_cases = [
        {
            "mat": [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]],
            "expected": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        },
        {
            "mat": [[1, 2, 3, 4], [2, 2, 3, 4], [5, 5, 6, 6], [7, 8, 9, 9]],
            "expected": [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9],
        },
        {"mat": [[1], [2], [3]], "expected": [1, 2, 3]},
        {
            "mat": [[1, 6, 10], [2, 5, 8], [3, 7, 9]],
            "expected": [1, 2, 3, 5, 6, 7, 8, 9, 10],
        },
    ]

    for i, test in enumerate(test_cases, 1):
        print(f"\n{'=' * 60}")
        print(f"TEST CASE {i}")
        print("=" * 60)
        mat = test["mat"]
        expected = test["expected"]

        print(f"\nInput matrices:")
        for idx, row in enumerate(mat):
            print(f"  Row {idx}: {row}")

        print(f"\nExpected output: {expected}")

        result_naive = merge_arrays_naive(mat)
        result_divide = merge_arrays_divide_conquer(mat)
        result_heap = merge_arrays_heap(mat)
        result_heap_list = merge_arrays_heap_with_list(mat)

        print(f"\nResults:")
        print(f"  Naive:         {result_naive}")
        print(f"  DivideConquer: {result_divide}")
        print(f"  Min Heap:      {result_heap}")
        print(f"  Heap w/Node:   {result_heap_list}")

        status = "PASS" if result_heap == expected else "FAIL"
        print(f"\n  Min Heap Status: {status}")

    print("\n" + "=" * 60)
    print("USING merge_k_arrays FUNCTION")
    print("=" * 60)

    arrays = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]

    print(f"\nInput arrays: {arrays}")
    result = merge_k_arrays(arrays)
    print(f"Merged result: {result}")

    print("\n" + "=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)
    print("\n1. Naive (Concatenate + Sort):")
    print("   Time:  O(n log n)")
    print("   Space: O(n)")
    print("\n2. Divide and Conquer:")
    print("   Time:  O(n log k)")
    print("   Space: O(n)")
    print("\n3. Min Heap:")
    print("   Time:  O(n log k)")
    print("   Space: O(k)")
    print("\nWhere k = number of arrays, n = total elements")
