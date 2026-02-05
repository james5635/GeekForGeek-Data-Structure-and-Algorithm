"""
Median of Two Sorted Arrays (Same Size)

Problem Description:
Given two sorted arrays a[] and b[], each of size n, find the median of the array
obtained after merging a[] and b[].

Note: Since the size of the merged array will always be even, the median will be
the average of the middle two numbers.

Examples:
- Input: a = [1, 12, 15, 26, 38], b = [2, 13, 17, 30, 45]
  Output: 16.0
  Explanation: Merged = [1, 2, 12, 13, 15, 17, 26, 30, 38, 45]
               Middle two: 15 and 17, Median = (15 + 17) / 2 = 16

- Input: a = [10], b = [21]
  Output: 15.5
  Explanation: Merged = [10, 21], Median = (10 + 21) / 2 = 15.5

Approach:
Use binary search to partition both arrays such that:
- Left half contains exactly n elements (half of total)
- All elements in left half <= all elements in right half
- Median = (max(left) + min(right)) / 2

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def median_of_two_sorted_arrays(a, b):
    """
    Find median of two sorted arrays of same size using binary search.

    Args:
        a: First sorted array
        b: Second sorted array (same size as a)

    Returns:
        float: Median of the merged array
    """
    if not a or not b or len(a) != len(b):
        raise ValueError("Both arrays must be non-empty and of same size")

    n = len(a)

    # We can take [0...n] elements from a
    low, high = 0, n

    while low <= high:
        # Take mid1 elements from a
        mid1 = (low + high) // 2
        # Take mid2 elements from b (total left half should be n)
        mid2 = n - mid1

        # Find elements to the left and right of partition in a
        l1 = float("-inf") if mid1 == 0 else a[mid1 - 1]
        r1 = float("inf") if mid1 == n else a[mid1]

        # Find elements to the left and right of partition in b
        l2 = float("-inf") if mid2 == 0 else b[mid2 - 1]
        r2 = float("inf") if mid2 == n else b[mid2]

        # Check if this is a valid partition
        if l1 <= r2 and l2 <= r1:
            # Valid partition found
            return (max(l1, l2) + min(r1, r2)) / 2.0

        # If we need to take fewer elements from a
        if l1 > r2:
            high = mid1 - 1
        else:
            # If we need to take more elements from a
            low = mid1 + 1

    return 0.0


def median_merge_approach(a, b):
    """
    Alternative approach using merge logic (O(n) time).

    Args:
        a: First sorted array
        b: Second sorted array

    Returns:
        float: Median of the merged array
    """
    n = len(a)
    i = j = 0
    m1 = m2 = -1

    # Loop till we reach n elements (middle of merged array)
    for _ in range(n + 1):
        m2 = m1

        if i < n and j < n:
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

    return (m1 + m2) / 2.0


def run_tests():
    """Test cases for median of two sorted arrays."""
    test_cases = [
        # Test case 1: Standard case
        {
            "a": [1, 12, 15, 26, 38],
            "b": [2, 13, 17, 30, 45],
            "expected": 16.0,
            "description": "Standard case: median is 16",
        },
        # Test case 2: Single element
        {
            "a": [10],
            "b": [21],
            "expected": 15.5,
            "description": "Single element arrays",
        },
        # Test case 3: Interleaved
        {
            "a": [1, 3, 5],
            "b": [2, 4, 6],
            "expected": 3.5,
            "description": "Perfectly interleaved: [1,2,3,4,5,6]",
        },
        # Test case 4: All elements in a smaller
        {
            "a": [1, 2, 3],
            "b": [10, 20, 30],
            "expected": 6.5,
            "description": "Separated ranges: median is (3+10)/2",
        },
        # Test case 5: Negative numbers
        {
            "a": [-5, -3, -1],
            "b": [0, 2, 4],
            "expected": -0.5,
            "description": "Negative and positive mix",
        },
        # Test case 6: Duplicates
        {
            "a": [1, 1, 1],
            "b": [1, 1, 1],
            "expected": 1.0,
            "description": "All duplicates",
        },
        # Test case 7: Large numbers
        {
            "a": [1000000, 2000000],
            "b": [3000000, 4000000],
            "expected": 2500000.0,
            "description": "Large numbers",
        },
    ]

    print("Running Median of Two Sorted Arrays Tests:")
    print("=" * 60)

    all_passed = True
    for i, test in enumerate(test_cases, 1):
        result_bs = median_of_two_sorted_arrays(test["a"].copy(), test["b"].copy())
        result_merge = median_merge_approach(test["a"].copy(), test["b"].copy())

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
