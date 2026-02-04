"""
Minimum Increment by K Operations to Make All Elements Equal

Given an array of n-elements, find the number of operations needed to make
all elements of array equal. A single operation can increment an element by k.
If it is not possible to make all elements equal, return -1.

Approach:
- Find the maximum element (target value)
- For each element, check if (max - element) is divisible by k
- If not divisible, return -1 (impossible)
- Otherwise, sum up all (max - element) / k operations

Time Complexity: O(n)
Space Complexity: O(1)
"""


def min_ops(arr, k):
    """
    Calculate minimum operations to make all elements equal by incrementing k.

    Args:
        arr: List of integers
        k: Integer increment value

    Returns:
        int: Minimum operations needed, or -1 if impossible
    """
    if not arr or k == 0:
        return -1

    # Find maximum element
    max_val = max(arr)
    res = 0

    # Iterate through all elements
    for x in arr:
        # Check if element can be made equal to max
        # If not, return -1
        if (max_val - x) % k != 0:
            return -1

        # Add required operations
        res += (max_val - x) // k

    return res


def test_min_ops():
    """Test the min_ops function with various test cases."""

    # Test Case 1: Example from problem
    arr1 = [4, 7, 19, 16]
    k1 = 3
    result1 = min_ops(arr1, k1)
    expected1 = 10
    print(f"Test 1: arr={arr1}, k={k1}")
    print(f"Result: {result1}, Expected: {expected1}")
    assert result1 == expected1, f"Test 1 failed!"
    print("✓ Test 1 passed!\n")

    # Test Case 2: All elements already equal
    arr2 = [4, 4, 4, 4]
    k2 = 3
    result2 = min_ops(arr2, k2)
    expected2 = 0
    print(f"Test 2: arr={arr2}, k={k2}")
    print(f"Result: {result2}, Expected: {expected2}")
    assert result2 == expected2, f"Test 2 failed!"
    print("✓ Test 2 passed!\n")

    # Test Case 3: Impossible case
    arr3 = [4, 2, 6, 8]
    k3 = 3
    result3 = min_ops(arr3, k3)
    expected3 = -1
    print(f"Test 3: arr={arr3}, k={k3}")
    print(f"Result: {result3}, Expected: {expected3}")
    assert result3 == expected3, f"Test 3 failed!"
    print("✓ Test 3 passed!\n")

    # Test Case 4: GeeksforGeeks example
    arr4 = [21, 33, 9, 45, 63]
    k4 = 6
    result4 = min_ops(arr4, k4)
    expected4 = 24
    print(f"Test 4: arr={arr4}, k={k4}")
    print(f"Result: {result4}, Expected: {expected4}")
    assert result4 == expected4, f"Test 4 failed!"
    print("✓ Test 4 passed!\n")

    # Test Case 5: Single element
    arr5 = [10]
    k5 = 5
    result5 = min_ops(arr5, k5)
    expected5 = 0
    print(f"Test 5: arr={arr5}, k={k5}")
    print(f"Result: {result5}, Expected: {expected5}")
    assert result5 == expected5, f"Test 5 failed!"
    print("✓ Test 5 passed!\n")

    # Test Case 6: Two elements
    arr6 = [5, 15]
    k6 = 5
    result6 = min_ops(arr6, k6)
    expected6 = 2  # (15-5)/5 = 2
    print(f"Test 6: arr={arr6}, k={k6}")
    print(f"Result: {result6}, Expected: {expected6}")
    assert result6 == expected6, f"Test 6 failed!"
    print("✓ Test 6 passed!\n")

    # Test Case 7: k=1 (always possible)
    arr7 = [1, 5, 9, 3]
    k7 = 1
    result7 = min_ops(arr7, k7)
    expected7 = (9 - 1) + (9 - 5) + (9 - 9) + (9 - 3)  # 8 + 4 + 0 + 6 = 18
    print(f"Test 7: arr={arr7}, k={k7}")
    print(f"Result: {result7}, Expected: {expected7}")
    assert result7 == expected7, f"Test 7 failed!"
    print("✓ Test 7 passed!\n")

    print("=" * 50)
    print("All tests passed successfully! ✓")
    print("=" * 50)


if __name__ == "__main__":
    test_min_ops()
