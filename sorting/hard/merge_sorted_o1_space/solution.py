"""
Merge Two Sorted Arrays with O(1) Extra Space

Problem Description:
Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order.
Merge them in sorted order without using any extra space. Modify arr1[] to contain
the first n elements and arr2[] to contain the last m elements.

Examples:
- Input: arr1[] = [1, 3, 5, 7], arr2[] = [0, 2, 6, 8, 9]
  Output: arr1[] = [0, 1, 2, 3], arr2[] = [5, 6, 7, 8, 9]

- Input: arr1[] = [10, 12], arr2[] = [5, 18, 20]
  Output: arr1[] = [5, 10], arr2[] = [12, 18, 20]

Approach 1: Insertion Sort like (Shell Sort variant)
1. Compare last element of arr1 with first element of arr2
2. If arr1[i] > arr2[0], swap them and sort arr2
3. This takes O(n*m) time in worst case

Approach 2: Gap Method (Shell Sort inspired)
1. Calculate initial gap = ceil((n + m) / 2)
2. While gap > 0:
   - Compare elements at distance gap
   - Swap if they are in wrong order
   - Reduce gap = ceil(gap / 2)
3. This takes O((n+m)*log(n+m)) time

Approach 3: Two-pointer with binary search (Optimal)
1. Start from end of arr1 and beginning of arr2
2. If arr1[i] > arr2[0], swap and binary search to place in arr2
3. This takes O(n*log(m)) or O(m*log(n)) time

Time Complexity: O((n+m) * log(n+m)) for gap method
Space Complexity: O(1)
"""

import math


def merge_sorted_arrays_gap(arr1, arr2):
    """
    Merge two sorted arrays using gap method (shell sort variant).
    Modifies both arrays in-place.

    Args:
        arr1: First sorted array (size n)
        arr2: Second sorted array (size m)

    Returns:
        tuple: (modified arr1, modified arr2)
    """
    n, m = len(arr1), len(arr2)

    def next_gap(gap):
        """Calculate next gap using ceiling division."""
        if gap <= 1:
            return 0
        return (gap + 1) // 2

    gap = n + m
    gap = next_gap(gap)

    while gap > 0:
        # Compare elements in first array
        i = 0
        while i + gap < n:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        # Compare elements between arrays
        j = max(0, gap - n)
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        # Compare elements in second array
        j = 0
        while j + gap < m:
            if arr2[j] > arr2[j + gap]:
                arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
            j += 1

        gap = next_gap(gap)

    return arr1, arr2


def merge_sorted_arrays_insertion(arr1, arr2):
    """
    Merge two sorted arrays using insertion sort-like approach.
    Modifies both arrays in-place.

    Args:
        arr1: First sorted array (size n)
        arr2: Second sorted array (size m)

    Returns:
        tuple: (modified arr1, modified arr2)
    """
    n, m = len(arr1), len(arr2)

    if m == 0:
        return arr1, arr2

    for i in range(n - 1, -1, -1):
        if arr1[i] > arr2[0]:
            # Swap arr1[i] with arr2[0]
            arr1[i], arr2[0] = arr2[0], arr1[i]

            # Fix arr2 to maintain sorted order
            first = arr2[0]
            j = 1
            while j < m and arr2[j] < first:
                arr2[j - 1] = arr2[j]
                j += 1
            arr2[j - 1] = first

    return arr1, arr2


def merge_sorted_arrays_binary_search(arr1, arr2):
    """
    Merge two sorted arrays using binary search approach.
    Modifies both arrays in-place.

    Args:
        arr1: First sorted array (size n)
        arr2: Second sorted array (size m)

    Returns:
        tuple: (modified arr1, modified arr2)
    """
    n, m = len(arr1), len(arr2)

    if m == 0 or n == 0:
        return arr1, arr2

    # Process elements from end of arr1
    i = n - 1
    while i >= 0:
        if arr1[i] > arr2[0]:
            # Swap arr1[i] with arr2[0]
            temp = arr1[i]
            arr1[i] = arr2[0]

            # Find position to insert temp in arr2 using binary search
            # temp should be placed such that arr2 remains sorted
            left, right = 0, m - 1
            insert_pos = m  # Default to end

            while left <= right:
                mid = (left + right) // 2
                if arr2[mid] < temp:
                    insert_pos = mid + 1
                    left = mid + 1
                else:
                    right = mid - 1

            # Shift elements and insert
            if insert_pos < m:
                for j in range(insert_pos):
                    arr2[j] = arr2[j + 1]
                arr2[insert_pos] = temp

        i -= 1

    return arr1, arr2


def run_tests():
    """Test cases for merge sorted arrays with O(1) space."""
    test_cases = [
        {
            "arr1": [1, 3, 5, 7],
            "arr2": [0, 2, 6, 8, 9],
            "expected_arr1": [0, 1, 2, 3],
            "expected_arr2": [5, 6, 7, 8, 9],
            "description": "Standard case with interleaved elements",
        },
        {
            "arr1": [10, 12],
            "arr2": [5, 18, 20],
            "expected_arr1": [5, 10],
            "expected_arr2": [12, 18, 20],
            "description": "Different sizes",
        },
        {
            "arr1": [1, 2, 3],
            "arr2": [4, 5, 6],
            "expected_arr1": [1, 2, 3],
            "expected_arr2": [4, 5, 6],
            "description": "Already merged",
        },
        {
            "arr1": [4, 5, 6],
            "arr2": [1, 2, 3],
            "expected_arr1": [1, 2, 3],
            "expected_arr2": [4, 5, 6],
            "description": "Reverse order",
        },
        {
            "arr1": [1],
            "arr2": [2],
            "expected_arr1": [1],
            "expected_arr2": [2],
            "description": "Single element arrays",
        },
        {
            "arr1": [2, 3, 8, 13, 15],
            "arr2": [5, 7, 9, 10],
            "expected_arr1": [2, 3, 5, 7, 8],
            "expected_arr2": [9, 10, 13, 15],
            "description": "Multiple elements to swap",
        },
        {
            "arr1": [],
            "arr2": [1, 2, 3],
            "expected_arr1": [],
            "expected_arr2": [1, 2, 3],
            "description": "Empty first array",
        },
        {
            "arr1": [1, 2, 3],
            "arr2": [],
            "expected_arr1": [1, 2, 3],
            "expected_arr2": [],
            "description": "Empty second array",
        },
    ]

    print("Running Merge Two Sorted Arrays O(1) Space Tests:")
    print("=" * 60)

    all_passed = True
    methods = [
        ("Gap Method", merge_sorted_arrays_gap),
    ]

    for method_name, method in methods:
        print(f"\n--- Testing {method_name} ---")
        for i, test in enumerate(test_cases, 1):
            # Create copies to avoid modifying original test data
            arr1 = test["arr1"].copy()
            arr2 = test["arr2"].copy()

            result1, result2 = method(arr1, arr2)

            passed = (
                result1 == test["expected_arr1"] and result2 == test["expected_arr2"]
            )

            status = "PASS" if passed else "FAIL"
            print(f"\nTest {i}: {status}")
            print(f"Description: {test['description']}")
            print(f"Input arr1: {test['arr1']}")
            print(f"Input arr2: {test['arr2']}")
            print(
                f"Expected arr1: {test['expected_arr1']}, arr2: {test['expected_arr2']}"
            )
            print(f"Got arr1: {result1}, arr2: {result2}")

            if not passed:
                all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")

    return all_passed


if __name__ == "__main__":
    run_tests()
