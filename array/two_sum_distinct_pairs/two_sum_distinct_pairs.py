"""
Find Distinct Pairs with Given Sum
Given an array and a target sum, find all distinct pairs that sum to the target.
Unlike 'all pairs', this returns unique pairs only (no duplicates).

Example:
Input: arr = [1, 5, 7, -1, 5], target = 6
Output: [(-1, 7), (1, 5)]  # Note: (1, 5) appears only once even though there are two 5s

Approaches:
1. Brute Force with Set: O(n²) - check all pairs, use set for uniqueness
2. Sort + Two Pointers: O(n log n) - sort, use two pointers
3. Hash Set: O(n) - use hash set to track complements
"""

from typing import List, Tuple, Set
from collections import Counter


def find_distinct_pairs_brute_force(
    arr: List[int], target: int
) -> List[Tuple[int, int]]:
    """
    Brute force: Check all pairs, use set to avoid duplicates.
    Time: O(n²)
    Space: O(k) where k is number of distinct pairs
    """
    distinct_pairs = set()
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                # Store as sorted tuple to avoid (a,b) and (b,a) duplicates
                pair = tuple(sorted([arr[i], arr[j]]))
                distinct_pairs.add(pair)

    return sorted(list(distinct_pairs))


def find_distinct_pairs_sort_two_pointers(
    arr: List[int], target: int
) -> List[Tuple[int, int]]:
    """
    Sort + Two Pointers approach.
    Returns distinct pairs only (no duplicates).
    Time: O(n log n) for sorting + O(n) for search = O(n log n)
    Space: O(1) - excluding result
    """
    if not arr:
        return []

    # Sort the array
    sorted_arr = sorted(arr)
    result = []
    left, right = 0, len(sorted_arr) - 1

    while left < right:
        current_sum = sorted_arr[left] + sorted_arr[right]

        if current_sum == target:
            # Found a distinct pair
            result.append((sorted_arr[left], sorted_arr[right]))

            # Skip all duplicates of left value
            left_val = sorted_arr[left]
            while left < right and sorted_arr[left] == left_val:
                left += 1

            # Skip all duplicates of right value
            right_val = sorted_arr[right]
            while left < right and sorted_arr[right] == right_val:
                right -= 1

        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return result


def find_distinct_pairs_hash_set(arr: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Hash Set approach.
    Uses set to track seen elements and avoid duplicates.
    Time: O(n)
    Space: O(n)
    """
    if not arr:
        return []

    seen = set()
    distinct_pairs = set()

    for num in arr:
        complement = target - num

        if complement in seen:
            # Found a pair
            pair = tuple(sorted([num, complement]))
            distinct_pairs.add(pair)

        seen.add(num)

    return sorted(list(distinct_pairs))


def find_distinct_pairs_optimal(arr: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Optimal approach - Hash Map with frequency tracking.
    Most efficient for handling duplicates.
    Time: O(n)
    Space: O(n)
    """
    if not arr:
        return []

    freq = Counter(arr)
    distinct_pairs = set()

    for num in list(freq.keys()):
        complement = target - num

        if complement not in freq:
            continue

        if num == complement:
            # Need at least 2 occurrences
            if freq[num] >= 2:
                distinct_pairs.add((num, complement))
        else:
            # Different values form a pair
            distinct_pairs.add(tuple(sorted([num, complement])))

    return sorted(list(distinct_pairs))


def test_find_distinct_pairs():
    """Test all implementations with various test cases"""
    test_cases = [
        # (arr, target, expected_distinct_pairs)
        ([1, 5, 7, -1, 5], 6, [(-1, 7), (1, 5)]),  # Basic case with duplicate 5
        ([1, 1, 1, 1], 2, [(1, 1)]),  # All same, only one distinct pair
        ([1, 2, 3, 4, 5], 5, [(1, 4), (2, 3)]),  # No duplicates
        ([], 5, []),  # Empty array
        ([5], 5, []),  # Single element
        ([3, 3, 3], 6, [(3, 3)]),  # All duplicates, one distinct pair
        ([-1, 1, 2, 3, -2], 0, [(-2, 2), (-1, 1)]),  # Negative numbers
        ([1, 2, 3, 4, 3, 2, 1], 4, [(1, 3), (2, 2)]),  # Multiple duplicates
    ]

    implementations = [
        ("Brute Force", find_distinct_pairs_brute_force),
        ("Sort + Two Pointers", find_distinct_pairs_sort_two_pointers),
        ("Hash Set", find_distinct_pairs_hash_set),
        ("Optimal (Hash Map)", find_distinct_pairs_optimal),
    ]

    print("=" * 70)
    print("FIND DISTINCT PAIRS WITH GIVEN SUM - TEST RESULTS")
    print("=" * 70)

    for name, func in implementations:
        print(f"\n{name} Approach:")
        print("-" * 50)

        all_passed = True
        for i, (arr, target, expected) in enumerate(test_cases):
            try:
                result = func(arr, target)
                # Sort both for comparison
                result_sorted = sorted(result)
                expected_sorted = sorted(expected)
                passed = result_sorted == expected_sorted
                status = "PASS" if passed else "FAIL"
                if not passed:
                    all_passed = False
                print(f"  Test {i + 1}: {status} - arr={arr}, target={target}")
                if not passed:
                    print(f"           Expected: {expected_sorted}")
                    print(f"           Got: {result_sorted}")
            except Exception as e:
                all_passed = False
                print(f"  Test {i + 1}: ERROR - {e}")

        print(f"  Overall: {'ALL PASSED' if all_passed else 'SOME FAILED'}")

    print("\n" + "=" * 70)

    # Print detailed example
    print("\nDetailed Example:")
    print("-" * 50)
    arr = [1, 5, 7, -1, 5]
    target = 6
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print("\nAll pairs (with duplicates):")
    all_pairs = find_all_pairs_brute_force(arr, target)
    print(f"  {all_pairs}")
    print("\nDistinct pairs only:")
    distinct_pairs = find_distinct_pairs_optimal(arr, target)
    print(f"  {distinct_pairs}")


# Import for the detailed example
def find_all_pairs_brute_force(arr, target):
    """Helper for comparison"""
    result = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                result.append((arr[i], arr[j]))
    return result


if __name__ == "__main__":
    test_find_distinct_pairs()
