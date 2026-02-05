"""
Submatrix with Corners as 1

Problem Description:
    Given a binary matrix, count the number of square submatrices
    where all four corners are 1.

Approach:
    Use hash map to store rows with 1s, then count pairs of rows
    that have 1s in the same columns.

Time Complexity: O(rows^2 * cols) or O(rows * cols^2)
Space Complexity: O(cols) or O(rows)
"""

from typing import List, Set, Dict
from collections import defaultdict


def count_submatrix_corners_one(matrix: List[List[int]]) -> int:
    """
    Count square submatrices with all four corners as 1.

    Args:
        matrix: Binary matrix

    Returns:
        Count of valid submatrices
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    # For each pair of rows, find columns where both have 1s
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows):
            # Find common columns with 1s in both rows
            common_ones = []
            for c in range(cols):
                if matrix[r1][c] == 1 and matrix[r2][c] == 1:
                    common_ones.append(c)

            # Number of ways to choose 2 columns from common_ones
            k = len(common_ones)
            count += k * (k - 1) // 2

    return count


def count_submatrix_corners_one_optimized(matrix: List[List[int]]) -> int:
    """
    Optimized approach using hash map.

    Time Complexity: O(rows^2 * cols) worst case
    Space Complexity: O(cols)
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # Preprocess: store set of columns with 1 for each row
    row_ones: List[Set[int]] = [set() for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                row_ones[r].add(c)

    count = 0

    # For each pair of rows, find intersection
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows):
            common = row_ones[r1] & row_ones[r2]
            k = len(common)
            count += k * (k - 1) // 2

    return count


def count_submatrix_corners_one_hashing(matrix: List[List[int]]) -> int:
    """
    Use hashing to count columns with 1s.

    Time Complexity: O(rows * cols + rows^2)
    Space Complexity: O(rows * cols)
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # Map from column pair to count of rows having 1s in both columns
    col_pair_count: Dict[tuple, int] = defaultdict(int)

    for r in range(rows):
        # Find all columns with 1 in this row
        ones_cols = [c for c in range(cols) if matrix[r][c] == 1]

        # For each pair of columns with 1s, increment count
        for i in range(len(ones_cols)):
            for j in range(i + 1, len(ones_cols)):
                col_pair = (ones_cols[i], ones_cols[j])
                col_pair_count[col_pair] += 1

    # For each column pair that appears k times, there are C(k,2) rectangles
    count = 0
    for k in col_pair_count.values():
        count += k * (k - 1) // 2

    return count


def count_all_ones_submatrix(matrix: List[List[int]]) -> int:
    """
    Count all submatrices filled with 1s.

    Time Complexity: O(rows * cols)
    Space Complexity: O(cols)
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # dp[j] represents the height of consecutive 1s ending at current row, column j
    dp = [0] * cols
    count = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                dp[c] += 1
            else:
                dp[c] = 0

        # Count submatrices ending at current row
        # For each column, we can form dp[c] submatrices of height 1, 2, ..., dp[c]
        # But we need to ensure width as well
        count += count_submatrices_in_histogram(dp)

    return count


def count_submatrices_in_histogram(heights: List[int]) -> int:
    """
    Count submatrices in histogram representation.

    For each position, count how many submatrices have this as the limiting height.
    """
    n = len(heights)
    count = 0

    for i in range(n):
        min_height = heights[i]
        for j in range(i, n):
            min_height = min(min_height, heights[j])
            count += min_height

    return count


def count_square_submatrices_all_ones(matrix: List[List[int]]) -> int:
    """
    Count all square submatrices with all 1s.

    Time Complexity: O(rows * cols)
    Space Complexity: O(rows * cols) can be optimized to O(cols)
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # dp[i][j] = size of largest square with bottom-right corner at (i,j)
    dp = [[0] * cols for _ in range(rows)]
    count = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                count += dp[r][c]  # dp[r][c] squares with bottom-right at (r,c)

    return count


def test_submatrix_corners():
    """Test cases for submatrix with corners as 1."""
    test_cases = [
        # (matrix, expected_count)
        ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 1),  # Four corners form one valid submatrix
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 9),  # All 2x2 and larger squares
        ([[1, 0], [0, 1]], 0),  # No valid submatrix
        ([[1, 1], [1, 1]], 1),  # One 2x2 submatrix
        (
            [[1, 0, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1]],
            4,
        ),  # Multiple valid submatrices
        ([], 0),  # Empty matrix
        ([[0]], 0),  # Single 0
        ([[1]], 0),  # Single 1 (need at least 2x2)
    ]

    print("Running test cases for Submatrix with Corners as 1:")
    print("=" * 60)

    for i, (matrix, expected) in enumerate(test_cases, 1):
        result = count_submatrix_corners_one_optimized(matrix)
        status = "✓ PASS" if result == expected else "✗ FAIL"

        print(f"Test {i}:")
        print(f"  Matrix:")
        for row in matrix:
            print(f"    {row}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print(f"  Status:   {status}\n")


if __name__ == "__main__":
    # Example usage
    matrix = [[1, 0, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1]]

    print("Matrix:")
    for row in matrix:
        print(row)

    print(
        f"\nSubmatrices with corners as 1: {count_submatrix_corners_one_optimized(matrix)}"
    )
    print(
        f"All square submatrices with all 1s: {count_square_submatrices_all_ones(matrix)}"
    )
    print()

    # Run tests
    test_submatrix_corners()
