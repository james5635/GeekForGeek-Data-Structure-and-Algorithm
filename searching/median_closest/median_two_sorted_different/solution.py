"""
Median of Two Sorted Arrays (Different Sizes)

Problem Description:
Given two sorted arrays a[] and b[] of different sizes, find the median of these
sorted arrays. Assume that the two sorted arrays are merged and then median is
selected from the combined array.

Examples:
- Input: a = [-5, 3, 6, 12, 15], b = [-12, -10, -6, -3, 4, 10]
  Output: 3
  Explanation: Merged = [-12, -10, -6, -5, -3, 3, 4, 6, 10, 12, 15]
               Median (middle element) = 3

- Input: a = [1], b = [2, 4, 5, 6, 7]
  Output: 4.5
  Explanation: Merged = [1, 2, 4, 5, 6, 7]
               Middle two: 4 and 5, Median = (4 + 5) / 2 = 4.5

Approach:
Use binary search on the smaller array to find correct partition.
Ensure left half has exactly (m + n + 1) // 2 elements.
Handle both odd and even total lengths.

Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)
"""


def median_of_two_sorted_arrays_diff_size(a, b):
    """
    Find median of two sorted arrays of different sizes.

    Args:
        a: First sorted array
        b: Second sorted array

    Returns:
        float: Median of the merged array
    """
    if not a and not b:
        raise ValueError("At least one array must be non-empty")

    # Ensure a is the smaller array
    if len(a) > len(b):
        a, b = b, a

    n, m = len(a), len(b)

    # Binary search on smaller array
    low, high = 0, n

    while low <= high:
        mid1 = (low + high) // 2
        mid2 = (n + m + 1) // 2 - mid1

        # Find elements around partition
        l1 = float("-inf") if mid1 == 0 else a[mid1 - 1]
        r1 = float("inf") if mid1 == n else a[mid1]
        l2 = float("-inf") if mid2 == 0 else b[mid2 - 1]
        r2 = float("inf") if mid2 == m else b[mid2]

        # Check if partition is valid
        if l1 <= r2 and l2 <= r1:
            # Valid partition found
            if (n + m) % 2 == 0:
                # Even length: average of two middle elements
                return (max(l1, l2) + min(r1, r2)) / 2.0
            else:
                # Odd length: middle element
                return max(l1, l2)

        # Adjust partition
        if l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1

    return 0.0


def median_merge_approach(a, b):
    """
    Alternative merge approach (O(m+n) time).

    Args:
        a: First sorted array
        b: Second sorted array

    Returns:
        float: Median of the merged array
    """
    n, m = len(a), len(b)
    i = j = 0
    m1 = m2 = -1

    # Loop until we pass the middle
    for count in range((n + m) // 2 + 1):
        m2 = m1

        if i < n and j < m:
            if a[i] > b[j]:
                m1 = b[j]
                j += 1
            else:
                m1 = a[i]
                i += 1
        elif i < n:
            m1 = a[i]
            i += 1
        else:
            m1 = b[j]
            j += 1

    if (n + m) % 2 == 1:
        return m1
    else:
        return (m1 + m2) / 2.0


def run_tests():
    """Test cases for median of two sorted arrays with different sizes."""
    test_cases = [
        # Test case 1: Odd total length
        {
            "a": [-5, 3, 6, 12, 15],
            "b": [-12, -10, -6, -3, 4, 10],
            "expected": 3,
            "description": "Odd total length: median is 3",
        },
        # Test case 2: Even total length
        {
            "a": [1],
            "b": [2, 4, 5, 6, 7],
            "expected": 4.5,
            "description": "Even total: (4+5)/2 = 4.5",
        },
        # Test case 3: One array empty
        {
            "a": [],
            "b": [1, 2, 3, 4, 5],
            "expected": 3,
            "description": "First array empty",
        },
        # Test case 4: Single elements
        {"a": [1], "b": [2], "expected": 1.5, "description": "Two single elements"},
        # Test case 5: a is larger
        {
            "a": [1, 2, 3, 4, 5, 6, 7, 8],
            "b": [3, 4],
            "expected": 4,
            "description": "First array larger",
        },
        # Test case 6: Negative numbers
        {
            "a": [-10, -5, 0],
            "b": [-3, -1],
            "expected": -3,
            "description": "Negative numbers mix",
        },
        # Test case 7: Large difference in sizes
        {
            "a": [100],
            "b": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "expected": 6.5,
            "description": "One element vs many",
        },
    ]

    print("Running Median of Two Sorted Arrays (Different Sizes) Tests:")
    print("=" * 60)

    all_passed = True
    for i, test in enumerate(test_cases, 1):
        # Handle empty array case
        a_copy = test["a"].copy() if test["a"] else []
        b_copy = test["b"].copy() if test["b"] else []

        if not a_copy:
            result_bs = median_merge_approach(a_copy, b_copy)
            result_merge = result_bs
        else:
            result_bs = median_of_two_sorted_arrays_diff_size(a_copy, b_copy)
            result_merge = median_merge_approach(a_copy, b_copy)

        passed_bs = abs(result_bs - test["expected"]) < 1e-9
        passed_merge = abs(result_merge - test["expected"]) < 1e-9

        status = "PASS" if passed_bs and passed_merge else "FAIL"
        print(f"\nTest {i}: {status}")
        print(f"Description: {test['description']}")
        print(f"Array a: {test['a']}")
        print(f"Array b: {test['b']}")
        print(f"Expected: {test['expected']}")
        print(f"Got (Binary Search): {result_bs}")
        print(f"Got (Merge): {result_merge}")

        if not (passed_bs and passed_merge):
            all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")

    return all_passed


if __name__ == "__main__":
    run_tests()
