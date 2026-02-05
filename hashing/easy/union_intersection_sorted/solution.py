"""
Union and Intersection of Two Sorted Arrays

Problem: Given two sorted arrays, find their union and intersection.
Union: All distinct elements from both arrays
Intersection: Common elements between both arrays

Example:
    Input: arr1[] = {1, 3, 4, 5, 7}, arr2[] = {2, 3, 5, 6}
    Output:
        Union: {1, 2, 3, 4, 5, 6, 7}
        Intersection: {3, 5}

Approach:
    Use two-pointer technique to traverse both sorted arrays simultaneously.
    For Union: Add elements from both arrays, skipping duplicates
    For Intersection: Add elements when both pointers point to same value

Time Complexity: O(m + n) where m and n are sizes of the arrays
Space Complexity: O(m + n) for storing union and intersection results
"""


def find_union(arr1, arr2):
    """
    Find union of two sorted arrays (all distinct elements from both).

    Args:
        arr1: First sorted array
        arr2: Second sorted array

    Returns:
        list: Sorted union of both arrays with distinct elements
    """
    i, j = 0, 0
    union = []

    while i < len(arr1) and j < len(arr2):
        # Skip duplicates in arr1
        while i > 0 and i < len(arr1) and arr1[i] == arr1[i - 1]:
            i += 1

        # Skip duplicates in arr2
        while j > 0 and j < len(arr2) and arr2[j] == arr2[j - 1]:
            j += 1

        if i >= len(arr1) or j >= len(arr2):
            break

        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1
        else:  # Equal elements
            union.append(arr1[i])
            i += 1
            j += 1

    # Add remaining elements from arr1
    while i < len(arr1):
        if i == 0 or arr1[i] != arr1[i - 1]:
            union.append(arr1[i])
        i += 1

    # Add remaining elements from arr2
    while j < len(arr2):
        if j == 0 or arr2[j] != arr2[j - 1]:
            union.append(arr2[j])
        j += 1

    return union


def find_intersection(arr1, arr2):
    """
    Find intersection of two sorted arrays (common elements).

    Args:
        arr1: First sorted array
        arr2: Second sorted array

    Returns:
        list: Sorted intersection of both arrays
    """
    i, j = 0, 0
    intersection = []

    while i < len(arr1) and j < len(arr2):
        # Skip duplicates in arr1
        while i > 0 and i < len(arr1) and arr1[i] == arr1[i - 1]:
            i += 1

        # Skip duplicates in arr2
        while j > 0 and j < len(arr2) and arr2[j] == arr2[j - 1]:
            j += 1

        if i >= len(arr1) or j >= len(arr2):
            break

        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:  # Equal elements - common element found
            intersection.append(arr1[i])
            i += 1
            j += 1

    return intersection


def find_union_intersection(arr1, arr2):
    """
    Find both union and intersection in a single pass.

    Args:
        arr1: First sorted array
        arr2: Second sorted array

    Returns:
        tuple: (union_list, intersection_list)
    """
    return find_union(arr1, arr2), find_intersection(arr1, arr2)


if __name__ == "__main__":
    # Test Case 1: Standard case
    arr1 = [1, 3, 4, 5, 7]
    arr2 = [2, 3, 5, 6]
    print(f"Test 1 - Union: {find_union(arr1, arr2)}")
    # Expected: [1, 2, 3, 4, 5, 6, 7]
    print(f"Test 1 - Intersection: {find_intersection(arr1, arr2)}")
    # Expected: [3, 5]

    # Test Case 2: Arrays with duplicates
    arr1 = [1, 2, 2, 3, 4]
    arr2 = [2, 2, 4, 6]
    print(f"\nTest 2 - Union: {find_union(arr1, arr2)}")
    # Expected: [1, 2, 3, 4, 6]
    print(f"Test 2 - Intersection: {find_intersection(arr1, arr2)}")
    # Expected: [2, 4]

    # Test Case 3: One array empty
    arr1 = [1, 2, 3]
    arr2 = []
    print(f"\nTest 3 - Union: {find_union(arr1, arr2)}")
    # Expected: [1, 2, 3]
    print(f"Test 3 - Intersection: {find_intersection(arr1, arr2)}")
    # Expected: []

    # Test Case 4: No common elements
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    print(f"\nTest 4 - Union: {find_union(arr1, arr2)}")
    # Expected: [1, 2, 3, 4, 5, 6]
    print(f"Test 4 - Intersection: {find_intersection(arr1, arr2)}")
    # Expected: []

    # Test Case 5: Identical arrays
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3]
    print(f"\nTest 5 - Union: {find_union(arr1, arr2)}")
    # Expected: [1, 2, 3]
    print(f"Test 5 - Intersection: {find_intersection(arr1, arr2)}")
    # Expected: [1, 2, 3]

    # Test Case 6: Single elements
    arr1 = [1]
    arr2 = [1]
    print(f"\nTest 6 - Union: {find_union(arr1, arr2)}")
    # Expected: [1]
    print(f"Test 6 - Intersection: {find_intersection(arr1, arr2)}")
    # Expected: [1]

    # Test Case 7: Both arrays with many duplicates
    arr1 = [1, 1, 1, 2, 2]
    arr2 = [1, 1, 2, 2, 2]
    print(f"\nTest 7 - Union: {find_union(arr1, arr2)}")
    # Expected: [1, 2]
    print(f"Test 7 - Intersection: {find_intersection(arr1, arr2)}")
    # Expected: [1, 2]

    # Test Case 8: Get both in one call
    arr1 = [1, 3, 4, 5, 7]
    arr2 = [2, 3, 5, 6]
    union, intersection = find_union_intersection(arr1, arr2)
    print(f"\nTest 8 - Union: {union}, Intersection: {intersection}")
