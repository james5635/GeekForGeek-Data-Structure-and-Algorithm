"""
Even Positioned Greater Than Odd

Rearrange array such that even positioned elements are greater than odd positioned elements.

Approaches:
1. Sort and assign: Sort array, put larger elements at even positions - O(n log n) time
2. Single pass swap: Swap adjacent elements if needed - O(n) time
"""


def rearrange_sort_approach(arr):
    """
    Approach 1: Sort and assign max to even positions.

    Time Complexity: O(n log n)
    Space Complexity: O(n) for the result (or O(1) if modifying in-place with sorting)

    Algorithm:
    1. Sort the array in ascending order
    2. Create result array
    3. Fill odd positions (1, 3, 5...) from start of sorted array
    4. Fill even positions (0, 2, 4...) from end of sorted array

    Args:
        arr: List of integers

    Returns:
        Rearranged array where even positioned elements >= odd positioned elements
    """
    n = len(arr)
    if n <= 1:
        return arr.copy()

    # Sort the array
    sorted_arr = sorted(arr)

    result = [0] * n

    # Pointers for sorted array
    left = 0  # Start (smaller elements)
    right = n - 1  # End (larger elements)

    # Fill odd positions with smaller elements
    for i in range(1, n, 2):
        result[i] = sorted_arr[left]
        left += 1

    # Fill even positions with larger elements
    for i in range(0, n, 2):
        result[i] = sorted_arr[right]
        right -= 1

    return result


def rearrange_single_pass(arr):
    """
    Approach 2: Single pass - swap adjacent elements if needed.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    Traverse array and for each pair (i, i+1):
    - If i is even: arr[i] should be >= arr[i+1]
    - If i is odd: arr[i] should be <= arr[i+1]
    - Swap if condition not met

    This ensures local ordering which leads to global ordering.

    Args:
        arr: List of integers

    Returns:
        Rearranged array (modifies in-place)
    """
    n = len(arr)

    for i in range(n - 1):
        if i % 2 == 0:
            # Even index: should be greater than or equal to next
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            # Odd index: should be less than or equal to next
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


def verify_rearrangement(arr):
    """
    Verify that even positioned elements are greater than or equal to odd positioned.

    Args:
        arr: List of integers

    Returns:
        True if rearrangement is correct, False otherwise
    """
    for i in range(0, len(arr) - 1, 2):
        if i + 1 < len(arr) and arr[i] < arr[i + 1]:
            return False
    return True


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5, 6],
        [6, 5, 4, 3, 2, 1],
        [1, 3, 2],
        [1, 2],
        [5],
        [],
        [1, 1, 1, 1],
        [10, 5, 8, 3, 7, 2],
    ]

    print("=" * 70)
    print("Even Positioned Greater Than Odd - Test Cases")
    print("=" * 70)

    for i, arr in enumerate(test_cases, 1):
        print(f"\nTest {i}: Original = {arr}")

        # Test sort approach
        result_sort = rearrange_sort_approach(arr)
        valid_sort = verify_rearrangement(result_sort)

        # Test single pass approach
        arr_copy = arr.copy()
        result_single = rearrange_single_pass(arr_copy)
        valid_single = verify_rearrangement(result_single)

        print(
            f"  Sort Approach O(n log n):   {result_sort} {'✓' if valid_sort else '✗'}"
        )
        print(
            f"  Single Pass O(n):           {result_single} {'✓' if valid_single else '✗'}"
        )

    print("\n" + "=" * 70)
