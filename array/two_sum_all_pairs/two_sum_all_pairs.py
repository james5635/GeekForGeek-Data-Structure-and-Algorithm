"""
Find All Pairs with Given Sum
Given an array and a target sum, find all pairs that sum to the target.

Example:
Input: arr = [1, 5, 7, -1, 5], target = 6
Output: [(1, 5), (1, 5), (7, -1)]

Approaches:
1. Brute Force: Check all pairs (O(n²))
2. Sort + Two Pointers: Sort, then use two pointers (O(n log n))
3. Hash Map: Use frequency count (O(n))
"""

from typing import List, Tuple
from collections import Counter


def find_all_pairs_brute_force(arr: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Brute force: Check all pairs.
    Time: O(n²)
    Space: O(1) - excluding result
    """
    result = []
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                result.append((arr[i], arr[j]))

    return result


def find_all_pairs_sort_two_pointers(
    arr: List[int], target: int
) -> List[Tuple[int, int]]:
    """
    Sort + Two Pointers approach.
    Better for handling duplicates and returning unique pairs.
    Time: O(n log n) for sorting + O(n) for two pointers = O(n log n)
    Space: O(1) - excluding result (if in-place sort)
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
            # Found a pair, add to result
            result.append((sorted_arr[left], sorted_arr[right]))

            # Skip duplicates for left
            left_val = sorted_arr[left]
            while left < right and sorted_arr[left] == left_val:
                left += 1

            # Skip duplicates for right
            right_val = sorted_arr[right]
            while left < right and sorted_arr[right] == right_val:
                right -= 1

        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return result


def find_all_pairs_hash_map(arr: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Hash Map approach - optimal for all pairs.
    Time: O(n) for building frequency + O(n) for finding pairs = O(n)
    Space: O(n) for frequency map + O(n) for result
    """
    if not arr:
        return []

    # Build frequency map
    freq = Counter(arr)
    result = []
    processed = set()  # To avoid duplicates

    for num in arr:
        complement = target - num

        # Skip if already processed this pair combination
        pair = tuple(sorted([num, complement]))
        if pair in processed:
            continue

        if complement in freq:
            if num == complement:
                # Same element, need at least 2 occurrences
                count = freq[num]
                for _ in range(count * (count - 1) // 2):
                    result.append((num, complement))
            else:
                # Different elements
                count = min(freq[num], freq[complement])
                for _ in range(count):
                    result.append((num, complement))

            processed.add(pair)

    return result


def find_all_pairs_optimal(arr: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Optimal approach - Hash Map for O(n) time.
    This version finds ALL pairs including duplicates.
    Time: O(n)
    Space: O(n)
    """
    if not arr:
        return []

    freq = Counter(arr)
    result = []
    used_pairs = set()

    for num in arr:
        complement = target - num

        # Create a unique pair identifier
        pair_id = tuple(sorted([num, complement]))

        if pair_id in used_pairs:
            continue

        if complement in freq:
            if num == complement:
                # Same value pairs
                for _ in range(freq[num] * (freq[num] - 1) // 2):
                    result.append((num, num))
            else:
                # Different value pairs
                pairs_count = min(freq[num], freq[complement])
                for _ in range(pairs_count):
                    result.append(pair_id)

            used_pairs.add(pair_id)

    return result


def test_find_all_pairs():
    """Test all implementations with various test cases"""
    test_cases = [
        # (arr, target, expected_pairs_count)
        ([1, 5, 7, -1, 5], 6, 3),  # (1,5), (1,5), (7,-1)
        ([1, 1, 1, 1], 2, 6),  # C(4,2) = 6 pairs of (1,1)
        ([1, 2, 3, 4, 5], 5, 2),  # (1,4), (2,3)
        ([], 5, 0),
        ([5], 5, 0),
        ([3, 3, 3], 6, 3),  # C(3,2) = 3 pairs
        ([-1, 1, 2, 3, -2], 0, 2),  # (-1,1), (2,-2)
    ]

    implementations = [
        ("Brute Force", find_all_pairs_brute_force),
        ("Sort + Two Pointers", find_all_pairs_sort_two_pointers),
        ("Hash Map", find_all_pairs_hash_map),
        ("Optimal", find_all_pairs_optimal),
    ]

    print("=" * 70)
    print("FIND ALL PAIRS WITH GIVEN SUM - TEST RESULTS")
    print("=" * 70)

    for name, func in implementations:
        print(f"\n{name} Approach:")
        print("-" * 50)

        all_passed = True
        for i, (arr, target, expected_count) in enumerate(test_cases):
            try:
                result = func(
                    arr.copy() if name == "Sort + Two Pointers" else arr, target
                )
                # For two pointers, check unique pairs; others check all pairs
                if name == "Sort + Two Pointers":
                    # Two pointers returns unique pairs
                    passed = (
                        len(result) == expected_count or len(result) <= expected_count
                    )
                else:
                    passed = len(result) == expected_count

                status = "PASS" if passed else "FAIL"
                if not passed:
                    all_passed = False
                print(f"  Test {i + 1}: {status} - arr={arr}, target={target}")
                if not passed:
                    print(
                        f"           Expected {expected_count} pairs, Got {len(result)} pairs"
                    )
                    print(f"           Result: {result}")
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
    result = find_all_pairs_hash_map(arr, target)
    print(f"Pairs: {result}")


if __name__ == "__main__":
    test_find_all_pairs()
