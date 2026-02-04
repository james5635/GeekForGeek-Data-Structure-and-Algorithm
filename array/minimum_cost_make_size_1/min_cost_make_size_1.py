"""
Minimum Cost to Make Array Size 1 by Removing Larger Pairs

Given an array of n integers, reduce the size of the array to one.
We are allowed to select a pair of integers and remove the larger one.
Cost of operation is equal to the smaller value. Find minimum total cost.

Approach:
- Find the minimum element in the array
- The minimum cost is (n - 1) * min_element
- This is because we need (n-1) operations to reduce array to size 1
- In each operation, pair the minimum with another element

Time Complexity: O(n)
Space Complexity: O(1)
"""


def min_cost(arr):
    """
    Calculate minimum cost to reduce array size to 1.

    Args:
        arr: List of integers

    Returns:
        int: Minimum cost, or -1 if array is empty
    """
    if not arr:
        return -1

    n = len(arr)

    # If array has only one element, no operations needed
    if n == 1:
        return 0

    # Find minimum element
    min_val = min(arr)

    # Minimum cost is (n-1) * min_element
    return (n - 1) * min_val


def min_cost_manual(arr):
    """
    Calculate minimum cost using manual min finding (without built-in min).

    Args:
        arr: List of integers

    Returns:
        int: Minimum cost, or -1 if array is empty
    """
    if not arr:
        return -1

    n = len(arr)

    # If array has only one element, no operations needed
    if n == 1:
        return 0

    # Find minimum element manually
    min_val = arr[0]
    for i in range(1, n):
        if arr[i] < min_val:
            min_val = arr[i]

    # Minimum cost is (n-1) * min_element
    return (n - 1) * min_val


def test_min_cost():
    """Test the min_cost function with various test cases."""

    # Test Case 1: Example from problem
    arr1 = [4, 3, 2]
    result1 = min_cost(arr1)
    expected1 = 4  # (3-1) * 2 = 4
    print(f"Test 1: arr={arr1}")
    print(f"Result: {result1}, Expected: {expected1}")
    assert result1 == expected1, f"Test 1 failed!"
    print("✓ Test 1 passed!\n")

    # Test Case 2: Second example from problem
    arr2 = [3, 4]
    result2 = min_cost(arr2)
    expected2 = 3  # (2-1) * 3 = 3
    print(f"Test 2: arr={arr2}")
    print(f"Result: {result2}, Expected: {expected2}")
    assert result2 == expected2, f"Test 2 failed!"
    print("✓ Test 2 passed!\n")

    # Test Case 3: Single element
    arr3 = [5]
    result3 = min_cost(arr3)
    expected3 = 0  # No operations needed
    print(f"Test 3: arr={arr3}")
    print(f"Result: {result3}, Expected: {expected3}")
    assert result3 == expected3, f"Test 3 failed!"
    print("✓ Test 3 passed!\n")

    # Test Case 4: All same elements
    arr4 = [5, 5, 5, 5]
    result4 = min_cost(arr4)
    expected4 = 15  # (4-1) * 5 = 15
    print(f"Test 4: arr={arr4}")
    print(f"Result: {result4}, Expected: {expected4}")
    assert result4 == expected4, f"Test 4 failed!"
    print("✓ Test 4 passed!\n")

    # Test Case 5: Two elements, min first
    arr5 = [2, 10]
    result5 = min_cost(arr5)
    expected5 = 2  # (2-1) * 2 = 2
    print(f"Test 5: arr={arr5}")
    print(f"Result: {result5}, Expected: {expected5}")
    assert result5 == expected5, f"Test 5 failed!"
    print("✓ Test 5 passed!\n")

    # Test Case 6: Two elements, min second
    arr6 = [10, 2]
    result6 = min_cost(arr6)
    expected6 = 2  # (2-1) * 2 = 2
    print(f"Test 6: arr={arr6}")
    print(f"Result: {result6}, Expected: {expected6}")
    assert result6 == expected6, f"Test 6 failed!"
    print("✓ Test 6 passed!\n")

    # Test Case 7: Larger array
    arr7 = [1, 100, 50, 200, 75]
    result7 = min_cost(arr7)
    expected7 = 4  # (5-1) * 1 = 4
    print(f"Test 7: arr={arr7}")
    print(f"Result: {result7}, Expected: {expected7}")
    assert result7 == expected7, f"Test 7 failed!"
    print("✓ Test 7 passed!\n")

    # Test Case 8: Negative numbers
    arr8 = [-5, -2, -10, -3]
    result8 = min_cost(arr8)
    expected8 = -30  # (4-1) * (-10) = -30
    print(f"Test 8: arr={arr8}")
    print(f"Result: {result8}, Expected: {expected8}")
    assert result8 == expected8, f"Test 8 failed!"
    print("✓ Test 8 passed!\n")

    # Test Case 9: Mixed positive and negative
    arr9 = [-5, 3, 10, -2, 8]
    result9 = min_cost(arr9)
    expected9 = -20  # (5-1) * (-5) = -20
    print(f"Test 9: arr={arr9}")
    print(f"Result: {result9}, Expected: {expected9}")
    assert result9 == expected9, f"Test 9 failed!"
    print("✓ Test 9 passed!\n")

    # Test Case 10: Empty array
    arr10 = []
    result10 = min_cost(arr10)
    expected10 = -1
    print(f"Test 10: arr={arr10}")
    print(f"Result: {result10}, Expected: {expected10}")
    assert result10 == expected10, f"Test 10 failed!"
    print("✓ Test 10 passed!\n")

    # Test manual implementation
    print("Testing manual min finding implementation...")
    for i, arr in enumerate([[4, 3, 2], [3, 4], [5], [1, 100, 50]], 1):
        assert min_cost(arr) == min_cost_manual(arr), f"Manual test {i} failed!"
    print("✓ Manual implementation tests passed!\n")

    print("=" * 50)
    print("All tests passed successfully! ✓")
    print("=" * 50)


if __name__ == "__main__":
    test_min_cost()
