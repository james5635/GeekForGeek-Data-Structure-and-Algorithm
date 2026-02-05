"""
Minimum Subsets with Distinct Elements

Problem: Given an array, find the minimum number of subsets that can be formed
such that each subset contains only distinct elements.

Approach: Find the maximum frequency of any element. This determines the minimum
number of subsets needed since each occurrence must go to different subset.

Time Complexity: O(n) - count frequencies
Space Complexity: O(n) - frequency map
"""

from collections import Counter


def min_subsets_distinct(arr):
    """
    Find minimum number of subsets with distinct elements.

    Args:
        arr: List of integers

    Returns:
        Minimum number of subsets required
    """
    if not arr:
        return 0

    freq = Counter(arr)
    return max(freq.values())


def form_subsets(arr):
    """
    Actually form the subsets (for verification).

    Args:
        arr: List of integers

    Returns:
        List of subsets with distinct elements
    """
    if not arr:
        return []

    from collections import defaultdict

    freq = Counter(arr)
    num_subsets = max(freq.values())

    # Create empty subsets
    subsets = [[] for _ in range(num_subsets)]

    # Track next available subset for each element
    next_subset = defaultdict(int)

    for num in arr:
        subset_idx = next_subset[num]
        subsets[subset_idx].append(num)
        next_subset[num] += 1

    return subsets


if __name__ == "__main__":
    # Test Case 1: Multiple duplicates
    arr1 = [1, 2, 3, 4]
    print(f"Array: {arr1}")
    print(f"Min subsets needed: {min_subsets_distinct(arr1)}")
    print(f"Subsets: {form_subsets(arr1)}")
    print()

    # Test Case 2: All same elements
    arr2 = [5, 5, 5, 5]
    print(f"Array: {arr2}")
    print(f"Min subsets needed: {min_subsets_distinct(arr2)}")
    print(f"Subsets: {form_subsets(arr2)}")
    print()

    # Test Case 3: Mixed frequencies
    arr3 = [1, 2, 2, 3, 3, 3]
    print(f"Array: {arr3}")
    print(f"Min subsets needed: {min_subsets_distinct(arr3)}")
    print(f"Subsets: {form_subsets(arr3)}")
    print()

    # Test Case 4: Empty array
    arr4 = []
    print(f"Array: {arr4}")
    print(f"Min subsets needed: {min_subsets_distinct(arr4)}")
    print()

    # Test Case 5: Single element
    arr5 = [1]
    print(f"Array: {arr5}")
    print(f"Min subsets needed: {min_subsets_distinct(arr5)}")
    print()

    # Test Case 6: Two elements same
    arr6 = [1, 1]
    print(f"Array: {arr6}")
    print(f"Min subsets needed: {min_subsets_distinct(arr6)}")
    print(f"Subsets: {form_subsets(arr6)}")
