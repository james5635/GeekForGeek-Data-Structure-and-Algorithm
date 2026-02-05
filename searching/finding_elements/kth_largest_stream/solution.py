"""
Kth Largest Element in a Stream

Problem:
Given a stream of n integers (as array) and k, after each insertion
find the kth largest element. If fewer than k elements, return -1.

Examples:
Input: [1, 2, 3, 4, 5, 6], k = 4
Output: [-1, -1, -1, 1, 2, 3]

Input: [10, 20, 5, 15], k = 2
Output: [-1, 10, 10, 15]

Approach:
Min Heap - Maintain min heap of size k. After each insertion, if
heap size >= k, top is kth largest.

Time Complexity: O(n log k) for n insertions
Space Complexity: O(k)

Reference:
https://www.geeksforgeeks.org/dsa/kth-largest-element-in-a-stream/
"""

import heapq


def kth_largest_in_stream(arr, k):
    """
    Find kth largest element after each insertion in stream.

    Args:
        arr: List of integers (stream)
        k: Position of largest element to find

    Returns:
        List of kth largest elements after each insertion
    """
    result = []
    min_heap = []

    for num in arr:
        # Add element to heap
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)

        # Record kth largest if we have k elements
        if len(min_heap) == k:
            result.append(min_heap[0])
        else:
            result.append(-1)

    return result


class KthLargest:
    """
    Class to handle continuous stream of integers.
    """

    def __init__(self, k, nums):
        """
        Initialize with k and initial numbers.

        Args:
            k: Position of largest element
            nums: Initial list of numbers
        """
        self.k = k
        self.min_heap = nums[:]
        heapq.heapify(self.min_heap)

        # Keep only k largest
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val):
        """
        Add new value and return kth largest.

        Args:
            val: New value to add

        Returns:
            kth largest element
        """
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)

        return self.min_heap[0] if len(self.min_heap) == self.k else -1


def test_kth_largest_stream():
    """Test cases for kth largest in stream."""
    # Test case 1: Basic stream
    assert kth_largest_in_stream([1, 2, 3, 4, 5, 6], 4) == [-1, -1, -1, 1, 2, 3]

    # Test case 2: Different stream
    assert kth_largest_in_stream([10, 20, 5, 15], 2) == [-1, 10, 10, 15]

    # Test case 3: k = 1
    assert kth_largest_in_stream([3, 4], 1) == [3, 4]

    # Test case 4: Decreasing values
    assert kth_largest_in_stream([5, 4, 3, 2, 1], 3) == [-1, -1, 3, 3, 3]

    # Test case 5: Using class
    kth = KthLargest(3, [4, 5, 8, 2])
    # Initial heap: [4, 5, 8], 3rd largest = 4
    assert kth.add(3) == 4  # 3 < 4, heap unchanged
    # After adding 5: 5 > 4, heap becomes [5, 5, 8], 3rd largest = 5
    assert kth.add(5) == 5
    # After adding 10: 10 > 5, heap becomes [5, 8, 10], 3rd largest = 5
    assert kth.add(10) == 5
    # After adding 9: 9 > 5, heap becomes [8, 9, 10], 3rd largest = 8
    assert kth.add(9) == 8
    # After adding 4: 4 < 8, heap unchanged, 3rd largest = 8
    assert kth.add(4) == 8

    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    arr = [1, 2, 3, 4, 5, 6]
    k = 4
    print(f"Stream: {arr}")
    print(f"k = {k}")
    result = kth_largest_in_stream(arr, k)
    print(f"Kth largest after each: {result}")

    # Run tests
    test_kth_largest_stream()
