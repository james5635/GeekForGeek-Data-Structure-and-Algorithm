"""
Union and Intersection of Two Unsorted Arrays

Problem: Given two unsorted arrays, find their union and intersection.
Union: All distinct elements from both arrays
Intersection: Common elements between both arrays

Example:
    Input: arr1[] = {3, 8, 2, 10, 5}, arr2[] = {7, 2, 10, 9, 3}
    Output:
        Union: {2, 3, 5, 7, 8, 9, 10} (or any order)
        Intersection: {2, 3, 10} (or any order)

Approach:
    Use hash sets for efficient lookups:
    - Union: Combine both arrays and use set to get distinct elements
    - Intersection: Use one set for lookups and another for common elements

Time Complexity: O(m + n) where m and n are sizes of the arrays
Space Complexity: O(m + n) for storing elements in hash sets
"""


def find_union(arr1, arr2):
    """
    Find union of two unsorted arrays (all distinct elements from both).

    Args:
        arr1: First unsorted array
        arr2: Second unsorted array

    Returns:
        list: Union of both arrays with distinct elements
    """
    # Use set to automatically handle duplicates
    union_set = set(arr1) | set(arr2)
    return list(union_set)


def find_union_sorted(arr1, arr2):
    """
    Find union and return sorted result.

    Args:
        arr1: First unsorted array
        arr2: Second unsorted array

    Returns:
        list: Sorted union of both arrays
    """
    union_set = set(arr1) | set(arr2)
    return sorted(union_set)


def find_intersection(arr1, arr2):
    """
    Find intersection of two unsorted arrays (common elements).

    Args:
        arr1: First unsorted array
        arr2: Second unsorted array

    Returns:
        list: Intersection of both arrays
    """
    # Convert first array to set for O(1) lookups
    set1 = set(arr1)

    # Find common elements
    intersection = []
    seen = set()  # To avoid duplicates in result

    for num in arr2:
        if num in set1 and num not in seen:
            intersection.append(num)
            seen.add(num)

    return intersection


def find_intersection_set(arr1, arr2):
    """
    Find intersection using set intersection operation.

    Args:
        arr1: First unsorted array
        arr2: Second unsorted array

    Returns:
        list: Intersection of both arrays
    """
    return list(set(arr1) & set(arr2))


def find_union_intersection(arr1, arr2):
    """
    Find both union and intersection in a single operation.

    Args:
        arr1: First unsorted array
        arr2: Second unsorted array

    Returns:
        tuple: (union_list, intersection_list)
    """
    set1 = set(arr1)
    set2 = set(arr2)

    union = list(set1 | set2)
    intersection = list(set1 & set2)

    return union, intersection


def find_union_intersection_with_counts(arr1, arr2):
    """
    Find union and intersection considering element frequencies.

    Args:
        arr1: First unsorted array
        arr2: Second unsorted array

    Returns:
        tuple: (union_list, intersection_list) with frequencies
    """
    from collections import Counter

    count1 = Counter(arr1)
    count2 = Counter(arr2)

    # Union: max frequency from both
    union_elements = list((count1 | count2).elements())

    # Intersection: min frequency from both
    intersection_elements = list((count1 & count2).elements())

    return union_elements, intersection_elements


if __name__ == "__main__":
    # Test Case 1: Standard case
    arr1 = [3, 8, 2, 10, 5]
    arr2 = [7, 2, 10, 9, 3]
    print(f"Test 1 - Union: {sorted(find_union(arr1, arr2))}")
    # Expected: [2, 3, 5, 7, 8, 9, 10]
    print(f"Test 1 - Intersection: {sorted(find_intersection(arr1, arr2))}")
    # Expected: [2, 3, 10]

    # Test Case 2: Arrays with duplicates
    arr1 = [1, 2, 2, 3, 4, 4]
    arr2 = [2, 2, 4, 6, 6]
    print(f"\nTest 2 - Union: {sorted(find_union(arr1, arr2))}")
    # Expected: [1, 2, 3, 4, 6]
    print(f"Test 2 - Intersection (set): {sorted(find_intersection_set(arr1, arr2))}")
    # Expected: [2, 4]

    # Test Case 3: One array empty
    arr1 = [1, 2, 3]
    arr2 = []
    print(f"\nTest 3 - Union: {sorted(find_union(arr1, arr2))}")
    # Expected: [1, 2, 3]
    print(f"Test 3 - Intersection: {find_intersection(arr1, arr2)}")
    # Expected: []

    # Test Case 4: No common elements
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    print(f"\nTest 4 - Union: {sorted(find_union(arr1, arr2))}")
    # Expected: [1, 2, 3, 4, 5, 6]
    print(f"Test 4 - Intersection: {find_intersection(arr1, arr2)}")
    # Expected: []

    # Test Case 5: Identical arrays
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3]
    print(f"\nTest 5 - Union: {sorted(find_union(arr1, arr2))}")
    # Expected: [1, 2, 3]
    print(f"Test 5 - Intersection: {sorted(find_intersection(arr1, arr2))}")
    # Expected: [1, 2, 3]

    # Test Case 6: Both arrays with many duplicates
    arr1 = [1, 1, 1, 2, 2]
    arr2 = [1, 1, 2, 2, 2]
    print(f"\nTest 6 - Union: {sorted(find_union(arr1, arr2))}")
    # Expected: [1, 2]
    print(f"Test 6 - Intersection: {sorted(find_intersection(arr1, arr2))}")
    # Expected: [1, 2]

    # Test Case 7: Get both in one call
    arr1 = [3, 8, 2, 10, 5]
    arr2 = [7, 2, 10, 9, 3]
    union, intersection = find_union_intersection(arr1, arr2)
    print(f"\nTest 7 - Union: {sorted(union)}, Intersection: {sorted(intersection)}")

    # Test Case 8: With counts (multiset operations)
    arr1 = [1, 1, 2, 3]
    arr2 = [1, 2, 2]
    union, intersection = find_union_intersection_with_counts(arr1, arr2)
    print(f"\nTest 8 - Union with counts: {sorted(union)}")
    # Expected: [1, 1, 2, 2, 3]
    print(f"Test 8 - Intersection with counts: {sorted(intersection)}")
    # Expected: [1, 2]
