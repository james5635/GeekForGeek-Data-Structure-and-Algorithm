"""
Count Quadruplets with Given Sum

Problem Description:
    Given an array arr[] and an integer target, find the count of all quadruplets
    (i, j, k, l) such that arr[i] + arr[j] + arr[k] + arr[l] == target.

Approaches:
    1. Naive O(n^4): Check all combinations
    2. Hashing O(n^2): Store pair sums in hash map
    3. Two pointers O(n^3): After sorting, use two pointers for each pair

Time Complexity (Hashing): O(n^2)
Space Complexity (Hashing): O(n^2)
"""

from collections import defaultdict
from typing import List


def count_quadruplets_brute_force(arr: List[int], target: int) -> int:
    """
    Count quadruplets using brute force approach.

    Time Complexity: O(n^4)
    Space Complexity: O(1)
    """
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        count += 1

    return count


def count_quadruplets_hashing(arr: List[int], target: int) -> int:
    """
    Count quadruplets using hashing approach.

    Store pair sums in a hash map and count valid quadruplets.

    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    n = len(arr)
    count = 0

    # Hash map to store frequency of pair sums
    pair_sum_map = defaultdict(int)

    # Consider each element as the fourth element
    for k in range(n - 1):
        # Add all pairs (i, j) where j < k to the map
        for i in range(k):
            for j in range(i + 1, k):
                pair_sum = arr[i] + arr[j]
                pair_sum_map[pair_sum] += 1

        # Find all pairs (k, l) and check if target - pair_sum exists
        for l in range(k + 1, n):
            current_sum = arr[k] + arr[l]
            needed = target - current_sum
            count += pair_sum_map[needed]

    return count


def count_quadruplets_two_pointer(arr: List[int], target: int) -> int:
    """
    Count quadruplets using two-pointer approach after sorting.

    Time Complexity: O(n^3)
    Space Complexity: O(1)
    """
    n = len(arr)
    arr.sort()
    count = 0

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1

            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if current_sum == target:
                    # Handle duplicates
                    if arr[left] == arr[right]:
                        # All elements between left and right are same
                        num_elements = right - left + 1
                        count += num_elements * (num_elements - 1) // 2
                        break

                    # Count duplicates on left
                    left_count = 1
                    while left + 1 < right and arr[left] == arr[left + 1]:
                        left_count += 1
                        left += 1

                    # Count duplicates on right
                    right_count = 1
                    while right - 1 > left and arr[right] == arr[right - 1]:
                        right_count += 1
                        right -= 1

                    count += left_count * right_count
                    left += 1
                    right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return count


def test_count_quadruplets():
    """Test cases for counting quadruplets with given sum."""
    test_cases = [
        # (array, target, expected_count)
        ([1, 0, -1, 0, -2, 2], 0, 3),
        ([2, 2, 2, 2, 2], 8, 5),
        ([1, 1, 1, 1], 4, 1),
        ([1, 2, 3, 4, 5], 10, 1),
        ([0, 0, 0, 0, 0], 0, 5),
        ([1, -1, 2, -2, 3, -3], 0, 2),
        ([10, 2, 3, 4, 5, 7, 8], 23, 3),
    ]

    print("Running test cases for Count Quadruplets:")
    print("=" * 60)

    for i, (arr, target, expected) in enumerate(test_cases, 1):
        # Test hashing approach (most efficient for large inputs)
        result_hash = count_quadruplets_hashing(arr.copy(), target)
        result_two_ptr = count_quadruplets_two_pointer(arr.copy(), target)

        status_hash = "✓" if result_hash == expected else "✗"
        status_two = "✓" if result_two_ptr == expected else "✗"

        print(f"Test {i}: arr = {arr}, target = {target}")
        print(f"  Expected: {expected}")
        print(f"  Hashing result: {result_hash} {status_hash}")
        print(f"  Two-pointer result: {result_two_ptr} {status_two}\n")


if __name__ == "__main__":
    # Example usage
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    print(f"Array: {arr}")
    print(f"Target sum: {target}")
    print(f"Number of quadruplets: {count_quadruplets_hashing(arr, target)}")
    print()

    # Run tests
    test_count_quadruplets()
