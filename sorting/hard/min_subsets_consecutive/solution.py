"""
Count Minimum Number of Subsets/Subsequences with Consecutive Numbers

Problem Description:
Given an array arr[] of n integers, find the minimum number of subsets
(or subsequences) such that each subset contains consecutive integers.
In other words, partition the array into minimum number of groups where
each group contains consecutive numbers.

Examples:
- Input: arr[] = [1, 2, 3, 4]
  Output: 1
  Explanation: All elements can be in one subset: {1, 2, 3, 4}

- Input: arr[] = [1, 2, 4, 5, 7]
  Output: 3
  Explanation: Three subsets: {1, 2}, {4, 5}, {7}

- Input: arr[] = [1, 3, 5, 7]
  Output: 4
  Explanation: Each element forms its own subset

Approach 1: Greedy Sorting
1. Sort the array - O(n log n)
2. Count consecutive groups - O(n)
3. Each break in consecutive sequence means new subset
4. Time: O(n log n), Space: O(1)

Approach 2: Using Hash Map (for unsorted arrays)
1. Count frequency of each element - O(n)
2. For each element, check if it's start of a consecutive sequence
3. Time: O(n), Space: O(n)

Time Complexity: O(n log n) for sorting approach
Space Complexity: O(1) auxiliary for sorting approach
"""

from collections import Counter


def min_subsets_consecutive_sorting(arr):
    """
    Count minimum subsets using sorting.
    Optimal and simple approach.

    Args:
        arr: Input array

    Returns:
        int: Minimum number of subsets
    """
    if not arr:
        return 0

    if len(arr) == 1:
        return 1

    arr.sort()
    subsets = 1

    for i in range(1, len(arr)):
        # Skip duplicates (they don't create new subsets)
        if arr[i] == arr[i - 1]:
            continue
        if arr[i] != arr[i - 1] + 1:
            # Gap found, need new subset
            subsets += 1

    return subsets


def min_subsets_consecutive_hash(arr):
    """
    Count minimum subsets using hash map.
    Works without sorting but uses extra space.

    Args:
        arr: Input array

    Returns:
        int: Minimum number of subsets
    """
    if not arr:
        return 0

    freq = Counter(arr)
    elements = sorted(freq.keys())

    subsets = 1
    for i in range(1, len(elements)):
        if elements[i] != elements[i - 1] + 1:
            subsets += 1

    return subsets


def min_subsets_consecutive_detailed(arr):
    """
    Return both count and the actual subsets.

    Args:
        arr: Input array

    Returns:
        tuple: (count, list of subsets)
    """
    if not arr:
        return 0, []

    arr.sort()
    subsets = []
    current_subset = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current_subset.append(arr[i])
        else:
            subsets.append(current_subset)
            current_subset = [arr[i]]

    subsets.append(current_subset)
    return len(subsets), subsets


def min_subsets_with_duplicates(arr):
    """
    Handle arrays with duplicate elements.
    Duplicates must be in same subset if they are consecutive.

    Args:
        arr: Input array (may contain duplicates)

    Returns:
        int: Minimum number of subsets
    """
    if not arr:
        return 0

    # Remove duplicates and sort
    unique_elements = sorted(set(arr))

    if len(unique_elements) == 1:
        return 1

    subsets = 1
    for i in range(1, len(unique_elements)):
        if unique_elements[i] != unique_elements[i - 1] + 1:
            subsets += 1

    return subsets


def min_subsets_consecutive_optimized(arr):
    """
    Optimized single-pass approach after sorting.

    Args:
        arr: Input array

    Returns:
        int: Minimum number of subsets
    """
    if not arr:
        return 0

    arr.sort()

    # Count gaps between consecutive elements (skip duplicates)
    gaps = sum(
        1
        for i in range(1, len(arr))
        if arr[i] != arr[i - 1] and arr[i] != arr[i - 1] + 1
    )

    return gaps + 1


def can_form_single_subset(arr):
    """
    Check if all elements can form a single consecutive subset.

    Args:
        arr: Input array

    Returns:
        bool: True if single subset possible
    """
    if not arr:
        return True

    arr.sort()

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return False

    return True


def run_tests():
    """Test cases for minimum subsets consecutive problem."""
    test_cases = [
        {
            "arr": [1, 2, 3, 4],
            "expected": 1,
            "description": "All consecutive",
        },
        {
            "arr": [1, 2, 4, 5, 7],
            "expected": 3,
            "description": "Three groups: {1,2}, {4,5}, {7}",
        },
        {
            "arr": [1, 3, 5, 7],
            "expected": 4,
            "description": "All isolated",
        },
        {
            "arr": [5],
            "expected": 1,
            "description": "Single element",
        },
        {
            "arr": [],
            "expected": 0,
            "description": "Empty array",
        },
        {
            "arr": [10, 11, 12, 20, 21, 22, 30],
            "expected": 3,
            "description": "Multiple groups of 3",
        },
        {
            "arr": [-3, -2, -1, 0, 1, 5, 6],
            "expected": 2,
            "description": "Negative and positive",
        },
        {
            "arr": [1, 2, 2, 3, 3, 4],
            "expected": 1,
            "description": "With duplicates (single subset)",
        },
        {
            "arr": [1, 1, 3, 3, 5, 5],
            "expected": 3,
            "description": "With duplicates (multiple subsets)",
        },
        {
            "arr": [100, 101, 102, 200, 201],
            "expected": 2,
            "description": "Large numbers",
        },
    ]

    print("Running Minimum Subsets Consecutive Tests:")
    print("=" * 60)

    all_passed = True
    methods = [
        ("Sorting", min_subsets_consecutive_sorting),
    ]

    for method_name, method in methods:
        print(f"\n--- Testing {method_name} ---")
        for i, test in enumerate(test_cases, 1):
            result = method(test["arr"].copy())
            passed = result == test["expected"]

            status = "PASS" if passed else "FAIL"
            print(f"\nTest {i}: {status}")
            print(f"Description: {test['description']}")
            print(f"Input: {test['arr']}")
            print(f"Expected: {test['expected']}")
            print(f"Got: {result}")

            if not passed:
                all_passed = False

    # Test detailed output
    print("\n--- Testing Detailed Output ---")
    arr = [1, 2, 4, 5, 7, 8, 10]
    count, subsets = min_subsets_consecutive_detailed(arr.copy())
    print(f"Input: {arr}")
    print(f"Count: {count}")
    print(f"Subsets: {subsets}")

    # Test with duplicates
    print("\n--- Testing With Duplicates ---")
    arr = [1, 1, 2, 2, 4, 4, 5, 5]
    result = min_subsets_with_duplicates(arr)
    print(f"Input: {arr}")
    print(f"Minimum subsets: {result}")

    print("\n" + "=" * 60)
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")

    return all_passed


if __name__ == "__main__":
    run_tests()
