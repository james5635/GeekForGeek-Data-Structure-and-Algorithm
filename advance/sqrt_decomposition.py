"""
Square Root (Sqrt) Decomposition Algorithm

Square Root Decomposition is a query optimization technique that decomposes
a given array into chunks of size sqrt(N). It allows efficient range queries
and point updates.

Key concepts:
- Array of N elements is decomposed into sqrt(N) blocks.
- Each block contains sqrt(N) elements and precomputed aggregate values.
- Range queries combine results from fully overlapped blocks and iterate
  through partially overlapped blocks.

Time Complexity:
  - Query: O(sqrt(N))
  - Update: O(1)
  - Preprocess: O(N)
Space Complexity: O(N)

Source: https://www.geeksforgeeks.org/dsa/square-root-sqrt-decomposition-algorithm/
"""

import math


class SqrtDecomposition:
    """
    A class implementing Square Root Decomposition for range sum queries
    with point updates.
    """

    def __init__(self, arr):
        """
        Initialize the sqrt decomposition structure.

        Args:
            arr: List of integers representing the input array.
        """
        self.n = len(arr)
        self.arr = arr[:]
        self.block_size = int(math.sqrt(self.n))
        self.num_blocks = (self.n + self.block_size - 1) // self.block_size
        self.blocks = [0] * self.num_blocks

        self._preprocess()

    def _preprocess(self):
        """Build the decomposed block array from the input array."""
        for i in range(self.n):
            block_idx = i // self.block_size
            self.blocks[block_idx] += self.arr[i]

    def update(self, idx, val):
        """
        Update the value at a given index.

        Args:
            idx: Index to update (0-based).
            val: New value to set at the given index.

        Time Complexity: O(1)
        """
        block_number = idx // self.block_size
        self.blocks[block_number] += val - self.arr[idx]
        self.arr[idx] = val

    def query(self, l, r):
        """
        Compute the sum of elements in range [l, r].

        Args:
            l: Left boundary of the range (inclusive, 0-based).
            r: Right boundary of the range (inclusive, 0-based).

        Returns:
            Sum of elements in the range [l, r].

        Time Complexity: O(sqrt(N))
        """
        total = 0

        # Traverse first block (partial)
        while l < r and l % self.block_size != 0 and l != 0:
            total += self.arr[l]
            l += 1

        # Traverse fully overlapped blocks
        while l + self.block_size - 1 <= r:
            total += self.blocks[l // self.block_size]
            l += self.block_size

        # Traverse last block (partial)
        while l <= r:
            total += self.arr[l]
            l += 1

        return total


if __name__ == "__main__":
    # Example 1 from GeeksforGeeks
    print("=== Example 1: Basic Range Sum Queries with Updates ===")
    input_arr = [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]
    sd = SqrtDecomposition(input_arr)

    print(f"Array: {input_arr}")
    print(f"Block size: {sd.block_size}")
    print(f"Blocks: {sd.blocks}")
    print()

    print(f"query(3, 8): {sd.query(3, 8)}")
    print(f"query(1, 6): {sd.query(1, 6)}")

    sd.update(8, 0)
    print(f"After update(8, 0) -> query(8, 8): {sd.query(8, 8)}")

    # Example 2: Multiple updates and queries
    print("\n=== Example 2: Multiple Updates and Queries ===")
    arr2 = [3, 7, 1, 4, 8, 2, 6, 5, 9, 10, 3, 7, 2, 8]
    sd2 = SqrtDecomposition(arr2)

    print(f"Array: {arr2}")
    print(f"query(0, 13): {sd2.query(0, 13)}")
    print(f"query(2, 7): {sd2.query(2, 7)}")

    sd2.update(5, 20)
    print(f"After update(5, 20) -> query(0, 13): {sd2.query(0, 13)}")
    print(f"After update(5, 20) -> query(3, 8): {sd2.query(3, 8)}")

    # Example 3: Verification with brute force
    print("\n=== Example 3: Verification with Brute Force ===")
    arr3 = [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]
    sd3 = SqrtDecomposition(arr3)

    test_queries = [(0, 9), (3, 8), (1, 6), (0, 0), (5, 5)]
    for l, r in test_queries:
        result = sd3.query(l, r)
        brute_force = sum(arr3[l : r + 1])
        match = "PASS" if result == brute_force else "FAIL"
        print(
            f"query({l}, {r}): SqrtDecomposition={result}, Brute Force={brute_force} [{match}]"
        )

    sd3.update(4, 100)
    arr3[4] = 100
    result = sd3.query(0, 9)
    brute_force = sum(arr3[0:10])
    match = "PASS" if result == brute_force else "FAIL"
    print(
        f"After update(4, 100) -> query(0, 9): SqrtDecomposition={result}, Brute Force={brute_force} [{match}]"
    )
