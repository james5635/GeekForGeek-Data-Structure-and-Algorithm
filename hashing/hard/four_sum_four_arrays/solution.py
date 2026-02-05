"""
4Sum from Four Sorted Arrays

Problem Description:
    Given four sorted arrays A, B, C, D of size n each, find the count of
    quadruples (i, j, k, l) such that A[i] + B[j] + C[k] + D[l] = 0.

Approach:
    Use hash map to store sums of pairs from first two arrays,
    then check for complementary sums from last two arrays.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

from typing import List
from collections import defaultdict


def count_quadruples_four_arrays(
    A: List[int], B: List[int], C: List[int], D: List[int]
) -> int:
    """
    Count quadruples from four arrays that sum to zero.

    Args:
        A, B, C, D: Four sorted arrays of integers

    Returns:
        Count of quadruples (i,j,k,l) where A[i]+B[j]+C[k]+D[l]=0
    """
    n = len(A)
    count = 0

    # Hash map to store sum of pairs from A and B
    sum_map = defaultdict(int)

    # Store all pair sums from A and B
    for i in range(n):
        for j in range(n):
            pair_sum = A[i] + B[j]
            sum_map[pair_sum] += 1

    # Check for each pair in C and D
    for k in range(n):
        for l in range(n):
            target = -(C[k] + D[l])
            count += sum_map[target]

    return count


def count_quadruples_general(
    A: List[int], B: List[int], C: List[int], D: List[int], target: int
) -> int:
    """
    Count quadruples that sum to given target.

    Args:
        A, B, C, D: Four sorted arrays of integers
        target: Target sum value

    Returns:
        Count of quadruples (i,j,k,l) where A[i]+B[j]+C[k]+D[l]=target
    """
    n = len(A)
    count = 0

    # Hash map to store sum of pairs from A and B
    sum_map = defaultdict(int)

    # Store all pair sums from A and B
    for i in range(n):
        for j in range(n):
            pair_sum = A[i] + B[j]
            sum_map[pair_sum] += 1

    # Check for each pair in C and D
    for k in range(n):
        for l in range(n):
            needed = target - (C[k] + D[l])
            count += sum_map[needed]

    return count


def find_quadruples_four_arrays(
    A: List[int], B: List[int], C: List[int], D: List[int]
) -> List[List[int]]:
    """
    Find all quadruples from four arrays that sum to zero.

    Time Complexity: O(n^2)
    Space Complexity: O(n^2)

    Returns:
        List of all valid quadruples [A[i], B[j], C[k], D[l]]
    """
    n = len(A)
    result = []

    # Hash map to store pairs from A and B indexed by their sum
    sum_map = defaultdict(list)

    # Store all pairs from A and B
    for i in range(n):
        for j in range(n):
            pair_sum = A[i] + B[j]
            sum_map[pair_sum].append((A[i], B[j]))

    # For each pair in C and D, find complementary pairs
    for k in range(n):
        for l in range(n):
            target = -(C[k] + D[l])
            if target in sum_map:
                for pair in sum_map[target]:
                    result.append([pair[0], pair[1], C[k], D[l]])

    return result


def test_four_sum_four_arrays():
    """Test cases for 4Sum from Four Sorted Arrays."""
    test_cases = [
        # (A, B, C, D, expected_count)
        ([-1, 2], [-2, 1], [1, 2], [2, -1], 2),
        ([1, 2], [3, 4], [5, 6], [7, 8], 0),
        ([0, 0], [0, 0], [0, 0], [0, 0], 16),
        ([-1, -1], [1, 1], [-1, -1], [1, 1], 16),
        ([1, 2, 3], [4, 5, 6], [-5, -4, -3], [-1, -2, -3], 3),
    ]

    print("Running test cases for 4Sum from Four Arrays:")
    print("=" * 60)

    for i, (A, B, C, D, expected) in enumerate(test_cases, 1):
        result = count_quadruples_four_arrays(A, B, C, D)
        status = "✓ PASS" if result == expected else "✗ FAIL"

        print(f"Test {i}:")
        print(f"  A = {A}")
        print(f"  B = {B}")
        print(f"  C = {C}")
        print(f"  D = {D}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print(f"  Status:   {status}\n")

    # Test with actual quadruplets
    print("\nTest with finding actual quadruplets:")
    A, B, C, D = [-1, 2], [-2, 1], [1, 2], [2, -1]
    quadruplets = find_quadruples_four_arrays(A, B, C, D)
    print(f"A = {A}, B = {B}, C = {C}, D = {D}")
    print(f"All quadruplets summing to 0:")
    for q in quadruplets:
        print(f"  {q} (sum = {sum(q)})")


if __name__ == "__main__":
    # Example usage
    A = [-1, 2]
    B = [-2, 1]
    C = [1, 2]
    D = [2, -1]

    print("4Sum from Four Arrays Example:")
    print(f"Arrays: A={A}, B={B}, C={C}, D={D}")
    print(
        f"Count of quadruples summing to 0: {count_quadruples_four_arrays(A, B, C, D)}"
    )
    print()

    # Run tests
    test_four_sum_four_arrays()
