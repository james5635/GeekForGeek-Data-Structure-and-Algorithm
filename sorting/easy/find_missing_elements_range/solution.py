"""
Find Missing Elements of Range

Problem Description:
    Given an array of distinct elements and a range [low, high], find all
    numbers in the range that are not present in the given array.

Algorithm:
    - Approach 1: Hash Set
        1. Add all array elements to a hash set
        2. Iterate through range [low, high]
        3. Check if each number is in the set

    - Approach 2: Boolean Array (for small ranges)
        1. Create boolean array of size (high - low + 1)
        2. Mark presence of elements
        3. Find unmarked positions

Time Complexity: O(n + (high - low + 1))
    - n: number of elements in array
    - (high - low + 1): size of the range
    - Effectively O(n + m) where m is range size

Space Complexity: O(n) or O(m)
    - For hash set or boolean array
"""


def find_missing_elements_hash(arr, low, high):
    """
    Find missing elements using hash set.

    Args:
        arr: List of integers
        low: Lower bound of range
        high: Upper bound of range

    Returns:
        list: Missing elements in the range
    """
    if not arr:
        return list(range(low, high + 1))

    # Create set of array elements
    elements = set(arr)

    # Find missing elements
    missing = []
    for num in range(low, high + 1):
        if num not in elements:
            missing.append(num)

    return missing


def find_missing_elements_boolean(arr, low, high):
    """
    Find missing elements using boolean array.

    Args:
        arr: List of integers
        low: Lower bound of range
        high: Upper bound of range

    Returns:
        list: Missing elements in the range
    """
    if not arr:
        return list(range(low, high + 1))

    # Create boolean array for the range
    range_size = high - low + 1
    present = [False] * range_size

    # Mark present elements
    for num in arr:
        if low <= num <= high:
            present[num - low] = True

    # Find missing elements
    missing = []
    for i in range(range_size):
        if not present[i]:
            missing.append(i + low)

    return missing


def find_missing_elements_sorted(arr, low, high):
    """
    Find missing elements when array is sorted (optimized approach).

    Args:
        arr: Sorted list of integers
        low: Lower bound of range
        high: Upper bound of range

    Returns:
        list: Missing elements in the range
    """
    if not arr:
        return list(range(low, high + 1))

    missing = []
    arr_idx = 0

    for num in range(low, high + 1):
        # Skip elements in array that are less than current number
        while arr_idx < len(arr) and arr[arr_idx] < num:
            arr_idx += 1

        # Check if current number is missing
        if arr_idx >= len(arr) or arr[arr_idx] != num:
            missing.append(num)
        else:
            arr_idx += 1

    return missing


def count_missing_elements(arr, low, high):
    """
    Count number of missing elements in range.

    Args:
        arr: List of integers
        low: Lower bound of range
        high: Upper bound of range

    Returns:
        int: Count of missing elements
    """
    if not arr:
        return high - low + 1

    elements_in_range = sum(1 for x in arr if low <= x <= high)
    return (high - low + 1) - elements_in_range


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr1 = [10, 12, 11, 15]
    low1, high1 = 10, 15
    print(f"Array: {arr1}")
    print(f"Range: [{low1}, {high1}]")
    print(f"Missing (hash): {find_missing_elements_hash(arr1, low1, high1)}")
    print(f"Missing (boolean): {find_missing_elements_boolean(arr1, low1, high1)}")
    print()

    # Test Case 2: Large range
    arr2 = [1, 3, 5, 7]
    low2, high2 = 1, 10
    print(f"Array: {arr2}")
    print(f"Range: [{low2}, {high2}]")
    print(f"Missing: {find_missing_elements_hash(arr2, low2, high2)}")
    print(f"Count: {count_missing_elements(arr2, low2, high2)}")
    print()

    # Test Case 3: No missing elements
    arr3 = [1, 2, 3, 4, 5]
    low3, high3 = 1, 5
    print(f"Array: {arr3}")
    print(f"Range: [{low3}, {high3}]")
    print(f"Missing: {find_missing_elements_hash(arr3, low3, high3)}")
    print()

    # Test Case 4: Empty array
    arr4 = []
    low4, high4 = 5, 10
    print(f"Array: {arr4}")
    print(f"Range: [{low4}, {high4}]")
    print(f"Missing: {find_missing_elements_hash(arr4, low4, high4)}")
    print()

    # Test Case 5: Array elements outside range
    arr5 = [1, 2, 20, 30]
    low5, high5 = 5, 15
    print(f"Array: {arr5}")
    print(f"Range: [{low5}, {high5}]")
    print(f"Missing: {find_missing_elements_hash(arr5, low5, high5)}")
    print()

    # Test Case 6: Single element range
    arr6 = [1, 2, 3, 5]
    low6, high6 = 4, 4
    print(f"Array: {arr6}")
    print(f"Range: [{low6}, {high6}]")
    print(f"Missing: {find_missing_elements_hash(arr6, low6, high6)}")
    print()

    # Test Case 7: Sorted array approach
    arr7 = sorted([1, 3, 5, 7, 9])
    low7, high7 = 1, 10
    print(f"Array (sorted): {arr7}")
    print(f"Range: [{low7}, {high7}]")
    print(
        f"Missing (sorted approach): {find_missing_elements_sorted(arr7, low7, high7)}"
    )
    print()

    # Test Case 8: Negative numbers
    arr8 = [-5, -3, -1, 0, 2]
    low8, high8 = -5, 2
    print(f"Array: {arr8}")
    print(f"Range: [{low8}, {high8}]")
    print(f"Missing: {find_missing_elements_hash(arr8, low8, high8)}")
