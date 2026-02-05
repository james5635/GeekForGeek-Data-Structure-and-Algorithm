"""
Check if Two Sets are Disjoint

Problem: Given two sets represented by two arrays, check if the two sets are
disjoint (no common elements between them).

Example:
    Input: arr1[] = {12, 34, 11, 9, 3}, arr2[] = {2, 1, 3, 5}
    Output: false (3 is common)

    Input: arr1[] = {12, 34, 11, 9, 3}, arr2[] = {7, 2, 1, 5}
    Output: true (no common elements)

Approach:
    Store all elements of first array in a hash set, then check if any element
    of second array exists in the set.

Time Complexity: O(m + n) where m and n are sizes of the arrays
Space Complexity: O(m) for storing elements in hash set
"""


def are_disjoint(arr1, arr2):
    """
    Check if two arrays represent disjoint sets.

    Args:
        arr1: First array
        arr2: Second array

    Returns:
        bool: True if sets are disjoint (no common elements), False otherwise
    """
    # Create a set from first array
    elements = set(arr1)

    # Check if any element of second array exists in the set
    for num in arr2:
        if num in elements:
            return False

    return True


def are_disjoint_optimized(arr1, arr2):
    """
    Memory-optimized version that uses the smaller array for the set.

    Args:
        arr1: First array
        arr2: Second array

    Returns:
        bool: True if sets are disjoint, False otherwise
    """
    # Use the smaller array to create the set for space optimization
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    elements = set(arr1)

    for num in arr2:
        if num in elements:
            return False

    return True


if __name__ == "__main__":
    # Test Case 1: Sets with common element
    arr1 = [12, 34, 11, 9, 3]
    arr2 = [2, 1, 3, 5]
    print(f"Test 1: {are_disjoint(arr1, arr2)}")  # Expected: False

    # Test Case 2: Disjoint sets
    arr1 = [12, 34, 11, 9, 3]
    arr2 = [7, 2, 1, 5]
    print(f"Test 2: {are_disjoint(arr1, arr2)}")  # Expected: True

    # Test Case 3: One empty set
    arr1 = [1, 2, 3]
    arr2 = []
    print(f"Test 3: {are_disjoint(arr1, arr2)}")  # Expected: True

    # Test Case 4: Both empty sets
    arr1 = []
    arr2 = []
    print(f"Test 4: {are_disjoint(arr1, arr2)}")  # Expected: True

    # Test Case 5: Identical sets
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3]
    print(f"Test 5: {are_disjoint(arr1, arr2)}")  # Expected: False

    # Test Case 6: Multiple common elements
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    print(f"Test 6: {are_disjoint(arr1, arr2)}")  # Expected: False

    # Test Case 7: Large array optimization test
    arr1 = list(range(1000))
    arr2 = list(range(1000, 2000))
    print(f"Test 7: {are_disjoint_optimized(arr1, arr2)}")  # Expected: True
