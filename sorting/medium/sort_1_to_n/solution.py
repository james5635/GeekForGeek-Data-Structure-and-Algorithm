"""
Sort Array Containing 1 to N Values

Given an array containing elements from 1 to n (where n is the array size),
sort the array efficiently without simply copying values 1 to n.

Algorithm:
1. Use Cycle Sort approach
2. For each element, if it's not at its correct position (index = value - 1),
   swap it with the element at its correct position
3. Continue until all elements are in place

Time Complexity: O(n) - Each element is swapped at most once
Space Complexity: O(1) - In-place sorting
"""


def sort_1_to_n(arr):
    """
    Sort array containing elements 1 to n using cycle sort.

    Args:
        arr: List of integers containing values from 1 to n

    Returns:
        list: Sorted array (1, 2, 3, ..., n)
    """
    if not arr:
        return []

    n = len(arr)
    i = 0

    while i < n:
        # The correct index for arr[i] is arr[i] - 1
        correct_idx = arr[i] - 1

        # If element is not at its correct position, swap it
        if arr[i] != arr[correct_idx]:
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
        else:
            # Element is at correct position, move to next
            i += 1

    return arr


def sort_1_to_n_alternative(arr):
    """
    Alternative implementation with explicit swap function.

    Args:
        arr: List of integers containing values from 1 to n

    Returns:
        list: Sorted array
    """
    if not arr:
        return []

    n = len(arr)

    def swap(i, j):
        """Swap elements at indices i and j."""
        arr[i], arr[j] = arr[j], arr[i]

    i = 0
    while i < n:
        correct_idx = arr[i] - 1

        # If not at correct position, swap
        if i != correct_idx:
            swap(i, correct_idx)
        else:
            i += 1

    return arr


def sort_1_to_n_using_negation(arr):
    """
    Alternative approach using negation (modifies array differently).
    Note: This only works if elements are guaranteed to be 1 to n.

    Args:
        arr: List of integers containing values from 1 to n

    Returns:
        list: Sorted array
    """
    if not arr:
        return []

    n = len(arr)

    # First, make all values negative to mark them
    for i in range(n):
        arr[i] = -arr[i]

    # Place each element at its correct position
    for i in range(n):
        val = -arr[i]
        correct_idx = val - 1

        if arr[correct_idx] > 0:
            # Already placed correctly
            continue

        # Mark the correct position
        arr[correct_idx] = -arr[correct_idx]

    # Restore values
    for i in range(n):
        if arr[i] < 0:
            arr[i] = -(i + 1)
        else:
            arr[i] = i + 1

    return arr


def test_sort_1_to_n():
    """Test cases for sorting array with 1 to n values."""
    # Test Case 1: Basic case
    arr = [2, 1, 3]
    result = sort_1_to_n(arr[:])
    expected = [1, 2, 3]
    assert result == expected, f"Test 1 failed: Expected {expected}, got {result}"
    print("Test 1 passed: Basic case")

    # Test Case 2: Larger array
    arr = [2, 1, 4, 3]
    result = sort_1_to_n(arr[:])
    expected = [1, 2, 3, 4]
    assert result == expected, f"Test 2 failed: Expected {expected}, got {result}"
    print("Test 2 passed: Larger array")

    # Test Case 3: Reverse sorted
    arr = [5, 4, 3, 2, 1]
    result = sort_1_to_n(arr[:])
    expected = [1, 2, 3, 4, 5]
    assert result == expected, f"Test 3 failed: Expected {expected}, got {result}"
    print("Test 3 passed: Reverse sorted")

    # Test Case 4: Already sorted
    arr = [1, 2, 3, 4, 5]
    result = sort_1_to_n(arr[:])
    expected = [1, 2, 3, 4, 5]
    assert result == expected, f"Test 4 failed: Expected {expected}, got {result}"
    print("Test 4 passed: Already sorted")

    # Test Case 5: Single element
    arr = [1]
    result = sort_1_to_n(arr[:])
    expected = [1]
    assert result == expected, f"Test 5 failed: Expected {expected}, got {result}"
    print("Test 5 passed: Single element")

    # Test Case 6: Empty array
    arr = []
    result = sort_1_to_n(arr[:])
    expected = []
    assert result == expected, f"Test 6 failed: Expected {expected}, got {result}"
    print("Test 6 passed: Empty array")

    # Test Case 7: Test alternative implementation
    arr = [3, 2, 5, 6, 1, 4]
    result1 = sort_1_to_n(arr[:])
    result2 = sort_1_to_n_alternative(arr[:])
    expected = [1, 2, 3, 4, 5, 6]
    assert result1 == expected, f"Test 7a failed: Expected {expected}, got {result1}"
    assert result2 == expected, f"Test 7b failed: Expected {expected}, got {result2}"
    print("Test 7 passed: Alternative implementation")

    # Test Case 8: In-place verification
    arr = [3, 1, 2]
    original_id = id(arr)
    sort_1_to_n(arr)
    assert id(arr) == original_id, "Test 8 failed: Function should sort in-place"
    assert arr == [1, 2, 3], f"Test 8 failed: Expected [1, 2, 3], got {arr}"
    print("Test 8 passed: In-place sorting verified")

    # Test Case 9: Verify each element moved correctly
    arr = [3, 2, 5, 6, 1, 4]
    original = arr[:]
    sort_1_to_n(arr)
    for i, val in enumerate(arr):
        assert val == i + 1, (
            f"Test 9 failed: Position {i} should have {i + 1}, got {val}"
        )
        assert val in original, f"Test 9 failed: {val} was not in original array"
    print("Test 9 passed: Elements correctness")

    # Test Case 10: Large array
    import random

    n = 100
    arr = list(range(1, n + 1))
    random.shuffle(arr)
    result = sort_1_to_n(arr)
    assert result == list(range(1, n + 1)), "Test 10 failed: Large array"
    print("Test 10 passed: Large array")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_sort_1_to_n()

    # Example usage
    print("\nExample 1:")
    arr = [3, 2, 5, 6, 1, 4]
    print(f"Input: {arr}")
    sort_1_to_n(arr)
    print(f"Sorted: {arr}")

    print("\nExample 2 (Step by step):")
    arr = [3, 1, 2]
    print(f"Initial: {arr}")
    n = len(arr)
    i = 0
    step = 1
    while i < n:
        correct_idx = arr[i] - 1
        if arr[i] != arr[correct_idx]:
            print(f"Step {step}: arr[{i}]={arr[i]} should be at index {correct_idx}")
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
            print(f"       After swap: {arr}")
            step += 1
        else:
            print(f"Step {step}: arr[{i}]={arr[i]} is at correct position")
            i += 1
            step += 1
    print(f"Final: {arr}")
