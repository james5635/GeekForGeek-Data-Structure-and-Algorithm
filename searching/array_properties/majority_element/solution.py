"""
Majority Element

Problem Description:
Given an array arr[] of size n, find the element that appears more than n/2 times.
If no such element exists, return -1.

Examples:
- Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
  Output: 1
  Explanation: Element 1 appears 4 times, which is > 7/2 = 3.5

- Input: arr[] = [7]
  Output: 7
  Explanation: Single element is always majority

- Input: arr[] = [2, 13]
  Output: -1
  Explanation: No element appears more than 2/2 = 1 time

Approach (Moore's Voting Algorithm):
1. Find a candidate using voting: cancel out different elements
2. Verify if candidate is actually majority

Time Complexity: O(n)
Space Complexity: O(1)
"""


def majority_element(arr):
    """
    Find majority element using Boyer-Moore Voting Algorithm.

    Args:
        arr: List of integers

    Returns:
        int: Majority element or -1 if none exists
    """
    if not arr:
        return -1

    n = len(arr)

    # Phase 1: Find candidate
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Phase 2: Verify candidate
    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    if count > n // 2:
        return candidate
    else:
        return -1


def majority_element_hashing(arr):
    """
    Alternative approach using hash map (O(n) time, O(n) space).

    Args:
        arr: List of integers

    Returns:
        int: Majority element or -1 if none exists
    """
    if not arr:
        return -1

    n = len(arr)
    count_map = {}

    for num in arr:
        count_map[num] = count_map.get(num, 0) + 1
        if count_map[num] > n // 2:
            return num

    return -1


def majority_element_sorted(arr):
    """
    Alternative approach using sorting (O(n log n) time, O(1) space).

    Args:
        arr: List of integers

    Returns:
        int: Majority element or -1 if none exists
    """
    if not arr:
        return -1

    n = len(arr)
    arr_sorted = sorted(arr)

    # Majority element must be at position n//2 in sorted array
    candidate = arr_sorted[n // 2]

    # Verify
    count = sum(1 for num in arr if num == candidate)

    return candidate if count > n // 2 else -1


def run_tests():
    """Test cases for majority element problem."""
    test_cases = [
        # Test case 1: Standard majority
        {
            "input": [1, 1, 2, 1, 3, 5, 1],
            "expected": 1,
            "description": "Standard case: 1 appears 4 times (> 3.5)",
        },
        # Test case 2: Single element
        {"input": [7], "expected": 7, "description": "Single element"},
        # Test case 3: No majority
        {"input": [2, 13], "expected": -1, "description": "No majority element"},
        # Test case 4: All same
        {"input": [5, 5, 5, 5, 5], "expected": 5, "description": "All elements same"},
        # Test case 5: Majority at end
        {
            "input": [1, 2, 3, 3, 3, 3, 3],
            "expected": 3,
            "description": "Majority at end",
        },
        # Test case 6: Majority at start
        {
            "input": [1, 1, 1, 1, 2, 3, 4],
            "expected": 1,
            "description": "Majority at start",
        },
        # Test case 7: Alternating (no majority)
        {
            "input": [1, 2, 1, 2, 1, 2],
            "expected": -1,
            "description": "Alternating pattern, no majority",
        },
        # Test case 8: Large array
        {
            "input": [1] * 50 + [2] * 49,
            "expected": 1,
            "description": "Large array with clear majority",
        },
    ]

    print("Running Majority Element Tests:")
    print("=" * 60)

    all_passed = True
    for i, test in enumerate(test_cases, 1):
        result_moore = majority_element(test["input"].copy())
        result_hash = majority_element_hashing(test["input"].copy())
        result_sorted = majority_element_sorted(test["input"].copy())

        passed = (
            result_moore == test["expected"]
            and result_hash == test["expected"]
            and result_sorted == test["expected"]
        )

        status = "PASS" if passed else "FAIL"
        print(f"\nTest {i}: {status}")
        print(f"Description: {test['description']}")
        print(f"Input: {test['input'][:20]}{'...' if len(test['input']) > 20 else ''}")
        print(f"Expected: {test['expected']}")
        print(f"Got (Moore): {result_moore}")
        print(f"Got (Hash): {result_hash}")
        print(f"Got (Sorted): {result_sorted}")

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
