"""
Meta Binary Search (One-Sided Binary Search)

Problem:
Find the position of an element x in a sorted array using Meta Binary Search.

Meta Binary Search is also known as One-Sided Binary Search. Instead of
comparing the middle element, it compares the bits of the target position.
It builds the position of the target bit by bit, starting from the most
significant bit.

This is useful when comparing elements is expensive but computing indices is cheap.

Example:
    Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], key = 6
    Output: 5 (index of 6)

    Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], key = 10
    Output: -1 (not found)

Time Complexity: O(log n) - number of bits needed to represent n
Space Complexity: O(1) - iterative approach
"""

import math


def meta_binary_search(arr: list[int], key: int) -> int:
    """
    Search for a key using meta binary search (one-sided binary search).

    This algorithm builds the position bit by bit from most significant
    to least significant bit, avoiding mid calculations.

    Args:
        arr: Sorted array to search in
        key: Element to search for

    Returns:
        Index of the key if found, -1 otherwise
    """
    if not arr:
        return -1

    n = len(arr)

    # Find the position of the most significant bit
    # This gives us the number of bits needed to represent n
    lg = int(math.log2(n - 1)) + 1 if n > 1 else 1

    pos = 0

    # Check each bit from most significant to least
    for i in range(lg, -1, -1):
        # If setting this bit doesn't exceed array bounds
        if pos + (1 << i) < n and arr[pos + (1 << i)] <= key:
            pos += 1 << i

    # Check if we found the key
    if arr[pos] == key:
        return pos

    return -1


# Alternative implementation using bit manipulation differently
def meta_binary_search_v2(arr: list[int], key: int) -> int:
    """
    Alternative meta binary search implementation.

    Uses bit masking approach to find the position.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if not arr:
        return -1

    n = len(arr)

    # Find number of bits in n
    num_bits = n.bit_length()

    # Start with all bits set (upper bound)
    # and clear bits from MSB to LSB
    idx = 0

    for i in range(num_bits - 1, -1, -1):
        # Try setting the i-th bit
        step = 1 << i
        new_idx = idx | step

        if new_idx < n and arr[new_idx] <= key:
            idx = new_idx

    if idx < n and arr[idx] == key:
        return idx

    return -1


if __name__ == "__main__":
    # Test Case 1: Standard case
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    key1 = 6
    result = meta_binary_search(arr1, key1)
    print(f"Test 1: arr={arr1}, key={key1}")
    print(f"Result: Index {result}")  # Expected: 5
    assert result == 5, "Test 1 failed"

    # Test Case 2: Key not found
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    key2 = 10
    result = meta_binary_search(arr2, key2)
    print(f"\nTest 2: arr={arr2}, key={key2}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 2 failed"

    # Test Case 3: Single element found
    arr3 = [5]
    key3 = 5
    result = meta_binary_search(arr3, key3)
    print(f"\nTest 3: arr={arr3}, key={key3}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 3 failed"

    # Test Case 4: Single element not found
    arr4 = [5]
    key4 = 3
    result = meta_binary_search(arr4, key4)
    print(f"\nTest 4: arr={arr4}, key={key4}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 4 failed"

    # Test Case 5: First element
    arr5 = [10, 20, 30, 40, 50]
    key5 = 10
    result = meta_binary_search(arr5, key5)
    print(f"\nTest 5: arr={arr5}, key={key5}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 5 failed"

    # Test Case 6: Last element
    arr6 = [10, 20, 30, 40, 50]
    key6 = 50
    result = meta_binary_search(arr6, key6)
    print(f"\nTest 6: arr={arr6}, key={key6}")
    print(f"Result: Index {result}")  # Expected: 4
    assert result == 4, "Test 6 failed"

    # Test Case 7: Large array (power of 2)
    arr7 = list(range(1, 65))  # 64 elements
    key7 = 42
    result = meta_binary_search(arr7, key7)
    print(f"\nTest 7: arr size={len(arr7)}, key={key7}")
    print(f"Result: Index {result}")  # Expected: 41
    assert result == 41, "Test 7 failed"

    # Test Case 8: Compare with v2
    arr8 = [1, 3, 5, 7, 9, 11, 13, 15]
    key8 = 11
    result1 = meta_binary_search(arr8, key8)
    result2 = meta_binary_search_v2(arr8, key8)
    print(f"\nTest 8: arr={arr8}, key={key8}")
    print(f"Result v1: Index {result1}")
    print(f"Result v2: Index {result2}")
    assert result1 == result2 == 5, "Test 8 failed"

    print("\nAll tests passed!")
