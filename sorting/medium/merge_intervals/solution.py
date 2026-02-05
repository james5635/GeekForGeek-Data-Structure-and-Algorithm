"""
Merge Intervals

Problem Description:
    Given an array of intervals where each interval is [start, end],
    merge all overlapping intervals and return an array of non-overlapping intervals.

Time Complexity: O(n log n)
- Sorting intervals by start time: O(n log n)
- Merging: O(n)

Space Complexity: O(n)
- Result array: O(n)
- Sorting auxiliary space: O(log n) to O(n)

Example:
    Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    Output: [[1, 6], [8, 10], [15, 18]]
    Explanation: [1, 3] and [2, 6] overlap, merge into [1, 6]

    Input: intervals = [[1, 4], [4, 5]]
    Output: [[1, 5]]
    Explanation: [1, 4] and [4, 5] overlap/touch, merge into [1, 5]

Approach:
    1. Sort intervals by start time
    2. Initialize result with first interval
    3. For each subsequent interval:
       - If it overlaps with last interval in result, merge them
       - Otherwise, add it to result
"""

from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals.

    Args:
        intervals: List of [start, end] intervals

    Returns:
        List of merged non-overlapping intervals
    """
    if not intervals or len(intervals) <= 1:
        return intervals

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        # Check if current interval overlaps with last merged interval
        if current[0] <= last[1]:
            # Merge by extending the end if needed
            last[1] = max(last[1], current[1])
        else:
            # No overlap, add current interval
            merged.append(current)

    return merged


def merge_intervals_alternative(intervals: List[List[int]]) -> List[List[int]]:
    """
    Alternative implementation without modifying input.

    Args:
        intervals: List of [start, end] intervals

    Returns:
        List of merged non-overlapping intervals
    """
    if not intervals or len(intervals) <= 1:
        return intervals

    # Sort intervals by start time
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged = []
    current_start, current_end = sorted_intervals[0]

    for start, end in sorted_intervals[1:]:
        if start <= current_end:
            # Overlapping, merge them
            current_end = max(current_end, end)
        else:
            # No overlap, add current interval and start new
            merged.append([current_start, current_end])
            current_start, current_end = start, end

    # Add the last interval
    merged.append([current_start, current_end])

    return merged


def has_overlap(intervals: List[List[int]]) -> bool:
    """
    Check if any intervals overlap (helper function).

    Args:
        intervals: List of [start, end] intervals

    Returns:
        True if any overlap exists
    """
    if len(intervals) <= 1:
        return False

    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] <= intervals[i - 1][1]:
            return True

    return False


# Test cases
def test_merge_intervals():
    """Test cases for merge_intervals function."""
    # Test case 1: Basic example
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result1 = merge_intervals(intervals1.copy())
    assert result1 == [[1, 6], [8, 10], [15, 18]], f"Test 1 failed: {result1}"

    # Test case 2: Touching intervals
    intervals2 = [[1, 4], [4, 5]]
    result2 = merge_intervals(intervals2.copy())
    assert result2 == [[1, 5]], f"Test 2 failed: {result2}"

    # Test case 3: No overlap
    intervals3 = [[1, 2], [3, 4], [5, 6]]
    result3 = merge_intervals(intervals3.copy())
    assert result3 == [[1, 2], [3, 4], [5, 6]], f"Test 3 failed: {result3}"

    # Test case 4: All overlap
    intervals4 = [[1, 10], [2, 3], [4, 5], [6, 7]]
    result4 = merge_intervals(intervals4.copy())
    assert result4 == [[1, 10]], f"Test 4 failed: {result4}"

    # Test case 5: Empty array
    intervals5 = []
    result5 = merge_intervals(intervals5)
    assert result5 == [], f"Test 5 failed: {result5}"

    # Test case 6: Single interval
    intervals6 = [[1, 5]]
    result6 = merge_intervals(intervals6.copy())
    assert result6 == [[1, 5]], f"Test 6 failed: {result6}"

    # Test case 7: Unsorted input
    intervals7 = [[5, 7], [1, 3], [2, 4], [6, 8]]
    result7 = merge_intervals(intervals7.copy())
    assert result7 == [[1, 4], [5, 8]], f"Test 7 failed: {result7}"

    # Test case 8: Compare implementations
    intervals8 = [[1, 3], [2, 6], [8, 10], [15, 18], [16, 20]]
    result8a = merge_intervals(intervals8.copy())
    result8b = merge_intervals_alternative(intervals8.copy())
    assert result8a == result8b, f"Test 8 failed: implementations differ"

    print("All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    test_merge_intervals()

    # Example usage
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Original intervals: {intervals}")
    print(f"Merged intervals: {merge_intervals(intervals.copy())}")
