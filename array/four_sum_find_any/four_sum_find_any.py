"""
Find Any Quadruplet with Given Sum (4Sum)
Given an array and a target sum, find any four elements that sum to the target.

Example:
Input: arr = [1, 0, -1, 0, -2, 2], target = 0
Output: [-1, 0, 0, 1] or [-2, -1, 1, 2] or [-2, 0, 0, 2]

Approaches:
1. Brute Force: O(n⁴) - four nested loops
2. Hash Map of Pair Sums: O(n²) - store pair sums, then two-sum approach
3. Sort + Two Pointers Extension: O(n³) - sort, fix two, two pointers for rest
"""

from typing import List, Optional, Tuple
from collections import defaultdict


def four_sum_brute_force(
    arr: List[int], target: int
) -> Optional[Tuple[int, int, int, int]]:
    """
    Brute force: Check all quadruplets using four nested loops.
    Time: O(n⁴)
    Space: O(1)
    """
    n = len(arr)
    if n < 4:
        return None

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        return (arr[i], arr[j], arr[k], arr[l])

    return None


def four_sum_hash_map_pair_sums(
    arr: List[int], target: int
) -> Optional[Tuple[int, int, int, int]]:
    """
    Hash Map of Pair Sums approach - Optimal O(n²).
    Store all pair sums in a hash map, then use two-sum approach on pairs.
    Time: O(n²) for building map + O(n²) for finding = O(n²)
    Space: O(n²) for storing pair sums
    """
    n = len(arr)
    if n < 4:
        return None

    # Hash map: sum -> list of (i, j) pairs with that sum
    pair_sums = defaultdict(list)

    # Store all pair sums
    for i in range(n):
        for j in range(i + 1, n):
            current_sum = arr[i] + arr[j]
            pair_sums[current_sum].append((i, j))

    # Now find two pairs that sum to target
    for sum1, pairs1 in pair_sums.items():
        sum2 = target - sum1

        if sum2 not in pair_sums:
            continue

        pairs2 = pair_sums[sum2]

        # Try all combinations of pairs
        for i1, j1 in pairs1:
            for i2, j2 in pairs2:
                # Check if all four indices are distinct
                indices = {i1, j1, i2, j2}
                if len(indices) == 4:
                    return (arr[i1], arr[j1], arr[i2], arr[j2])

    return None


def four_sum_sort_two_pointers(
    arr: List[int], target: int
) -> Optional[Tuple[int, int, int, int]]:
    """
    Sort + Two Pointers extension approach.
    Fix two elements, use two pointers for remaining.
    Time: O(n log n) for sort + O(n³) for search = O(n³)
    Space: O(1) or O(n) for sorting
    """
    n = len(arr)
    if n < 4:
        return None

    # Sort the array
    sorted_arr = sorted(arr)

    for i in range(n - 3):
        # Skip duplicates for first element
        if i > 0 and sorted_arr[i] == sorted_arr[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicates for second element
            if j > i + 1 and sorted_arr[j] == sorted_arr[j - 1]:
                continue

            # Use two pointers for remaining sum
            left, right = j + 1, n - 1
            remaining_target = target - sorted_arr[i] - sorted_arr[j]

            while left < right:
                current_sum = sorted_arr[left] + sorted_arr[right]

                if current_sum == remaining_target:
                    return (
                        sorted_arr[i],
                        sorted_arr[j],
                        sorted_arr[left],
                        sorted_arr[right],
                    )

                # Move pointers
                if current_sum < remaining_target:
                    left += 1
                else:
                    right -= 1

    return None


def four_sum_all_quadruplets(
    arr: List[int], target: int
) -> List[Tuple[int, int, int, int]]:
    """
    Find ALL unique quadruplets (not just any one) with given sum.
    Uses sort + two pointers extension approach.
    Time: O(n³)
    Space: O(k) where k is number of quadruplets
    """
    n = len(arr)
    if n < 4:
        return []

    sorted_arr = sorted(arr)
    result = []

    for i in range(n - 3):
        # Skip duplicates for first element
        if i > 0 and sorted_arr[i] == sorted_arr[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicates for second element
            if j > i + 1 and sorted_arr[j] == sorted_arr[j - 1]:
                continue

            left, right = j + 1, n - 1
            remaining_target = target - sorted_arr[i] - sorted_arr[j]

            while left < right:
                current_sum = sorted_arr[left] + sorted_arr[right]

                if current_sum == remaining_target:
                    result.append(
                        (
                            sorted_arr[i],
                            sorted_arr[j],
                            sorted_arr[left],
                            sorted_arr[right],
                        )
                    )

                    # Skip duplicates
                    left_val = sorted_arr[left]
                    while left < right and sorted_arr[left] == left_val:
                        left += 1

                    right_val = sorted_arr[right]
                    while left < right and sorted_arr[right] == right_val:
                        right -= 1

                elif current_sum < remaining_target:
                    left += 1
                else:
                    right -= 1

    return result


def test_four_sum():
    """Test all implementations with various test cases"""
    test_cases = [
        # (arr, target, should_find_quadruplet)
        ([1, 0, -1, 0, -2, 2], 0, True),  # Classic example
        ([2, 2, 2, 2, 2], 8, True),  # All same elements
        ([1, 2, 3, 4], 100, False),  # No valid quadruplet
        ([], 0, False),  # Empty array
        ([1, 2, 3], 6, False),  # Less than 4 elements
        ([-3, -2, -1, 0, 1, 2, 3], 0, True),  # With negatives
        ([1, 1, -1, -1, 0, 0, 2, -2], 0, True),  # Many duplicates
    ]

    implementations = [
        ("Brute Force", four_sum_brute_force),
        ("Hash Map (Pair Sums)", four_sum_hash_map_pair_sums),
        ("Sort + Two Pointers", four_sum_sort_two_pointers),
    ]

    print("=" * 70)
    print("FIND ANY QUADRUPLET WITH GIVEN SUM (4SUM) - TEST RESULTS")
    print("=" * 70)

    for name, func in implementations:
        print(f"\n{name} Approach:")
        print("-" * 50)

        all_passed = True
        for i, (arr, target, should_find) in enumerate(test_cases):
            try:
                result = func(arr, target)

                found = result is not None
                passed = found == should_find

                # Additional check: if found, verify the sum
                if found and result:
                    actual_sum = sum(result)
                    if actual_sum != target:
                        passed = False

                status = "PASS" if passed else "FAIL"
                if not passed:
                    all_passed = False

                if len(arr) <= 6:
                    print(f"  Test {i + 1}: {status} - arr={arr}, target={target}")
                else:
                    print(
                        f"  Test {i + 1}: {status} - arr=[...{len(arr)} elements...], target={target}"
                    )

                if not passed:
                    print(f"           Expected to find: {should_find}, Found: {found}")
                    if result:
                        print(f"           Result: {result}, Sum: {sum(result)}")
            except Exception as e:
                all_passed = False
                print(f"  Test {i + 1}: ERROR - {e}")

        print(f"  Overall: {'ALL PASSED' if all_passed else 'SOME FAILED'}")

    print("\n" + "=" * 70)

    # Test all quadruplets finder
    print("\n\nFIND ALL QUADRUPLETS:")
    print("=" * 70)
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    result = four_sum_all_quadruplets(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"All unique quadruplets: {result}")
    for q in result:
        print(f"  {q} -> sum = {sum(q)}")

    # Detailed example
    print("\n\nDetailed Example:")
    print("-" * 50)
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    print(f"Array: {arr}")
    print(f"Target: {target}")
    result = four_sum_hash_map_pair_sums(arr, target)
    print(f"Quadruplet: {result}")
    if result:
        print(f"Verification: {' + '.join(map(str, result))} = {sum(result)}")


if __name__ == "__main__":
    test_four_sum()
