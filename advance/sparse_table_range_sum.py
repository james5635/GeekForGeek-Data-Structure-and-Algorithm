"""
Range Sum Query using Sparse Table

Sparse Table is a data structure that allows answering range sum queries efficiently
on a static array (no updates). It preprocesses the array in O(n log n) time and
answers each query in O(log n) time.

The idea is to precompute sums of all subarrays of size 2^j where j varies from 0 to log n.
For a query [L, R], we decompose the range into powers of 2 and sum the precomputed values.

Time Complexity:
    - Preprocessing: O(n log n)
    - Query: O(log n)
    - Space: O(n log n)
"""

import math


class SparseTableRangeSum:
    """Sparse Table for efficient range sum queries on static arrays."""

    def __init__(self, arr):
        """
        Build the sparse table from the given array.

        Args:
            arr: List of integers
        """
        self.n = len(arr)
        if self.n == 0:
            self.table = []
            return

        self.k = int(math.floor(math.log2(self.n))) if self.n > 1 else 0
        self.table = [[0] * (self.k + 1) for _ in range(self.n)]

        for i in range(self.n):
            self.table[i][0] = arr[i]

        for j in range(1, self.k + 1):
            for i in range(self.n - (1 << j) + 1):
                self.table[i][j] = (
                    self.table[i][j - 1] + self.table[i + (1 << (j - 1))][j - 1]
                )

    def query(self, L, R):
        """
        Return the sum of elements in range [L, R] (0-indexed, inclusive).

        Args:
            L: Left boundary of the range
            R: Right boundary of the range

        Returns:
            Sum of elements from index L to R
        """
        if L > R or L < 0 or R >= self.n:
            return 0

        answer = 0
        for j in range(self.k, -1, -1):
            if L + (1 << j) - 1 <= R:
                answer += self.table[L][j]
                L += 1 << j

        return answer


if __name__ == "__main__":
    arr = [3, 7, 2, 5, 8, 9]
    n = len(arr)

    sparse_table = SparseTableRangeSum(arr)

    print(f"Array: {arr}")
    print()

    queries = [(0, 5), (3, 5), (2, 4)]
    for L, R in queries:
        result = sparse_table.query(L, R)
        print(f"Sum of range [{L}, {R}] = {result}")

    print()
    print("Expected Output:")
    print("Sum of range [0, 5] = 34")
    print("Sum of range [3, 5] = 22")
    print("Sum of range [2, 4] = 15")
