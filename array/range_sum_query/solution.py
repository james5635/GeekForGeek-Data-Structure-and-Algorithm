"""
Range Sum Query using Sparse Table

Problem Description:
This implementation demonstrates using a Sparse Table for Range Sum Queries.
However, it's important to note that Sparse Tables are not ideal for sum queries
because they cannot handle overlapping ranges efficiently (unlike RMQ).

For sum queries, a better approach would be to use:
1. Prefix sums (O(1) query, O(n) preprocessing)
2. Segment tree (O(log n) query, O(n) preprocessing, supports updates)

This implementation is for educational purposes to show how Sparse Tables work,
and includes a comparison with the prefix sum approach.

Time Complexity:
- Sparse Table approach:
  - Preprocessing: O(n log n)
  - Query: O(log n) - not O(1) because sum is not idempotent
- Prefix Sum approach:
  - Preprocessing: O(n)
  - Query: O(1)

Space Complexity:
- Sparse Table: O(n log n)
- Prefix Sum: O(n)

Note: For range sum queries, prefix sums are the optimal solution for static arrays.
This implementation includes both for comparison and educational purposes.
"""

import math
from typing import List


class RangeSumSparseTable:
    """
    Sparse Table for Range Sum Query (educational implementation).

    Note: This is NOT the optimal approach for sum queries.
    Use prefix sums instead for O(1) queries.
    """

    def __init__(self, arr: List[int]):
        """
        Initialize sparse table for range sum.

        Args:
            arr: Input array
        """
        self.n = len(arr)

        if self.n == 0:
            self.log_table = []
            self.st = []
            return

        # Precompute logarithms
        self.log_table = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1

        self.k = self.log_table[self.n] + 1

        # Build sparse table
        # st[j][i] = sum of range [i, i + 2^j - 1]
        self.st = [[0] * self.n for _ in range(self.k)]

        # Initialize for ranges of length 1
        for i in range(self.n):
            self.st[0][i] = arr[i]

        # Build table for increasing powers of 2
        for j in range(1, self.k):
            i = 0
            while i + (1 << j) <= self.n:
                self.st[j][i] = self.st[j - 1][i] + self.st[j - 1][i + (1 << (j - 1))]
                i += 1

    def query(self, left: int, right: int) -> int:
        """
        Get sum of elements in range [left, right].

        Note: This takes O(log n) because we need to combine non-overlapping ranges.
        """
        if left > right or left < 0 or right >= self.n:
            raise ValueError(f"Invalid range: [{left}, {right}]")

        result = 0
        length = right - left + 1

        # Decompose range into powers of 2 (like binary representation)
        j = self.k - 1
        while length > 0:
            if length >= (1 << j):
                result += self.st[j][left]
                left += 1 << j
                length -= 1 << j
            j -= 1

        return result


class PrefixSum:
    """
    Optimal solution for Range Sum Query using prefix sums.
    """

    def __init__(self, arr: List[int]):
        """
        Initialize prefix sum array.

        Args:
            arr: Input array
        """
        self.n = len(arr)
        self.prefix = [0] * (self.n + 1)

        for i in range(self.n):
            self.prefix[i + 1] = self.prefix[i] + arr[i]

    def query(self, left: int, right: int) -> int:
        """
        Get sum of elements in range [left, right] in O(1).
        """
        if left > right or left < 0 or right >= self.n:
            raise ValueError(f"Invalid range: [{left}, {right}]")

        return self.prefix[right + 1] - self.prefix[left]


def brute_force_sum(arr: List[int], left: int, right: int) -> int:
    """Brute force method for verification."""
    return sum(arr[left : right + 1])


if __name__ == "__main__":
    # Test Case 1: Compare Sparse Table vs Prefix Sum
    print("=" * 60)
    print("Test Case 1: Comparing Approaches")
    print("=" * 60)

    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    st = RangeSumSparseTable(arr1)
    ps = PrefixSum(arr1)

    print(f"Array: {arr1}")
    print(f"\nApproach Comparison:")
    print(f"  Sparse Table:")
    print(f"    - Preprocessing: O(n log n)")
    print(f"    - Query: O(log n)")
    print(f"    - Space: O(n log n)")
    print(f"  Prefix Sum:")
    print(f"    - Preprocessing: O(n)")
    print(f"    - Query: O(1)")
    print(f"    - Space: O(n)")

    queries1 = [
        (0, 4),  # Sum = 15
        (2, 6),  # Sum = 25
        (5, 9),  # Sum = 40
        (0, 9),  # Sum = 55
        (3, 3),  # Sum = 4
    ]

    print(f"\nQuery Results:")
    all_passed = True
    for i, (left, right) in enumerate(queries1):
        st_result = st.query(left, right)
        ps_result = ps.query(left, right)
        expected = brute_force_sum(arr1, left, right)

        st_ok = st_result == expected
        ps_ok = ps_result == expected

        if not (st_ok and ps_ok):
            all_passed = False

        print(f"  Query [{left}, {right}]:")
        print(f"    Expected: {expected}")
        print(f"    Sparse Table: {st_result} - {'PASS' if st_ok else 'FAIL'}")
        print(f"    Prefix Sum: {ps_result} - {'PASS' if ps_ok else 'FAIL'}")

    # Test Case 2: Performance Comparison
    print("\n" + "=" * 60)
    print("Test Case 2: Performance Comparison")
    print("=" * 60)

    import random
    import time

    random.seed(42)
    large_arr = [random.randint(1, 1000) for _ in range(100000)]
    num_queries = 10000

    # Generate queries
    queries = []
    for _ in range(num_queries):
        left = random.randint(0, len(large_arr) - 1)
        right = random.randint(left, len(large_arr) - 1)
        queries.append((left, right))

    # Time Sparse Table
    start = time.time()
    st_large = RangeSumSparseTable(large_arr)
    st_build_time = time.time() - start

    start = time.time()
    st_results = [st_large.query(l, r) for l, r in queries]
    st_query_time = time.time() - start

    # Time Prefix Sum
    start = time.time()
    ps_large = PrefixSum(large_arr)
    ps_build_time = time.time() - start

    start = time.time()
    ps_results = [ps_large.query(l, r) for l, r in queries]
    ps_query_time = time.time() - start

    # Verify correctness
    st_correct = all(a == b for a, b in zip(st_results, ps_results))

    print(f"Array size: {len(large_arr)}")
    print(f"Number of queries: {num_queries}")
    print(f"\nSparse Table:")
    print(f"  Build time: {st_build_time:.4f}s")
    print(f"  Query time: {st_query_time:.4f}s")
    print(f"  Average query: {(st_query_time / num_queries) * 1e6:.2f} μs")
    print(f"\nPrefix Sum:")
    print(f"  Build time: {ps_build_time:.4f}s")
    print(f"  Query time: {ps_query_time:.4f}s")
    print(f"  Average query: {(ps_query_time / num_queries) * 1e6:.2f} μs")
    print(f"\nResults match: {'PASS' if st_correct else 'FAIL'}")
    print(f"Speedup (query): {st_query_time / ps_query_time:.2f}x")

    # Test Case 3: Edge Cases
    print("\n" + "=" * 60)
    print("Test Case 3: Edge Cases")
    print("=" * 60)

    # Single element
    arr2 = [42]
    st2 = RangeSumSparseTable(arr2)
    ps2 = PrefixSum(arr2)

    st_result = st2.query(0, 0)
    ps_result = ps2.query(0, 0)
    print(
        f"Single element [0, 0]: ST={st_result}, PS={ps_result} - {'PASS' if st_result == ps_result == 42 else 'FAIL'}"
    )

    # Empty array
    arr3 = []
    st3 = RangeSumSparseTable(arr3)
    ps3 = PrefixSum(arr3)
    print(f"Empty array: Both initialized - PASS")

    # Large values
    arr4 = [1000000] * 1000
    st4 = RangeSumSparseTable(arr4)
    ps4 = PrefixSum(arr4)
    st_result = st4.query(0, 999)
    ps_result = ps4.query(0, 999)
    expected = 1000000 * 1000
    print(
        f"Large values [0, 999]: ST={st_result}, PS={ps_result}, Expected={expected} - {'PASS' if st_result == ps_result == expected else 'FAIL'}"
    )

    # Test Case 4: Why Sparse Table is not ideal for sum
    print("\n" + "=" * 60)
    print("Test Case 4: Educational - Why O(log n) for Sum?")
    print("=" * 60)

    arr5 = [1, 2, 3, 4, 5, 6, 7, 8]
    st5 = RangeSumSparseTable(arr5)

    print(f"Array: {arr5}")
    print(f"\nSparse Table structure:")
    for j in range(st5.k):
        row = []
        for i in range(st5.n):
            if i + (1 << j) <= st5.n:
                row.append(st5.st[j][i])
        print(f"  j={j} (length {1 << j}): {row}")

    print(f"\nQuery [0, 5] (sum should be 21):")
    print(f"  Binary decomposition of length 6: 6 = 4 + 2 = 2^2 + 2^1")
    print(f"  Need to sum 2 ranges: [0,3] + [4,5]")
    print(
        f"  Result: st[2][0] + st[1][4] = {st5.st[2][0]} + {st5.st[1][4]} = {st5.st[2][0] + st5.st[1][4]}"
    )

    result = st5.query(0, 5)
    print(f"  Actual query result: {result}")

    print("\n" + "=" * 60)
    print("Conclusion: Use Prefix Sums for Range Sum Query!")
    print("=" * 60)

    print("\nAll tests completed!")
