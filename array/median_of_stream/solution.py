"""
Median of Stream of Integers (Running Integers) Problem

Problem Description:
Given a stream of integers, find the median after each new integer is added.
The median is the middle value in an ordered integer list.
- If the list size is odd, the median is the middle element.
- If the list size is even, the median is the average of two middle elements.

Example:
Input: stream = [5, 15, 1, 3]
Output: [5.0, 10.0, 5.0, 4.0]
Explanation:
- After 5: [5] -> median = 5.0
- After 15: [5, 15] -> median = (5+15)/2 = 10.0
- After 1: [1, 5, 15] -> median = 5.0
- After 3: [1, 3, 5, 15] -> median = (3+5)/2 = 4.0

Time Complexity: O(log n) per insertion using two heaps
Space Complexity: O(n) to store all elements

Approach:
Use two heaps:
- Max heap (left half): Contains smaller half of numbers
- Min heap (right half): Contains larger half of numbers
- Balance: size of max heap = size of min heap or 1 more
"""

from typing import List
import heapq


class MedianFinder:
    """
    Class to find running median of a stream of integers.
    Uses two heaps to maintain median efficiently.
    """

    def __init__(self):
        """
        Initialize the MedianFinder.
        max_heap: stores smaller half (using negative values for max heap)
        min_heap: stores larger half
        """
        # Max heap for left half (smaller numbers)
        # Python has only min heap, so we store negatives
        self.max_heap = []

        # Min heap for right half (larger numbers)
        self.min_heap = []

    def add_num(self, num: int) -> None:
        """
        Add a number to the data structure.
        Time: O(log n)
        """
        if not self.max_heap or num <= -self.max_heap[0]:
            # Add to max heap (left half)
            heapq.heappush(self.max_heap, -num)
        else:
            # Add to min heap (right half)
            heapq.heappush(self.min_heap, num)

        # Balance the heaps
        # max_heap can have at most 1 more element than min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            # Move top of max heap to min heap
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            # Move top of min heap to max heap
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def find_median(self) -> float:
        """
        Find the median of all numbers seen so far.
        Time: O(1)
        """
        if len(self.max_heap) > len(self.min_heap):
            # Odd number of elements, max heap has the median
            return float(-self.max_heap[0])
        else:
            # Even number of elements
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0


def find_running_median(stream: List[int]) -> List[float]:
    """
    Find running median for a stream of integers.

    Args:
        stream: List of integers representing the stream

    Returns:
        List of medians after each insertion
    """
    mf = MedianFinder()
    medians = []

    for num in stream:
        mf.add_num(num)
        medians.append(mf.find_median())

    return medians


class MedianFinderInsertionSort:
    """
    Alternative implementation using insertion sort approach.
    Time: O(n) per insertion, Space: O(n)
    """

    def __init__(self):
        self.nums = []

    def add_num(self, num: int) -> None:
        # Insertion sort
        idx = 0
        while idx < len(self.nums) and self.nums[idx] < num:
            idx += 1
        self.nums.insert(idx, num)

    def find_median(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return float(self.nums[n // 2])
        else:
            return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0


def find_running_median_sorting(stream: List[int]) -> List[float]:
    """
    Simple approach using sorting.
    Time: O(n^2 log n) total, Space: O(n)
    """
    nums = []
    medians = []

    for num in stream:
        nums.append(num)
        nums.sort()
        n = len(nums)
        if n % 2 == 1:
            medians.append(float(nums[n // 2]))
        else:
            medians.append((nums[n // 2 - 1] + nums[n // 2]) / 2.0)

    return medians


if __name__ == "__main__":
    # Test Case 1: Standard example
    stream1 = [5, 15, 1, 3]
    result1 = find_running_median(stream1)
    print(f"Stream: {stream1}")
    print(f"Running medians: {result1}")
    print(f"Expected: [5.0, 10.0, 5.0, 4.0]")
    print(f"Pass: {result1 == [5.0, 10.0, 5.0, 4.0]}\n")

    # Test Case 2: Increasing sequence
    stream2 = [1, 2, 3, 4, 5]
    result2 = find_running_median(stream2)
    print(f"Stream: {stream2}")
    print(f"Running medians: {result2}")
    print(f"Expected: [1.0, 1.5, 2.0, 2.5, 3.0]")
    print(f"Pass: {result2 == [1.0, 1.5, 2.0, 2.5, 3.0]}\n")

    # Test Case 3: Decreasing sequence
    stream3 = [5, 4, 3, 2, 1]
    result3 = find_running_median(stream3)
    print(f"Stream: {stream3}")
    print(f"Running medians: {result3}")
    print(f"Expected: [5.0, 4.5, 4.0, 3.5, 3.0]")
    print(f"Pass: {result3 == [5.0, 4.5, 4.0, 3.5, 3.0]}\n")

    # Test Case 4: All same values
    stream4 = [5, 5, 5, 5]
    result4 = find_running_median(stream4)
    print(f"Stream: {stream4}")
    print(f"Running medians: {result4}")
    print(f"Expected: [5.0, 5.0, 5.0, 5.0]")
    print(f"Pass: {result4 == [5.0, 5.0, 5.0, 5.0]}\n")

    # Test Case 5: Empty stream
    stream5 = []
    result5 = find_running_median(stream5)
    print(f"Stream: {stream5}")
    print(f"Running medians: {result5}")
    print(f"Expected: []")
    print(f"Pass: {result5 == []}\n")

    # Test Case 6: Single element
    stream6 = [42]
    result6 = find_running_median(stream6)
    print(f"Stream: {stream6}")
    print(f"Running medians: {result6}")
    print(f"Expected: [42.0]")
    print(f"Pass: {result6 == [42.0]}\n")

    # Test Case 7: Two elements
    stream7 = [1, 2]
    result7 = find_running_median(stream7)
    print(f"Stream: {stream7}")
    print(f"Running medians: {result7}")
    print(f"Expected: [1.0, 1.5]")
    print(f"Pass: {result7 == [1.0, 1.5]}\n")

    # Test Case 8: Negative numbers
    stream8 = [-1, -5, 3, -2, 0]
    result8 = find_running_median(stream8)
    print(f"Stream: {stream8}")
    print(f"Running medians: {result8}")
    print(f"Expected: [-1.0, -3.0, -1.0, -1.5, -1.0]")
    print(f"Pass: {result8 == [-1.0, -3.0, -1.0, -1.5, -1.0]}")
