"""
Sort by Set Bits Count

Problem Description:
    Given an integer array, sort the array according to the count of set bits
    (1s in binary representation) in ascending order. If two elements have the
    same set bit count, they should maintain their relative order (stable sort).

Algorithm:
    - Count set bits for each number using Brian Kernighan's algorithm
    - Use counting sort or stable sort based on set bit count
    - Brian Kernighan's algorithm: repeatedly clear the rightmost set bit

Time Complexity: O(n log n) or O(n * log(max_value))
    - Sorting: O(n log n)
    - Counting set bits: O(log(max_value)) per number

Space Complexity: O(n)
    - For storing count information or during sorting
"""


def count_set_bits(n):
    """
    Count number of set bits in a number using Brian Kernighan's algorithm.

    Args:
        n: Integer

    Returns:
        int: Count of set bits
    """
    count = 0
    while n:
        n &= n - 1  # Clear the rightmost set bit
        count += 1
    return count


def sort_by_set_bits_builtin(arr):
    """
    Sort array by set bit count using Python's stable sort.

    Args:
        arr: List of integers

    Returns:
        list: Sorted array
    """
    return sorted(arr, key=count_set_bits)


def sort_by_set_bits_counting(arr):
    """
    Sort array by set bit count using counting sort approach.

    Args:
        arr: List of integers

    Returns:
        list: Sorted array
    """
    if not arr:
        return arr

    # Group numbers by their set bit count
    # Max set bits for 32-bit integer is 32
    buckets = [[] for _ in range(33)]

    for num in arr:
        bits = count_set_bits(num)
        buckets[bits].append(num)

    # Concatenate all buckets
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


def sort_by_set_bits_descending(arr):
    """
    Sort array by set bit count in descending order.

    Args:
        arr: List of integers

    Returns:
        list: Sorted array (descending by set bits)
    """
    return sorted(arr, key=count_set_bits, reverse=True)


def sort_by_set_bits_then_value(arr):
    """
    Sort by set bits count, then by value for same count.

    Args:
        arr: List of integers

    Returns:
        list: Sorted array
    """
    return sorted(arr, key=lambda x: (count_set_bits(x), x))


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr1 = [5, 2, 3, 9, 4, 6, 7, 15, 32]
    print(f"Original: {arr1}")
    print(f"Binary representations:")
    for num in arr1:
        print(f"  {num}: {bin(num)} (bits: {count_set_bits(num)})")
    print(f"Sorted by set bits: {sort_by_set_bits_builtin(arr1.copy())}")
    print()

    # Test Case 2: Using counting sort approach
    arr2 = [1, 2, 3, 4, 5, 6]
    print(f"Original: {arr2}")
    print(f"Sorted (counting): {sort_by_set_bits_counting(arr2.copy())}")
    print()

    # Test Case 3: Descending order
    arr3 = [5, 2, 3, 9, 4, 6, 7, 15]
    print(f"Original: {arr3}")
    print(f"Sorted (descending): {sort_by_set_bits_descending(arr3.copy())}")
    print()

    # Test Case 4: Same set bits count
    arr4 = [3, 5, 6, 9, 10, 12]  # All have 2 set bits
    print(f"Original: {arr4}")
    print(f"Sorted: {sort_by_set_bits_builtin(arr4.copy())}")
    print(f"Same relative order maintained: {sort_by_set_bits_counting(arr4.copy())}")
    print()

    # Test Case 5: Empty array
    arr5 = []
    print(f"Original: {arr5}")
    print(f"Sorted: {sort_by_set_bits_builtin(arr5.copy())}")
    print()

    # Test Case 6: Single element
    arr6 = [7]
    print(f"Original: {arr6}")
    print(f"Sorted: {sort_by_set_bits_builtin(arr6.copy())}")
    print()

    # Test Case 7: All zeros
    arr7 = [0, 0, 0]
    print(f"Original: {arr7}")
    print(f"Sorted: {sort_by_set_bits_builtin(arr7.copy())}")
    print()

    # Test Case 8: Sort by set bits then value
    arr8 = [3, 5, 6, 9, 10, 12]
    print(f"Original: {arr8}")
    print(f"Sorted (bits then value): {sort_by_set_bits_then_value(arr8.copy())}")
    print()

    # Test Case 9: Large numbers
    arr9 = [255, 128, 127, 64, 63, 32]
    print(f"Original: {arr9}")
    print(f"Binary:")
    for num in arr9:
        print(f"  {num}: {bin(num)} ({count_set_bits(num)} bits)")
    print(f"Sorted: {sort_by_set_bits_builtin(arr9.copy())}")
