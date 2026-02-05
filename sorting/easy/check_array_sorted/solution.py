"""
Check if Array is Sorted

Problem Description:
    Given an array of size n, write a program to check if the array is sorted
    in ascending order or not. This can be done using both iterative and
    recursive approaches.

Algorithm:
    - Iterate through the array from index 0 to n-2
    - Compare each element with the next element
    - If any element is greater than the next, array is not sorted
    - If loop completes without finding violations, array is sorted

Time Complexity: O(n)
    - Single pass through the array

Space Complexity: O(1)
    - Only using a constant amount of extra space
"""


def is_sorted_iterative(arr):
    """
    Check if array is sorted in ascending order using iterative approach.

    Args:
        arr: List of comparable elements

    Returns:
        bool: True if sorted in ascending order, False otherwise
    """
    n = len(arr)
    if n <= 1:
        return True

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def is_sorted_recursive(arr, index=0):
    """
    Check if array is sorted in ascending order using recursive approach.

    Args:
        arr: List of comparable elements
        index: Current index being checked (default 0)

    Returns:
        bool: True if sorted in ascending order, False otherwise
    """
    n = len(arr)
    if n <= 1 or index >= n - 1:
        return True

    if arr[index] > arr[index + 1]:
        return False

    return is_sorted_recursive(arr, index + 1)


if __name__ == "__main__":
    # Test Case 1: Already sorted array
    arr1 = [1, 2, 3, 4, 5]
    print(f"Array: {arr1}")
    print(f"Iterative: {is_sorted_iterative(arr1)}")
    print(f"Recursive: {is_sorted_recursive(arr1)}")
    print()

    # Test Case 2: Not sorted array
    arr2 = [1, 3, 2, 4, 5]
    print(f"Array: {arr2}")
    print(f"Iterative: {is_sorted_iterative(arr2)}")
    print(f"Recursive: {is_sorted_recursive(arr2)}")
    print()

    # Test Case 3: Single element
    arr3 = [5]
    print(f"Array: {arr3}")
    print(f"Iterative: {is_sorted_iterative(arr3)}")
    print(f"Recursive: {is_sorted_recursive(arr3)}")
    print()

    # Test Case 4: Empty array
    arr4 = []
    print(f"Array: {arr4}")
    print(f"Iterative: {is_sorted_iterative(arr4)}")
    print(f"Recursive: {is_sorted_recursive(arr4)}")
    print()

    # Test Case 5: Reverse sorted
    arr5 = [5, 4, 3, 2, 1]
    print(f"Array: {arr5}")
    print(f"Iterative: {is_sorted_iterative(arr5)}")
    print(f"Recursive: {is_sorted_recursive(arr5)}")
    print()

    # Test Case 6: Array with duplicates
    arr6 = [1, 2, 2, 3, 4]
    print(f"Array: {arr6}")
    print(f"Iterative: {is_sorted_iterative(arr6)}")
    print(f"Recursive: {is_sorted_recursive(arr6)}")
