"""
Array is Subset of Another Array

Problem: Given two arrays arr1[] and arr2[] of size m and n respectively,
return true if arr2[] is a subset of arr1[].

Example:
    Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}
    Output: true

    Input: arr1[] = {1, 2, 3, 4, 5}, arr2[] = {2, 3, 6}
    Output: false

Approach:
    Use a hash set to store all elements of arr1, then check if all elements
    of arr2 exist in the set.

Time Complexity: O(m + n) where m and n are sizes of the arrays
Space Complexity: O(m) for storing elements in hash set
"""


def is_subset(arr1, arr2):
    """
    Check if arr2 is a subset of arr1.

    Args:
        arr1: First array (main array)
        arr2: Second array (potential subset)

    Returns:
        bool: True if arr2 is subset of arr1, False otherwise
    """
    if not arr2:
        return True

    if not arr1:
        return False

    # Create a set from arr1 for O(1) lookups
    elements = set(arr1)

    # Check if all elements of arr2 are in the set
    for num in arr2:
        if num not in elements:
            return False

    return True


def is_subset_counter(arr1, arr2):
    """
    Alternative approach using Counter to handle duplicates.
    More robust version that considers element frequencies.

    Args:
        arr1: First array (main array)
        arr2: Second array (potential subset)

    Returns:
        bool: True if arr2 is subset of arr1 considering frequencies
    """
    from collections import Counter

    count1 = Counter(arr1)
    count2 = Counter(arr2)

    for element, count in count2.items():
        if count1[element] < count:
            return False

    return True


if __name__ == "__main__":
    # Test Case 1: Basic subset
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]
    print(f"Test 1: {is_subset(arr1, arr2)}")  # Expected: True

    # Test Case 2: Not a subset
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 3, 6]
    print(f"Test 2: {is_subset(arr1, arr2)}")  # Expected: False

    # Test Case 3: Empty subset
    arr1 = [1, 2, 3]
    arr2 = []
    print(f"Test 3: {is_subset(arr1, arr2)}")  # Expected: True

    # Test Case 4: Both empty
    arr1 = []
    arr2 = []
    print(f"Test 4: {is_subset(arr1, arr2)}")  # Expected: True

    # Test Case 5: With duplicates (using Counter version)
    arr1 = [1, 2, 2, 3, 3, 3]
    arr2 = [2, 2, 3]
    print(f"Test 5: {is_subset_counter(arr1, arr2)}")  # Expected: True

    # Test Case 6: Insufficient duplicates
    arr1 = [1, 2, 3, 3]
    arr2 = [2, 2, 3]
    print(f"Test 6: {is_subset_counter(arr1, arr2)}")  # Expected: False
