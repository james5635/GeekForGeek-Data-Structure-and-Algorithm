"""
Sort Array with Two Types of Elements

Problem Description:
    Given an array A[] consisting of only 0s, 1s, and 2s (or any two types of
    elements), sort the array in ascending order. This is also known as the
    Dutch National Flag problem when sorting 0s, 1s, and 2s.

Algorithm (Dutch National Flag Algorithm):
    - Maintain three pointers: low, mid, high
    - low: boundary of 0s (elements before low are 0s)
    - mid: current element being examined
    - high: boundary of 2s (elements after high are 2s)
    - Iterate while mid <= high:
        - If arr[mid] == 0: swap with arr[low], increment both
        - If arr[mid] == 1: just increment mid
        - If arr[mid] == 2: swap with arr[high], decrement high

Time Complexity: O(n)
    - Single pass through the array

Space Complexity: O(1)
    - In-place sorting with constant extra space
"""


def sort_two_types(arr):
    """
    Sort array containing 0s and 1s (or two types of elements).

    Args:
        arr: List containing two types of elements (e.g., 0s and 1s)

    Returns:
        List: Sorted array
    """
    if not arr:
        return arr

    # Use two-pointer approach for binary types
    left = 0
    right = len(arr) - 1

    while left < right:
        # Move left pointer until we find a 1 (or second type)
        while left < right and arr[left] == 0:
            left += 1

        # Move right pointer until we find a 0 (or first type)
        while left < right and arr[right] == 1:
            right -= 1

        # Swap if pointers haven't crossed
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr


def sort_three_types(arr):
    """
    Sort array containing 0s, 1s, and 2s using Dutch National Flag algorithm.

    Args:
        arr: List containing 0s, 1s, and 2s

    Returns:
        List: Sorted array
    """
    if not arr:
        return arr

    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


def segregate_positive_negative(arr):
    """
    Segregate positive and negative numbers.
    All negative numbers come before positive numbers.

    Args:
        arr: List of integers

    Returns:
        List: Array with negatives first, then positives
    """
    if not arr:
        return arr

    left = 0
    right = len(arr) - 1

    while left < right:
        # Move left until we find a positive
        while left < right and arr[left] < 0:
            left += 1

        # Move right until we find a negative
        while left < right and arr[right] >= 0:
            right -= 1

        # Swap
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr


if __name__ == "__main__":
    # Test Case 1: Binary array (0s and 1s)
    arr1 = [0, 1, 0, 1, 0, 0, 1, 1, 0]
    print(f"Original (binary): {arr1}")
    print(f"Sorted: {sort_two_types(arr1.copy())}")
    print()

    # Test Case 2: Ternary array (0s, 1s, and 2s)
    arr2 = [0, 1, 2, 0, 1, 2, 0, 0, 1, 2, 1, 0]
    print(f"Original (ternary): {arr2}")
    print(f"Sorted: {sort_three_types(arr2.copy())}")
    print()

    # Test Case 3: Segregate positive and negative
    arr3 = [-1, 2, -3, 4, -5, 6, -7, 8]
    print(f"Original (mixed): {arr3}")
    print(f"Segregated: {segregate_positive_negative(arr3.copy())}")
    print()

    # Test Case 4: All zeros
    arr4 = [0, 0, 0, 0]
    print(f"All zeros: {arr4}")
    print(f"Sorted: {sort_two_types(arr4.copy())}")
    print()

    # Test Case 5: All ones
    arr5 = [1, 1, 1, 1]
    print(f"All ones: {arr5}")
    print(f"Sorted: {sort_two_types(arr5.copy())}")
    print()

    # Test Case 6: Empty array
    arr6 = []
    print(f"Empty: {arr6}")
    print(f"Sorted: {sort_two_types(arr6.copy())}")
