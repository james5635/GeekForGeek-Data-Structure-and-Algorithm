"""
Find Repetitive Element

Problem: Given an array of n+1 integers where each integer is between 1 and n
(inclusive), find the repetitive element. There is only one repeated number.

Approach: Use a hash set to track visited elements. Return the first element
that is already in the set.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - hash set stores visited elements
"""


def find_repetitive_element(arr):
    """
    Find the repetitive element in array.

    Args:
        arr: List of integers (n+1 elements, values 1 to n)

    Returns:
        The repetitive element, or None if not found
    """
    seen = set()

    for num in arr:
        if num in seen:
            return num
        seen.add(num)

    return None


def find_repetitive_xor(arr):
    """
    Find repetitive element using XOR (O(1) space).

    Args:
        arr: List of integers (n+1 elements, values 1 to n)

    Returns:
        The repetitive element
    """
    n = len(arr) - 1
    xor_all = 0
    xor_arr = 0

    # XOR of 1 to n
    for i in range(1, n + 1):
        xor_all ^= i

    # XOR of array elements
    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr


if __name__ == "__main__":
    # Test Case 1: Simple repetitive
    arr1 = [1, 2, 3, 3, 4]
    print(f"Array: {arr1}")
    print(f"Repetitive element: {find_repetitive_element(arr1)}")
    print()

    # Test Case 2: Repetitive at start
    arr2 = [1, 1, 2, 3, 4]
    print(f"Array: {arr2}")
    print(f"Repetitive element: {find_repetitive_element(arr2)}")
    print()

    # Test Case 3: Repetitive at end
    arr3 = [1, 2, 3, 4, 4]
    print(f"Array: {arr3}")
    print(f"Repetitive element: {find_repetitive_element(arr3)}")
    print()

    # Test Case 4: Large repetitive
    arr4 = [1, 2, 3, 4, 5, 5]
    print(f"Array: {arr4}")
    print(f"Repetitive element (Hash): {find_repetitive_element(arr4)}")
    print(f"Repetitive element (XOR): {find_repetitive_xor(arr4)}")
    print()

    # Test Case 5: No repetitive
    arr5 = [1, 2, 3, 4]
    print(f"Array: {arr5}")
    print(f"Repetitive element: {find_repetitive_element(arr5)}")
    print()

    # Test Case 6: Two elements
    arr6 = [1, 1]
    print(f"Array: {arr6}")
    print(f"Repetitive element: {find_repetitive_element(arr6)}")
