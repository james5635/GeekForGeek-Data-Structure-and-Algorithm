"""
Check if a given array represents a Binary Max-Heap

Problem:
Given an array, check if the given array represents a Binary Max-Heap.

Examples:
Input: arr[] = {90, 15, 10, 7, 12, 2}
Output: True (array represents a max-heap)

Input: arr[] = {9, 15, 10, 7, 12, 11}
Output: False (9 is smaller than its children 15 and 10)

Algorithm Steps (Efficient Approach):
1. Start from root (index 0) and go till the last internal node (index (n-2)//2)
2. For each internal node at index i:
   - Check if left child (2*i + 1) exists and is greater than parent
   - Check if right child (2*i + 2) exists and is greater than parent
3. If any child is greater than parent, it's not a max-heap
4. If all internal nodes satisfy the max-heap property, return True

Time Complexity: O(n)
Space Complexity: O(1)
"""

import math
from typing import List


def is_heap_recursive(arr: List[int], i: int, n: int) -> bool:
    """
    Check if array represents a max-heap using recursion.

    Args:
        arr: Input array
        i: Current index (starting from 0)
        n: Size of array

    Returns:
        True if arr[i..n-1] represents a max-heap, False otherwise
    """
    left = 2 * i + 1
    right = 2 * i + 2

    if left >= n:
        return True

    if arr[i] < arr[left]:
        return False

    if right < n and arr[i] < arr[right]:
        return False

    return is_heap_recursive(arr, left, n) and (
        right >= n or is_heap_recursive(arr, right, n)
    )


def is_heap_iterative(arr: List[int], n: int) -> bool:
    """
    Check if array represents a max-heap using iteration.
    This is more efficient as it avoids recursion overhead.

    Args:
        arr: Input array
        n: Size of array

    Returns:
        True if array represents a max-heap, False otherwise
    """
    for i in range((n - 2) // 2 + 1):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[i]:
            return False

        if right < n and arr[right] > arr[i]:
            return False

    return True


def check_binary_heap(arr: List[int], method: str = "iterative") -> bool:
    """
    Check if an array represents a binary max-heap.

    Args:
        arr: Input array to check
        method: "iterative" (default) or "recursive"

    Returns:
        True if the array represents a max-heap, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(1) for iterative, O(h) for recursive (h = height)
    """
    n = len(arr)

    if n <= 1:
        return True

    if method == "recursive":
        return is_heap_recursive(arr, 0, n)
    else:
        return is_heap_iterative(arr, n)


if __name__ == "__main__":
    test_cases = [
        {"arr": [90, 15, 10, 7, 12, 2], "expected": True},
        {"arr": [9, 15, 10, 7, 12, 11], "expected": False},
        {"arr": [90, 15, 10, 7, 12, 2, 7, 3], "expected": True},
        {"arr": [1], "expected": True},
        {"arr": [2, 1], "expected": True},
        {"arr": [1, 2], "expected": False},
        {"arr": [10, 20, 15, 40, 50, 25, 35, 30], "expected": False},
        {"arr": [10, 5, 10], "expected": True},
    ]

    print("Binary Heap Check Test Cases")
    print("=" * 50)

    for i, tc in enumerate(test_cases):
        arr = tc["arr"]
        expected = tc["expected"]

        result_iterative = check_binary_heap(arr, "iterative")
        result_recursive = check_binary_heap(arr, "recursive")

        status = (
            "PASS"
            if (result_iterative == expected and result_recursive == expected)
            else "FAIL"
        )

        print(f"Test {i + 1}: arr = {arr}")
        print(
            f"  Expected: {expected}, Iterative: {result_iterative}, Recursive: {result_recursive}"
        )
        print(f"  Status: {status}")
        print()
