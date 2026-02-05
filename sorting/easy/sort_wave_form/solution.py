"""
Sort Array in Wave Form

Problem Description:
    Given an unsorted array of integers, sort the array into a wave-like array.
    An array 'arr[0..n-1]' is sorted in wave form if:
    arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= ...

    In other words, elements at even indexes are peak elements and elements
    at odd indexes are valley elements.

Algorithm (Optimal - Single Pass):
    - Traverse all even positioned elements
    - For each even index i:
        - If arr[i] < arr[i-1], swap them
        - If arr[i] < arr[i+1], swap them
    - This ensures arr[i] is greater than both neighbors

Time Complexity: O(n)
    - Single pass through the array

Space Complexity: O(1)
    - In-place sorting with constant extra space
"""


def sort_in_wave_form(arr):
    """
    Sort array in wave form using single pass approach.

    Args:
        arr: List of integers

    Returns:
        list: Array sorted in wave form
    """
    if not arr or len(arr) < 2:
        return arr

    n = len(arr)

    # Traverse all even indexed elements
    for i in range(0, n, 2):
        # If current even element is smaller than previous
        if i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]

        # If current even element is smaller than next
        if i < n - 1 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


def sort_in_wave_form_sort_first(arr):
    """
    Alternative: Sort array first, then swap adjacent elements.

    Args:
        arr: List of integers

    Returns:
        list: Array sorted in wave form
    """
    if not arr or len(arr) < 2:
        return arr

    n = len(arr)

    # Sort the array
    arr.sort()

    # Swap adjacent elements
    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


def is_wave_form(arr):
    """
    Check if array is in wave form.

    Args:
        arr: List of integers

    Returns:
        bool: True if array is in wave form
    """
    n = len(arr)
    for i in range(1, n, 2):
        if i > 0 and arr[i] > arr[i - 1]:
            return False
        if i < n - 1 and arr[i] > arr[i + 1]:
            return False
    return True


def find_wave_form_max(arr):
    """
    Find the maximum element in wave form array (peak element).

    Args:
        arr: List of integers in wave form

    Returns:
        int: Maximum element
    """
    if not arr:
        return None

    # In wave form, max is at even index 0 or any peak
    max_val = arr[0]
    for i in range(0, len(arr), 2):
        max_val = max(max_val, arr[i])
    return max_val


if __name__ == "__main__":
    # Test Case 1: Random array
    arr1 = [10, 5, 6, 3, 2, 20, 100, 80]
    print(f"Original: {arr1}")
    result1 = sort_in_wave_form(arr1.copy())
    print(f"Wave form: {result1}")
    print(f"Is valid wave form: {is_wave_form(result1)}")
    print()

    # Test Case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5, 6]
    print(f"Original: {arr2}")
    result2 = sort_in_wave_form(arr2.copy())
    print(f"Wave form: {result2}")
    print(f"Is valid wave form: {is_wave_form(result2)}")
    print()

    # Test Case 3: Reverse sorted array
    arr3 = [6, 5, 4, 3, 2, 1]
    print(f"Original: {arr3}")
    result3 = sort_in_wave_form(arr3.copy())
    print(f"Wave form: {result3}")
    print(f"Is valid wave form: {is_wave_form(result3)}")
    print()

    # Test Case 4: Two elements
    arr4 = [1, 2]
    print(f"Original: {arr4}")
    result4 = sort_in_wave_form(arr4.copy())
    print(f"Wave form: {result4}")
    print(f"Is valid wave form: {is_wave_form(result4)}")
    print()

    # Test Case 5: Single element
    arr5 = [5]
    print(f"Original: {arr5}")
    result5 = sort_in_wave_form(arr5.copy())
    print(f"Wave form: {result5}")
    print()

    # Test Case 6: All same elements
    arr6 = [5, 5, 5, 5, 5]
    print(f"Original: {arr6}")
    result6 = sort_in_wave_form(arr6.copy())
    print(f"Wave form: {result6}")
    print(f"Is valid wave form: {is_wave_form(result6)}")
    print()

    # Test Case 7: Compare both approaches
    arr7 = [3, 6, 5, 10, 7, 20]
    print(f"Original: {arr7}")
    print(f"Optimal approach: {sort_in_wave_form(arr7.copy())}")
    print(f"Sort-first approach: {sort_in_wave_form_sort_first(arr7.copy())}")
    print()

    # Test Case 8: Find max in wave form
    arr8 = [100, 5, 80, 3, 60, 2]
    print(f"Wave form array: {arr8}")
    print(f"Maximum element: {find_wave_form_max(arr8)}")
