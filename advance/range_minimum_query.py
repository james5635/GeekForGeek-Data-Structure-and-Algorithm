"""
Range Minimum Query (RMQ) using Sparse Table

Sparse Table is a data structure that allows answering range minimum queries
efficiently on a static array (no updates). It preprocesses the array in O(n log n)
time and answers each query in O(1) time.

The idea is to precompute minimums of all subarrays of size 2^j where j varies
from 0 to log n. For a query [L, R], we find the largest power of 2 that fits
in the range and compare two overlapping intervals.

Time Complexity:
    - Preprocessing: O(n log n)
    - Query: O(1)
    - Space: O(n log n)
"""

import math


class RangeMinimumQuery:
    """Sparse Table for efficient range minimum queries on static arrays."""

    def __init__(self, arr):
        """
        Build the sparse table from the given array.

        Args:
            arr: List of integers
        """
        self.n = len(arr)
        self.arr = arr
        if self.n == 0:
            self.lookup = []
            return

        self.k = int(math.floor(math.log2(self.n))) if self.n > 1 else 0
        self.lookup = [[0] * (self.k + 1) for _ in range(self.n)]

        for i in range(self.n):
            self.lookup[i][0] = i

        for j in range(1, self.k + 1):
            i = 0
            while i + (1 << j) - 1 < self.n:
                if (
                    arr[self.lookup[i][j - 1]]
                    < arr[self.lookup[i + (1 << (j - 1))][j - 1]]
                ):
                    self.lookup[i][j] = self.lookup[i][j - 1]
                else:
                    self.lookup[i][j] = self.lookup[i + (1 << (j - 1))][j - 1]
                i += 1

    def query(self, L, R):
        """
        Return the minimum element in range [L, R] (0-indexed, inclusive).

        Args:
            L: Left boundary of the range
            R: Right boundary of the range

        Returns:
            Minimum element from index L to R
        """
        if L > R or L < 0 or R >= self.n:
            return None

        j = int(math.log2(R - L + 1))

        if self.arr[self.lookup[L][j]] <= self.arr[self.lookup[R - (1 << j) + 1][j]]:
            return self.arr[self.lookup[L][j]]
        else:
            return self.arr[self.lookup[R - (1 << j) + 1][j]]


if __name__ == "__main__":
    arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    n = len(arr)

    rmq = RangeMinimumQuery(arr)

    print(f"Array: {arr}")
    print()

    queries = [(0, 4), (4, 7), (7, 8)]
    for L, R in queries:
        result = rmq.query(L, R)
        print(f"Minimum of [{L}, {R}] is {result}")

    print()
    print("Expected Output:")
    print("Minimum of [0, 4] is 0")
    print("Minimum of [4, 7] is 3")
    print("Minimum of [7, 8] is 12")
