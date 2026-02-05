"""
Find Missing Elements in Range

Problem: Given an array of distinct elements and a range [low, high], find all
missing elements in the range that are not present in the array.

Approach: Use a hash set for O(1) lookup. Iterate through the range and check
which elements are missing from the set.

Time Complexity: O(n + (high-low+1)) where n is array size
Space Complexity: O(n) - hash set stores array elements
"""


def find_missing_elements(arr, low, high):
    """
    Find missing elements in range [low, high].

    Args:
        arr: List of distinct integers
        low: Lower bound of range
        high: Upper bound of range

    Returns:
        List of missing elements in sorted order
    """
    element_set = set(arr)
    missing = []

    for num in range(low, high + 1):
        if num not in element_set:
            missing.append(num)

    return missing


def find_missing_elements_optimized(arr, low, high):
    """
    Optimized version that modifies input array (O(1) extra space).

    Args:
        arr: List of distinct integers
        low: Lower bound of range
        high: Upper bound of range

    Returns:
        List of missing elements
    """
    # Mark elements in range by making them negative
    for i in range(len(arr)):
        if low <= arr[i] <= high:
            idx = abs(arr[i]) - low
            if 0 <= idx < len(arr):
                arr[idx] = -abs(arr[idx])

    missing = []
    for i in range(high - low + 1):
        if i < len(arr) and arr[i] > 0:
            missing.append(low + i)

    return missing


if __name__ == "__main__":
    # Test Case 1: Basic range
    arr1 = [10, 12, 11, 15]
    low1, high1 = 10, 15
    print(f"Array: {arr1}, Range: [{low1}, {high1}]")
    print(f"Missing elements: {find_missing_elements(arr1, low1, high1)}")
    print()

    # Test Case 2: All elements present
    arr2 = [1, 2, 3, 4, 5]
    low2, high2 = 1, 5
    print(f"Array: {arr2}, Range: [{low2}, {high2}]")
    print(f"Missing elements: {find_missing_elements(arr2, low2, high2)}")
    print()

    # Test Case 3: No elements present
    arr3 = [10, 20, 30]
    low3, high3 = 1, 5
    print(f"Array: {arr3}, Range: [{low3}, {high3}]")
    print(f"Missing elements: {find_missing_elements(arr3, low3, high3)}")
    print()

    # Test Case 4: Negative range
    arr4 = [-2, -1, 1, 2]
    low4, high4 = -3, 3
    print(f"Array: {arr4}, Range: [{low4}, {high4}]")
    print(f"Missing elements: {find_missing_elements(arr4, low4, high4)}")
    print()

    # Test Case 5: Empty array
    arr5 = []
    low5, high5 = 1, 5
    print(f"Array: {arr5}, Range: [{low5}, {high5}]")
    print(f"Missing elements: {find_missing_elements(arr5, low5, high5)}")
    print()

    # Test Case 6: Single element range
    arr6 = [5, 6, 7]
    low6, high6 = 5, 5
    print(f"Array: {arr6}, Range: [{low6}, {high6}]")
    print(f"Missing elements: {find_missing_elements(arr6, low6, high6)}")
