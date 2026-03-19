"""
K-th Largest Sum Contiguous Subarray
URL: https://www.geeksforgeeks.org/k-th-largest-sum-contiguous-subarray/
Source: GeeksforGeeks

Problem:
Given an array arr[] of size n, find the k-th largest sum of contiguous
subarray within the array of numbers (both negative and positive).

Examples:
Input: arr[] = [20, -5, -1], k = 3
Output: 14
Explanation: All sums are (20, 15, 14, -5, -6, -1), 3rd largest is 14.

Input: arr[] = [10, -10, 20, -40], k = 6
Output: -10

Approaches:
1. Naive: Generate all subarrays, store sums, sort descending - O(n^2 log n)
2. Better: Use prefix sum with min heap - O(n^2 log k) time, O(k) space
3. Best: Min heap maintains k largest sums efficiently
"""

import heapq


def kth_largest_naive(arr, k):
    """
    Naive approach: Generate all subarray sums and sort.

    Time: O(n^2 log n)
    Space: O(n^2)
    """
    n = len(arr)
    sums = []

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            sums.append(current_sum)

    sums.sort(reverse=True)
    return sums[k - 1]


def kth_largest_prefix_heap(arr, k):
    """
    Better approach: Prefix sum with min heap.

    Time: O(n^2 log k)
    Space: O(k)
    """
    n = len(arr)

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    pq = []
    heapq.heapify(pq)

    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            subarray_sum = prefix_sum[j] - prefix_sum[i]

            if len(pq) < k:
                heapq.heappush(pq, subarray_sum)
            else:
                if subarray_sum > pq[0]:
                    heapq.heapreplace(pq, subarray_sum)

    return pq[0]


def kth_largest(arr, k):
    """
    Expected approach: Using Min Heap.

    Algorithm:
    1. Calculate prefix sums for all subarrays
    2. Use min heap of size k to keep track of k largest sums
    3. For each subarray sum, if heap size < k, push
       Else if current sum > smallest in heap, replace

    Time: O(n^2 log k)
    Space: O(k)

    Args:
        arr: Input array
        k: Position of largest sum to find

    Returns:
        k-th largest contiguous subarray sum
    """
    n = len(arr)

    prefix = [0] * (n + 1)
    prefix[0] = 0
    prefix[1] = arr[0]
    for i in range(2, n + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]

    pq = []

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            x = prefix[j] - prefix[i - 1]

            if len(pq) < k:
                heapq.heappush(pq, x)
            else:
                if pq[0] < x:
                    heapq.heapreplace(pq, x)

    return pq[0]


def kth_largest_streaming(arr, k):
    """
    Streaming version using generator and heap.
    Useful for very large arrays.
    """
    n = len(arr)

    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]

    pq = []

    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            subarray_sum = prefix[j] - prefix[i]
            yield subarray_sum


def kth_largest_efficient(arr, k):
    """
    Efficient implementation with clear comments.
    """
    n = len(arr)
    pq = []

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]

            if len(pq) < k:
                heapq.heappush(pq, current_sum)
            elif current_sum > pq[0]:
                heapq.heapreplace(pq, current_sum)

    return pq[0] if pq else None


if __name__ == "__main__":
    print("=" * 60)
    print("K-TH LARGEST SUM CONTIGUOUS SUBARRAY")
    print("=" * 60)

    test_cases = [
        {"arr": [20, -5, -1], "k": 3, "expected": 14},
        {"arr": [10, -10, 20, -40], "k": 6, "expected": -10},
        {"arr": [1, 2, 3, 4], "k": 3, "expected": 9},
        {"arr": [-2, -1, -3, -5, -1], "k": 2, "expected": -1},
    ]

    print("\nTest Case 1:")
    arr = [20, -5, -1]
    k = 3
    print(f"  Array: {arr}")
    print(f"  k = {k}")
    print(f"  All subarray sums: ", end="")

    n = len(arr)
    all_sums = []
    for i in range(n):
        for j in range(i, n):
            all_sums.append(sum(arr[i : j + 1]))
    all_sums.sort(reverse=True)
    print(all_sums)
    print(f"  3rd largest = {all_sums[k - 1]}")

    result = kth_largest(arr, k)
    print(f"\n  kth_largest() result: {result}")
    print(f"  Expected: {test_cases[0]['expected']}")
    print(f"  Status: {'PASS' if result == test_cases[0]['expected'] else 'FAIL'}")

    print("\n" + "-" * 60)
    print("\nTest Case 2:")
    arr = [10, -10, 20, -40]
    k = 6
    print(f"  Array: {arr}")
    print(f"  k = {k}")
    result = kth_largest(arr, k)
    print(f"\n  kth_largest() result: {result}")
    print(f"  Expected: {test_cases[1]['expected']}")
    print(f"  Status: {'PASS' if result == test_cases[1]['expected'] else 'FAIL'}")

    print("\n" + "-" * 60)
    print("\nTest Case 3:")
    arr = [1, 2, 3, 4]
    k = 3
    print(f"  Array: {arr}")
    print(f"  k = {k}")
    result = kth_largest(arr, k)
    print(f"\n  kth_largest() result: {result}")
    print(f"  Expected: {test_cases[2]['expected']}")
    print(f"  Status: {'PASS' if result == test_cases[2]['expected'] else 'FAIL'}")

    print("\n" + "-" * 60)
    print("\nTest Case 4 (all negative):")
    arr = [-2, -1, -3, -5, -1]
    k = 2
    print(f"  Array: {arr}")
    print(f"  k = {k}")
    result = kth_largest(arr, k)
    print(f"\n  kth_largest() result: {result}")
    print(f"  Expected: {test_cases[3]['expected']}")
    print(f"  Status: {'PASS' if result == test_cases[3]['expected'] else 'FAIL'}")

    print("\n" + "=" * 60)
    print("ALGORITHM COMPARISON")
    print("=" * 60)

    arr = [100, -10, 50, 20, -5, 30]
    k = 4

    print(f"\nArray: {arr}, k = {k}")
    print(f"\nNaive approach: {kth_largest_naive(arr, k)}")
    print(f"Prefix + Heap: {kth_largest_prefix_heap(arr, k)}")
    print(f"Min Heap:      {kth_largest(arr, k)}")
    print(f"Efficient:     {kth_largest_efficient(arr, k)}")

    print("\n" + "=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)
    print("\nNaive Approach:")
    print("  Time:  O(n² log n)")
    print("  Space: O(n²)")
    print("\nPrefix Sum + Min Heap:")
    print("  Time:  O(n² log k)")
    print("  Space: O(k)")
    print("\nEfficient Min Heap:")
    print("  Time:  O(n² log k)")
    print("  Space: O(k)")
