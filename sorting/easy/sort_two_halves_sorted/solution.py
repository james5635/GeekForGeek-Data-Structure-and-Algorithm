"""
Sort Array When Two Halves are Sorted

Problem Description:
    Given an integer array arr[] whose first k elements and remaining n-k elements
    are each sorted, merge these two sorted halves into a single fully sorted array.
    Note: There doesn't exist more than two sorted halves in an array.

Example:
    Input: arr = [2, 3, 8, -1, 7, 10]
    Output: [-1, 2, 3, 7, 8, 10]
    Explanation: First half [2, 3, 8] and second half [-1, 7, 10] are each sorted.
                 After merging, we get [-1, 2, 3, 7, 8, 10]

Time Complexity: O(n) - Linear time using merge technique
Space Complexity: O(n) - For the temporary array
"""


def sort_two_halves(arr):
    """
    Sort an array where two halves are individually sorted.

    Args:
        arr: Array with two sorted halves

    Returns:
        Sorted array
    """
    n = len(arr)
    if n <= 1:
        return arr

    # Find the point where array is divided into two halves
    split_index = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            split_index = i + 1
            break

    # If array is already fully sorted
    if split_index == 0:
        return arr.copy()

    # Merge the two sorted halves
    temp = [0] * n
    i, j, k = 0, split_index, 0

    while i < split_index and j < n:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    # Copy remaining elements from first half
    while i < split_index:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements from second half
    while j < n:
        temp[k] = arr[j]
        j += 1
        k += 1

    return temp


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr = [2, 3, 8, -1, 7, 10]
    print("Test 1:")
    print(f"Input:  {arr}")
    result = sort_two_halves(arr)
    print(f"Output: {result}")
    print()

    # Test Case 2: Different split point
    arr = [-4, 6, 9, -1, 3]
    print("Test 2:")
    print(f"Input:  {arr}")
    result = sort_two_halves(arr)
    print(f"Output: {result}")
    print()

    # Test Case 3: Already sorted
    arr = [1, 2, 3, 4, 5]
    print("Test 3:")
    print(f"Input:  {arr}")
    result = sort_two_halves(arr)
    print(f"Output: {result}")
    print()

    # Test Case 4: Single element halves
    arr = [5, 1]
    print("Test 4:")
    print(f"Input:  {arr}")
    result = sort_two_halves(arr)
    print(f"Output: {result}")
    print()

    # Test Case 5: With duplicates
    arr = [1, 2, 2, 1, 2, 3]
    print("Test 5:")
    print(f"Input:  {arr}")
    result = sort_two_halves(arr)
    print(f"Output: {result}")
    print()

    # Test Case 6: Empty array
    arr = []
    print("Test 6:")
    print(f"Input:  {arr}")
    result = sort_two_halves(arr)
    print(f"Output: {result}")
