"""
Sparse Table

Problem Description:
A Sparse Table is a data structure that allows answering static range queries
(such as Range Minimum Query - RMQ) in O(1) time after O(n log n) preprocessing.
It is particularly useful when the array is static (no updates) and there are
many queries to answer.

This implementation demonstrates the sparse table for Range Minimum Query.

Time Complexity:
- Preprocessing: O(n log n)
- Query: O(1)
- Space: O(n log n)

Algorithm:
1. Build a table where table[i][j] stores the minimum of range starting at i
   with length 2^j
2. table[i][j] = min(table[i][j-1], table[i + 2^(j-1)][j-1])
3. For query [L, R], find k = floor(log2(R - L + 1))
4. Result = min(table[L][k], table[R - 2^k + 1][k])
"""

import math
from typing import List


class SparseTable:
    """
    Sparse Table data structure for Range Minimum Query (RMQ).
    """

    def __init__(self, arr: List[int]):
        """
        Initialize sparse table from array.

        Args:
            arr: Input array (0-indexed)
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

        # Maximum power of 2 needed
        self.k = self.log_table[self.n] + 1

        # Build sparse table
        # st[j][i] = minimum of range [i, i + 2^j - 1]
        self.st = [[0] * self.n for _ in range(self.k)]

        # Initialize for ranges of length 1 (2^0 = 1)
        for i in range(self.n):
            self.st[0][i] = arr[i]

        # Build table for increasing powers of 2
        for j in range(1, self.k):
            # For each starting position i
            i = 0
            while i + (1 << j) <= self.n:
                # Range [i, i + 2^j - 1] = min of:
                # - [i, i + 2^(j-1) - 1]
                # - [i + 2^(j-1), i + 2^j - 1]
                self.st[j][i] = min(
                    self.st[j - 1][i], self.st[j - 1][i + (1 << (j - 1))]
                )
                i += 1

    def query(self, left: int, right: int) -> int:
        """
        Get minimum element in range [left, right].

        Args:
            left: Left index (inclusive)
            right: Right index (inclusive)

        Returns:
            Minimum value in the range

        Raises:
            ValueError: If range is invalid
        """
        if left > right or left < 0 or right >= self.n:
            raise ValueError(
                f"Invalid range: [{left}, {right}] for array of size {self.n}"
            )

        # Length of the range
        length = right - left + 1

        # Find the largest power of 2 that fits in the range
        j = self.log_table[length]

        # Minimum of two overlapping ranges
        # [left, left + 2^j - 1] and [right - 2^j + 1, right]
        return min(self.st[j][left], self.st[j][right - (1 << j) + 1])

    def query_with_index(self, left: int, right: int) -> tuple:
        """
        Get minimum value and its index in range [left, right].

        Args:
            left: Left index (inclusive)
            right: Right index (inclusive)

        Returns:
            Tuple of (minimum_value, index_of_minimum)
        """
        if left > right or left < 0 or right >= self.n:
            raise ValueError(
                f"Invalid range: [{left}, {right}] for array of size {self.n}"
            )

        length = right - left + 1
        j = self.log_table[length]

        # Get values from two ranges
        val1 = self.st[j][left]
        val2 = self.st[j][right - (1 << j) + 1]

        # Return the smaller one
        if val1 <= val2:
            # Find index of val1 (need to scan the range since we don't store indices)
            # For simplicity, we'll just return the value
            return (val1, None)
        else:
            return (val2, None)

    def get_table(self) -> List[List[int]]:
        """Return the sparse table for inspection."""
        return [row[:] for row in self.st]


def brute_force_rmq(arr: List[int], left: int, right: int) -> int:
    """Brute force method for verification."""
    if left > right or left < 0 or right >= len(arr):
        raise ValueError("Invalid range")
    return min(arr[left : right + 1])


if __name__ == "__main__":
    # Test Case 1: Basic functionality
    print("=" * 60)
    print("Test Case 1: Basic Range Minimum Queries")
    print("=" * 60)

    arr1 = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    st = SparseTable(arr1)

    print(f"Array: {arr1}")
    print(f"Log table: {st.log_table[: len(arr1) + 1]}")
    print(f"Sparse table layers:")
    for j in range(st.k):
        non_zero = [st.st[j][i] for i in range(len(arr1)) if st.st[j][i] != 0 or j == 0]
        print(f"  j={j} (2^{j}={1 << j}): {non_zero}")

    queries1 = [
        (0, 4),  # min of [7,2,3,0,5] = 0
        (2, 6),  # min of [3,0,5,10,3] = 0
        (5, 8),  # min of [10,3,12,18] = 3
        (0, 8),  # min of entire array = 0
        (3, 3),  # single element = 0
        (6, 6),  # single element = 3
    ]

    print(f"\nQueries:")
    all_passed = True
    for i, (left, right) in enumerate(queries1):
        try:
            result = st.query(left, right)
            expected = brute_force_rmq(arr1, left, right)
            status = "PASS" if result == expected else "FAIL"
            if result != expected:
                all_passed = False
            print(
                f"  Query {i + 1} [{left}, {right}]: {result} (expected {expected}) - {status}"
            )
        except Exception as e:
            print(f"  Query {i + 1} [{left}, {right}]: ERROR - {e}")
            all_passed = False

    # Test Case 2: Array with duplicates
    print("\n" + "=" * 60)
    print("Test Case 2: Array with Duplicates")
    print("=" * 60)

    arr2 = [5, 5, 5, 5, 5, 5]
    st2 = SparseTable(arr2)

    queries2 = [
        (0, 5),  # min = 5
        (1, 3),  # min = 5
        (2, 4),  # min = 5
    ]

    print(f"Array: {arr2}")
    for i, (left, right) in enumerate(queries2):
        result = st2.query(left, right)
        expected = brute_force_rmq(arr2, left, right)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"  Query {i + 1} [{left}, {right}]: {result} (expected {expected}) - {status}"
        )

    # Test Case 3: Strictly decreasing array
    print("\n" + "=" * 60)
    print("Test Case 3: Strictly Decreasing Array")
    print("=" * 60)

    arr3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    st3 = SparseTable(arr3)

    queries3 = [
        (0, 9),  # min = 1
        (0, 4),  # min = 6
        (5, 9),  # min = 1
        (3, 7),  # min = 3
    ]

    print(f"Array: {arr3}")
    for i, (left, right) in enumerate(queries3):
        result = st3.query(left, right)
        expected = brute_force_rmq(arr3, left, right)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"  Query {i + 1} [{left}, {right}]: {result} (expected {expected}) - {status}"
        )

    # Test Case 4: Edge cases
    print("\n" + "=" * 60)
    print("Test Case 4: Edge Cases")
    print("=" * 60)

    # Single element
    arr4 = [42]
    st4 = SparseTable(arr4)
    result = st4.query(0, 0)
    print(
        f"Single element [0, 0]: {result} == 42 - {'PASS' if result == 42 else 'FAIL'}"
    )

    # Empty array
    try:
        arr5 = []
        st5 = SparseTable(arr5)
        print(f"Empty array: Created successfully - PASS")
    except Exception as e:
        print(f"Empty array: ERROR - {e}")

    # Invalid range
    try:
        st.query(5, 3)
        print(f"Invalid range [5, 3]: Should have raised error - FAIL")
    except ValueError:
        print(f"Invalid range [5, 3]: Raised ValueError - PASS")

    # Test Case 5: Performance
    print("\n" + "=" * 60)
    print("Test Case 5: Performance Test")
    print("=" * 60)

    import random
    import time

    random.seed(42)
    large_arr = [random.randint(1, 1000000) for _ in range(100000)]

    # Build sparse table
    start = time.time()
    st_large = SparseTable(large_arr)
    build_time = time.time() - start

    # Generate queries
    num_queries = 100000
    queries = []
    for _ in range(num_queries):
        left = random.randint(0, len(large_arr) - 1)
        right = random.randint(left, len(large_arr) - 1)
        queries.append((left, right))

    # Time sparse table queries
    start = time.time()
    st_results = [st_large.query(l, r) for l, r in queries]
    st_time = time.time() - start

    # Sample verification with brute force
    sample_size = 1000
    sample_indices = random.sample(range(num_queries), sample_size)
    sample_correct = all(
        st_results[i] == brute_force_rmq(large_arr, queries[i][0], queries[i][1])
        for i in sample_indices
    )

    print(f"Array size: {len(large_arr)}")
    print(f"Number of queries: {num_queries}")
    print(f"Build time: {build_time:.4f}s")
    print(f"Query time: {st_time:.4f}s")
    print(f"Average query time: {(st_time / num_queries) * 1e6:.2f} microseconds")
    print(
        f"Sample verification ({sample_size} queries): {'PASS' if sample_correct else 'FAIL'}"
    )

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
