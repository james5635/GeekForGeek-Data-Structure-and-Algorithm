"""
Sort N Numbers in Range 0 to N²-1 in Linear Time

Given an array of n numbers where elements are in range from 0 to n²-1,
sort the array in linear time.

Algorithm:
1. Use Radix Sort with base n
2. Each number in range [0, n²-1] can be represented using 2 digits in base n
3. Perform counting sort on least significant digit (exp=1)
4. Perform counting sort on most significant digit (exp=n)

Time Complexity: O(n) - Two passes of counting sort, each O(n)
Space Complexity: O(n) - Output array and count array
"""


def count_sort_radix(arr, n, exp):
    """
    Perform counting sort on the digit represented by exp.

    Args:
        arr: Input array
        n: Size of array (also the base)
        exp: Exponent representing current digit position
    """
    output = [0] * n
    count = [0] * n

    # Count occurrences
    for i in range(n):
        index = (arr[i] // exp) % n
        count[index] += 1

    # Change count[i] to contain actual position
    for i in range(1, n):
        count[i] += count[i - 1]

    # Build output array (stable sort)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % n
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy back to original array
    for i in range(n):
        arr[i] = output[i]


def sort_range_0_to_n2(arr):
    """
    Sort array with elements in range [0, n²-1] in O(n) time.

    Args:
        arr: List of integers in range [0, n²-1]

    Returns:
        list: Sorted array
    """
    if not arr:
        return []

    n = len(arr)

    # If n is 0 or 1, array is already sorted
    if n <= 1:
        return arr[:]

    # Create a copy to avoid modifying input
    result = arr[:]

    # Do counting sort for first digit (n^0 = 1)
    count_sort_radix(result, n, 1)

    # Do counting sort for second digit (n^1 = n)
    count_sort_radix(result, n, n)

    return result


def sort_range_0_to_n2_general(arr, power):
    """
    General version for range [0, n^power - 1].

    Args:
        arr: List of integers
        power: The power p where elements are in range [0, n^p - 1]

    Returns:
        list: Sorted array
    """
    if not arr:
        return []

    n = len(arr)

    if n <= 1:
        return arr[:]

    result = arr[:]

    # Perform counting sort for each digit position
    exp = 1
    for _ in range(power):
        count_sort_radix(result, n, exp)
        exp *= n

    return result


def test_sort_range_0_to_n2():
    """Test cases for sorting array with range 0 to n²-1."""
    # Test Case 1: Basic case
    arr = [0, 23, 14, 12, 9]  # n=5, range 0-24
    result = sort_range_0_to_n2(arr)
    expected = [0, 9, 12, 14, 23]
    assert result == expected, f"Test 1 failed: Expected {expected}, got {result}"
    print("Test 1 passed: Basic case")

    # Test Case 2: Small array
    arr = [7, 0, 2]  # n=3, range 0-8
    result = sort_range_0_to_n2(arr)
    expected = [0, 2, 7]
    assert result == expected, f"Test 2 failed: Expected {expected}, got {result}"
    print("Test 2 passed: Small array")

    # Test Case 3: From GeeksforGeeks example
    arr = [40, 12, 45, 32, 33, 1, 22]  # n=7, range 0-48
    result = sort_range_0_to_n2(arr)
    expected = [1, 12, 22, 32, 33, 40, 45]
    assert result == expected, f"Test 3 failed: Expected {expected}, got {result}"
    print("Test 3 passed: GFG example")

    # Test Case 4: Already sorted
    arr = [0, 1, 2, 3, 4]
    result = sort_range_0_to_n2(arr)
    expected = [0, 1, 2, 3, 4]
    assert result == expected, f"Test 4 failed: Expected {expected}, got {result}"
    print("Test 4 passed: Already sorted")

    # Test Case 5: Reverse sorted
    arr = [24, 20, 15, 10, 5]  # n=5, all valid in range 0-24
    result = sort_range_0_to_n2(arr)
    expected = [5, 10, 15, 20, 24]
    assert result == expected, f"Test 5 failed: Expected {expected}, got {result}"
    print("Test 5 passed: Reverse sorted")

    # Test Case 6: Single element
    arr = [5]
    result = sort_range_0_to_n2(arr)
    expected = [5]
    assert result == expected, f"Test 6 failed: Expected {expected}, got {result}"
    print("Test 6 passed: Single element")

    # Test Case 7: Empty array
    arr = []
    result = sort_range_0_to_n2(arr)
    expected = []
    assert result == expected, f"Test 7 failed: Expected {expected}, got {result}"
    print("Test 7 passed: Empty array")

    # Test Case 8: Array with duplicates
    arr = [8, 8, 4, 4, 0]  # n=5, range 0-24
    result = sort_range_0_to_n2(arr)
    expected = [0, 4, 4, 8, 8]
    assert result == expected, f"Test 8 failed: Expected {expected}, got {result}"
    print("Test 8 passed: Array with duplicates")

    # Test Case 9: General version for n³-1 range
    arr = [0, 15, 7, 26, 8]  # n=5, testing with values up to 26 (n³-1 = 124)
    result = sort_range_0_to_n2_general(arr, 3)
    expected = [0, 7, 8, 15, 26]
    assert result == expected, f"Test 9 failed: Expected {expected}, got {result}"
    print("Test 9 passed: General version for n³ range")

    # Test Case 10: Verify all elements are within valid range
    import random

    n = 10
    arr = [random.randint(0, n * n - 1) for _ in range(n)]
    result = sort_range_0_to_n2(arr)
    assert result == sorted(arr), "Test 10 failed: Result doesn't match Python's sort"
    print("Test 10 passed: Random test verification")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_sort_range_0_to_n2()

    # Example usage
    print("\nExample 1:")
    arr = [40, 12, 45, 32, 33, 1, 22]
    print(f"Input: {arr}")
    print(f"n = {len(arr)}, valid range: 0 to {len(arr) ** 2 - 1}")
    result = sort_range_0_to_n2(arr)
    print(f"Sorted: {result}")

    print("\nExample 2:")
    arr = [0, 23, 14, 12, 9]
    print(f"Input: {arr}")
    result = sort_range_0_to_n2(arr)
    print(f"Sorted: {result}")
