"""
Find Minimum and Maximum Elements in Array using Recursion

Given an array of integers, find the minimum and maximum elements
using recursion only.

Approach:
- Base case: single element array - element is both min and max
- Recursive case: find min/max of first n-1 elements, then compare
  with nth element to update min/max

Time Complexity: O(n)
Space Complexity: O(n) - recursion stack space
"""

from typing import List, Tuple


def find_min_max_rec(arr: List[int], index: int) -> Tuple[int, int]:
    """
    Helper recursive function to find min and max.

    Args:
        arr: List of integers
        index: Current index being processed

    Returns:
        Tuple of (min_value, max_value)
    """
    # Base case: only one element
    if index == 0:
        return arr[0], arr[0]

    # Recursive call for first index elements
    min_val, max_val = find_min_max_rec(arr, index - 1)

    # Update min if current element is smaller
    if arr[index] < min_val:
        min_val = arr[index]

    # Update max if current element is larger
    if arr[index] > max_val:
        max_val = arr[index]

    return min_val, max_val


def find_min_max(arr: List[int]) -> Tuple[int, int]:
    """
    Find minimum and maximum elements in array.

    Args:
        arr: List of integers (non-empty)

    Returns:
        Tuple of (minimum, maximum)
    """
    if not arr:
        raise ValueError("Array cannot be empty")

    return find_min_max_rec(arr, len(arr) - 1)


def main():
    """Test cases for finding min and max."""
    test_cases = [
        [1, 4, 3, -5, -4, 8, 6],
        [12, 3, 15, 7, 9],
        [5],
        [1, 1, 1, 1],
        [-10, -5, -20, -3],
        [100, 50, 200, 25, 300],
    ]

    print("Find Min and Max using Recursion")
    print("=" * 50)

    for arr in test_cases:
        min_val, max_val = find_min_max(arr)
        print(f"Array: {arr}")
        print(f"Minimum: {min_val}")
        print(f"Maximum: {max_val}")
        print("-" * 30)


if __name__ == "__main__":
    main()
