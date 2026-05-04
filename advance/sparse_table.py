"""
Sparse Table

Sparse Table is a data structure used for fast queries on static data
(elements do not change). It precomputes values for all subarrays whose
lengths are powers of two, enabling O(1) query time.

This implementation supports:
- Range Minimum Query (RMQ)
- Range GCD Query

Time Complexity:
  - Build: O(N * log N)
  - Query: O(1)
Space Complexity: O(N * log N)

Source: https://www.geeksforgeeks.org/dsa/sparse-table/
"""

import math


class SparseTableRMQ:
    """
    Sparse Table for Range Minimum Query on static arrays.
    """

    def __init__(self, arr):
        """
        Build the sparse table for range minimum queries.

        Args:
            arr: List of integers representing the input array.
        """
        self.n = len(arr)
        self.arr = arr
        self.max_log = int(math.log2(self.n)) + 1 if self.n > 0 else 0
        self.lookup = [[0] * self.max_log for _ in range(self.n)]

        self._build()

    def _build(self):
        """Build the lookup table in bottom-up manner."""
        # Initialize for intervals of length 1
        for i in range(self.n):
            self.lookup[i][0] = self.arr[i]

        # Compute values from smaller to bigger intervals
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                if self.lookup[i][j - 1] < self.lookup[i + (1 << (j - 1))][j - 1]:
                    self.lookup[i][j] = self.lookup[i][j - 1]
                else:
                    self.lookup[i][j] = self.lookup[i + (1 << (j - 1))][j - 1]
                i += 1
            j += 1

    def query(self, l, r):
        """
        Return the minimum value in arr[l..r].

        Args:
            l: Left boundary (inclusive, 0-based).
            r: Right boundary (inclusive, 0-based).

        Returns:
            Minimum value in the range [l, r].

        Time Complexity: O(1)
        """
        j = int(math.log2(r - l + 1))

        if self.lookup[l][j] <= self.lookup[r - (1 << j) + 1][j]:
            return self.lookup[l][j]
        else:
            return self.lookup[r - (1 << j) + 1][j]


class SparseTableGCD:
    """
    Sparse Table for Range GCD Query on static arrays.
    """

    @staticmethod
    def _gcd(a, b):
        """Compute GCD of two numbers using Euclidean algorithm."""
        while b:
            a, b = b, a % b
        return a

    def __init__(self, arr):
        """
        Build the sparse table for range GCD queries.

        Args:
            arr: List of integers representing the input array.
        """
        self.n = len(arr)
        self.arr = arr
        self.max_log = int(math.log2(self.n)) + 1 if self.n > 0 else 0
        self.lookup = [[0] * self.max_log for _ in range(self.n)]

        self._build()

    def _build(self):
        """Build the lookup table in bottom-up manner."""
        # GCD of single element is the element itself
        for i in range(self.n):
            self.lookup[i][0] = self.arr[i]

        # Build sparse table
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while i <= self.n - (1 << j):
                self.lookup[i][j] = self._gcd(
                    self.lookup[i][j - 1], self.lookup[i + (1 << (j - 1))][j - 1]
                )
                i += 1
            j += 1

    def query(self, l, r):
        """
        Return the GCD of all elements in arr[l..r].

        Args:
            l: Left boundary (inclusive, 0-based).
            r: Right boundary (inclusive, 0-based).

        Returns:
            GCD of all elements in the range [l, r].

        Time Complexity: O(1)
        """
        j = int(math.log2(r - l + 1))

        return self._gcd(self.lookup[l][j], self.lookup[r - (1 << j) + 1][j])


def solve_rmq_queries(arr, queries):
    """
    Solve multiple range minimum queries.

    Args:
        arr: List of integers.
        queries: List of [L, R] pairs.

    Returns:
        List of minimum values for each query.
    """
    table = SparseTableRMQ(arr)
    return [table.query(l, r) for l, r in queries]


def solve_gcd_queries(arr, queries):
    """
    Solve multiple range GCD queries.

    Args:
        arr: List of integers.
        queries: List of [L, R] pairs.

    Returns:
        List of GCD values for each query.
    """
    table = SparseTableGCD(arr)
    return [table.query(l, r) for l, r in queries]


if __name__ == "__main__":
    # Example 1: Range Minimum Query from GeeksforGeeks
    print("=== Example 1: Range Minimum Query ===")
    arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    queries = [[0, 4], [4, 7], [7, 8]]

    print(f"Array: {arr}")
    print(f"Queries: {queries}")
    print()

    table = SparseTableRMQ(arr)
    results = [table.query(l, r) for l, r in queries]
    print("Results:", " ".join(map(str, results)))

    # Example 2: Range GCD Query from GeeksforGeeks
    print("\n=== Example 2: Range GCD Query ===")
    arr2 = [2, 3, 5, 4, 6, 8]
    queries2 = [[0, 2], [3, 5], [2, 3]]

    print(f"Array: {arr2}")
    print(f"Queries: {queries2}")
    print()

    gcd_table = SparseTableGCD(arr2)
    gcd_results = [gcd_table.query(l, r) for l, r in queries2]
    print("Results:", " ".join(map(str, gcd_results)))

    # Example 3: Verification with brute force
    print("\n=== Example 3: RMQ Verification ===")
    arr3 = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    table3 = SparseTableRMQ(arr3)

    test_queries = [[0, 4], [4, 7], [7, 8], [0, 8], [2, 5]]
    for l, r in test_queries:
        result = table3.query(l, r)
        brute_force = min(arr3[l : r + 1])
        match = "PASS" if result == brute_force else "FAIL"
        print(
            f"query({l}, {r}): SparseTable={result}, Brute Force={brute_force} [{match}]"
        )

    print("\n=== Example 4: GCD Verification ===")
    arr4 = [2, 3, 5, 4, 6, 8]
    gcd_table4 = SparseTableGCD(arr4)

    gcd_queries = [[0, 2], [3, 5], [2, 3], [0, 5], [1, 4]]
    for l, r in gcd_queries:
        from functools import reduce

        result = gcd_table4.query(l, r)
        brute_force = reduce(math.gcd, arr4[l : r + 1])
        match = "PASS" if result == brute_force else "FAIL"
        print(
            f"query({l}, {r}): SparseTable={result}, Brute Force={brute_force} [{match}]"
        )
