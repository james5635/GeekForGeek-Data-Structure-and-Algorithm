"""
Merge Two Sorted Arrays

Problem Description:
    Given two sorted arrays arr1[] of size n and arr2[] of size m.
    Merge these two arrays such that after the merge:
    - The first n smallest elements of the combined sorted array are stored in arr1[]
    - The remaining m largest elements are stored in arr2[]
    - Both arr1[] and arr2[] must remain sorted in non-decreasing order

Example:
    Input: arr1 = [1, 3, 5, 7], arr2 = [2, 4, 6, 8]
    Output: arr1 = [1, 2, 3, 4], arr2 = [5, 6, 7, 8]

Time Complexity: O(n + m) - Linear time using two-pointer technique
Space Complexity: O(n + m) - For the temporary merged array
"""


def merge_arrays(arr1, arr2):
    """
    Merge two sorted arrays in-place.

    Args:
        arr1: First sorted array (modified in-place)
        arr2: Second sorted array (modified in-place)
    """
    n, m = len(arr1), len(arr2)
    i, j = 0, 0
    merged = []

    # Merge elements in sorted order using two-pointer technique
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Copy remaining elements from arr1
    while i < n:
        merged.append(arr1[i])
        i += 1

    # Copy remaining elements from arr2
    while j < m:
        merged.append(arr2[j])
        j += 1

    # Distribute merged elements back to arr1 and arr2
    for i in range(n):
        arr1[i] = merged[i]
    for j in range(m):
        arr2[j] = merged[n + j]


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]
    print("Test 1:")
    print(f"Before: arr1 = {arr1}, arr2 = {arr2}")
    merge_arrays(arr1, arr2)
    print(f"After:  arr1 = {arr1}, arr2 = {arr2}")
    print()

    # Test Case 2: Arrays with duplicates
    arr1 = [1, 3, 4, 5]
    arr2 = [2, 4, 6, 8]
    print("Test 2:")
    print(f"Before: arr1 = {arr1}, arr2 = {arr2}")
    merge_arrays(arr1, arr2)
    print(f"After:  arr1 = {arr1}, arr2 = {arr2}")
    print()

    # Test Case 3: Different sizes
    arr1 = [5, 8, 9]
    arr2 = [4, 7, 8]
    print("Test 3:")
    print(f"Before: arr1 = {arr1}, arr2 = {arr2}")
    merge_arrays(arr1, arr2)
    print(f"After:  arr1 = {arr1}, arr2 = {arr2}")
    print()

    # Test Case 4: One empty array
    arr1 = []
    arr2 = [1, 2, 3]
    print("Test 4:")
    print(f"Before: arr1 = {arr1}, arr2 = {arr2}")
    merge_arrays(arr1, arr2)
    print(f"After:  arr1 = {arr1}, arr2 = {arr2}")
    print()

    # Test Case 5: Arrays with negative numbers
    arr1 = [-5, 0, 5]
    arr2 = [-3, 2, 8]
    print("Test 5:")
    print(f"Before: arr1 = {arr1}, arr2 = {arr2}")
    merge_arrays(arr1, arr2)
    print(f"After:  arr1 = {arr1}, arr2 = {arr2}")
