"""
Jump Search

Problem:
Find the position of an element x in a sorted array using Jump Search.

Jump Search is a searching algorithm for sorted arrays. It works by
jumping ahead by fixed steps (block size) and then performing linear
search within the identified block.

The optimal block size is √n where n is the array length.

Example:
    Input: arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], key = 55
    Output: 10 (index of 55)

    Input: arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], key = 100
    Output: -1 (not found)

Time Complexity: O(√n) - optimal block size is √n
Space Complexity: O(1) - iterative approach
"""

import math


def jump_search(arr: list[int], key: int) -> int:
    """
    Search for a key using jump search algorithm.

    Jumps ahead by √n steps to find the block where key could be,
    then performs linear search within that block.

    Args:
        arr: Sorted array to search in
        key: Element to search for

    Returns:
        Index of the key if found, -1 otherwise
    """
    if not arr:
        return -1

    n = len(arr)

    # Optimal block size is √n
    step = int(math.sqrt(n))

    # Find the block where key could be
    prev = 0

    # Jump ahead in blocks
    while prev < n and arr[min(step, n) - 1] < key:
        prev = step
        step += int(math.sqrt(n))

        # If we've gone past the array, key not present
        if prev >= n:
            return -1

    # Linear search within the identified block
    while prev < n and prev < step and arr[prev] < key:
        prev += 1

    # Check if we found the key
    if prev < n and arr[prev] == key:
        return prev

    return -1


# Alternative implementation with clearer variable names
def jump_search_v2(arr: list[int], key: int) -> int:
    """
    Alternative jump search with cleaner implementation.

    Time Complexity: O(√n)
    Space Complexity: O(1)
    """
    if not arr:
        return -1

    n = len(arr)
    block_size = int(math.sqrt(n))

    # Finding the block where element could be present
    left = 0
    right = block_size

    # Jump through blocks
    while right < n and arr[right - 1] < key:
        left = right
        right += block_size

        # If right exceeds array length, set to n
        if right > n:
            right = n

    # Linear search in the current block
    for i in range(left, right):
        if arr[i] == key:
            return i

    return -1


if __name__ == "__main__":
    # Test Case 1: Standard case (Fibonacci sequence)
    arr1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    key1 = 55
    result = jump_search(arr1, key1)
    print(f"Test 1: arr={arr1}, key={key1}")
    print(f"Result: Index {result}")  # Expected: 10
    assert result == 10, "Test 1 failed"

    # Test Case 2: Key not found
    arr2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    key2 = 100
    result = jump_search(arr2, key2)
    print(f"\nTest 2: arr={arr2}, key={key2}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 2 failed"

    # Test Case 3: First element
    arr3 = [10, 20, 30, 40, 50, 60, 70]
    key3 = 10
    result = jump_search(arr3, key3)
    print(f"\nTest 3: arr={arr3}, key={key3}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 3 failed"

    # Test Case 4: Last element
    arr4 = [10, 20, 30, 40, 50, 60, 70]
    key4 = 70
    result = jump_search(arr4, key4)
    print(f"\nTest 4: arr={arr4}, key={key4}")
    print(f"Result: Index {result}")  # Expected: 6
    assert result == 6, "Test 4 failed"

    # Test Case 5: Single element
    arr5 = [42]
    key5 = 42
    result = jump_search(arr5, key5)
    print(f"\nTest 5: arr={arr5}, key={key5}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 5 failed"

    # Test Case 6: Small array (2 elements)
    arr6 = [5, 10]
    key6 = 5
    result = jump_search(arr6, key6)
    print(f"\nTest 6: arr={arr6}, key={key6}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 6 failed"

    # Test Case 7: Large array
    arr7 = list(range(0, 1000, 5))  # [0, 5, 10, ..., 995]
    key7 = 555
    result = jump_search(arr7, key7)
    print(f"\nTest 7: arr size={len(arr7)}, key={key7}")
    print(f"Result: Index {result}")  # Expected: 111
    assert result == 111, "Test 7 failed"

    # Test Case 8: Compare v2
    arr8 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    key8 = 14
    result1 = jump_search(arr8, key8)
    result2 = jump_search_v2(arr8, key8)
    print(f"\nTest 8: arr={arr8}, key={key8}")
    print(f"V1 Result: Index {result1}")
    print(f"V2 Result: Index {result2}")
    assert result1 == result2 == 6, "Test 8 failed"

    # Test Case 9: Empty array
    arr9 = []
    key9 = 10
    result = jump_search(arr9, key9)
    print(f"\nTest 9: arr={arr9}, key={key9}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 9 failed"

    print("\nAll tests passed!")
