"""
MO's Algorithm (Query Square Root Decomposition)

Problem Description:
MO's algorithm is used to efficiently answer range queries on a static array.
It works by sorting queries in a specific order to minimize pointer movements,
achieving O((N + Q) * sqrt(N)) complexity for answering Q queries on an array of size N.

This implementation demonstrates range sum queries, but the technique can be
applied to various other query types (XOR, frequency counting, etc.).

Time Complexity:
- Preprocessing: O(1)
- Query Processing: O((N + Q) * sqrt(N)) where Q is number of queries
- Per query amortized: O(sqrt(N))

Space Complexity:
- O(Q) for storing queries and results
- O(1) auxiliary space for processing

Algorithm:
1. Divide array into blocks of size sqrt(N)
2. Sort queries by block index of left endpoint, then by right endpoint
3. Process queries in sorted order, maintaining current range
4. Add/remove elements from current range as pointers move
"""

import math
from typing import List, Tuple


class Query:
    """Represents a query with left, right indices and original index."""

    def __init__(self, left: int, right: int, idx: int):
        self.left = left
        self.right = right
        self.idx = idx


def mo_algorithm(arr: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    """
    Process range sum queries using MO's algorithm.

    Args:
        arr: Input array
        queries: List of (left, right) tuples (0-indexed, inclusive)

    Returns:
        List of results for each query in original order
    """
    n = len(arr)
    q = len(queries)

    if n == 0 or q == 0:
        return []

    # Block size for sqrt decomposition
    block_size = int(math.sqrt(n)) + 1

    # Create query objects
    query_objects = []
    for i, (left, right) in enumerate(queries):
        query_objects.append(Query(left, right, i))

    # Sort queries using MO's ordering
    # Primary: block index of left endpoint
    # Secondary: right endpoint (alternating order for optimization)
    def mo_compare(query: Query) -> Tuple[int, int]:
        block = query.left // block_size
        # Alternate sorting direction for even/odd blocks (Hilbert curve optimization)
        if block % 2 == 0:
            return (block, query.right)
        else:
            return (block, -query.right)

    query_objects.sort(key=mo_compare)

    # Initialize pointers and current sum
    curr_left = 0
    curr_right = -1  # Empty range initially
    curr_sum = 0
    results = [0] * q

    # Process queries in sorted order
    for query in query_objects:
        left, right, idx = query.left, query.right, query.idx

        # Extend range to the right
        while curr_right < right:
            curr_right += 1
            curr_sum += arr[curr_right]

        # Shrink range from the right
        while curr_right > right:
            curr_sum -= arr[curr_right]
            curr_right -= 1

        # Extend range to the left
        while curr_left < left:
            curr_sum -= arr[curr_left]
            curr_left += 1

        # Shrink range from the left
        while curr_left > left:
            curr_left -= 1
            curr_sum += arr[curr_left]

        results[idx] = curr_sum

    return results


def brute_force_range_sum(arr: List[int], left: int, right: int) -> int:
    """Brute force method for verification."""
    return sum(arr[left : right + 1])


if __name__ == "__main__":
    # Test Case 1: Basic functionality
    print("=" * 60)
    print("Test Case 1: Basic Range Sum Queries")
    print("=" * 60)

    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    queries1 = [
        (0, 4),  # Sum of [1,2,3,4,5] = 15
        (2, 6),  # Sum of [3,4,5,6,7] = 25
        (5, 9),  # Sum of [6,7,8,9,10] = 40
        (0, 9),  # Sum of entire array = 55
        (3, 3),  # Single element = 4
    ]

    print(f"Array: {arr1}")
    print(f"Queries: {queries1}")

    results = mo_algorithm(arr1, queries1)

    print("\nResults:")
    for i, (left, right) in enumerate(queries1):
        expected = brute_force_range_sum(arr1, left, right)
        status = "PASS" if results[i] == expected else "FAIL"
        print(
            f"  Query {i + 1} [{left}, {right}]: {results[i]} (expected {expected}) - {status}"
        )

    # Test Case 2: Random array with multiple queries
    print("\n" + "=" * 60)
    print("Test Case 2: Random Array Stress Test")
    print("=" * 60)

    import random

    random.seed(42)

    arr2 = [random.randint(1, 100) for _ in range(100)]
    queries2 = [(random.randint(0, 99), random.randint(i, 99)) for i in range(20)]
    queries2 = [(min(l, r), max(l, r)) for l, r in queries2]

    results2 = mo_algorithm(arr2, queries2)

    all_passed = True
    for i, (left, right) in enumerate(queries2):
        expected = brute_force_range_sum(arr2, left, right)
        if results2[i] != expected:
            print(
                f"  Query {i + 1} [{left}, {right}]: {results2[i]} != {expected} - FAIL"
            )
            all_passed = False

    if all_passed:
        print(f"  All {len(queries2)} random queries passed!")

    # Test Case 3: Edge cases
    print("\n" + "=" * 60)
    print("Test Case 3: Edge Cases")
    print("=" * 60)

    # Single element array
    arr3 = [42]
    queries3 = [(0, 0)]
    results3 = mo_algorithm(arr3, queries3)
    print(
        f"  Single element: {results3[0]} == 42 - {'PASS' if results3[0] == 42 else 'FAIL'}"
    )

    # Empty queries
    arr4 = [1, 2, 3, 4, 5]
    queries4 = []
    results4 = mo_algorithm(arr4, queries4)
    print(f"  Empty queries: {results4} == [] - {'PASS' if results4 == [] else 'FAIL'}")

    # Large range query
    arr5 = list(range(1000))
    queries5 = [(0, 999), (100, 900), (500, 500)]
    results5 = mo_algorithm(arr5, queries5)
    expected5 = [sum(range(1000)), sum(range(100, 901)), 500]
    print(
        f"  Large range [0,999]: {results5[0]} == {expected5[0]} - {'PASS' if results5[0] == expected5[0] else 'FAIL'}"
    )
    print(
        f"  Large range [100,900]: {results5[1]} == {expected5[1]} - {'PASS' if results5[1] == expected5[1] else 'FAIL'}"
    )

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
