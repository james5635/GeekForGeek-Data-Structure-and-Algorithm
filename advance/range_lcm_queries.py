"""
Range LCM Queries using Segment Tree

A Segment Tree is used to efficiently answer range LCM (Least Common Multiple) queries
on a static array. Each node in the tree stores the LCM value for its segment.

The LCM of two numbers a and b is computed as: LCM(a, b) = (a * b) / GCD(a, b)

Time Complexity:
    - Build: O(n * log(max_value))
    - Query: O(log n * log(max_value))
    - Space: O(n)
"""

import math


def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    """Return the least common multiple of a and b."""
    return (a * b) // gcd(a, b)


class RangeLCMQuery:
    """Segment Tree for efficient range LCM queries."""

    def __init__(self, arr):
        """
        Build the segment tree from the given array.

        Args:
            arr: List of integers
        """
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(1, 0, self.n - 1)

    def _build(self, node, start, end):
        """Build the segment tree recursively."""
        if start == end:
            self.tree[node] = self.arr[start]
            return

        mid = (start + end) // 2
        self._build(2 * node, start, mid)
        self._build(2 * node + 1, mid + 1, end)

        left_lcm = self.tree[2 * node]
        right_lcm = self.tree[2 * node + 1]
        self.tree[node] = lcm(left_lcm, right_lcm)

    def query(self, l, r):
        """
        Return the LCM of elements in range [l, r] (0-indexed, inclusive).

        Args:
            l: Left boundary of the range
            r: Right boundary of the range

        Returns:
            LCM of all elements from index l to r
        """
        if l > r or l < 0 or r >= self.n:
            return 1
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        """Query the segment tree recursively."""
        if end < l or start > r:
            return 1

        if l <= start and r >= end:
            return self.tree[node]

        mid = (start + end) // 2
        left_lcm = self._query(2 * node, start, mid, l, r)
        right_lcm = self._query(2 * node + 1, mid + 1, end, l, r)
        return lcm(left_lcm, right_lcm)


if __name__ == "__main__":
    arr = [5, 7, 5, 2, 10, 12, 11, 17, 14, 1, 44]
    n = len(arr)

    lcm_tree = RangeLCMQuery(arr)

    print(f"Array: {arr}")
    print()

    queries = [(2, 5), (5, 10), (0, 10)]
    for l, r in queries:
        result = lcm_tree.query(l, r)
        print(f"LCM of range [{l}, {r}] = {result}")

    print()
    print("Expected Output:")
    print("LCM of range [2, 5] = 60")
    print("LCM of range [5, 10] = 15708")
    print("LCM of range [0, 10] = 78540")

    print()
    print("--- Additional Test Case ---")
    arr2 = [2, 4, 8, 16]
    lcm_tree2 = RangeLCMQuery(arr2)
    queries2 = [(2, 3), (0, 1)]
    for l, r in queries2:
        result = lcm_tree2.query(l, r)
        print(f"LCM of range [{l}, {r}] = {result}")

    print()
    print("Expected Output:")
    print("LCM of range [2, 3] = 16")
    print("LCM of range [0, 1] = 4")
