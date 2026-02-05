"""
Maximum Element in Bitonic Array

Problem Description:
Given an array arr[] of integers which is initially strictly increasing and then
strictly decreasing (bitonic sequence), find the bitonic point (maximum value).

Note: Bitonic Point is a point in bitonic sequence before which elements are
strictly increasing and after which elements are strictly decreasing.

Examples:
- Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
  Output: 8
  Explanation: 8 is the maximum element at index 5

- Input: arr[] = [10, 20, 30, 40, 50]
  Output: 50
  Explanation: Array is strictly increasing, last element is max

- Input: arr[] = [120, 100, 80, 20, 0]
  Output: 120
  Explanation: Array is strictly decreasing, first element is max

Approach:
Use modified binary search:
- If arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]: found peak
- If arr[mid] > arr[mid-1]: peak is on right
- Else: peak is on left

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def find_max_in_bitonic(arr):
    """
    Find maximum element in bitonic array using binary search.

    Args:
        arr: Bitonic array (first increasing, then decreasing)

    Returns:
        int: Maximum element
    """
    if not arr:
        return None

    if len(arr) == 1:
        return arr[0]

    n = len(arr)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if mid is the peak
        # Handle edge cases for first and last elements
        prev = arr[mid - 1] if mid > 0 else float("-inf")
        next_val = arr[mid + 1] if mid < n - 1 else float("-inf")

        if arr[mid] > prev and arr[mid] > next_val:
            return arr[mid]

        # If mid is on increasing slope, peak is on right
        if arr[mid] > prev:
            left = mid + 1
        else:
            # Mid is on decreasing slope, peak is on left
            right = mid - 1

    return arr[left] if left < n else arr[right]


def find_max_linear(arr):
    """
    Alternative linear search approach (O(n) time).

    Args:
        arr: Bitonic array

    Returns:
        int: Maximum element
    """
    if not arr:
        return None

    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num

    return max_val


def find_max_with_index(arr):
    """
    Find maximum element and its index.

    Args:
        arr: Bitonic array

    Returns:
        tuple: (max_value, index)
    """
    if not arr:
        return None, None

    if len(arr) == 1:
        return arr[0], 0

    n = len(arr)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        prev = arr[mid - 1] if mid > 0 else float("-inf")
        next_val = arr[mid + 1] if mid < n - 1 else float("-inf")

        if arr[mid] > prev and arr[mid] > next_val:
            return arr[mid], mid

        if arr[mid] > prev:
            left = mid + 1
        else:
            right = mid - 1

    idx = left if left < n else right
    return arr[idx], idx


def run_tests():
    """Test cases for maximum element in bitonic array."""
    test_cases = [
        # Test case 1: Standard bitonic
        {
            "input": [1, 2, 4, 5, 7, 8, 3],
            "expected": 8,
            "description": "Standard bitonic: peak at 8",
        },
        # Test case 2: Strictly increasing
        {
            "input": [10, 20, 30, 40, 50],
            "expected": 50,
            "description": "Strictly increasing: last element",
        },
        # Test case 3: Strictly decreasing
        {
            "input": [120, 100, 80, 20, 0],
            "expected": 120,
            "description": "Strictly decreasing: first element",
        },
        # Test case 4: Single element
        {"input": [5], "expected": 5, "description": "Single element"},
        # Test case 5: Two elements increasing
        {"input": [1, 2], "expected": 2, "description": "Two elements increasing"},
        # Test case 6: Two elements decreasing
        {"input": [2, 1], "expected": 2, "description": "Two elements decreasing"},
        # Test case 7: Peak in middle
        {
            "input": [1, 3, 5, 7, 9, 11, 10, 8, 6, 4, 2],
            "expected": 11,
            "description": "Peak in middle: 11",
        },
        # Test case 8: Large values
        {
            "input": [1000000, 2000000, 3000000, 2000000, 1000000],
            "expected": 3000000,
            "description": "Large values",
        },
    ]

    print("Running Maximum Element in Bitonic Array Tests:")
    print("=" * 60)

    all_passed = True
    for i, test in enumerate(test_cases, 1):
        result_bs = find_max_in_bitonic(test["input"].copy())
        result_linear = find_max_linear(test["input"].copy())
        result_with_idx = find_max_with_index(test["input"].copy())

        passed = (
            result_bs == test["expected"]
            and result_linear == test["expected"]
            and result_with_idx[0] == test["expected"]
        )

        status = "PASS" if passed else "FAIL"
        print(f"\nTest {i}: {status}")
        print(f"Description: {test['description']}")
        print(f"Input: {test['input']}")
        print(f"Expected: {test['expected']}")
        print(f"Got (Binary Search): {result_bs}")
        print(f"Got (Linear): {result_linear}")
        print(f"Got (With Index): {result_with_idx}")

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
