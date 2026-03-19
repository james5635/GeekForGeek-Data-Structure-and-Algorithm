"""
Nearly Sorted Algorithm - GeeksforGeeks
https://www.geeksforgeeks.org/nearly-sorted-algorithm/

Problem: Given an array arr[] and an integer k, where every element is at most k positions
away from its correct sorted position. Sort the array.

Approach: Use a min-heap to efficiently sort the nearly sorted array.
- For each position i, the element must come from the next k+1 elements
- Use min-heap to always extract the minimum from the current window

Time Complexity: O(n*log(k))
Space Complexity: O(k)
"""

import heapq


def nearly_sorted(arr, k):
    """
    Sort a nearly sorted array where each element is at most k positions away
    from its correct sorted position.

    Args:
        arr: List of integers to sort
        k: Maximum distance each element is from its sorted position

    Returns:
        None (sorts in-place)
    """
    n = len(arr)
    pq = []

    for i in range(k):
        heapq.heappush(pq, arr[i])

    i = k
    index = 0

    while i < n:
        heapq.heappush(pq, arr[i])
        arr[index] = heapq.heappop(pq)
        i += 1
        index += 1

    while pq:
        arr[index] = heapq.heappop(pq)
        index += 1


if __name__ == "__main__":
    # Example 1
    arr = [2, 3, 1, 4]
    k = 2
    nearly_sorted(arr, k)
    print("Sorted array:", arr)  # Output: [1, 2, 3, 4]

    # Example 2
    arr = [1, 4, 5, 2, 3, 6, 7, 8, 9, 10]
    k = 2
    nearly_sorted(arr, k)
    print("Sorted array:", arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
