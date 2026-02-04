"""
Find Any Triplet with Given Sum (3Sum)
Given an array and a target sum, find any three elements that sum to the target.

Example:
Input: arr = [1, 4, 45, 6, 10, 8], target = 22
Output: [4, 10, 8] or [1, 4, 6, ... wait that's 4 elements]
Actually: 4 + 10 + 8 = 22, so [4, 10, 8]

Approaches:
1. Brute Force: O(n³) - three nested loops
2. Sort + Binary Search: O(n² log n) - fix one, binary search for two
3. Sort + Two Pointers: O(n²) - fix one, use two pointers for remaining
"""

from typing import List, Optional, Tuple


def three_sum_brute_force(
    arr: List[int], target: int
) -> Optional[Tuple[int, int, int]]:
    """
    Brute force: Check all triplets using three nested loops.
    Time: O(n³)
    Space: O(1)
    """
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return (arr[i], arr[j], arr[k])

    return None


def three_sum_sort_binary_search(
    arr: List[int], target: int
) -> Optional[Tuple[int, int, int]]:
    """
    Sort + Binary Search approach.
    Fix one element, then use binary search to find pair in remaining.
    Time: O(n log n) for sort + O(n * n log n) for search = O(n² log n)
    Space: O(1) or O(n) depending on sort implementation
    """
    if len(arr) < 3:
        return None

    # Sort the array
    sorted_arr = sorted(arr)
    n = len(sorted_arr)

    for i in range(n - 2):
        # Skip duplicate values for i
        if i > 0 and sorted_arr[i] == sorted_arr[i - 1]:
            continue

        # For remaining array [i+1 to n-1], find pair with sum = target - sorted_arr[i]
        remaining_target = target - sorted_arr[i]

        # Use binary search approach for two sum
        left, right = i + 1, n - 1

        while left < right:
            current_sum = sorted_arr[left] + sorted_arr[right]

            if current_sum == remaining_target:
                return (sorted_arr[i], sorted_arr[left], sorted_arr[right])
            elif current_sum < remaining_target:
                left += 1
            else:
                right -= 1

    return None


def three_sum_sort_two_pointers(
    arr: List[int], target: int
) -> Optional[Tuple[int, int, int]]:
    """
    Sort + Two Pointers approach - Optimal solution.
    Fix one element, use two pointers on remaining sorted array.
    Time: O(n log n) for sort + O(n²) for search = O(n²)
    Space: O(1) or O(n) depending on sort
    """
    if len(arr) < 3:
        return None

    # Sort the array
    sorted_arr = sorted(arr)
    n = len(sorted_arr)

    for i in range(n - 2):
        # Skip duplicate values for first element
        if i > 0 and sorted_arr[i] == sorted_arr[i - 1]:
            continue

        # Use two pointers for remaining sum
        left, right = i + 1, n - 1
        remaining_target = target - sorted_arr[i]

        while left < right:
            current_sum = sorted_arr[left] + sorted_arr[right]

            if current_sum == remaining_target:
                return (sorted_arr[i], sorted_arr[left], sorted_arr[right])
            elif current_sum < remaining_target:
                left += 1
            else:
                right -= 1

    return None


def three_sum_all_triplets(arr: List[int], target: int) -> List[Tuple[int, int, int]]:
    """
    Find ALL unique triplets (not just any one) with given sum.
    Uses sort + two pointers approach.
    Time: O(n²)
    Space: O(1) excluding result
    """
    if len(arr) < 3:
        return []

    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    result = []

    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and sorted_arr[i] == sorted_arr[i - 1]:
            continue

        left, right = i + 1, n - 1
        remaining_target = target - sorted_arr[i]

        while left < right:
            current_sum = sorted_arr[left] + sorted_arr[right]

            if current_sum == remaining_target:
                result.append((sorted_arr[i], sorted_arr[left], sorted_arr[right]))

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


def test_three_sum():
    """Test all implementations with various test cases"""
    test_cases = [
        # (arr, target, expected_triplet or None)
        ([1, 4, 45, 6, 10, 8], 22, (4, 10, 8)),  # Basic case
        ([1, 2, 3, 4, 5], 9, (2, 3, 4)),  # Consecutive numbers
        ([0, -1, 2, -3, 1], 0, (-3, 1, 2)),  # With negatives
        ([], 5, None),  # Empty array
        ([1, 2], 3, None),  # Less than 3 elements
        ([1, 1, 1, 1], 3, (1, 1, 1)),  # All same
        ([-1, 0, 1, 2, -1, -4], 0, (-1, 0, 1)),  # Multiple valid triplets
    ]

    implementations = [
        ("Brute Force", three_sum_brute_force),
        ("Sort + Binary Search", three_sum_sort_binary_search),
        ("Sort + Two Pointers", three_sum_sort_two_pointers),
    ]

    print("=" * 70)
    print("FIND ANY TRIPLET WITH GIVEN SUM (3SUM) - TEST RESULTS")
    print("=" * 70)

    for name, func in implementations:
        print(f"\n{name} Approach:")
        print("-" * 50)

        all_passed = True
        for i, (arr, target, expected) in enumerate(test_cases):
            try:
                result = func(arr, target)

                # Check if result is valid (None or matching expected)
                if expected is None:
                    passed = result is None
                else:
                    # Result should be a valid triplet summing to target
                    if result is None:
                        passed = False
                    else:
                        # Check if sum matches target
                        passed = sum(result) == target

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

    # Test all triplets finder
    print("\n\nFIND ALL TRIPLETS - ADDITIONAL TEST")
    print("=" * 70)
    arr = [-1, 0, 1, 2, -1, -4]
    target = 0
    result = three_sum_all_triplets(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"All unique triplets: {result}")

    # Detailed example
    print("\n\nDetailed Example:")
    print("-" * 50)
    arr = [1, 4, 45, 6, 10, 8]
    target = 22
    print(f"Array: {arr}")
    print(f"Target: {target}")
    result = three_sum_sort_two_pointers(arr, target)
    print(f"Triplet: {result}")
    if result:
        print(f"Verification: {result[0]} + {result[1]} + {result[2]} = {sum(result)}")


if __name__ == "__main__":
    test_three_sum()
