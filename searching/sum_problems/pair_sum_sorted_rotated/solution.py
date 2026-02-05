"""
Pair Sum in Sorted Rotated Array

Problem Description:
Given an array arr[] of size n, which is sorted and then rotated around an unknown pivot,
the task is to check whether there exists a pair of elements in the array whose sum
equals a given target value.

Examples:
- Input: arr[] = [11, 15, 6, 8, 9, 10], target = 16
  Output: True
  Explanation: There is a pair (6, 10) with sum 16

- Input: arr[] = [11, 11, 15, 26, 38, 9, 10], target = 35
  Output: True
  Explanation: There is a pair (26, 9) with sum 35

- Input: arr[] = [9, 10, 10, 11, 15, 26, 38], target = 45
  Output: False
  Explanation: No pair sums to 45

Approach:
1. Find the pivot (largest element) which divides array into two sorted parts
2. Use two pointers: one at smallest element (pivot+1), one at largest (pivot)
3. Apply standard two-pointer technique for sorted arrays

Time Complexity: O(n)
Space Complexity: O(1)
"""


def find_pivot(arr):
    """
    Find the pivot index (index of largest element) in rotated sorted array.

    Args:
        arr: Rotated sorted array

    Returns:
        int: Index of pivot element
    """
    n = len(arr)

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return i

    # Array is not rotated
    return n - 1


def pair_sum_rotated(arr, target):
    """
    Check if there exists a pair with given sum in sorted rotated array.

    Args:
        arr: Sorted and rotated array
        target: Target sum

    Returns:
        bool: True if pair exists, False otherwise
    """
    if not arr or len(arr) < 2:
        return False

    n = len(arr)

    # Find pivot
    pivot = find_pivot(arr)

    # Initialize pointers
    # Left is at smallest element (after pivot)
    left = (pivot + 1) % n
    # Right is at largest element (pivot)
    right = pivot

    while left != right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True

        # If sum is less than target, move left forward to increase sum
        if current_sum < target:
            left = (left + 1) % n
        else:
            # If sum is greater than target, move right backward to decrease sum
            right = (n + right - 1) % n

    return False


def pair_sum_rotated_with_pair(arr, target):
    """
    Return the actual pair if found, otherwise None.

    Args:
        arr: Sorted and rotated array
        target: Target sum

    Returns:
        tuple or None: The pair if found, None otherwise
    """
    if not arr or len(arr) < 2:
        return None

    n = len(arr)
    pivot = find_pivot(arr)

    left = (pivot + 1) % n
    right = pivot

    while left != right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (arr[left], arr[right])

        if current_sum < target:
            left = (left + 1) % n
        else:
            right = (n + right - 1) % n

    return None


def run_tests():
    """Test cases for the pair sum in rotated array problem."""
    test_cases = [
        # Test case 1: Basic rotated array
        {
            "input": [11, 15, 6, 8, 9, 10],
            "target": 16,
            "expected": True,
            "pair": (6, 10),
            "description": "Basic rotated array, pair (6,10) exists",
        },
        # Test case 2: Another rotated array
        {
            "input": [11, 11, 15, 26, 38, 9, 10],
            "target": 35,
            "expected": True,
            "pair": (26, 9),
            "description": "Pair (26,9) with sum 35",
        },
        # Test case 3: No pair exists
        {
            "input": [9, 10, 10, 11, 15, 26, 38],
            "target": 45,
            "expected": False,
            "pair": None,
            "description": "No pair sums to 45",
        },
        # Test case 4: Not rotated (edge case)
        {
            "input": [1, 2, 3, 4, 5],
            "target": 7,
            "expected": True,
            "pair": (2, 5),
            "description": "Array not rotated, pair (2,5)",
        },
        # Test case 5: Two elements
        {
            "input": [2, 1],
            "target": 3,
            "expected": True,
            "pair": (1, 2),
            "description": "Two element array",
        },
        # Test case 6: Negative target
        {
            "input": [5, -3, 0, 2, 4],
            "target": -1,
            "expected": True,
            "pair": (-3, 2),
            "description": "Negative target: (-3) + 2 = -1",
        },
        # Test case 7: Duplicate elements
        {
            "input": [5, 5, 5, 5],
            "target": 10,
            "expected": True,
            "pair": (5, 5),
            "description": "All duplicates, sum 10 exists",
        },
    ]

    print("Running Pair Sum in Rotated Array Tests:")
    print("=" * 60)

    all_passed = True
    for i, test in enumerate(test_cases, 1):
        result = pair_sum_rotated(test["input"].copy(), test["target"])
        passed = result == test["expected"]

        status = "PASS" if passed else "FAIL"
        print(f"\nTest {i}: {status}")
        print(f"Description: {test['description']}")
        print(f"Input: {test['input']}")
        print(f"Target: {test['target']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")

        # Also show the pair if exists
        pair_result = pair_sum_rotated_with_pair(test["input"].copy(), test["target"])
        print(f"Pair found: {pair_result}")

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
