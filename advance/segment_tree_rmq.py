"""
Segment Tree - Range Minimum Query (RMQ)

Given an array arr[0..n-1], efficiently find the minimum value from
index qs (query start) to qe (query end) where 0 <= qs <= qe <= n-1.

Approach: Build a segment tree where leaf nodes store array elements
and internal nodes store the minimum of their children. Range queries
are answered in O(log n) time.

- Tree Construction: O(n) time, O(n) space
- Range Query: O(log n) time

Source: https://www.geeksforgeeks.org/dsa/segment-tree-range-minimum-query/
"""

import math


class SegmentTreeRMQ:
    """Segment Tree for Range Minimum Query operations."""

    def __init__(self, arr):
        """Initialize segment tree with the given array.

        Args:
            arr: A list of integers.
        """
        self.arr = arr
        self.n = len(arr)
        if self.n == 0:
            self.tree = []
            return

        height = math.ceil(math.log2(self.n))
        max_size = 2 * (2**height) - 1
        self.tree = [0] * max_size
        self._build(0, 0, self.n - 1)

    def _build(self, node, start, end):
        """Recursively build the segment tree.

        Args:
            node: Current node index in the tree array.
            start: Start index of the current segment.
            end: End index of the current segment.

        Returns:
            The minimum value in the current segment.
        """
        if start == end:
            self.tree[node] = self.arr[start]
            return self.arr[start]

        mid = start + (end - start) // 2
        left_min = self._build(2 * node + 1, start, mid)
        right_min = self._build(2 * node + 2, mid + 1, end)
        self.tree[node] = min(left_min, right_min)
        return self.tree[node]

    def query(self, qs, qe):
        """Find the minimum value in the range [qs, qe].

        Args:
            qs: Query start index (0-based, inclusive).
            qe: Query end index (0-based, inclusive).

        Returns:
            The minimum value in arr[qs..qe], or -1 for invalid input.
        """
        if qs < 0 or qe > self.n - 1 or qs > qe:
            print("Invalid Input")
            return -1
        return self._query_util(0, 0, self.n - 1, qs, qe)

    def _query_util(self, node, start, end, qs, qe):
        """Recursive helper for range minimum query.

        Args:
            node: Current node index in the tree array.
            start: Start index of the current segment.
            end: End index of the current segment.
            qs: Query start index.
            qe: Query end index.

        Returns:
            The minimum value in the intersection of [start, end] and [qs, qe].
        """
        if qs <= start and qe >= end:
            return self.tree[node]

        if end < qs or start > qe:
            return float("inf")

        mid = start + (end - start) // 2
        left_min = self._query_util(2 * node + 1, start, mid, qs, qe)
        right_min = self._query_util(2 * node + 2, mid + 1, end, qs, qe)
        return min(left_min, right_min)

    def update(self, index, new_val):
        """Update a value in the array and the segment tree.

        Args:
            index: Index in the array to update.
            new_val: The new value to set.
        """
        if index < 0 or index >= self.n:
            print("Invalid Input")
            return
        self.arr[index] = new_val
        self._update_util(0, 0, self.n - 1, index, new_val)

    def _update_util(self, node, start, end, index, new_val):
        """Recursive helper for updating the segment tree.

        Args:
            node: Current node index in the tree array.
            start: Start index of the current segment.
            end: End index of the current segment.
            index: Index in the array to update.
            new_val: The new value to set.
        """
        if start == end:
            self.tree[node] = new_val
            return

        mid = start + (end - start) // 2
        if index <= mid:
            self._update_util(2 * node + 1, start, mid, index, new_val)
        else:
            self._update_util(2 * node + 2, mid + 1, end, index, new_val)

        self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])


def construct_st(arr):
    """Functional interface to construct a segment tree.

    Args:
        arr: A list of integers.

    Returns:
        A SegmentTreeRMQ object.
    """
    return SegmentTreeRMQ(arr)


def rmq(st, qs, qe):
    """Functional interface for range minimum query.

    Args:
        st: A SegmentTreeRMQ object.
        qs: Query start index.
        qe: Query end index.

    Returns:
        The minimum value in the range.
    """
    return st.query(qs, qe)


if __name__ == "__main__":
    print("Test Case 1:")
    arr = [1, 3, 2, 7, 9, 11]
    print(f"Array: {arr}")

    st = construct_st(arr)

    qs, qe = 1, 5
    result = rmq(st, qs, qe)
    print(f"Minimum of values in range [{qs}, {qe}] is = {result}")

    qs, qe = 0, 3
    result = rmq(st, qs, qe)
    print(f"Minimum of values in range [{qs}, {qe}] is = {result}")

    print("\nTest Case 2:")
    arr2 = [10, 20, 5, 30, 15, 25, 8]
    print(f"Array: {arr2}")

    st2 = construct_st(arr2)

    for qs, qe in [(0, 6), (2, 4), (1, 3), (5, 5)]:
        result = rmq(st2, qs, qe)
        print(f"Minimum of values in range [{qs}, {qe}] is = {result}")

    print("\nTest Case 3 (with update):")
    arr3 = [1, 3, 2, 7, 9, 11]
    print(f"Original array: {arr3}")

    st3 = construct_st(arr3)
    print(f"Min in range [0, 5]: {rmq(st3, 0, 5)}")

    st3.update(2, 0)
    print(f"After updating index 2 to 0: {st3.arr}")
    print(f"Min in range [0, 5]: {rmq(st3, 0, 5)}")
    print(f"Min in range [1, 3]: {rmq(st3, 1, 3)}")

    print("\nTest Case 4 (invalid input):")
    result = rmq(st, -1, 3)
    result = rmq(st, 3, 2)
