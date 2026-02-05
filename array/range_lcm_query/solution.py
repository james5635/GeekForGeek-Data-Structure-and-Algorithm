"""
Range LCM Queries using Segment Tree

Problem: Given an array arr[0...n-1] and multiple queries. For each query L, R,
find the LCM of all array elements from index L to R.

Example:
    Input: arr = [2, 7, 6, 5, 4]
    Query 1: L=0, R=2 -> LCM(2, 7, 6) = 42
    Query 2: L=1, R=4 -> LCM(7, 6, 5, 4) = 420

Time Complexity:
    - Build: O(n log MAX) where MAX is max element
    - Query: O(log n * log MAX)
    - Space: O(n)

Author: Generated for GeekForGeeks DSA Tutorial
"""

import math
from typing import List, Tuple


class RangeLCMQuery:
    """Segment tree for range LCM queries."""

    def __init__(self, arr: List[int]):
        """
        Initialize segment tree with array.

        Args:
            arr: Input array of integers
        """
        self.n = len(arr)
        self.arr = arr
        # Segment tree size: 4 * n is sufficient
        self.tree = [1] * (4 * self.n)
        self._build(0, 0, self.n - 1)

    def _lcm(self, a: int, b: int) -> int:
        """Calculate LCM of two numbers."""
        if a == 0:
            return b
        if b == 0:
            return a
        return abs(a * b) // math.gcd(a, b)

    def _build(self, node: int, start: int, end: int) -> None:
        """Build segment tree recursively."""
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self._build(2 * node + 1, start, mid)
            self._build(2 * node + 2, mid + 1, end)
            self.tree[node] = self._lcm(
                self.tree[2 * node + 1], self.tree[2 * node + 2]
            )

    def _query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        """Query LCM in range [l, r]."""
        # Range completely outside
        if start > r or end < l:
            return 1  # Identity for LCM

        # Range completely inside
        if l <= start and end <= r:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        left_lcm = self._query(2 * node + 1, start, mid, l, r)
        right_lcm = self._query(2 * node + 2, mid + 1, end, l, r)
        return self._lcm(left_lcm, right_lcm)

    def query(self, l: int, r: int) -> int:
        """
        Get LCM of elements in range [l, r].

        Args:
            l: Left index (inclusive)
            r: Right index (inclusive)

        Returns:
            LCM of all elements in range
        """
        if l < 0 or r >= self.n or l > r:
            raise ValueError("Invalid range")
        return self._query(0, 0, self.n - 1, l, r)

    def _update(self, node: int, start: int, end: int, idx: int, value: int) -> None:
        """Update element at index idx to value."""
        if start == end:
            self.arr[idx] = value
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self._update(2 * node + 1, start, mid, idx, value)
            else:
                self._update(2 * node + 2, mid + 1, end, idx, value)
            self.tree[node] = self._lcm(
                self.tree[2 * node + 1], self.tree[2 * node + 2]
            )

    def update(self, idx: int, value: int) -> None:
        """
        Update element at index to new value.

        Args:
            idx: Index to update
            value: New value
        """
        if idx < 0 or idx >= self.n:
            raise ValueError("Invalid index")
        self._update(0, 0, self.n - 1, idx, value)


def solve_range_lcm_queries(
    arr: List[int], queries: List[Tuple[int, int]]
) -> List[int]:
    """
    Solve multiple range LCM queries.

    Args:
        arr: Input array
        queries: List of (L, R) tuples

    Returns:
        List of LCM results for each query
    """
    rmq = RangeLCMQuery(arr)
    results = []
    for l, r in queries:
        results.append(rmq.query(l, r))
    return results


if __name__ == "__main__":
    # Test Case 1: Basic functionality
    print("=" * 50)
    print("Test Case 1: Basic Range LCM Queries")
    print("=" * 50)

    arr1 = [2, 7, 6, 5, 4]
    print(f"Array: {arr1}")

    rmq1 = RangeLCMQuery(arr1)
    queries1 = [(0, 2), (1, 4), (0, 4), (2, 3)]

    for l, r in queries1:
        result = rmq1.query(l, r)
        print(f"LCM({l}, {r}) = {result}")

    # Test Case 2: Update operation
    print("\n" + "=" * 50)
    print("Test Case 2: Update and Query")
    print("=" * 50)

    arr2 = [1, 2, 3, 4, 5]
    rmq2 = RangeLCMQuery(arr2)
    print(f"Initial array: {arr2}")
    print(f"LCM(0, 4) = {rmq2.query(0, 4)}")

    rmq2.update(2, 6)
    print(f"After updating index 2 to 6: {rmq2.arr}")
    print(f"LCM(0, 4) = {rmq2.query(0, 4)}")

    # Test Case 3: Edge cases
    print("\n" + "=" * 50)
    print("Test Case 3: Edge Cases")
    print("=" * 50)

    arr3 = [5]
    rmq3 = RangeLCMQuery(arr3)
    print(f"Single element array: {arr3}")
    print(f"LCM(0, 0) = {rmq3.query(0, 0)}")

    arr4 = [2, 4, 8, 16]
    rmq4 = RangeLCMQuery(arr4)
    print(f"\nPowers of 2: {arr4}")
    print(f"LCM(0, 3) = {rmq4.query(0, 3)}")

    arr5 = [7, 13, 17, 19]
    rmq5 = RangeLCMQuery(arr5)
    print(f"\nPrime numbers: {arr5}")
    print(f"LCM(0, 3) = {rmq5.query(0, 3)}")

    # Test Case 4: Batch queries
    print("\n" + "=" * 50)
    print("Test Case 4: Batch Query Processing")
    print("=" * 50)

    arr6 = [3, 4, 6, 8, 12, 15]
    queries6 = [(0, 2), (1, 3), (2, 5), (0, 5)]
    results = solve_range_lcm_queries(arr6, queries6)

    print(f"Array: {arr6}")
    print("Queries and Results:")
    for (l, r), res in zip(queries6, results):
        print(f"  LCM({l}, {r}) = {res}")

    print("\n" + "=" * 50)
    print("All tests completed successfully!")
    print("=" * 50)
