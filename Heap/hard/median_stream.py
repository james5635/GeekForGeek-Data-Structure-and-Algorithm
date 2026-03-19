"""
Median of Stream of Running Integers
URL: https://www.geeksforgeeks.org/median-of-stream-of-running-integers/
Source: GeeksforGeeks

Problem:
Given that integers are being read from a data stream, find the median of all
the elements read so far starting from the first integer till the last integer.
This is also called the Median of Running Integers.

What is Median?
Median can be defined as the element in the data set which separates the higher
half of the data sample from the lower half. When the input size is odd, we
take the middle element of sorted data. If the input size is even, we pick an
average of middle two elements.

Examples:
Input: 5 10 15
Output: 5, 7.5, 10

Input: 1, 2, 3, 4
Output: 1, 1.5, 2, 2.5

Approach:
Use max heap to store lower half and min heap to store higher half.
At any time, try to make heaps balanced (sizes differ by at most 1).

Algorithm Steps:
1. Create two heaps - max heap for lower half, min heap for higher half
2. For each new element:
   - If max heap has more elements and new element < previous median,
     move top of max heap to min heap and insert new to max heap
   - If max heap has less elements and new element > previous median,
     move top of min heap to max heap and insert new to min heap
   - If sizes are equal, check if element < median to decide placement
3. Calculate median based on heap sizes

Time Complexity: O(n log n) - each insertion takes log n
Space Complexity: O(n) - storing all elements in heaps
"""

from heapq import heapify, heappush, heappop, nlargest, nsmallest


def print_medians(arr, n):
    """
    Calculate running median using max heap and min heap.

    Args:
        arr: Input array of integers
        n: Length of array

    Returns:
        List of medians after each element is processed
    """
    s = []
    g = []

    heapify(s)
    heapify(g)

    med = arr[0]
    heappush(s, arr[0])

    print(med)
    medians = [med]

    for i in range(1, n):
        x = arr[i]

        if len(s) > len(g):
            if x < med:
                heappush(g, heappop(s))
                heappush(s, x)
            else:
                heappush(g, x)
            med = (nlargest(1, s)[0] + nsmallest(1, g)[0]) / 2

        elif len(s) == len(g):
            if x < med:
                heappush(s, x)
                med = nlargest(1, s)[0]
            else:
                heappush(g, x)
                med = nsmallest(1, g)[0]

        else:
            if x > med:
                heappush(s, heappop(g))
                heappush(g, x)
            else:
                heappush(s, x)
            med = (nlargest(1, s)[0] + nsmallest(1, g)[0]) / 2

        print(med)
        medians.append(med)

    return medians


class RunningMedian:
    """
    Class to maintain running median for a stream of integers.
    Uses max heap (stored as negative values) for lower half
    and min heap for upper half.
    """

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        heapify(self.max_heap)
        heapify(self.min_heap)

    def add_num(self, num):
        """
        Add a number to the data stream.

        Args:
            num: Integer to add
        """
        if not self.max_heap or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        self._rebalance()

    def _rebalance(self):
        """
        Rebalance heaps to maintain size property.
        Max heap can have at most 1 more element than min heap.
        """
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heappop(self.max_heap)
            heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heappop(self.min_heap)
            heappush(self.max_heap, -val)

    def get_median(self):
        """
        Get the current median.

        Returns:
            Median value (float if even count, int otherwise)
        """
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]


if __name__ == "__main__":
    print("=" * 60)
    print("MEDIAN OF STREAM - TEST CASE 1")
    print("=" * 60)
    arr = [5, 15, 10, 20, 3]
    print(f"Input stream: {arr}")
    print("\nRunning medians:")
    medians = print_medians(arr, len(arr))

    print("\n" + "=" * 60)
    print("MEDIAN OF STREAM - TEST CASE 2")
    print("=" * 60)
    arr2 = [5, 10, 15]
    print(f"Input stream: {arr2}")
    print("\nRunning medians:")
    print_medians(arr2, len(arr2))

    print("\n" + "=" * 60)
    print("MEDIAN OF STREAM - TEST CASE 3")
    print("=" * 60)
    arr3 = [1, 2, 3, 4]
    print(f"Input stream: {arr3}")
    print("\nRunning medians:")
    print_medians(arr3, len(arr3))

    print("\n" + "=" * 60)
    print("USING RunningMedian CLASS")
    print("=" * 60)
    median_tracker = RunningMedian()
    test_stream = [12, 4, 5, 3, 8, 7]
    print(f"Input stream: {test_stream}")
    print("\nProcessing:")
    for num in test_stream:
        median_tracker.add_num(num)
        print(f"  Added {num} -> Median: {median_tracker.get_median()}")


print("\nComplexity Analysis:")
print("-" * 40)
print("Time Complexity: O(n log n)")
print("  - Each insertion to heap takes O(log n)")
print("  - For n elements: O(n log n)")
print("\nSpace Complexity: O(n)")
print("  - Need to store all n elements in heaps")
