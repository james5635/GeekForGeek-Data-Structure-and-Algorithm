"""
K Maximum Sum Combinations from Two Arrays - GeeksforGeeks
https://www.geeksforgeeks.org/k-maximum-sum-combinations-two-arrays/

Problem: Given two integer arrays a[] and b[] of same length, find top k maximum sum
combinations where each combination is a[i] + b[j]. Return k largest sums in descending order.

Time Complexity:
- Naive: O(n^2 * log(n^2))
- Better: O(n^2 * log(k)) using min-heap of size k
- Expected: O(n * log(n)) using max-heap with index tracking

Space Complexity: O(k) for all approaches
"""

import heapq


def top_k_sum_pairs_naive(a, b, k):
    """
    Generate all combinations and sort.
    O(n^2 * log(n^2)) time, O(n^2) space
    """
    n = len(a)
    all_possible = []

    for i in range(n):
        for j in range(n):
            curr_sum = a[i] + b[j]
            all_possible.append(curr_sum)

    all_possible.sort(reverse=True)
    return all_possible[:k]


def top_k_sum_pairs_heap(a, b, k):
    """
    Use min-heap of size k to track top k sums.
    O(n^2 * log(k)) time, O(k) space
    """
    n = len(a)
    min_heap = []

    for i in range(n):
        for j in range(n):
            curr_sum = a[i] + b[j]

            if len(min_heap) < k:
                heapq.heappush(min_heap, curr_sum)
            elif curr_sum > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, curr_sum)

    res = []
    while min_heap:
        res.append(heapq.heappop(min_heap))

    res.reverse()
    return res


def top_k_sum_pairs_max_heap(a, b, k):
    """
    Use max-heap with index tracking (most efficient).
    Sort arrays in descending order, use max-heap to explore pairs.
    O(n * log(n) + k * log(k)) time, O(k) space
    """
    n = len(a)
    a.sort(reverse=True)
    b.sort(reverse=True)

    visited = set()
    heap = []

    heapq.heappush(heap, (-(a[0] + b[0]), 0, 0))
    visited.add((0, 0))

    res = []

    while len(res) < k:
        neg_sum, i, j = heapq.heappop(heap)
        res.append(-neg_sum)

        if i + 1 < n and (i + 1, j) not in visited:
            heapq.heappush(heap, (-(a[i + 1] + b[j]), i + 1, j))
            visited.add((i + 1, j))

        if j + 1 < n and (i, j + 1) not in visited:
            heapq.heappush(heap, (-(a[i] + b[j + 1]), i, j + 1))
            visited.add((i, j + 1))

    return res


if __name__ == "__main__":
    # Example 1
    a = [3, 2]
    b = [1, 4]
    k = 2
    print(f"Top {k} sums: {top_k_sum_pairs_max_heap(a, b, k)}")  # [7, 6]

    # Example 2
    a = [1, 4, 2, 3]
    b = [2, 5, 1, 6]
    k = 3
    print(f"Top {k} sums: {top_k_sum_pairs_max_heap(a, b, k)}")  # [10, 9, 9]

    # Verify all approaches give same result
    a = [1, 4, 2, 3]
    b = [2, 5, 1, 6]
    k = 3

    print("\nVerification:")
    print(f"  Naive:     {top_k_sum_pairs_naive(a, b, k)}")
    print(f"  Min-Heap: {top_k_sum_pairs_heap(a, b, k)}")
    print(f"  Max-Heap: {top_k_sum_pairs_max_heap(a, b, k)}")
