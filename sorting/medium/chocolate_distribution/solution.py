"""
Chocolate Distribution Problem

Problem Description:
    Given an array of integers where each value represents the number of chocolates
    in a packet. There are m students, and the task is to distribute chocolate packets
    such that:
    1. Each student gets exactly one packet
    2. The difference between the maximum and minimum chocolates given is minimized

Time Complexity: O(n log n)
- Sorting the array: O(n log n)
- Finding minimum difference: O(n)

Space Complexity: O(1) auxiliary
- Sorting may use O(log n) to O(n) space
- Only using a few variables

Example:
    Input: arr = [7, 3, 2, 4, 9, 12, 56], m = 3
    Output: 2
    Explanation: If we distribute packets [2, 3, 4],
                 difference = 4 - 2 = 2 (minimum possible)

    Input: arr = [3, 4, 1, 9, 56, 7, 9, 12], m = 5
    Output: 6
    Explanation: Distribute [3, 4, 7, 9, 9], difference = 9 - 3 = 6

Approach:
    1. Sort the array
    2. Use sliding window of size m to find minimum difference
    3. For each window, calculate difference between max and min
    4. Return the minimum difference found
"""

from typing import List


def find_min_diff(arr: List[int], m: int) -> int:
    """
    Find minimum difference between maximum and minimum chocolates distributed.

    Args:
        arr: List of integers representing chocolate packets
        m: Number of students

    Returns:
        Minimum difference between max and min chocolates

    Raises:
        ValueError: If m > len(arr) or m <= 0
    """
    if not arr or m <= 0:
        raise ValueError("Invalid input: array cannot be empty and m must be positive")

    n = len(arr)

    if m > n:
        raise ValueError(f"Not enough packets for {m} students")

    # Sort the array
    arr.sort()

    min_diff = float("inf")

    # Sliding window of size m
    for i in range(n - m + 1):
        # In sorted array, min is arr[i] and max is arr[i + m - 1]
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)

    return min_diff


def find_min_diff_with_packets(arr: List[int], m: int) -> dict:
    """
    Find minimum difference and the actual packet distribution.

    Args:
        arr: List of integers representing chocolate packets
        m: Number of students

    Returns:
        Dictionary with min_diff and the packets to distribute
    """
    if not arr or m <= 0 or m > len(arr):
        raise ValueError("Invalid input")

    n = len(arr)
    arr.sort()

    min_diff = float("inf")
    best_start = 0

    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
            best_start = i

    return {
        "min_diff": min_diff,
        "packets": arr[best_start : best_start + m],
        "min_chocolates": arr[best_start],
        "max_chocolates": arr[best_start + m - 1],
    }


def find_min_diff_optimized(arr: List[int], m: int) -> int:
    """
    Memory-optimized version that doesn't store indices.

    Args:
        arr: List of integers
        m: Number of students

    Returns:
        Minimum difference
    """
    if m > len(arr) or m <= 0:
        raise ValueError("Invalid input")

    arr.sort()

    # Use list comprehension for concise code
    return min(arr[i + m - 1] - arr[i] for i in range(len(arr) - m + 1))


# Test cases
def test_find_min_diff():
    """Test cases for find_min_diff function."""
    # Test case 1: Basic example
    arr1 = [7, 3, 2, 4, 9, 12, 56]
    m1 = 3
    result1 = find_min_diff(arr1.copy(), m1)
    assert result1 == 2, f"Test 1 failed: {result1}"

    # Test case 2: Another example
    arr2 = [3, 4, 1, 9, 56, 7, 9, 12]
    m2 = 5
    result2 = find_min_diff(arr2.copy(), m2)
    assert result2 == 6, f"Test 2 failed: {result2}"

    # Test case 3: Minimum case
    arr3 = [1, 2]
    m3 = 2
    result3 = find_min_diff(arr3.copy(), m3)
    assert result3 == 1, f"Test 3 failed: {result3}"

    # Test case 4: All same values
    arr4 = [5, 5, 5, 5, 5]
    m4 = 3
    result4 = find_min_diff(arr4.copy(), m4)
    assert result4 == 0, f"Test 4 failed: {result4}"

    # Test case 5: Single student
    arr5 = [7, 3, 2, 4, 9, 12, 56]
    m5 = 1
    result5 = find_min_diff(arr5.copy(), m5)
    assert result5 == 0, f"Test 5 failed: {result5}"

    # Test case 6: Large difference
    arr6 = [1, 100, 200, 300, 400]
    m6 = 2
    result6 = find_min_diff(arr6.copy(), m6)
    # Sorted: [1, 100, 200, 300, 400], windows: [1,100]=99, [100,200]=100, etc.
    assert result6 == 99, f"Test 6 failed: {result6}"

    # Test case 7: Verify with optimized version
    arr7 = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
    m7 = 7
    result7a = find_min_diff(arr7.copy(), m7)
    result7b = find_min_diff_optimized(arr7.copy(), m7)
    assert result7a == result7b, f"Test 7 failed: {result7a} != {result7b}"

    # Test case 8: Invalid input
    try:
        find_min_diff([1, 2], 3)
        assert False, "Test 8 failed: should raise error"
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    test_find_min_diff()

    # Example usage
    arr = [7, 3, 2, 4, 9, 12, 56]
    m = 3
    result = find_min_diff_with_packets(arr.copy(), m)
    print(f"Packets: {arr}")
    print(f"Students: {m}")
    print(f"Minimum difference: {result['min_diff']}")
    print(f"Distribute packets: {result['packets']}")
    print(
        f"Student gets chocolates from {result['min_chocolates']} to {result['max_chocolates']}"
    )
