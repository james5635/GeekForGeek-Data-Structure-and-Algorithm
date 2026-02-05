"""
Surpasser Count Problem

Problem Description:
Given an array arr[], the surpasser count of an element arr[i] is the number of elements
that are greater than arr[i] and appear to its right in the array.

For example, in array [2, 7, 5, 3, 0, 8, 1]:
- Surpasser count of 2 is 4 (7, 5, 3, 8)
- Surpasser count of 7 is 1 (8)
- Surpasser count of 5 is 1 (8)

Time Complexity: O(n log n) using Merge Sort approach
Space Complexity: O(n) for auxiliary arrays

Approach:
Use modified Merge Sort to count surpassers efficiently.
"""

from typing import List


def find_surpasser_count(arr: List[int]) -> List[int]:
    """
    Find surpasser count for each element in the array.

    Args:
        arr: List of integers

    Returns:
        List of surpasser counts for each element
    """
    if not arr:
        return []

    n = len(arr)
    result = [0] * n

    # Create pairs of (value, original_index) to track elements
    indexed_arr = [(arr[i], i) for i in range(n)]
    temp: List[tuple] = [(0, 0)] * n

    def merge_sort(left: int, right: int):
        """Modified merge sort to count surpassers."""
        if left < right:
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            merge(left, mid, right)

    def merge(left: int, mid: int, right: int):
        """Merge two sorted halves and count surpassers."""
        i = left
        j = mid + 1
        k = left

        # Count surpassers during merge
        while i <= mid and j <= right:
            if indexed_arr[i][0] < indexed_arr[j][0]:
                # indexed_arr[j] and all elements to its right in right half
                # are surpassers for indexed_arr[i]
                result[indexed_arr[i][1]] += right - j + 1
                temp[k] = indexed_arr[i]
                i += 1
            else:
                temp[k] = indexed_arr[j]
                j += 1
            k += 1

        while i <= mid:
            temp[k] = indexed_arr[i]
            i += 1
            k += 1

        while j <= right:
            temp[k] = indexed_arr[j]
            j += 1
            k += 1

        # Copy back to original array
        for idx in range(left, right + 1):
            indexed_arr[idx] = temp[idx]

    merge_sort(0, n - 1)
    return result


def find_surpasser_count_brute_force(arr: List[int]) -> List[int]:
    """
    Brute force approach for comparison.
    Time: O(n^2), Space: O(1)
    """
    n = len(arr)
    result = []

    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                count += 1
        result.append(count)

    return result


if __name__ == "__main__":
    # Test Case 1: Basic example
    arr1 = [2, 7, 5, 3, 0, 8, 1]
    result1 = find_surpasser_count(arr1)
    expected1 = [4, 1, 1, 1, 2, 0, 0]
    print(f"Input: {arr1}")
    print(f"Surpasser counts: {result1}")
    print(f"Expected: {expected1}")
    print(f"Pass: {result1 == expected1}\n")

    # Test Case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    result2 = find_surpasser_count(arr2)
    expected2 = [4, 3, 2, 1, 0]
    print(f"Input: {arr2}")
    print(f"Surpasser counts: {result2}")
    print(f"Expected: {expected2}")
    print(f"Pass: {result2 == expected2}\n")

    # Test Case 3: Reverse sorted array
    arr3 = [5, 4, 3, 2, 1]
    result3 = find_surpasser_count(arr3)
    expected3 = [0, 0, 0, 0, 0]
    print(f"Input: {arr3}")
    print(f"Surpasser counts: {result3}")
    print(f"Expected: {expected3}")
    print(f"Pass: {result3 == expected3}\n")

    # Test Case 4: Array with duplicates
    arr4 = [3, 1, 2, 3, 1]
    result4 = find_surpasser_count(arr4)
    print(f"Input: {arr4}")
    print(f"Surpasser counts: {result4}\n")

    # Test Case 5: Empty array
    arr5 = []
    result5 = find_surpasser_count(arr5)
    print(f"Input: {arr5}")
    print(f"Surpasser counts: {result5}")
    print(f"Expected: []")
    print(f"Pass: {result5 == []}\n")

    # Test Case 6: Single element
    arr6 = [42]
    result6 = find_surpasser_count(arr6)
    print(f"Input: {arr6}")
    print(f"Surpasser counts: {result6}")
    print(f"Expected: [0]")
    print(f"Pass: {result6 == [0]}")
