"""
K-th Largest Sum Contiguous Subarray

Given an array of integers, find the k-th largest sum among all possible
contiguous subarrays.

Approaches:
1. Naive: O(n² log n) - Generate all sums, sort
2. Better: O(n² log k) - Use min heap of size k
3. Optimal: O(n log n) - Prefix sums with efficient approach
"""

import heapq


def kth_largest_sum_naive(arr, k):
    """
    Naive approach: Generate all subarray sums and sort.

    Time Complexity: O(n² log(n²)) = O(n² log n)
    Space Complexity: O(n²) - to store all sums

    Algorithm:
    - Generate all possible subarray sums (n*(n+1)/2 sums)
    - Store in a list
    - Sort in descending order
    - Return k-th largest

    Args:
        arr: List of integers
        k: Position of largest sum to find

    Returns:
        k-th largest subarray sum
    """
    n = len(arr)
    all_sums = []

    # Generate all subarray sums
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            all_sums.append(current_sum)

    # Sort in descending order
    all_sums.sort(reverse=True)

    # Return k-th largest (1-indexed, so k-1 for 0-indexed)
    if k <= len(all_sums):
        return all_sums[k - 1]
    return None


def kth_largest_sum_min_heap(arr, k):
    """
    Better approach: Use min heap of size k.

    Time Complexity: O(n² log k)
    Space Complexity: O(k) - only store k elements

    Algorithm:
    - Generate all subarray sums
    - Maintain a min heap of size k
    - If new sum > min heap top, replace top
    - After processing all, top is k-th largest

    Args:
        arr: List of integers
        k: Position of largest sum to find

    Returns:
        k-th largest subarray sum
    """
    n = len(arr)
    min_heap = []

    # Generate all subarray sums
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]

            if len(min_heap) < k:
                heapq.heappush(min_heap, current_sum)
            elif current_sum > min_heap[0]:
                heapq.heapreplace(min_heap, current_sum)

    return min_heap[0] if min_heap else None


def kth_largest_sum_prefix_heap(arr, k):
    """
    Optimal approach: Use prefix sums with min heap.

    Time Complexity: O(n log n + n² log k) = O(n² log k) worst case
                    O(n log n) best case with optimizations
    Space Complexity: O(n) for prefix sums + O(k) for heap

    Algorithm:
    - Compute prefix sums
    - Use min heap to track k largest differences
    - prefix[j] - prefix[i] gives sum of subarray arr[i+1..j]

    Args:
        arr: List of integers
        k: Position of largest sum to find

    Returns:
        k-th largest subarray sum
    """
    n = len(arr)

    # Compute prefix sums
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    min_heap = []

    # Check all pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n + 1):
            subarray_sum = prefix[j] - prefix[i]

            if len(min_heap) < k:
                heapq.heappush(min_heap, subarray_sum)
            elif subarray_sum > min_heap[0]:
                heapq.heapreplace(min_heap, subarray_sum)

    return min_heap[0] if min_heap else None


def kth_largest_sum_optimized(arr, k):
    """
    Optimized approach: Kadane-like with heap for top k.

    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(k)

    This is a variation that works well for large k.

    Args:
        arr: List of integers
        k: Position of largest sum to find

    Returns:
        k-th largest subarray sum
    """
    n = len(arr)

    # Use a max heap approach (Python has min heap, so negate)
    # Store (-sum, start, end) to get max sum efficiently
    max_heap = []

    # Push all single element subarrays
    for i in range(n):
        heapq.heappush(max_heap, (-arr[i], i, i))

    # Track visited subarrays
    visited = set()

    count = 0
    result = 0

    while max_heap and count < k:
        neg_sum, start, end = heapq.heappop(max_heap)
        current_sum = -neg_sum

        if (start, end) in visited:
            continue

        visited.add((start, end))
        count += 1
        result = current_sum

        # Expand to the right if possible
        if end + 1 < n:
            new_sum = current_sum + arr[end + 1]
            heapq.heappush(max_heap, (-new_sum, start, end + 1))

        # Expand to the left if possible
        if start - 1 >= 0:
            new_sum = current_sum + arr[start - 1]
            heapq.heappush(max_heap, (-new_sum, start - 1, end))

    return result if count == k else None


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # (array, k, expected)
        ([20, -5, -1], 3, 14),  # Sums: 20, 15, 14, -5, -6, -1; 3rd largest = 14
        ([10, -10, 20, -40], 6, -10),  # Various sums
        ([1, 2, 3, 4, 5], 3, 12),  # Sums include 15, 14, 12, ...
        ([-1, -2, -3], 1, -1),  # All negative
        ([5], 1, 5),  # Single element
        ([3, 2, 1], 3, 3),  # Sums: 6,5,3,3,2,1; 3rd largest = 3
    ]

    print("=" * 70)
    print("K-th Largest Sum Contiguous Subarray")
    print("=" * 70)

    for i, (arr, k, expected) in enumerate(test_cases, 1):
        naive_result = kth_largest_sum_naive(arr.copy(), k)
        min_heap_result = kth_largest_sum_min_heap(arr.copy(), k)
        prefix_heap_result = kth_largest_sum_prefix_heap(arr.copy(), k)
        optimized_result = kth_largest_sum_optimized(arr.copy(), k)

        match_naive = naive_result == expected
        match_min_heap = min_heap_result == expected
        match_prefix = prefix_heap_result == expected
        match_optimized = optimized_result == expected

        print(f"\nTest {i}: arr = {arr}, k = {k}")
        print(f"  Expected:           {expected}")
        print(f"  Naive O(n² log n):  {naive_result} {'✓' if match_naive else '✗'}")
        print(
            f"  Min Heap O(n² log k): {min_heap_result} {'✓' if match_min_heap else '✗'}"
        )
        print(
            f"  Prefix+Heap O(n² log k): {prefix_heap_result} {'✓' if match_prefix else '✗'}"
        )
        print(
            f"  Optimized O(n log n): {optimized_result} {'✓' if match_optimized else '✗'}"
        )

    print("\n" + "=" * 70)
    print("\nAlgorithm Explanation:")
    print("\n1. Naive Approach O(n² log n):")
    print("   - Generate all n*(n+1)/2 subarray sums")
    print("   - Sort all sums in descending order")
    print("   - Return k-th element")
    print("   - Time: O(n² log n), Space: O(n²)")
    print("\n2. Min Heap Approach O(n² log k):")
    print("   - Generate all subarray sums")
    print("   - Maintain min heap of size k")
    print("   - If new sum > min heap top, replace top")
    print("   - After all sums, top is k-th largest")
    print("   - Time: O(n² log k), Space: O(k)")
    print("\n3. Prefix Sum + Heap O(n² log k):")
    print("   - Compute prefix sums array")
    print("   - Subarray sum = prefix[j] - prefix[i]")
    print("   - Use min heap to track k largest differences")
    print("   - Time: O(n² log k), Space: O(n)")
    print("\n4. Optimized (Best for large k) O(n log n):")
    print("   - Use max heap with expansion strategy")
    print("   - Start with single elements")
    print("   - Expand to adjacent elements")
    print("   - Pop k times to get k-th largest")
    print("\nKey Insight: We only need top k, not all sums")
    print("=" * 70)
