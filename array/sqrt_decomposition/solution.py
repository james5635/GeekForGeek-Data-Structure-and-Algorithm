"""
Square Root Decomposition

Problem Description:
Square root decomposition is a technique to preprocess an array to answer
range queries efficiently. The array is divided into blocks of size sqrt(N),
allowing range queries to be answered by combining complete blocks and
individual elements from partial blocks.

This implementation demonstrates range sum queries using sqrt decomposition.

Time Complexity:
- Preprocessing: O(N)
- Query Processing: O(sqrt(N))
- Update: O(1) for point updates

Space Complexity:
- O(N) for the array
- O(sqrt(N)) for block sums

Algorithm:
1. Divide array into blocks of size sqrt(N)
2. Precompute sum for each block
3. For query [L, R]:
   - Sum complete blocks fully contained in [L, R]
   - Sum individual elements in partial blocks at boundaries
"""

import math
from typing import List


class SqrtDecomposition:
    """
    Square Root Decomposition data structure for range sum queries.
    """

    def __init__(self, arr: List[int]):
        """
        Initialize sqrt decomposition structure.

        Args:
            arr: Input array
        """
        self.n = len(arr)
        self.arr = arr.copy()

        if self.n == 0:
            self.block_size = 0
            self.num_blocks = 0
            self.block_sums = []
            return

        # Calculate block size as sqrt(n)
        self.block_size = int(math.sqrt(self.n)) + 1
        self.num_blocks = (self.n + self.block_size - 1) // self.block_size

        # Initialize block sums
        self.block_sums = [0] * self.num_blocks
        self._build_blocks()

    def _build_blocks(self):
        """Build block sums from the array."""
        for i in range(self.n):
            block_idx = i // self.block_size
            self.block_sums[block_idx] += self.arr[i]

    def _get_block_range(self, block_idx: int) -> tuple:
        """Get the range of indices for a given block."""
        start = block_idx * self.block_size
        end = min(start + self.block_size, self.n) - 1
        return (start, end)

    def query(self, left: int, right: int) -> int:
        """
        Get sum of elements in range [left, right].

        Args:
            left: Left index (inclusive)
            right: Right index (inclusive)

        Returns:
            Sum of elements in the range
        """
        if left > right or left < 0 or right >= self.n:
            return 0

        result = 0

        # Get block indices
        left_block = left // self.block_size
        right_block = right // self.block_size

        if left_block == right_block:
            # Range is within a single block, sum directly
            for i in range(left, right + 1):
                result += self.arr[i]
        else:
            # Sum partial left block
            left_block_end = (left_block + 1) * self.block_size - 1
            for i in range(left, min(left_block_end + 1, self.n)):
                result += self.arr[i]

            # Sum complete blocks in between
            for block_idx in range(left_block + 1, right_block):
                result += self.block_sums[block_idx]

            # Sum partial right block
            right_block_start = right_block * self.block_size
            for i in range(right_block_start, right + 1):
                result += self.arr[i]

        return result

    def update(self, index: int, value: int):
        """
        Update element at index to new value.

        Args:
            index: Index to update
            value: New value
        """
        if index < 0 or index >= self.n:
            return

        # Update block sum
        block_idx = index // self.block_size
        self.block_sums[block_idx] += value - self.arr[index]

        # Update array
        self.arr[index] = value

    def get_array(self) -> List[int]:
        """Return a copy of the current array."""
        return self.arr.copy()


def brute_force_range_sum(arr: List[int], left: int, right: int) -> int:
    """Brute force method for verification."""
    if left > right or left < 0 or right >= len(arr):
        return 0
    return sum(arr[left : right + 1])


if __name__ == "__main__":
    # Test Case 1: Basic functionality
    print("=" * 60)
    print("Test Case 1: Basic Range Sum Queries")
    print("=" * 60)

    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sqrt_dec = SqrtDecomposition(arr1)

    queries1 = [
        (0, 4),  # Sum of [1,2,3,4,5] = 15
        (2, 6),  # Sum of [3,4,5,6,7] = 25
        (5, 9),  # Sum of [6,7,8,9,10] = 40
        (0, 9),  # Sum of entire array = 55
        (3, 3),  # Single element = 4
        (7, 7),  # Single element = 8
    ]

    print(f"Array: {arr1}")
    print(f"Block size: {sqrt_dec.block_size}, Number of blocks: {sqrt_dec.num_blocks}")
    print(f"Block sums: {sqrt_dec.block_sums}")
    print(f"\nQueries:")

    all_passed = True
    for i, (left, right) in enumerate(queries1):
        result = sqrt_dec.query(left, right)
        expected = brute_force_range_sum(arr1, left, right)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(
            f"  Query {i + 1} [{left}, {right}]: {result} (expected {expected}) - {status}"
        )

    # Test Case 2: Update operations
    print("\n" + "=" * 60)
    print("Test Case 2: Update Operations")
    print("=" * 60)

    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sqrt_dec2 = SqrtDecomposition(arr2)

    print(f"Initial array: {sqrt_dec2.get_array()}")
    print(f"Initial block sums: {sqrt_dec2.block_sums}")

    # Update index 5 from 6 to 20
    sqrt_dec2.update(5, 20)
    print(f"\nAfter update(5, 20):")
    print(f"Array: {sqrt_dec2.get_array()}")
    print(f"Block sums: {sqrt_dec2.block_sums}")

    # Query after update
    result = sqrt_dec2.query(0, 9)
    expected = sum([1, 2, 3, 4, 5, 20, 7, 8, 9, 10])
    print(
        f"Query [0, 9]: {result} (expected {expected}) - {'PASS' if result == expected else 'FAIL'}"
    )

    # Test Case 3: Edge cases
    print("\n" + "=" * 60)
    print("Test Case 3: Edge Cases")
    print("=" * 60)

    # Single element
    arr3 = [42]
    sqrt_dec3 = SqrtDecomposition(arr3)
    result = sqrt_dec3.query(0, 0)
    print(
        f"Single element [0, 0]: {result} == 42 - {'PASS' if result == 42 else 'FAIL'}"
    )

    # Empty array
    arr4 = []
    sqrt_dec4 = SqrtDecomposition(arr4)
    result = sqrt_dec4.query(0, 0)
    print(f"Empty array query: {result} == 0 - {'PASS' if result == 0 else 'FAIL'}")

    # Out of bounds
    arr5 = [1, 2, 3, 4, 5]
    sqrt_dec5 = SqrtDecomposition(arr5)
    result = sqrt_dec5.query(3, 10)
    print(f"Out of bounds [3, 10]: {result} == 0 - {'PASS' if result == 0 else 'FAIL'}")

    # Test Case 4: Performance comparison
    print("\n" + "=" * 60)
    print("Test Case 4: Large Array Performance")
    print("=" * 60)

    import random
    import time

    random.seed(42)
    large_arr = [random.randint(1, 1000) for _ in range(10000)]

    # Build sqrt decomposition
    start = time.time()
    sqrt_dec_large = SqrtDecomposition(large_arr)
    build_time = time.time() - start

    # Generate random queries
    num_queries = 1000
    queries = []
    for _ in range(num_queries):
        left = random.randint(0, len(large_arr) - 1)
        right = random.randint(left, len(large_arr) - 1)
        queries.append((left, right))

    # Time sqrt decomposition queries
    start = time.time()
    sqrt_results = [sqrt_dec_large.query(l, r) for l, r in queries]
    sqrt_time = time.time() - start

    # Time brute force queries
    start = time.time()
    brute_results = [brute_force_range_sum(large_arr, l, r) for l, r in queries]
    brute_time = time.time() - start

    # Verify correctness
    correct = all(a == b for a, b in zip(sqrt_results, brute_results))

    print(f"Array size: {len(large_arr)}")
    print(f"Number of queries: {num_queries}")
    print(f"Build time: {build_time:.4f}s")
    print(f"Sqrt decomposition query time: {sqrt_time:.4f}s")
    print(f"Brute force query time: {brute_time:.4f}s")
    print(f"Speedup: {brute_time / sqrt_time:.2f}x")
    print(f"All queries correct: {'PASS' if correct else 'FAIL'}")

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
