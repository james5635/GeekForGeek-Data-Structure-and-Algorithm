"""
Smallest Range with Elements from K Sorted Lists
URL: https://www.geeksforgeeks.org/find-smallest-range-containing-elements-from-k-lists/
Source: GeeksforGeeks

Problem:
Given a 2D integer array mat[][] where each row is sorted in ascending order,
find the smallest range that includes at least one element from each of the rows.

Note: If there are two possible ranges [a, b] and [c, d] with the same size,
choose the one with the smaller starting value.

Examples:
Input: mat[][] = [[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]]
Output: [6, 8]

Input: mat[][] = [[2, 4], [1, 7], [20, 40]]
Output: [4, 20]

Approaches:
1. Naive: Try all combinations - O(n^k) - Not feasible
2. K Pointers: Track pointers for each row - O(n*k²)
3. Min Heap: Optimal solution - O(n*k*log k)
"""

import heapq
import sys


def find_smallest_range_k_pointers(mat):
    """
    K Pointers approach.

    Time: O(n*k²)
    Space: O(k)
    """
    k = len(mat)
    n = len(mat[0])

    ptr = [0] * k

    min_range = float("inf")
    start = -1
    end = -1

    while True:
        min_val = float("inf")
        max_val = float("-inf")
        min_row = -1

        for i in range(k):
            if ptr[i] == n:
                return [start, end]

            if mat[i][ptr[i]] < min_val:
                min_val = mat[i][ptr[i]]
                min_row = i

            if mat[i][ptr[i]] > max_val:
                max_val = mat[i][ptr[i]]

        if max_val - min_val < min_range:
            min_range = max_val - min_val
            start = min_val
            end = max_val

        ptr[min_row] += 1

    return [start, end]


class HeapNode:
    """
    Node for min heap containing element info.
    """

    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col

    def __repr__(self):
        return f"({self.val}, row={self.row}, col={self.col})"

    def __lt__(self, other):
        return self.val < other.val


def find_smallest_range_heap(mat):
    """
    Min Heap approach - optimal solution.

    Algorithm:
    1. Push first element of each row into min heap
    2. Track current maximum among heap elements
    3. Extract minimum, update smallest range if needed
    4. Push next element from same row
    5. Repeat until any row is exhausted

    Time: O(n*k*log k)
    Space: O(k)

    Args:
        mat: 2D matrix where each row is sorted

    Returns:
        Smallest range as [start, end]
    """
    N = len(mat)
    K = len(mat[0])

    pq = []
    max_val = -sys.maxsize

    for i in range(N):
        heapq.heappush(pq, HeapNode(mat[i][0], i, 0))
        max_val = max(max_val, mat[i][0])

    min_range = sys.maxsize
    min_el = 0
    max_el = 0

    while True:
        curr = heapq.heappop(pq)
        min_val = curr.val

        if max_val - min_val < min_range:
            min_range = max_val - min_val
            min_el = min_val
            max_el = max_val

        if curr.col + 1 == K:
            break

        next_val = mat[curr.row][curr.col + 1]
        heapq.heappush(pq, HeapNode(next_val, curr.row, curr.col + 1))
        max_val = max(max_val, next_val)

    return [min_el, max_el]


def find_smallest_range_heap_simple(mat):
    """
    Simplified heap implementation without custom class.

    Heap stores tuples: (value, row_index, col_index)
    """
    N = len(mat)
    K = len(mat[0])

    pq = []
    max_val = -sys.maxsize

    for i in range(N):
        heapq.heappush(pq, (mat[i][0], i, 0))
        max_val = max(max_val, mat[i][0])

    min_range = sys.maxsize
    range_start = 0
    range_end = 0

    while True:
        val, row, col = heapq.heappop(pq)

        current_range = max_val - val
        if current_range < min_range:
            min_range = current_range
            range_start = val
            range_end = max_val

        if col + 1 == K:
            break

        next_val = mat[row][col + 1]
        heapq.heappush(pq, (next_val, row, col + 1))
        max_val = max(max_val, next_val)

    return [range_start, range_end]


def find_smallest_range_brute_force(mat):
    """
    Brute force approach for small inputs.
    For educational purposes only.
    """
    k = len(mat)
    n = len(mat[0])

    best_start = mat[0][0]
    best_end = mat[0][0]

    for i in range(k):
        best_start = min(best_start, mat[i][0])
        best_end = max(best_end, mat[i][-1])

    return [best_start, best_end]


def verify_range(mat, start, end):
    """
    Verify that a range contains at least one element from each row.
    """
    k = len(mat)
    count = 0

    for row in mat:
        for val in row:
            if start <= val <= end:
                count += 1
                break

    return count == k


if __name__ == "__main__":
    print("=" * 60)
    print("SMALLEST RANGE FROM K SORTED LISTS")
    print("=" * 60)

    test_cases = [
        {
            "mat": [[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]],
            "expected": [6, 8],
            "description": "Standard case with multiple rows",
        },
        {
            "mat": [[2, 4], [1, 7], [20, 40]],
            "expected": [4, 20],
            "description": "Sparse ranges",
        },
        {
            "mat": [[1, 5, 10], [2, 6, 11], [3, 7, 12]],
            "expected": [3, 7],
            "description": "Overlapping ranges",
        },
        {
            "mat": [[0, 10, 20], [5, 15, 25], [10, 20, 30]],
            "expected": [10, 20],
            "description": "Multiple valid ranges",
        },
    ]

    for i, test in enumerate(test_cases, 1):
        print(f"\n{'=' * 60}")
        print(f"TEST CASE {i}: {test['description']}")
        print("=" * 60)

        mat = test["mat"]
        expected = test["expected"]

        print(f"\nInput matrix:")
        for idx, row in enumerate(mat):
            print(f"  Row {idx}: {row}")

        print(f"\nExpected range: [{expected[0]}, {expected[1]}]")

        result_pointers = find_smallest_range_k_pointers(mat)
        result_heap = find_smallest_range_heap(mat)
        result_simple = find_smallest_range_heap_simple(mat)

        print(f"\nResults:")
        print(f"  K Pointers:    [{result_pointers[0]}, {result_pointers[1]}]")
        print(f"  Min Heap:      [{result_heap[0]}, {result_heap[1]}]")
        print(f"  Simple Heap:   [{result_simple[0]}, {result_simple[1]}]")

        status = "PASS" if result_heap == expected else "FAIL"
        print(f"\n  Min Heap Status: {status}")

        if result_heap != expected:
            print(f"  Warning: Expected {expected}, got {result_heap}")

        valid = verify_range(mat, result_heap[0], result_heap[1])
        print(f"  Range validity: {'VALID' if valid else 'INVALID'}")

    print("\n" + "=" * 60)
    print("ALGORITHM EXPLANATION")
    print("=" * 60)

    print("""
Min Heap Approach:
-----------------
1. Initialize min heap with first element from each row
2. Track current maximum among heap elements
3. Extract minimum from heap (forms current range with max)
4. Update smallest range if current range is smaller
5. Push next element from the row we extracted from
6. Continue until any row is exhausted

Example walkthrough:
Input: [[4, 7, 9], [0, 8, 10], [6, 12, 16]]

Step 1: Heap = [(0,1,0), (4,0,0), (6,2,0)], max = 6
        Range: [0, 6]
        Extract 0, push 8

Step 2: Heap = [(4,0,0), (6,2,0), (8,1,1)], max = 8
        Range: [4, 8]
        Extract 4, push 7

Step 3: Heap = [(6,2,0), (7,0,1), (8,1,1)], max = 8
        Range: [6, 8] <- Smallest!
        Extract 6, push 12

... and so on
""")

    print("=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)
    print("\n1. K Pointers Approach:")
    print("   Time:  O(n*k²)")
    print("   Space: O(k)")
    print("\n2. Min Heap Approach:")
    print("   Time:  O(n*k*log k)")
    print("   Space: O(k)")
    print("\nWhere k = number of rows, n = elements per row")
