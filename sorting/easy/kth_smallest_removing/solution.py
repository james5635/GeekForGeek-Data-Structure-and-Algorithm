"""
K-th Smallest Element After Removing Integers from Natural Numbers

Problem Description:
    Given an array arr[] of size 'n' and a positive integer k.
    Consider series of natural numbers and remove arr[0], arr[1], ..., arr[n-1] from it.
    Find the k-th smallest number in the remaining set of natural numbers.
    If no such number exists, print -1.

Example:
    Input: arr = [1], k = 1
    Output: 2
    Explanation: Natural numbers are {1, 2, 3, 4, ...}
                 After removing {1}, we get {2, 3, 4, ...}
                 1st smallest element = 2

Time Complexity: O(n log n) - Due to sorting the removed array
Space Complexity: O(n) - For the set of removed elements
"""

from typing import List


def kth_smallest_after_removal(arr: List[int], k: int) -> int:
    """
    Find k-th smallest element after removing given integers from natural numbers.

    Args:
        arr: Array of integers to remove from natural numbers
        k: Position of the element to find (1-based)

    Returns:
        k-th smallest element in remaining natural numbers, or -1 if not found
    """
    if k <= 0:
        return -1

    # Create a set of removed elements for O(1) lookup
    removed = set(arr)

    # Count valid numbers until we find the k-th one
    count = 0
    num = 1

    while count < k:
        if num not in removed:
            count += 1
            if count == k:
                return num
        num += 1

        # Safety check to avoid infinite loop
        if num > 10**9:
            return -1

    return -1


def kth_smallest_optimized(arr: List[int], k: int) -> int:
    """
    Optimized approach using sorting.

    Args:
        arr: Array of integers to remove from natural numbers
        k: Position of the element to find (1-based)

    Returns:
        k-th smallest element in remaining natural numbers
    """
    if k <= 0:
        return -1

    # Sort the removed array
    arr_sorted = sorted(set(arr))

    # Iterate through removed elements and adjust k
    for num in arr_sorted:
        if num <= k:
            k += 1
        else:
            break

    return k


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr = [1]
    k = 1
    print("Test 1:")
    print(f"Removed: {arr}, k = {k}")
    result = kth_smallest_after_removal(arr, k)
    print(f"K-th smallest: {result}")
    result_opt = kth_smallest_optimized(arr, k)
    print(f"Optimized: {result_opt}")
    print()

    # Test Case 2: Multiple removals
    arr = [1, 3]
    k = 4
    print("Test 2:")
    print(f"Removed: {arr}, k = {k}")
    result = kth_smallest_after_removal(arr, k)
    print(f"K-th smallest: {result}")
    result_opt = kth_smallest_optimized(arr, k)
    print(f"Optimized: {result_opt}")
    print()

    # Test Case 3: No removals
    arr = []
    k = 5
    print("Test 3:")
    print(f"Removed: {arr}, k = {k}")
    result = kth_smallest_after_removal(arr, k)
    print(f"K-th smallest: {result}")
    result_opt = kth_smallest_optimized(arr, k)
    print(f"Optimized: {result_opt}")
    print()

    # Test Case 4: Remove consecutive numbers
    arr = [1, 2, 3, 4, 5]
    k = 3
    print("Test 4:")
    print(f"Removed: {arr}, k = {k}")
    result = kth_smallest_after_removal(arr, k)
    print(f"K-th smallest: {result}")
    result_opt = kth_smallest_optimized(arr, k)
    print(f"Optimized: {result_opt}")
    print()

    # Test Case 5: Large k
    arr = [2, 4, 6]
    k = 10
    print("Test 5:")
    print(f"Removed: {arr}, k = {k}")
    result = kth_smallest_after_removal(arr, k)
    print(f"K-th smallest: {result}")
    result_opt = kth_smallest_optimized(arr, k)
    print(f"Optimized: {result_opt}")
    print()

    # Test Case 6: All numbers before k
    arr = [1, 2, 3]
    k = 1
    print("Test 6:")
    print(f"Removed: {arr}, k = {k}")
    result = kth_smallest_after_removal(arr, k)
    print(f"K-th smallest: {result}")
    result_opt = kth_smallest_optimized(arr, k)
    print(f"Optimized: {result_opt}")
