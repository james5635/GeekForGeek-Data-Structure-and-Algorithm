"""
Top K Frequent Elements Problem

Problem Description:
Given an array of integers and a number k, find the k most frequent elements in the array.
If multiple elements have the same frequency, return them in any order.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1, 2]

Time Complexity: O(n log k) using Min Heap
Space Complexity: O(n) for frequency map and heap

Approaches:
1. Brute Force: Count all, sort by frequency, O(n log n)
2. Min Heap: Keep k elements in heap, O(n log k)
3. Bucket Sort: O(n) time, best for large k
"""

from typing import List
from collections import Counter
import heapq


def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    """
    Find top k frequent elements using Min Heap.

    Args:
        nums: List of integers
        k: Number of top frequent elements to find

    Returns:
        List of k most frequent elements
    """
    if k == 0 or not nums:
        return []

    # Count frequencies
    freq_map = Counter(nums)

    # Use min heap to keep top k elements
    # Heap will store (frequency, element)
    min_heap = []

    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Extract elements from heap
    result = [item[1] for item in min_heap]
    return result


def top_k_frequent_bucket_sort(nums: List[int], k: int) -> List[int]:
    """
    Find top k frequent elements using Bucket Sort.
    Time: O(n), Space: O(n)
    """
    if k == 0 or not nums:
        return []

    # Count frequencies
    freq_map = Counter(nums)

    # Create buckets where index represents frequency
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]

    for num, freq in freq_map.items():
        buckets[freq].append(num)

    # Collect top k elements from highest frequency buckets
    result = []
    for i in range(n, 0, -1):
        if buckets[i]:
            result.extend(buckets[i])
            if len(result) >= k:
                return result[:k]

    return result


def top_k_frequent_quickselect(nums: List[int], k: int) -> List[int]:
    """
    Find top k frequent elements using QuickSelect.
    Time: O(n) average case, Space: O(n)
    """
    if k == 0 or not nums:
        return []

    freq_map = Counter(nums)
    unique = list(freq_map.keys())

    def partition(left: int, right: int, pivot_idx: int) -> int:
        pivot_freq = freq_map[unique[pivot_idx]]
        # Move pivot to end
        unique[pivot_idx], unique[right] = unique[right], unique[pivot_idx]

        store_idx = left
        for i in range(left, right):
            if freq_map[unique[i]] < pivot_freq:
                unique[store_idx], unique[i] = unique[i], unique[store_idx]
                store_idx += 1

        # Move pivot to its final place
        unique[right], unique[store_idx] = unique[store_idx], unique[right]
        return store_idx

    def quickselect(left: int, right: int, k_smallest: int) -> None:
        if left == right:
            return

        pivot_idx = (left + right) // 2
        pivot_idx = partition(left, right, pivot_idx)

        if k_smallest == pivot_idx:
            return
        elif k_smallest < pivot_idx:
            quickselect(left, pivot_idx - 1, k_smallest)
        else:
            quickselect(pivot_idx + 1, right, k_smallest)

    n = len(unique)
    quickselect(0, n - 1, n - k)

    return unique[n - k :]


if __name__ == "__main__":
    # Test Case 1: Standard example
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = sorted(top_k_frequent_heap(nums1, k1))
    print(f"Input: {nums1}, k = {k1}")
    print(f"Top {k1} frequent: {result1}")
    print(f"Expected: [1, 2]")
    print(f"Pass: {result1 == [1, 2]}\n")

    # Test Case 2: Single element
    nums2 = [1]
    k2 = 1
    result2 = top_k_frequent_heap(nums2, k2)
    print(f"Input: {nums2}, k = {k2}")
    print(f"Top {k2} frequent: {result2}")
    print(f"Expected: [1]")
    print(f"Pass: {result2 == [1]}\n")

    # Test Case 3: All elements same frequency
    nums3 = [1, 2, 3, 4]
    k3 = 2
    result3 = top_k_frequent_heap(nums3, k3)
    print(f"Input: {nums3}, k = {k3}")
    print(f"Top {k3} frequent: {result3}")
    print(f"All have frequency 1, any 2 is valid")
    print(f"Pass: {len(result3) == 2}\n")

    # Test Case 4: k equals number of unique elements
    nums4 = [1, 2, 3]
    k4 = 3
    result4 = sorted(top_k_frequent_heap(nums4, k4))
    print(f"Input: {nums4}, k = {k4}")
    print(f"Top {k4} frequent: {result4}")
    print(f"Expected: [1, 2, 3]")
    print(f"Pass: {result4 == [1, 2, 3]}\n")

    # Test Case 5: Empty array
    nums5 = []
    k5 = 1
    result5 = top_k_frequent_heap(nums5, k5)
    print(f"Input: {nums5}, k = {k5}")
    print(f"Top {k5} frequent: {result5}")
    print(f"Expected: []")
    print(f"Pass: {result5 == []}\n")

    # Test Case 6: Large frequency differences
    nums6 = [1, 1, 1, 1, 2, 2, 3]
    k6 = 1
    result6 = top_k_frequent_heap(nums6, k6)
    print(f"Input: {nums6}, k = {k6}")
    print(f"Top {k6} frequent: {result6}")
    print(f"Expected: [1]")
    print(f"Pass: {result6 == [1]}\n")

    # Test Case 7: Negative numbers
    nums7 = [-1, -1, 1, 1, 1, 2, 2]
    k7 = 2
    result7 = sorted(top_k_frequent_heap(nums7, k7))
    print(f"Input: {nums7}, k = {k7}")
    print(f"Top {k7} frequent: {result7}")
    print(f"Expected: [-1, 1] (order may vary)")
    print(f"Pass: {result7 == [-1, 1]}")
