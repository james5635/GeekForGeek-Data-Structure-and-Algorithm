"""
Four Elements Sum (4Sum)

Problem Description:
    Given an array arr[] and an integer target, find all unique quadruplets
    in the array which sum up to the target value.

Approaches:
    1. Hashing O(n^2): Store pair sums and find complementary pairs
    2. Two pointers O(n^3): Sort and use two pointers technique

Time Complexity (Optimal): O(n^3)
Space Complexity (Optimal): O(1) excluding result
"""

from typing import List, Set, Tuple


def four_sum_hashing(arr: List[int], target: int) -> List[List[int]]:
    """
    Find all unique quadruplets using hashing approach.

    Time Complexity: O(n^2 * log n) due to sorting each quadruplet
    Space Complexity: O(n^2) for storing pair sums
    """
    n = len(arr)
    result = set()

    # Dictionary to store pair sums and their indices
    pair_sum_map = {}

    for i in range(n):
        for j in range(i + 1, n):
            current_sum = arr[i] + arr[j]
            complement = target - current_sum

            if complement in pair_sum_map:
                for pair in pair_sum_map[complement]:
                    k, l = pair
                    # Ensure all indices are distinct
                    if k != i and k != j and l != i and l != j:
                        quadruplet = tuple(sorted([arr[i], arr[j], arr[k], arr[l]]))
                        result.add(quadruplet)

            if current_sum not in pair_sum_map:
                pair_sum_map[current_sum] = []
            pair_sum_map[current_sum].append((i, j))

    return [list(q) for q in sorted(result)]


def four_sum_two_pointer(arr: List[int], target: int) -> List[List[int]]:
    """
    Find all unique quadruplets using two-pointer approach.

    Time Complexity: O(n^3)
    Space Complexity: O(1) excluding result
    """
    n = len(arr)
    arr.sort()
    result = []

    for i in range(n - 3):
        # Skip duplicate values for first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicate values for second element
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if current_sum == target:
                    result.append([arr[i], arr[j], arr[left], arr[right]])

                    # Skip duplicates for third element
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    # Skip duplicates for fourth element
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result


def four_sum_optimized(arr: List[int], target: int) -> List[List[int]]:
    """
    Optimized two-pointer approach with early termination.

    Time Complexity: O(n^3)
    Space Complexity: O(1) excluding result
    """
    n = len(arr)
    if n < 4:
        return []

    arr.sort()
    result = []

    for i in range(n - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # Early termination if sum is too large
        if arr[i] + arr[i + 1] + arr[i + 2] + arr[i + 3] > target:
            break

        # Skip if sum is too small
        if arr[i] + arr[n - 3] + arr[n - 2] + arr[n - 1] < target:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            # Early termination for inner loop
            if arr[i] + arr[j] + arr[j + 1] + arr[j + 2] > target:
                break

            if arr[i] + arr[j] + arr[n - 2] + arr[n - 1] < target:
                continue

            left, right = j + 1, n - 1

            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if current_sum == target:
                    result.append([arr[i], arr[j], arr[left], arr[right]])

                    temp_left = arr[left]
                    temp_right = arr[right]

                    while left < right and arr[left] == temp_left:
                        left += 1
                    while left < right and arr[right] == temp_right:
                        right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result


def test_four_sum():
    """Test cases for Four Elements Sum problem."""
    test_cases = [
        # (array, target, expected_result)
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ([1, 1, 1, 1], 4, [[1, 1, 1, 1]]),
        ([10, 2, 3, 4, 5, 7, 8], 23, [[2, 3, 8, 10], [2, 4, 7, 10], [3, 5, 7, 8]]),
        (
            [1, -2, -3, 4, -1, 2, 3],
            0,
            [[-3, -2, 1, 4], [-3, -1, 0, 4], [-3, -1, 1, 3], [-2, -1, 0, 3]],
        ),
        ([], 0, []),
        ([1, 2, 3], 6, []),
    ]

    print("Running test cases for Four Elements Sum:")
    print("=" * 60)

    for i, (arr, target, expected) in enumerate(test_cases, 1):
        result = four_sum_optimized(arr.copy(), target)

        # Normalize for comparison
        expected_sorted = sorted([sorted(x) for x in expected])
        result_sorted = sorted([sorted(x) for x in result])

        status = "✓ PASS" if result_sorted == expected_sorted else "✗ FAIL"

        print(f"Test {i}: arr = {arr}, target = {target}")
        print(f"  Expected: {expected_sorted}")
        print(f"  Got:      {result_sorted}")
        print(f"  Status:   {status}\n")


if __name__ == "__main__":
    # Example usage
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    print(f"Array: {arr}")
    print(f"Target sum: {target}")
    print(f"Quadruplets: {four_sum_optimized(arr, target)}")
    print()

    # Run tests
    test_four_sum()
