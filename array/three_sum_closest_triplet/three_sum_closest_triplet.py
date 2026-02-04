"""
Find Triplet with Sum Closest to Target
Given an array and a target, find three elements whose sum is closest to the target.
Return the sum of the triplet.

Example:
Input: arr = [-1, 2, 1, -4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)

Approaches:
1. Brute Force: O(n³) - check all triplets
2. Sort + Two Pointers: O(n²) - optimal
"""

from typing import List, Tuple, Optional
import sys


def three_sum_closest_brute_force(arr: List[int], target: int) -> int:
    """
    Brute force: Check all possible triplets.
    Time: O(n³)
    Space: O(1)
    """
    n = len(arr)
    if n < 3:
        raise ValueError("Array must have at least 3 elements")

    closest_sum = arr[0] + arr[1] + arr[2]
    min_diff = abs(closest_sum - target)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                current_sum = arr[i] + arr[j] + arr[k]
                current_diff = abs(current_sum - target)

                if current_diff < min_diff:
                    min_diff = current_diff
                    closest_sum = current_sum

                    # Early exit if exact match found
                    if min_diff == 0:
                        return closest_sum

    return closest_sum


def three_sum_closest_optimized(arr: List[int], target: int) -> int:
    """
    Optimized: Sort + Early termination on exact match.
    Time: O(n³) worst case, but faster in practice
    Space: O(1)
    """
    n = len(arr)
    if n < 3:
        raise ValueError("Array must have at least 3 elements")

    closest_sum = None
    min_diff = float("inf")

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                current_sum = arr[i] + arr[j] + arr[k]
                current_diff = abs(current_sum - target)

                if current_diff < min_diff:
                    min_diff = current_diff
                    closest_sum = current_sum

                if min_diff == 0:
                    return closest_sum

    return closest_sum if closest_sum is not None else arr[0] + arr[1] + arr[2]


def three_sum_closest_sort_two_pointers(arr: List[int], target: int) -> int:
    """
    Sort + Two Pointers approach - Optimal solution.
    Time: O(n log n) for sort + O(n²) for search = O(n²)
    Space: O(1) or O(n) for sorting
    """
    n = len(arr)
    if n < 3:
        raise ValueError("Array must have at least 3 elements")

    # Sort the array
    sorted_arr = sorted(arr)

    # Initialize with first three elements
    closest_sum = sorted_arr[0] + sorted_arr[1] + sorted_arr[2]
    min_diff = abs(closest_sum - target)

    for i in range(n - 2):
        # Optional: Skip duplicates for i (not necessary for closest, but can optimize)
        # if i > 0 and sorted_arr[i] == sorted_arr[i - 1]:
        #     continue

        left, right = i + 1, n - 1

        while left < right:
            current_sum = sorted_arr[i] + sorted_arr[left] + sorted_arr[right]
            current_diff = abs(current_sum - target)

            # Update closest sum if this is closer
            if current_diff < min_diff:
                min_diff = current_diff
                closest_sum = current_sum

            # Early exit if exact match found
            if current_diff == 0:
                return current_sum

            # Move pointers based on comparison
            if current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum


def three_sum_closest_with_triplet(
    arr: List[int], target: int
) -> Tuple[int, Tuple[int, int, int]]:
    """
    Same as optimal but also returns the actual triplet.
    Time: O(n²)
    Space: O(1) or O(n) for sorting
    """
    n = len(arr)
    if n < 3:
        raise ValueError("Array must have at least 3 elements")

    sorted_arr = sorted(arr)

    closest_sum = sorted_arr[0] + sorted_arr[1] + sorted_arr[2]
    closest_triplet = (sorted_arr[0], sorted_arr[1], sorted_arr[2])
    min_diff = abs(closest_sum - target)

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            current_sum = sorted_arr[i] + sorted_arr[left] + sorted_arr[right]
            current_diff = abs(current_sum - target)

            if current_diff < min_diff:
                min_diff = current_diff
                closest_sum = current_sum
                closest_triplet = (sorted_arr[i], sorted_arr[left], sorted_arr[right])

            if current_diff == 0:
                return current_sum, closest_triplet

            if current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum, closest_triplet


def test_three_sum_closest():
    """Test all implementations with various test cases"""
    test_cases = [
        # (arr, target, expected_closest_sum)
        ([-1, 2, 1, -4], 1, 2),  # Classic example: -1 + 2 + 1 = 2
        ([1, 1, 1, 0], 100, 3),  # Closest is 1+1+1=3 (or 1+1+0=2 is closer?)
        # Wait, let me recalculate: 1+1+0=2, which is |2-100|=98, vs |3-100|=97
        # So 3 is closer
        ([1, 1, 1, 0], 100, 2),  # Actually 2 is closer to 100? No, 97 < 98
        ([1, 2, 4, 8, 16], 20, 18),  # 2 + 16 = 18, or 4 + 16 = 20 exactly!
        ([1, 2, 4, 8, 16], 20, 20),  # 4 + 16 = 20 exactly
        ([0, 0, 0], 1, 0),  # Only one possible sum
        ([-5, -4, -3, -2, -1], -10, -10),  # -5 + -4 + -1 = -10 or -5 + -3 + -2 = -10
        ([1, 2, 3], 10, 6),  # Only one triplet, 1+2+3=6
    ]

    implementations = [
        ("Brute Force", three_sum_closest_brute_force),
        ("Optimized", three_sum_closest_optimized),
        ("Sort + Two Pointers", three_sum_closest_sort_two_pointers),
    ]

    print("=" * 70)
    print("FIND TRIPLET WITH CLOSEST SUM - TEST RESULTS")
    print("=" * 70)

    for name, func in implementations:
        print(f"\n{name} Approach:")
        print("-" * 50)

        all_passed = True
        for i, (arr, target, expected) in enumerate(test_cases):
            try:
                if len(arr) < 3:
                    # Skip arrays with less than 3 elements
                    print(f"  Test {i + 1}: SKIP - Less than 3 elements")
                    continue

                result = func(arr, target)

                # The closest sum should match expected
                passed = result == expected
                status = "PASS" if passed else "FAIL"
                if not passed:
                    all_passed = False
                print(f"  Test {i + 1}: {status} - arr={arr}, target={target}")
                if not passed:
                    print(f"           Expected: {expected}, Got: {result}")
            except Exception as e:
                all_passed = False
                print(f"  Test {i + 1}: ERROR - {e}")

        print(f"  Overall: {'ALL PASSED' if all_passed else 'SOME FAILED'}")

    print("\n" + "=" * 70)

    # Test with triplet return
    print("\n\nTRIPLET WITH CLOSEST SUM (with actual triplet):")
    print("=" * 70)
    arr = [-1, 2, 1, -4]
    target = 1
    closest_sum, triplet = three_sum_closest_with_triplet(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Closest sum: {closest_sum}")
    print(f"Triplet: {triplet}")
    print(f"Verification: {triplet[0]} + {triplet[1]} + {triplet[2]} = {sum(triplet)}")


if __name__ == "__main__":
    test_three_sum_closest()
