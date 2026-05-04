"""
Merge Sort Tree for Range Order Statistics

A Merge Sort Tree is a segment tree where each node stores a sorted list of elements
in its range. It allows answering k-th smallest number queries in a range efficiently.

The tree is built by sorting pairs of (value, index) and storing indices at each node.
For a query, we use binary search to determine how many elements in the left subtree
fall within the query range, then decide whether to go left or right.

Time Complexity:
    - Build: O(n log n)
    - Query: O(log^2 n)
    - Space: O(n log n)
"""

import bisect


class MergeSortTree:
    """Merge Sort Tree for k-th smallest element queries in a range."""

    def __init__(self, arr):
        """
        Build the Merge Sort Tree from the given array.

        Args:
            arr: List of integers
        """
        self.arr = arr
        self.n = len(arr)
        if self.n == 0:
            self.tree = []
            return

        sorted_pairs = sorted((arr[i], i) for i in range(self.n))

        self.tree = [[] for _ in range(4 * self.n)]
        self._build(1, 0, self.n - 1, sorted_pairs)

    def _build(self, node, l, r, sorted_pairs):
        """Build the merge sort tree recursively."""
        if l == r:
            self.tree[node].append(sorted_pairs[l][1])
            return

        mid = (l + r) // 2
        self._build(2 * node, l, mid, sorted_pairs)
        self._build(2 * node + 1, mid + 1, r, sorted_pairs)

        self.tree[node] = sorted(self.tree[2 * node] + self.tree[2 * node + 1])

    def kth_smallest(self, start, end, k):
        """
        Find the k-th smallest element in range [start, end] (1-indexed range, k-th smallest).

        Args:
            start: Start of the query range (1-indexed)
            end: End of the query range (1-indexed)
            k: Which smallest element to find (1-indexed)

        Returns:
            The k-th smallest element in the given range
        """
        query_start = start - 1
        query_end = end - 1
        index = self._query(0, self.n - 1, query_start, query_end, 1, k)
        return self.arr[index]

    def _query(self, seg_start, seg_end, query_start, query_end, node, k):
        """Recursively find the k-th smallest element index."""
        if seg_start == seg_end:
            return self.tree[node][0]

        mid = (seg_start + seg_end) // 2

        left_child = self.tree[2 * node]

        last_in_range = bisect.bisect_right(left_child, query_end)
        first_in_range = bisect.bisect_left(left_child, query_start)

        m = last_in_range - first_in_range

        if m >= k:
            return self._query(seg_start, mid, query_start, query_end, 2 * node, k)
        else:
            return self._query(
                mid + 1, seg_end, query_start, query_end, 2 * node + 1, k - m
            )


if __name__ == "__main__":
    arr = [3, 2, 5, 1, 8, 9]
    n = len(arr)

    mst = MergeSortTree(arr)

    print(f"Array: {arr}")
    print()

    print("Query 1: range [2, 5], k = 2")
    result1 = mst.kth_smallest(2, 5, 2)
    print(f"Result: {result1}")
    print(
        f"Explanation: Subarray [2, 5, 1, 8] -> sorted [1, 2, 5, 8], 2nd smallest = 2"
    )

    print()
    print("Query 2: range [1, 6], k = 4")
    result2 = mst.kth_smallest(1, 6, 4)
    print(f"Result: {result2}")
    print(
        f"Explanation: Subarray [3, 2, 5, 1, 8, 9] -> sorted [1, 2, 3, 5, 8, 9], 4th smallest = 5"
    )

    print()
    print("Expected Output:")
    print("2")
    print("5")
