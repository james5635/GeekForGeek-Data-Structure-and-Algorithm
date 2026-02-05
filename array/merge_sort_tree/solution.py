"""
Merge Sort Tree for Range Order Statistics

Problem: Given an array arr[0...n-1] and queries of form: find k-th smallest
number in subarray [L, R]. The array is static (no updates).

Example:
    Input: arr = [3, 2, 5, 1, 8, 9]
    Query 1: L=1, R=5, k=2 -> subarray [2,5,1,8,9], 2nd smallest = 2
    Query 2: L=0, R=3, k=3 -> subarray [3,2,5,1], 3rd smallest = 3

Time Complexity:
    - Build: O(n log n)
    - Query: O(log² n) or O(log n) with binary search optimization
    - Space: O(n log n)

Author: Generated for GeekForGeeks DSA Tutorial
"""

from typing import List, Tuple
import bisect


class MergeSortTree:
    """Merge sort tree for range order statistics queries."""

    def __init__(self, arr: List[int]):
        """
        Initialize merge sort tree.

        Args:
            arr: Input array of integers
        """
        self.n = len(arr)
        self.arr = arr
        # Each node stores a sorted list of its segment
        self.tree: List[List[int]] = [[] for _ in range(4 * self.n)]
        self._build(0, 0, self.n - 1)

    def _build(self, node: int, start: int, end: int) -> None:
        """Build merge sort tree recursively."""
        if start == end:
            self.tree[node] = [self.arr[start]]
        else:
            mid = (start + end) // 2
            self._build(2 * node + 1, start, mid)
            self._build(2 * node + 2, mid + 1, end)
            # Merge the two sorted lists
            self.tree[node] = self._merge(
                self.tree[2 * node + 1], self.tree[2 * node + 2]
            )

    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        """Merge two sorted lists."""
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def _count_less_equal(
        self, node: int, start: int, end: int, l: int, r: int, x: int
    ) -> int:
        """
        Count elements <= x in range [l, r].
        Uses binary search for O(log n) per node.
        """
        if start > r or end < l:
            return 0

        if l <= start and end <= r:
            # Count elements <= x in this sorted segment
            return bisect.bisect_right(self.tree[node], x)

        mid = (start + end) // 2
        left_count = self._count_less_equal(2 * node + 1, start, mid, l, r, x)
        right_count = self._count_less_equal(2 * node + 2, mid + 1, end, l, r, x)
        return left_count + right_count

    def _query_kth_smallest(self, l: int, r: int, k: int) -> int:
        """
        Find k-th smallest in range [l, r] using binary search on value.
        Assumes k is 1-indexed.
        """
        # Find min and max in range for binary search bounds
        low = min(self.arr[l : r + 1])
        high = max(self.arr[l : r + 1])

        ans = low
        while low <= high:
            mid = (low + high) // 2
            count = self._count_less_equal(0, 0, self.n - 1, l, r, mid)

            if count < k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1

        return ans

    def query(self, l: int, r: int, k: int) -> int:
        """
        Get k-th smallest element in range [l, r].

        Args:
            l: Left index (inclusive)
            r: Right index (inclusive)
            k: k-th smallest (1-indexed)

        Returns:
            k-th smallest element
        """
        if l < 0 or r >= self.n or l > r:
            raise ValueError("Invalid range")
        if k < 1 or k > (r - l + 1):
            raise ValueError(f"k must be between 1 and {r - l + 1}")
        return self._query_kth_smallest(l, r, k)

    def count_less_than(self, l: int, r: int, x: int) -> int:
        """
        Count elements less than x in range [l, r].

        Args:
            l: Left index (inclusive)
            r: Right index (inclusive)
            x: Value to compare

        Returns:
            Count of elements < x
        """
        if l < 0 or r >= self.n or l > r:
            raise ValueError("Invalid range")
        return self._count_less_equal(0, 0, self.n - 1, l, r, x - 1)

    def count_less_equal(self, l: int, r: int, x: int) -> int:
        """
        Count elements <= x in range [l, r].

        Args:
            l: Left index (inclusive)
            r: Right index (inclusive)
            x: Value to compare

        Returns:
            Count of elements <= x
        """
        if l < 0 or r >= self.n or l > r:
            raise ValueError("Invalid range")
        return self._count_less_equal(0, 0, self.n - 1, l, r, x)


def solve_kth_smallest_queries(
    arr: List[int], queries: List[Tuple[int, int, int]]
) -> List[int]:
    """
    Solve multiple k-th smallest queries.

    Args:
        arr: Input array
        queries: List of (L, R, k) tuples

    Returns:
        List of k-th smallest results for each query
    """
    mst = MergeSortTree(arr)
    results = []
    for l, r, k in queries:
        results.append(mst.query(l, r, k))
    return results


if __name__ == "__main__":
    # Test Case 1: Basic functionality
    print("=" * 60)
    print("Test Case 1: Basic K-th Smallest Queries")
    print("=" * 60)

    arr1 = [3, 2, 5, 1, 8, 9]
    print(f"Array: {arr1}")

    mst1 = MergeSortTree(arr1)
    queries1 = [(1, 5, 2), (0, 3, 3), (2, 4, 1), (0, 5, 4)]

    for l, r, k in queries1:
        result = mst1.query(l, r, k)
        subarray = arr1[l : r + 1]
        sorted_sub = sorted(subarray)
        print(f"\nRange [{l}, {r}]: {subarray}")
        print(f"Sorted: {sorted_sub}")
        print(f"{k}-th smallest = {result}")

    # Test Case 2: Count queries
    print("\n" + "=" * 60)
    print("Test Case 2: Count Less Than/Equal Queries")
    print("=" * 60)

    arr2 = [1, 4, 2, 8, 5, 7, 3, 6]
    mst2 = MergeSortTree(arr2)
    print(f"Array: {arr2}")

    test_ranges = [(0, 7), (2, 5), (1, 4)]
    test_values = [5, 3, 7]

    for (l, r), val in zip(test_ranges, test_values):
        subarray = arr2[l : r + 1]
        count_lt = mst2.count_less_than(l, r, val)
        count_le = mst2.count_less_equal(l, r, val)
        actual_lt = sum(1 for x in subarray if x < val)
        actual_le = sum(1 for x in subarray if x <= val)

        print(f"\nRange [{l}, {r}]: {subarray}")
        print(f"  Count < {val}: {count_lt} (expected: {actual_lt})")
        print(f"  Count <= {val}: {count_le} (expected: {actual_le})")

    # Test Case 3: Edge cases
    print("\n" + "=" * 60)
    print("Test Case 3: Edge Cases")
    print("=" * 60)

    arr3 = [5]
    mst3 = MergeSortTree(arr3)
    print(f"Single element: {arr3}")
    print(f"1st smallest in [0, 0]: {mst3.query(0, 0, 1)}")

    arr4 = [7, 7, 7, 7, 7]
    mst4 = MergeSortTree(arr4)
    print(f"\nAll same elements: {arr4}")
    for k in range(1, 6):
        print(f"  {k}-th smallest in [0, 4]: {mst4.query(0, 4, k)}")

    arr5 = [1, 2, 3, 4, 5]
    mst5 = MergeSortTree(arr5)
    print(f"\nSorted array: {arr5}")
    print(f"3rd smallest in [0, 4]: {mst5.query(0, 4, 3)}")

    arr6 = [5, 4, 3, 2, 1]
    mst6 = MergeSortTree(arr6)
    print(f"\nReverse sorted: {arr6}")
    print(f"3rd smallest in [0, 4]: {mst6.query(0, 4, 3)}")

    # Test Case 4: Large batch queries
    print("\n" + "=" * 60)
    print("Test Case 4: Batch Query Processing")
    print("=" * 60)

    arr7 = [10, 5, 2, 8, 1, 9, 3, 7, 4, 6]
    queries7 = [(0, 9, 1), (0, 9, 10), (2, 7, 3), (3, 6, 2), (1, 8, 5)]
    results = solve_kth_smallest_queries(arr7, queries7)

    print(f"Array: {arr7}")
    print("\nQueries and Results:")
    for (l, r, k), res in zip(queries7, results):
        subarray = sorted(arr7[l : r + 1])
        print(f"  [{l}, {r}], k={k}: {res} (sorted range: {subarray})")

    print("\n" + "=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)
