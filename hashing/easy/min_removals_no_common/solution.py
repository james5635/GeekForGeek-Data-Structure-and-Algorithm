"""
Minimum Removals to Make Array Elements Unique

Problem: Given two arrays, find the minimum number of elements to remove from both
arrays such that there is no common element between the resulting arrays.

Approach: Find common elements between both arrays. For each common element,
we need to remove all occurrences from one of the arrays. Choose to remove from
the array with fewer occurrences to minimize total removals.

Time Complexity: O(n + m) where n and m are array sizes
Space Complexity: O(n + m) - frequency maps
"""

from collections import Counter


def min_removals_no_common(arr1, arr2):
    """
    Find minimum removals to make arrays have no common elements.

    Args:
        arr1: First array
        arr2: Second array

    Returns:
        Minimum number of removals required
    """
    freq1 = Counter(arr1)
    freq2 = Counter(arr2)

    removals = 0

    # For each common element
    for elem in set(arr1) & set(arr2):
        # Remove all occurrences from the array with fewer occurrences
        removals += min(freq1[elem], freq2[elem])

    return removals


if __name__ == "__main__":
    # Test Case 1: Common elements
    arr1_1 = [1, 2, 3, 4]
    arr2_1 = [2, 4, 5, 6]
    print(f"Array 1: {arr1_1}")
    print(f"Array 2: {arr2_1}")
    print(f"Min removals: {min_removals_no_common(arr1_1, arr2_1)}")
    print()

    # Test Case 2: No common elements
    arr1_2 = [1, 2, 3]
    arr2_2 = [4, 5, 6]
    print(f"Array 1: {arr1_2}")
    print(f"Array 2: {arr2_2}")
    print(f"Min removals: {min_removals_no_common(arr1_2, arr2_2)}")
    print()

    # Test Case 3: All elements common
    arr1_3 = [1, 1, 2]
    arr2_3 = [1, 2, 2]
    print(f"Array 1: {arr1_3}")
    print(f"Array 2: {arr2_3}")
    print(f"Min removals: {min_removals_no_common(arr1_3, arr2_3)}")
    print()

    # Test Case 4: Empty array
    arr1_4 = []
    arr2_4 = [1, 2, 3]
    print(f"Array 1: {arr1_4}")
    print(f"Array 2: {arr2_4}")
    print(f"Min removals: {min_removals_no_common(arr1_4, arr2_4)}")
    print()

    # Test Case 5: One element common
    arr1_5 = [1, 2, 3]
    arr2_5 = [3, 4, 5]
    print(f"Array 1: {arr1_5}")
    print(f"Array 2: {arr2_5}")
    print(f"Min removals: {min_removals_no_common(arr1_5, arr2_5)}")
    print()

    # Test Case 6: Multiple occurrences
    arr1_6 = [1, 1, 1, 2, 2]
    arr2_6 = [1, 1, 2, 3, 3]
    print(f"Array 1: {arr1_6}")
    print(f"Array 2: {arr2_6}")
    print(f"Min removals: {min_removals_no_common(arr1_6, arr2_6)}")
