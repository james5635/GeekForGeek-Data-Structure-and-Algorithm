"""
Search in a Sorted Infinite Array

Problem:
Given a sorted infinite array (or an array of unknown size),
search for an element x in the array.

Since the array is infinite, we cannot use array.length or len(arr).
We assume we have a function get(index) that returns the element at
that index or infinity/exception if index is out of bounds.

Example:
    Array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, ...] (infinite)
    Key: 10
    Output: 9 (index of 10)

Time Complexity: O(log p) where p is the position of the key
Space Complexity: O(1) - iterative approach
"""

from typing import Callable


def search_infinite_array(get: Callable[[int], int], key: int) -> int:
    """
    Search for a key in a sorted infinite array.

    First, find the range where the key could be by exponentially
    increasing the search range, then do binary search.

    Args:
        get: Function that returns element at given index
        key: Element to search for

    Returns:
        Index of the key if found, -1 otherwise
    """
    # First, find the range where key could be
    low, high = 0, 1

    # Exponentially increase high until we find a value >= key
    # or we hit a very large number (simulating infinity)
    while get(high) < key and get(high) != float("inf"):
        low = high
        high = high * 2

    # Binary search in the found range
    return binary_search_infinite(get, low, high, key)


def binary_search_infinite(
    get: Callable[[int], int], low: int, high: int, key: int
) -> int:
    """Binary search on infinite array using get function."""
    while low <= high:
        mid = low + (high - low) // 2
        mid_val = get(mid)

        if mid_val == float("inf") or mid_val > key:
            high = mid - 1
        elif mid_val < key:
            low = mid + 1
        else:
            return mid

    return -1


# Simulated infinite array for testing
class InfiniteArray:
    """Simulates an infinite sorted array for testing."""

    def __init__(self, data: list[int]):
        self.data = data

    def get(self, index: int) -> int:
        """Return element at index or infinity if out of bounds."""
        if index < len(self.data):
            return self.data[index]
        return float("inf")


if __name__ == "__main__":
    # Test Case 1: Standard case
    arr1 = list(range(1, 1001))  # [1, 2, 3, ..., 1000]
    inf_arr1 = InfiniteArray(arr1)
    key1 = 500
    result = search_infinite_array(inf_arr1.get, key1)
    print(f"Test 1: key={key1}")
    print(f"Result: Index {result}")  # Expected: 499
    assert result == 499, "Test 1 failed"

    # Test Case 2: Key at beginning
    arr2 = list(range(1, 1001))
    inf_arr2 = InfiniteArray(arr2)
    key2 = 1
    result = search_infinite_array(inf_arr2.get, key2)
    print(f"\nTest 2: key={key2}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 2 failed"

    # Test Case 3: Key not in array
    arr3 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    inf_arr3 = InfiniteArray(arr3)
    key3 = 5
    result = search_infinite_array(inf_arr3.get, key3)
    print(f"\nTest 3: key={key3}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 3 failed"

    # Test Case 4: Key at position requiring exponential search
    arr4 = list(range(1, 10001))
    inf_arr4 = InfiniteArray(arr4)
    key4 = 7890
    result = search_infinite_array(inf_arr4.get, key4)
    print(f"\nTest 4: key={key4}")
    print(f"Result: Index {result}")  # Expected: 7889
    assert result == 7889, "Test 4 failed"

    # Test Case 5: Small array
    arr5 = [10, 20, 30]
    inf_arr5 = InfiniteArray(arr5)
    key5 = 20
    result = search_infinite_array(inf_arr5.get, key5)
    print(f"\nTest 5: key={key5}")
    print(f"Result: Index {result}")  # Expected: 1
    assert result == 1, "Test 5 failed"

    # Test Case 6: Duplicate elements
    arr6 = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
    inf_arr6 = InfiniteArray(arr6)
    key6 = 2
    result = search_infinite_array(inf_arr6.get, key6)
    print(f"\nTest 6: key={key6}")
    print(f"Result: Index {result}")  # Expected: any index with value 2
    assert result in [1, 2, 3], "Test 6 failed"

    print("\nAll tests passed!")
