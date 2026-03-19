"""
Kth Largest Element in a Stream - GeeksforGeeks
https://www.geeksforgeeks.org/kth-largest-element-in-a-stream/

Problem: Given an input stream of n integers, after each insertion, determine
the kth largest element so far. Return -1 if less than k elements inserted.

Approach: Use a min-heap of size k to track the k largest elements.
- The smallest in the heap is the kth largest overall
- If heap has less than k elements, return -1

Time Complexity: O(n*log(k))
Space Complexity: O(k)
"""

import heapq
import bisect


def kth_largest(arr, k):
    """
    Find kth largest element after each insertion using min-heap.

    Args:
        arr: List of integers in stream order
        k: The kth largest to find

    Returns:
        List of kth largest values after each insertion
    """
    res = []
    min_heap = []

    for i in range(len(arr)):
        if len(min_heap) < k:
            heapq.heappush(min_heap, arr[i])
        elif arr[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, arr[i])

        if len(min_heap) == k:
            res.append(min_heap[0])
        else:
            res.append(-1)

    return res


def kth_largest_set(arr, k):
    """
    Alternative approach using sorted list and bisect.
    Time: O(n*k) for insertion, Space: O(k)
    """
    res = []
    st = []

    for i in range(len(arr)):
        bisect.insort(st, arr[i])

        if len(st) > k:
            st.pop(0)

        if len(st) == k:
            res.append(st[0])
        else:
            res.append(-1)

    return res


def kth_largest_naive(arr, k):
    """
    Naive approach: sort after each insertion.
    Time: O(n^2 * log(n)), Space: O(n)
    """
    res = []
    top_k = []

    for i in range(len(arr)):
        top_k.append(arr[i])
        top_k.sort()

        if len(top_k) >= k:
            res.append(top_k[i - k + 1])
        else:
            res.append(-1)

    return res


if __name__ == "__main__":
    # Example 1
    arr = [1, 2, 3, 4, 5, 6]
    k = 4
    print(f"arr = {arr}, k = {k}")
    print(f"Kth largest after each insertion: {kth_largest(arr, k)}")
    # Output: [-1, -1, -1, 1, 2, 3]

    # Example 2
    arr = [10, 20, 5, 15]
    k = 2
    print(f"\narr = {arr}, k = {k}")
    print(f"Kth largest after each insertion: {kth_largest(arr, k)}")
    # Output: [-1, 10, 10, 15]

    # Example 3
    arr = [3, 4]
    k = 1
    print(f"\narr = {arr}, k = {k}")
    print(f"Kth largest after each insertion: {kth_largest(arr, k)}")
    # Output: [3, 4]
