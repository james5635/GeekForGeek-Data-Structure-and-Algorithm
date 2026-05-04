"""
Count-based Absolute Difference for Array Element

Implements an algorithm to compute, for each array element, the absolute
difference between the count of elements to the left that are strictly greater,
and the count of elements to the right that are strictly lesser. Uses Binary
Indexed Tree (Fenwick Tree) for efficient counting.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""


class BinaryIndexTree:
    """Binary Indexed Tree (Fenwick Tree) for prefix sum queries."""

    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        """Add delta to element at index (1-based)."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        """Return prefix sum from 1 to index (inclusive)."""
        sum_val = 0
        while index > 0:
            sum_val += self.tree[index]
            index -= index & -index
        return sum_val


def count_based_abs_difference(arr: list) -> list:
    """
    Compute count-based absolute difference for each array element.

    Args:
        arr: List of integers

    Returns:
        List of absolute differences for each element
    """
    n = len(arr)

    # Sort array and create mapping of value to sorted index (1-based)
    sorted_arr = sorted(arr)
    value_to_idx = {val: i + 1 for i, val in enumerate(sorted_arr)}

    # Convert array to sorted indices
    sorted_indices = [value_to_idx[val] for val in arr]

    # Compute right side: count of elements strictly lesser to the right
    bit_right = BinaryIndexTree(n)
    right_counts = [0] * n
    for i in range(n - 1, -1, -1):
        right_counts[i] = bit_right.query(sorted_indices[i] - 1)
        bit_right.update(sorted_indices[i], 1)

    # Compute left side: count of elements strictly greater to the left
    # Invert indices to count greater elements using the same BIT logic
    inverted_indices = [n + 1 - idx for idx in sorted_indices]
    bit_left = BinaryIndexTree(n)
    left_counts = [0] * n
    for i in range(n):
        left_counts[i] = bit_left.query(inverted_indices[i] - 1)
        bit_left.update(inverted_indices[i], 1)

    # Compute absolute differences
    return [abs(right_counts[i] - left_counts[i]) for i in range(n)]


if __name__ == "__main__":
    # Test case 1
    arr1 = [5, 4, 3, 2, 1]
    result1 = count_based_abs_difference(arr1)
    print(f"Test 1 - Count-based differences: {result1} (Expected: [4, 2, 0, 2, 4])")

    # Test case 2
    arr2 = [1, 2, 3, 4, 5]
    result2 = count_based_abs_difference(arr2)
    print(f"Test 2 - Count-based differences: {result2} (Expected: [0, 0, 0, 0, 0])")
