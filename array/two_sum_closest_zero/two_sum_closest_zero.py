"""
Two Sum Closest to Zero

Find two elements whose sum is closest to zero.

Approaches:
1. Naive: Check all pairs - O(n²) time, O(1) space
2. Better: Sort + Binary Search - O(n log n) time, O(1) or O(n) space
3. Optimal: Sort + Two Pointer - O(n log n) time, O(1) or O(n) space
"""


def two_sum_closest_zero_naive(arr):
    """
    Naive approach: Check all pairs.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: List of integers

    Returns:
        Tuple of two elements with sum closest to zero
    """
    n = len(arr)
    if n < 2:
        return None

    min_sum = float("inf")
    result = (None, None)

    for i in range(n):
        for j in range(i + 1, n):
            current_sum = arr[i] + arr[j]
            if abs(current_sum) < abs(min_sum):
                min_sum = current_sum
                result = (arr[i], arr[j])

    return result


def two_sum_closest_zero_sort_binary_search(arr):
    """
    Better approach: Sort and use binary search for each element.

    Time Complexity: O(n log n)
    Space Complexity: O(1) or O(n) depending on sort

    Algorithm:
    - Sort the array
    - For each element, binary search for its negative (closest to zero sum)

    Args:
        arr: List of integers

    Returns:
        Tuple of two elements with sum closest to zero
    """
    if len(arr) < 2:
        return None

    sorted_arr = sorted(arr)
    n = len(sorted_arr)

    min_sum = float("inf")
    result = (None, None)

    for i in range(n):
        target = -sorted_arr[i]
        # Binary search for target
        left, right = i + 1, n - 1

        while left <= right:
            mid = (left + right) // 2
            current_sum = sorted_arr[i] + sorted_arr[mid]

            if abs(current_sum) < abs(min_sum):
                min_sum = current_sum
                result = (sorted_arr[i], sorted_arr[mid])

            if sorted_arr[mid] == target:
                return result  # Exact zero sum found
            elif sorted_arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

    return result


def two_sum_closest_zero_two_pointer(arr):
    """
    Optimal approach: Sort and use two pointers.

    Time Complexity: O(n log n)
    Space Complexity: O(1) or O(n) depending on sort

    Algorithm:
    - Sort the array
    - Use two pointers from both ends
    - Track sum closest to zero
    - Move pointers based on sum comparison

    Args:
        arr: List of integers

    Returns:
        Tuple of two elements with sum closest to zero
    """
    if len(arr) < 2:
        return None

    sorted_arr = sorted(arr)
    n = len(sorted_arr)

    left, right = 0, n - 1
    min_sum = float("inf")
    result = (None, None)

    while left < right:
        current_sum = sorted_arr[left] + sorted_arr[right]

        # Update if closer to zero
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            result = (sorted_arr[left], sorted_arr[right])

        # Move pointers
        if current_sum < 0:
            # Need larger sum, move left right
            left += 1
        elif current_sum > 0:
            # Need smaller sum, move right left
            right -= 1
        else:
            # Exact zero found
            break

    return result


def two_sum_closest_zero_with_indices(arr):
    """
    Two pointer approach that returns original indices.

    Args:
        arr: List of integers

    Returns:
        Tuple of ((val1, idx1), (val2, idx2), sum)
    """
    if len(arr) < 2:
        return None

    # Store (value, original_index)
    indexed = [(val, i) for i, val in enumerate(arr)]
    indexed.sort()  # Sort by value

    left, right = 0, len(indexed) - 1
    min_sum = float("inf")
    result = None

    while left < right:
        current_sum = indexed[left][0] + indexed[right][0]

        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            result = (indexed[left], indexed[right], current_sum)

        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1
        else:
            break

    return result


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 60, -10, 70, -80, 85],
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1],
        [-10, -5, 0, 5, 10],
        [5, -5],
        [1, -1, 2, -2],
        [10, 20],
        [-10, -20],
    ]

    print("=" * 70)
    print("Two Sum Closest to Zero")
    print("=" * 70)
    print("\nFind two elements whose sum is closest to zero.\n")

    for i, arr in enumerate(test_cases, 1):
        naive = two_sum_closest_zero_naive(arr)
        sort_bs = two_sum_closest_zero_sort_binary_search(arr)
        sort_tp = two_sum_closest_zero_two_pointer(arr)

        match = naive == sort_tp

        print(f"Test {i}: arr = {arr}")
        if naive and naive[0] is not None:
            current_sum = naive[0] + naive[1]
            print(f"  Naive O(n²):            {naive[0]} + {naive[1]} = {current_sum}")
        if sort_bs and sort_bs[0] is not None:
            current_sum = sort_bs[0] + sort_bs[1]
            print(
                f"  Sort + Binary Search:   {sort_bs[0]} + {sort_bs[1]} = {current_sum}"
            )
        if sort_tp and sort_tp[0] is not None:
            current_sum = sort_tp[0] + sort_tp[1]
            print(
                f"  Two Pointer O(n log n): {sort_tp[0]} + {sort_tp[1]} = {current_sum} {'✓' if match else '✗'}"
            )
        print()

    print("=" * 70)
    print("\nTwo Pointer Approach Explanation:")
    print("  1. Sort the array")
    print("  2. Use two pointers from both ends")
    print("  3. Track sum closest to zero")
    print("  4. If sum < 0, need larger → move left++")
    print("  5. If sum > 0, need smaller → move right--")
    print("  6. If sum = 0, optimal found!")
    print("=" * 70)
