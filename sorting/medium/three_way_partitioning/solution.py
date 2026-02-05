"""
Three Way Partitioning of an Array Around a Given Range

Problem Description:
    Given an array and a range [low, high], partition the array such that:
    1. All elements smaller than 'low' come first
    2. All elements in range [low, high] come next
    3. All elements greater than 'high' appear in the end

Time Complexity: O(n)
- Single pass through array: O(n)

Space Complexity: O(1)
- In-place partitioning
- Only using a few pointers

Example:
    Input: arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 9, 10], low = 14, high = 20
    Output: [1, 5, 4, 2, 9, 10, 14, 20, 20, 54, 87]
    Explanation: Elements < 14: [1, 5, 4, 2, 9, 10]
                 Elements in [14, 20]: [14, 20, 20]
                 Elements > 20: [54, 87]

Approach:
    1. Use three pointers: low, mid, high (similar to Dutch National Flag)
    2. low pointer: tracks boundary of elements < given low
    3. mid pointer: current element being examined
    4. high pointer: tracks boundary of elements > given high
    5. Swap elements to their correct regions
"""

from typing import List


def three_way_partition(arr: List[int], low_val: int, high_val: int) -> List[int]:
    """
    Partition array into three parts around [low_val, high_val].

    Args:
        arr: List of integers
        low_val: Lower bound of range
        high_val: Upper bound of range

    Returns:
        Partitioned array
    """
    if not arr or low_val > high_val:
        return arr

    n = len(arr)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if arr[mid] < low_val:
            # Element belongs to first region (smaller than low)
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] > high_val:
            # Element belongs to third region (greater than high)
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            # Don't increment mid, need to check swapped element
        else:
            # Element belongs to middle region (within range)
            mid += 1

    return arr


def three_way_partition_verbose(arr: List[int], low_val: int, high_val: int) -> dict:
    """
    Partition array with detailed output.

    Args:
        arr: List of integers
        low_val: Lower bound
        high_val: Upper bound

    Returns:
        Dictionary with result and partition info
    """
    if not arr or low_val > high_val:
        return {"result": arr, "less": [], "in_range": [], "greater": []}

    result = three_way_partition(arr.copy(), low_val, high_val)

    return {
        "result": result,
        "less": [x for x in result if x < low_val],
        "in_range": [x for x in result if low_val <= x <= high_val],
        "greater": [x for x in result if x > high_val],
    }


def verify_partition(arr: List[int], low_val: int, high_val: int) -> bool:
    """
    Verify if array is correctly partitioned.

    Args:
        arr: List to verify
        low_val: Lower bound
        high_val: Upper bound

    Returns:
        True if correctly partitioned
    """
    seen_less = True
    seen_range = False
    seen_greater = False

    for num in arr:
        if num < low_val:
            if seen_range or seen_greater:
                return False
        elif low_val <= num <= high_val:
            if seen_greater:
                return False
            seen_range = True
            seen_less = False
        else:  # num > high_val
            seen_greater = True
            seen_less = False
            seen_range = True

    return True


# Test cases
def test_three_way_partition():
    """Test cases for three_way_partition function."""
    # Test case 1: Basic example
    arr1 = [1, 14, 5, 20, 4, 2, 54, 20, 87, 9, 10]
    low1, high1 = 14, 20
    result1 = three_way_partition(arr1.copy(), low1, high1)
    assert verify_partition(result1, low1, high1), f"Test 1 verification failed"

    # Test case 2: All elements less than low
    arr2 = [1, 2, 3, 4, 5]
    result2 = three_way_partition(arr2.copy(), 10, 20)
    assert verify_partition(result2, 10, 20), f"Test 2 verification failed"

    # Test case 3: All elements greater than high
    arr3 = [50, 60, 70, 80]
    result3 = three_way_partition(arr3.copy(), 10, 20)
    assert verify_partition(result3, 10, 20), f"Test 3 verification failed"

    # Test case 4: All elements in range
    arr4 = [10, 15, 12, 18, 20]
    result4 = three_way_partition(arr4.copy(), 10, 20)
    assert verify_partition(result4, 10, 20), f"Test 4 verification failed"

    # Test case 5: Empty array
    arr5 = []
    result5 = three_way_partition(arr5, 5, 10)
    assert result5 == [], f"Test 5 failed"

    # Test case 6: Single element
    arr6 = [5]
    result6 = three_way_partition(arr6.copy(), 1, 10)
    assert verify_partition(result6, 1, 10), f"Test 6 verification failed"

    # Test case 7: Two elements
    arr7 = [1, 100]
    result7 = three_way_partition(arr7.copy(), 10, 50)
    assert result7 == [1, 100], f"Test 7 failed: {result7}"

    # Test case 8: Duplicate elements
    arr8 = [5, 5, 5, 10, 10, 15, 20, 20, 25]
    result8 = three_way_partition(arr8.copy(), 10, 20)
    assert verify_partition(result8, 10, 20), f"Test 8 verification failed"

    # Test case 9: Negative numbers
    arr9 = [-10, -5, 0, 5, 10, 15, 20]
    result9 = three_way_partition(arr9.copy(), 0, 10)
    assert verify_partition(result9, 0, 10), f"Test 9 verification failed"

    print("All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    test_three_way_partition()

    # Example usage
    arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 9, 10]
    low, high = 14, 20
    result = three_way_partition_verbose(arr.copy(), low, high)
    print(f"Original: {arr}")
    print(f"Range: [{low}, {high}]")
    print(f"Result: {result['result']}")
    print(f"Elements < {low}: {result['less']}")
    print(f"Elements in range: {result['in_range']}")
    print(f"Elements > {high}: {result['greater']}")
