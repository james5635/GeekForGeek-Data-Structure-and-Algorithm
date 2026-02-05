"""
Range Minimum Query (Static Array)

Problem Description:
Range Minimum Query (RMQ) is a classic problem where we need to answer
queries about the minimum element in a given range [L, R] of a static array.
Since the array doesn't change, we can preprocess it to answer queries quickly.

This implementation provides three approaches:
1. Sparse Table - O(n log n) preprocessing, O(1) query
2. Segment Tree - O(n) preprocessing, O(log n) query, supports updates
3. Brute Force - O(1) preprocessing, O(n) query (for comparison)

Time Complexity:
- Sparse Table:
  - Preprocessing: O(n log n)
  - Query: O(1)
  - Space: O(n log n)

- Segment Tree:
  - Preprocessing: O(n)
  - Query: O(log n)
  - Space: O(n)
  - Update: O(log n) (advantage over sparse table)

Algorithm - Sparse Table:
1. Build table where st[j][i] = min of range [i, i+2^j-1]
2. For query [L,R], find largest k where 2^k <= R-L+1
3. Return min(st[k][L], st[k][R-2^k+1])

Algorithm - Segment Tree:
1. Build binary tree where each node stores min of a range
2. For query, traverse tree and combine relevant ranges
3. Each query visits at most 4*log(n) nodes
"""

import math
from typing import List, Optional


class SparseTableRMQ:
    """Sparse Table implementation for RMQ - O(1) query time."""

    def __init__(self, arr: List[int]):
        self.n = len(arr)

        if self.n == 0:
            self.log_table = []
            self.st = []
            return

        # Precompute logs
        self.log_table = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1

        self.k = self.log_table[self.n] + 1

        # Build sparse table
        self.st = [[0] * self.n for _ in range(self.k)]

        for i in range(self.n):
            self.st[0][i] = arr[i]

        for j in range(1, self.k):
            i = 0
            while i + (1 << j) <= self.n:
                self.st[j][i] = min(
                    self.st[j - 1][i], self.st[j - 1][i + (1 << (j - 1))]
                )
                i += 1

    def query(self, left: int, right: int) -> int:
        """O(1) range minimum query."""
        if left > right or left < 0 or right >= self.n:
            raise ValueError(f"Invalid range: [{left}, {right}]")

        j = self.log_table[right - left + 1]
        return min(self.st[j][left], self.st[j][right - (1 << j) + 1])


class SegmentTreeRMQ:
    """Segment Tree implementation for RMQ - O(log n) query time, supports updates."""

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.arr = arr.copy()

        if self.n == 0:
            self.tree = []
            return

        # Size of segment tree (next power of 2 * 2)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1

        # Tree array (1-indexed for easier navigation)
        self.tree = [float("inf")] * (2 * self.size)

        # Build tree
        self._build()

    def _build(self):
        """Build segment tree from array."""
        # Copy array to leaves
        for i in range(self.n):
            self.tree[self.size + i] = self.arr[i]

        # Build internal nodes
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, left: int, right: int) -> int:
        """
        O(log n) range minimum query.

        Args:
            left: Left index (inclusive)
            right: Right index (inclusive)
        """
        if left > right or left < 0 or right >= self.n:
            raise ValueError(f"Invalid range: [{left}, {right}]")

        # Convert to 0-indexed in tree leaves
        left += self.size
        right += self.size

        result = float("inf")

        while left <= right:
            # If left is right child, include it and move right
            if left % 2 == 1:
                result = min(result, self.tree[left])
                left += 1

            # If right is left child, include it and move left
            if right % 2 == 0:
                result = min(result, self.tree[right])
                right -= 1

            # Move to parents
            left //= 2
            right //= 2

        return result

    def update(self, index: int, value: int):
        """
        O(log n) point update.

        Args:
            index: Index to update
            value: New value
        """
        if index < 0 or index >= self.n:
            raise ValueError(f"Invalid index: {index}")

        # Update leaf
        pos = self.size + index
        self.tree[pos] = value
        self.arr[index] = value

        # Update ancestors
        pos //= 2
        while pos >= 1:
            new_val = min(self.tree[2 * pos], self.tree[2 * pos + 1])
            if self.tree[pos] == new_val:
                break  # No change needed further up
            self.tree[pos] = new_val
            pos //= 2

    def get_array(self) -> List[int]:
        """Return current array state."""
        return self.arr.copy()


def brute_force_rmq(arr: List[int], left: int, right: int) -> int:
    """Brute force RMQ for verification."""
    return min(arr[left : right + 1])


if __name__ == "__main__":
    # Test Case 1: Compare all approaches
    print("=" * 70)
    print("Test Case 1: Comparing RMQ Approaches")
    print("=" * 70)

    arr1 = [7, 2, 3, 0, 5, 10, 3, 12, 18, 1, 5, 8]

    st = SparseTableRMQ(arr1)
    seg_tree = SegmentTreeRMQ(arr1)

    print(f"Array: {arr1}")
    print(f"\nApproach Comparison:")
    print(f"  Sparse Table:  O(n log n) build, O(1) query, O(n log n) space")
    print(f"  Segment Tree:  O(n) build, O(log n) query, O(n) space, supports updates")
    print(f"  Brute Force:   O(1) build, O(n) query, O(1) space")

    queries1 = [
        (0, 4),  # min = 0
        (2, 6),  # min = 0
        (5, 8),  # min = 3
        (0, 11),  # min = 0
        (3, 3),  # min = 0
        (9, 11),  # min = 1
    ]

    print(f"\nQuery Results:")
    all_passed = True
    for i, (left, right) in enumerate(queries1):
        st_result = st.query(left, right)
        seg_result = seg_tree.query(left, right)
        brute_result = brute_force_rmq(arr1, left, right)

        st_ok = st_result == brute_result
        seg_ok = seg_result == brute_result

        if not (st_ok and seg_ok):
            all_passed = False

        print(
            f"  Query [{left:2d}, {right:2d}]: ST={st_result:2d}, Seg={seg_result:2d}, "
            f"Expected={brute_result:2d} - {'PASS' if st_ok and seg_ok else 'FAIL'}"
        )

    # Test Case 2: Segment Tree Updates
    print("\n" + "=" * 70)
    print("Test Case 2: Segment Tree Updates")
    print("=" * 70)

    arr2 = [5, 8, 2, 9, 1, 7, 3, 6]
    seg_tree2 = SegmentTreeRMQ(arr2)

    print(f"Initial array: {seg_tree2.get_array()}")

    # Query before update
    result1 = seg_tree2.query(0, 7)
    print(f"Query [0, 7] before update: {result1} (expected 1)")

    # Update index 4 from 1 to 20
    seg_tree2.update(4, 20)
    print(f"\nAfter update(4, 20): {seg_tree2.get_array()}")

    # Query after update
    result2 = seg_tree2.query(0, 7)
    expected2 = min([5, 8, 2, 9, 20, 7, 3, 6])
    print(
        f"Query [0, 7] after update: {result2} (expected {expected2}) - "
        f"{'PASS' if result2 == expected2 else 'FAIL'}"
    )

    # Query partial range
    result3 = seg_tree2.query(0, 3)
    expected3 = min([5, 8, 2, 9])
    print(
        f"Query [0, 3] after update: {result3} (expected {expected3}) - "
        f"{'PASS' if result3 == expected3 else 'FAIL'}"
    )

    # Test Case 3: Performance Comparison
    print("\n" + "=" * 70)
    print("Test Case 3: Performance Comparison")
    print("=" * 70)

    import random
    import time

    random.seed(42)
    large_arr = [random.randint(1, 1000000) for _ in range(100000)]
    num_queries = 100000

    # Generate queries
    queries = []
    for _ in range(num_queries):
        left = random.randint(0, len(large_arr) - 1)
        right = random.randint(left, len(large_arr) - 1)
        queries.append((left, right))

    print(f"Array size: {len(large_arr)}")
    print(f"Number of queries: {num_queries}")

    # Sparse Table
    start = time.time()
    st_large = SparseTableRMQ(large_arr)
    st_build = time.time() - start

    start = time.time()
    st_results = [st_large.query(l, r) for l, r in queries]
    st_query = time.time() - start

    # Segment Tree
    start = time.time()
    seg_large = SegmentTreeRMQ(large_arr)
    seg_build = time.time() - start

    start = time.time()
    seg_results = [seg_large.query(l, r) for l, r in queries]
    seg_query = time.time() - start

    # Verify correctness
    results_match = all(a == b for a, b in zip(st_results, seg_results))

    print(f"\nSparse Table:")
    print(f"  Build time: {st_build:.4f}s")
    print(f"  Query time: {st_query:.4f}s")
    print(f"  Avg query:  {(st_query / num_queries) * 1e6:.2f} μs")
    print(f"\nSegment Tree:")
    print(f"  Build time: {seg_build:.4f}s")
    print(f"  Query time: {seg_query:.4f}s")
    print(f"  Avg query:  {(seg_query / num_queries) * 1e6:.2f} μs")
    print(f"\nResults match: {'PASS' if results_match else 'FAIL'}")
    print(f"Query speedup (ST vs Seg): {seg_query / st_query:.2f}x")

    # Test Case 4: Edge Cases
    print("\n" + "=" * 70)
    print("Test Case 4: Edge Cases")
    print("=" * 70)

    # Single element
    arr3 = [42]
    st3 = SparseTableRMQ(arr3)
    seg3 = SegmentTreeRMQ(arr3)

    st_result = st3.query(0, 0)
    seg_result = seg3.query(0, 0)
    print(
        f"Single element [0, 0]: ST={st_result}, Seg={seg_result} - "
        f"{'PASS' if st_result == seg_result == 42 else 'FAIL'}"
    )

    # All same elements
    arr4 = [5] * 100
    st4 = SparseTableRMQ(arr4)
    seg4 = SegmentTreeRMQ(arr4)

    st_result = st4.query(10, 90)
    seg_result = seg4.query(10, 90)
    print(
        f"All same [10, 90]: ST={st_result}, Seg={seg_result} - "
        f"{'PASS' if st_result == seg_result == 5 else 'FAIL'}"
    )

    # Strictly decreasing
    arr5 = list(range(100, 0, -1))
    st5 = SparseTableRMQ(arr5)
    seg5 = SegmentTreeRMQ(arr5)

    st_result = st5.query(50, 99)
    seg_result = seg5.query(50, 99)
    expected = min(arr5[50:100])
    print(
        f"Decreasing [50, 99]: ST={st_result}, Seg={seg_result}, Expected={expected} - "
        f"{'PASS' if st_result == seg_result == expected else 'FAIL'}"
    )

    # Test Case 5: When to use which?
    print("\n" + "=" * 70)
    print("Test Case 5: Guidelines for Choosing an Approach")
    print("=" * 70)

    print("""
    Use Sparse Table when:
    - Array is static (no updates)
    - You need O(1) query time
    - Memory is not a constraint (O(n log n))
    - You have many queries
    
    Use Segment Tree when:
    - You need to support updates
    - Memory is constrained (O(n))
    - O(log n) query time is acceptable
    - You need a more general solution
    
    Use Brute Force when:
    - Array is very small
    - You have very few queries
    - Simplicity is more important than performance
    """)

    print("\nAll tests completed!")
