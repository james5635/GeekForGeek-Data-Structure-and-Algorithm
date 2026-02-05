"""
Inversion Count in Array Using Merge Sort

Problem Description:
    Given an array, count the number of inversions.
    An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].

Time Complexity: O(n log n)
- Merge sort based approach: O(n log n)

Space Complexity: O(n)
- Temporary array for merging: O(n)
- Recursion stack: O(log n)

Example:
    Input: arr = [2, 4, 1, 3, 5]
    Output: 3
    Explanation: Inversions are: (2,1), (4,1), (4,3)

    Input: arr = [5, 4, 3, 2, 1]
    Output: 10
    Explanation: All pairs are inversions (reverse sorted array)

Approach:
    Modified Merge Sort:
    1. Divide array into two halves
    2. Count inversions in left half
    3. Count inversions in right half
    4. Count inversions during merge (when element from right comes before left)
    5. Return total count

Key Insight:
    During merge, if arr[i] > arr[j] (where i is in left, j is in right),
    then all elements from i to mid are greater than arr[j] (since left is sorted).
    So we add (mid - i + 1) to inversion count.
"""

from typing import List


def count_inversions(arr: List[int]) -> int:
    """
    Count inversions using modified merge sort.

    Args:
        arr: List of integers

    Returns:
        Number of inversions
    """
    if not arr or len(arr) <= 1:
        return 0

    temp_arr = [0] * len(arr)
    return _merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)


def _merge_sort_and_count(
    arr: List[int], temp_arr: List[int], left: int, right: int
) -> int:
    """
    Helper function for merge sort with inversion counting.

    Args:
        arr: Original array
        temp_arr: Temporary array for merging
        left: Left index
        right: Right index

    Returns:
        Inversion count for this subarray
    """
    inv_count = 0

    if left < right:
        mid = (left + right) // 2

        # Count inversions in left half
        inv_count += _merge_sort_and_count(arr, temp_arr, left, mid)

        # Count inversions in right half
        inv_count += _merge_sort_and_count(arr, temp_arr, mid + 1, right)

        # Count inversions during merge
        inv_count += _merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count


def _merge_and_count(
    arr: List[int], temp_arr: List[int], left: int, mid: int, right: int
) -> int:
    """
    Merge two sorted subarrays and count split inversions.

    Args:
        arr: Original array
        temp_arr: Temporary array
        left: Left index
        mid: Mid index
        right: Right index

    Returns:
        Number of split inversions
    """
    i = left  # Starting index for left subarray
    j = mid + 1  # Starting index for right subarray
    k = left  # Starting index for temp array
    inv_count = 0

    # Merge while counting inversions
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # Inversion found: arr[i] > arr[j]
            # All elements from i to mid are > arr[j]
            temp_arr[k] = arr[j]
            inv_count += mid - i + 1
            j += 1
        k += 1

    # Copy remaining elements of left subarray
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements of right subarray
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy back to original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def count_inversions_brute_force(arr: List[int]) -> int:
    """
    Brute force approach for verification (O(n^2)).

    Args:
        arr: List of integers

    Returns:
        Number of inversions
    """
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1

    return count


def count_inversions_using_bst(arr: List[int]) -> int:
    """
    Alternative: Using modified BST (AVL or Red-Black tree).
    Time: O(n log n), Space: O(n)
    Not implemented here but mentioned for completeness.
    """
    pass


# Test cases
def test_count_inversions():
    """Test cases for count_inversions function."""
    # Test case 1: Basic example
    arr1 = [2, 4, 1, 3, 5]
    result1 = count_inversions(arr1.copy())
    assert result1 == 3, f"Test 1 failed: {result1}"
    # Inversions: (2,1), (4,1), (4,3)

    # Test case 2: Reverse sorted
    arr2 = [5, 4, 3, 2, 1]
    result2 = count_inversions(arr2.copy())
    assert result2 == 10, f"Test 2 failed: {result2}"
    # Inversions: C(5,2) = 10

    # Test case 3: Already sorted
    arr3 = [1, 2, 3, 4, 5]
    result3 = count_inversions(arr3.copy())
    assert result3 == 0, f"Test 3 failed: {result3}"

    # Test case 4: All same elements
    arr4 = [1, 1, 1, 1]
    result4 = count_inversions(arr4.copy())
    assert result4 == 0, f"Test 4 failed: {result4}"

    # Test case 5: Single element
    arr5 = [5]
    result5 = count_inversions(arr5.copy())
    assert result5 == 0, f"Test 5 failed: {result5}"

    # Test case 6: Empty array
    arr6 = []
    result6 = count_inversions(arr6.copy())
    assert result6 == 0, f"Test 6 failed: {result6}"

    # Test case 7: Two elements - inverted
    arr7 = [2, 1]
    result7 = count_inversions(arr7.copy())
    assert result7 == 1, f"Test 7 failed: {result7}"

    # Test case 8: Two elements - not inverted
    arr8 = [1, 2]
    result8 = count_inversions(arr8.copy())
    assert result8 == 0, f"Test 8 failed: {result8}"

    # Test case 9: Compare with brute force
    arr9 = [8, 4, 2, 1, 5, 3, 7, 6]
    result9a = count_inversions(arr9.copy())
    result9b = count_inversions_brute_force(arr9.copy())
    assert result9a == result9b, f"Test 9 failed: {result9a} != {result9b}"

    # Test case 10: Large array comparison
    import random

    arr10 = [random.randint(1, 100) for _ in range(50)]
    result10a = count_inversions(arr10.copy())
    result10b = count_inversions_brute_force(arr10.copy())
    assert result10a == result10b, f"Test 10 failed: {result10a} != {result10b}"

    print("All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    test_count_inversions()

    # Example usage
    arr = [2, 4, 1, 3, 5]
    print(f"Array: {arr}")
    print(f"Inversion count: {count_inversions(arr.copy())}")

    arr2 = [5, 4, 3, 2, 1]
    print(f"\nArray: {arr2}")
    print(f"Inversion count: {count_inversions(arr2.copy())}")
