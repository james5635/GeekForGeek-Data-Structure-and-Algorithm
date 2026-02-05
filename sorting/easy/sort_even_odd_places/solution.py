"""
Sort Even Increasing Odd Decreasing

Problem Description:
    Given an array of integers, sort the array such that:
    - Elements at even positions (0, 2, 4, ...) are in increasing order
    - Elements at odd positions (1, 3, 5, ...) are in decreasing order

    The relative positions of even and odd index elements should be maintained,
    only their order within their groups changes.

Algorithm:
    - Extract elements at even indices and sort in ascending order
    - Extract elements at odd indices and sort in descending order
    - Rebuild the array by interleaving the sorted groups

Time Complexity: O(n log n)
    - Extracting: O(n)
    - Sorting: O(n log n)
    - Rebuilding: O(n)

Space Complexity: O(n)
    - For storing even and odd index elements
"""


def sort_even_increasing_odd_decreasing(arr):
    """
    Sort even index elements in increasing order and
    odd index elements in decreasing order.

    Args:
        arr: List of integers

    Returns:
        list: Modified array
    """
    if not arr or len(arr) < 2:
        return arr

    # Extract even and odd index elements
    even_elements = [arr[i] for i in range(0, len(arr), 2)]
    odd_elements = [arr[i] for i in range(1, len(arr), 2)]

    # Sort even elements in increasing order
    even_elements.sort()

    # Sort odd elements in decreasing order
    odd_elements.sort(reverse=True)

    # Rebuild the array
    result = []
    even_idx = 0
    odd_idx = 0

    for i in range(len(arr)):
        if i % 2 == 0:
            result.append(even_elements[even_idx])
            even_idx += 1
        else:
            result.append(odd_elements[odd_idx])
            odd_idx += 1

    return result


def sort_even_odd_inplace(arr):
    """
    Alternative: Sort even and odd positions in-place without extra arrays.

    Args:
        arr: List of integers

    Returns:
        list: Modified array
    """
    if not arr or len(arr) < 2:
        return arr

    n = len(arr)

    # Simple bubble sort for even indices (ascending)
    for i in range(0, n, 2):
        for j in range(i + 2, n, 2):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    # Simple bubble sort for odd indices (descending)
    for i in range(1, n, 2):
        for j in range(i + 2, n, 2):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


def verify_sort_even_odd(arr):
    """
    Verify if array is sorted according to even-odd pattern.

    Args:
        arr: List of integers

    Returns:
        bool: True if correctly sorted
    """
    n = len(arr)

    # Check even indices are increasing
    for i in range(0, n - 2, 2):
        if arr[i] > arr[i + 2]:
            return False

    # Check odd indices are decreasing
    for i in range(1, n - 2, 2):
        if arr[i] < arr[i + 2]:
            return False

    return True


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"Original: {arr1}")
    result1 = sort_even_increasing_odd_decreasing(arr1.copy())
    print(f"Sorted: {result1}")
    print(f"Even indices (increasing): {result1[::2]}")
    print(f"Odd indices (decreasing): {result1[1::2]}")
    print(f"Valid: {verify_sort_even_odd(result1)}")
    print()

    # Test Case 2: Random array
    arr2 = [5, 2, 8, 1, 9, 4, 3, 7]
    print(f"Original: {arr2}")
    result2 = sort_even_increasing_odd_decreasing(arr2.copy())
    print(f"Sorted: {result2}")
    print(f"Valid: {verify_sort_even_odd(result2)}")
    print()

    # Test Case 3: Already sorted
    arr3 = [1, 9, 2, 8, 3, 7, 4, 6]
    print(f"Original: {arr3}")
    result3 = sort_even_increasing_odd_decreasing(arr3.copy())
    print(f"Sorted: {result3}")
    print(f"Valid: {verify_sort_even_odd(result3)}")
    print()

    # Test Case 4: Single element
    arr4 = [5]
    print(f"Original: {arr4}")
    result4 = sort_even_increasing_odd_decreasing(arr4.copy())
    print(f"Sorted: {result4}")
    print()

    # Test Case 5: Two elements
    arr5 = [2, 1]
    print(f"Original: {arr5}")
    result5 = sort_even_increasing_odd_decreasing(arr5.copy())
    print(f"Sorted: {result5}")
    print(f"Valid: {verify_sort_even_odd(result5)}")
    print()

    # Test Case 6: Empty array
    arr6 = []
    print(f"Original: {arr6}")
    result6 = sort_even_increasing_odd_decreasing(arr6.copy())
    print(f"Sorted: {result6}")
    print()

    # Test Case 7: All same elements
    arr7 = [5, 5, 5, 5, 5]
    print(f"Original: {arr7}")
    result7 = sort_even_increasing_odd_decreasing(arr7.copy())
    print(f"Sorted: {result7}")
    print(f"Valid: {verify_sort_even_odd(result7)}")
    print()

    # Test Case 8: In-place approach
    arr8 = [7, 1, 5, 9, 3, 8, 2, 6]
    print(f"Original: {arr8}")
    result8 = sort_even_odd_inplace(arr8.copy())
    print(f"In-place sorted: {result8}")
    print(f"Valid: {verify_sort_even_odd(result8)}")
    print()

    # Test Case 9: Larger array
    arr9 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"Original: {arr9}")
    result9 = sort_even_increasing_odd_decreasing(arr9.copy())
    print(f"Sorted: {result9}")
    print(f"Even positions: {result9[::2]}")
    print(f"Odd positions: {result9[1::2]}")
    print(f"Valid: {verify_sort_even_odd(result9)}")
