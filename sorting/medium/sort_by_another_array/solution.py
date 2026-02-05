"""
Sort Array According to Order Defined by Another Array

Given two arrays a1[] and a2[], sort a1[] such that elements appear in the order
defined by a2[]. Elements in a1[] that are not in a2[] should be placed at the
end in ascending order.

Algorithm:
1. Count frequency of each element in a1 using a hash map
2. Place elements from a2 in a1 based on their frequency
3. Collect remaining elements, sort them, and append

Time Complexity: O(m log m + n) where m = len(a1), n = len(a2)
Space Complexity: O(m) for the frequency map
"""

from collections import Counter


def sort_by_another_array(a1, a2):
    """
    Sort a1 according to order defined by a2.

    Args:
        a1: List of integers to be sorted
        a2: List defining the relative order

    Returns:
        list: Sorted array according to a2's order
    """
    if not a1:
        return []

    # Count frequency of elements in a1
    freq = Counter(a1)

    result = []

    # Place elements in order of a2
    for elem in a2:
        if elem in freq:
            result.extend([elem] * freq[elem])
            del freq[elem]

    # Collect remaining elements and sort them
    remaining = []
    for elem, count in freq.items():
        remaining.extend([elem] * count)
    remaining.sort()

    # Append remaining elements
    result.extend(remaining)

    return result


def sort_by_another_array_inplace(a1, a2):
    """
    In-place version that modifies a1 directly.

    Args:
        a1: List of integers to be sorted (modified in-place)
        a2: List defining the relative order
    """
    if not a1:
        return

    # Count frequency
    freq = {}
    for elem in a1:
        freq[elem] = freq.get(elem, 0) + 1

    index = 0

    # Place elements from a2 first
    for elem in a2:
        while freq.get(elem, 0) > 0:
            a1[index] = elem
            index += 1
            freq[elem] -= 1
        freq.pop(elem, None)

    # Collect remaining elements
    remaining = []
    for elem, count in freq.items():
        remaining.extend([elem] * count)
    remaining.sort()

    # Place remaining elements
    for elem in remaining:
        a1[index] = elem
        index += 1


def sort_by_another_array_custom_key(a1, a2):
    """
    Alternative implementation using custom sort key.

    Args:
        a1: List of integers to be sorted
        a2: List defining the relative order

    Returns:
        list: Sorted array according to a2's order
    """
    if not a1:
        return []

    # Create order map from a2
    order_map = {elem: i for i, elem in enumerate(a2)}

    # Sort a1 using custom key
    # Elements in a2 get priority based on their index
    # Elements not in a2 get infinity as priority and are sorted by value
    return sorted(a1, key=lambda x: (order_map.get(x, float("inf")), x))


def test_sort_by_another_array():
    """Test cases for sort by another array algorithm."""
    # Test Case 1: Basic case from problem
    a1 = [2, 1, 2, 3, 4]
    a2 = [2, 1, 2]
    result = sort_by_another_array(a1, a2)
    expected = [2, 2, 1, 3, 4]
    assert result == expected, f"Test 1 failed: Expected {expected}, got {result}"
    print("Test 1 passed: Basic case")

    # Test Case 2: Another example
    a1 = [4, 1, 3, 3, 2]
    a2 = [3, 1]
    result = sort_by_another_array(a1, a2)
    expected = [3, 3, 1, 2, 4]
    assert result == expected, f"Test 2 failed: Expected {expected}, got {result}"
    print("Test 2 passed: Another example")

    # Test Case 3: All elements in a2
    a1 = [3, 1, 2, 3, 1, 2]
    a2 = [1, 2, 3]
    result = sort_by_another_array(a1, a2)
    expected = [1, 1, 2, 2, 3, 3]
    assert result == expected, f"Test 3 failed: Expected {expected}, got {result}"
    print("Test 3 passed: All elements in a2")

    # Test Case 4: No elements from a2
    a1 = [5, 6, 7, 8]
    a2 = [1, 2, 3]
    result = sort_by_another_array(a1, a2)
    expected = [5, 6, 7, 8]
    assert result == expected, f"Test 4 failed: Expected {expected}, got {result}"
    print("Test 4 passed: No elements from a2")

    # Test Case 5: Empty a1
    a1 = []
    a2 = [1, 2, 3]
    result = sort_by_another_array(a1, a2)
    expected = []
    assert result == expected, f"Test 5 failed: Expected {expected}, got {result}"
    print("Test 5 passed: Empty a1")

    # Test Case 6: Single element
    a1 = [5]
    a2 = [5]
    result = sort_by_another_array(a1, a2)
    expected = [5]
    assert result == expected, f"Test 6 failed: Expected {expected}, got {result}"
    print("Test 6 passed: Single element")

    # Test Case 7: Duplicates
    a1 = [1, 1, 1, 2, 2, 3]
    a2 = [2, 1]
    result = sort_by_another_array(a1, a2)
    expected = [2, 2, 1, 1, 1, 3]
    assert result == expected, f"Test 7 failed: Expected {expected}, got {result}"
    print("Test 7 passed: Duplicates")

    # Test Case 8: In-place version
    a1 = [2, 1, 2, 3, 4]
    a2 = [2, 1, 2]
    sort_by_another_array_inplace(a1, a2)
    expected = [2, 2, 1, 3, 4]
    assert a1 == expected, f"Test 8 failed: Expected {expected}, got {a1}"
    print("Test 8 passed: In-place version")

    # Test Case 9: Custom key version
    a1 = [4, 1, 3, 3, 2]
    a2 = [3, 1]
    result = sort_by_another_array_custom_key(a1, a2)
    expected = [3, 3, 1, 2, 4]
    assert result == expected, f"Test 9 failed: Expected {expected}, got {result}"
    print("Test 9 passed: Custom key version")

    # Test Case 10: Large array
    a1 = list(range(100, 0, -1)) * 2
    a2 = list(range(1, 51))
    result = sort_by_another_array(a1, a2)
    # Verify all elements from a2 come first in order
    pos = 0
    for elem in a2:
        count = result[pos : pos + 2].count(elem)
        assert count == 2, f"Test 10 failed: Expected 2 occurrences of {elem}"
        pos += 2
    # Verify remaining elements are sorted
    remaining = result[pos:]
    assert remaining == sorted(remaining), (
        "Test 10 failed: Remaining elements not sorted"
    )
    print("Test 10 passed: Large array")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_sort_by_another_array()

    # Example usage
    print("\nExample 1:")
    a1 = [2, 1, 2, 3, 4]
    a2 = [2, 1, 2]
    result = sort_by_another_array(a1, a2)
    print(f"a1 = {a1}")
    print(f"a2 = {a2}")
    print(f"Result: {result}")

    print("\nExample 2:")
    a1 = [4, 1, 3, 3, 2]
    a2 = [3, 1]
    result = sort_by_another_array(a1, a2)
    print(f"a1 = {a1}")
    print(f"a2 = {a2}")
    print(f"Result: {result}")
