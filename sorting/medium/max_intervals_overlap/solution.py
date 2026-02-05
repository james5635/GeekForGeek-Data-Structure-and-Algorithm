"""
Maximum Intervals Overlap Point

Problem Description:
    Given a set of intervals, find the point where the maximum number of
    intervals overlap.

Time Complexity: O(n log n)
- Sorting all start and end points: O(n log n)
- Linear scan: O(n)

Space Complexity: O(n)
- Arrays for start and end times: O(n)

Example:
    Input: intervals = [[1, 5], [2, 6], [3, 7], [4, 8]]
    Output: 4 (or any point between 4 and 5)
    Explanation: At time 4, all 4 intervals are active

    Input: intervals = [[1, 4], [2, 5], [9, 12], [5, 9], [5, 12]]
    Output: 5
    Explanation: At time 5, 4 intervals are active

Approach:
    1. Extract all start times and end times separately
    2. Sort both arrays
    3. Use two pointers to track active intervals
    4. When we encounter a start time, increment count
    5. When we encounter an end time, decrement count
    6. Track the maximum count and corresponding time
"""

from typing import List


def find_max_overlap(intervals: List[List[int]]) -> int:
    """
    Find the point where maximum intervals overlap.

    Args:
        intervals: List of [start, end] intervals

    Returns:
        The point where maximum intervals overlap
    """
    if not intervals:
        return None

    if len(intervals) == 1:
        return intervals[0][0]

    # Extract start and end times
    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])

    max_overlap = 0
    current_overlap = 0
    max_time = starts[0]

    i, j = 0, 0
    n = len(intervals)

    while i < n and j < n:
        if starts[i] <= ends[j]:
            # A new interval starts
            current_overlap += 1

            # Update max if needed
            if current_overlap > max_overlap:
                max_overlap = current_overlap
                max_time = starts[i]

            i += 1
        else:
            # An interval ends
            current_overlap -= 1
            j += 1

    return max_time


def find_max_overlap_count(intervals: List[List[int]]) -> tuple:
    """
    Find both the point and the count of maximum overlap.

    Args:
        intervals: List of [start, end] intervals

    Returns:
        Tuple of (point, max_count) where maximum intervals overlap
    """
    if not intervals:
        return None, 0

    if len(intervals) == 1:
        return intervals[0][0], 1

    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])

    max_overlap = 0
    current_overlap = 0
    max_time = starts[0]

    i, j = 0, 0
    n = len(intervals)

    while i < n and j < n:
        if starts[i] <= ends[j]:
            current_overlap += 1
            if current_overlap > max_overlap:
                max_overlap = current_overlap
                max_time = starts[i]
            i += 1
        else:
            current_overlap -= 1
            j += 1

    return max_time, max_overlap


def find_all_max_overlap_points(intervals: List[List[int]]) -> List[int]:
    """
    Find all points where maximum overlap occurs.

    Args:
        intervals: List of [start, end] intervals

    Returns:
        List of all points with maximum overlap
    """
    if not intervals:
        return []

    if len(intervals) == 1:
        return [intervals[0][0]]

    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])

    max_overlap = 0
    current_overlap = 0
    max_times = []

    i, j = 0, 0
    n = len(intervals)

    while i < n and j < n:
        if starts[i] <= ends[j]:
            current_overlap += 1
            if current_overlap > max_overlap:
                max_overlap = current_overlap
                max_times = [starts[i]]
            elif current_overlap == max_overlap:
                max_times.append(starts[i])
            i += 1
        else:
            current_overlap -= 1
            j += 1

    return max_times


# Test cases
def test_find_max_overlap():
    """Test cases for find_max_overlap function."""
    # Test case 1: Basic example
    intervals1 = [[1, 5], [2, 6], [3, 7], [4, 8]]
    result1 = find_max_overlap(intervals1)
    assert result1 == 4, f"Test 1 failed: {result1}"

    # Test case 2: Another example
    intervals2 = [[1, 4], [2, 5], [9, 12], [5, 9], [5, 12]]
    result2 = find_max_overlap(intervals2)
    assert result2 == 5, f"Test 2 failed: {result2}"

    # Test case 3: No overlap
    intervals3 = [[1, 2], [3, 4], [5, 6]]
    result3 = find_max_overlap(intervals3)
    assert result3 == 1, f"Test 3 failed: {result3}"

    # Test case 4: All overlap
    intervals4 = [[1, 10], [2, 9], [3, 8], [4, 7]]
    result4 = find_max_overlap(intervals4)
    assert result4 == 4, f"Test 4 failed: {result4}"

    # Test case 5: Empty array
    intervals5 = []
    result5 = find_max_overlap(intervals5)
    assert result5 is None, f"Test 5 failed: {result5}"

    # Test case 6: Single interval
    intervals6 = [[1, 5]]
    result6 = find_max_overlap(intervals6)
    assert result6 == 1, f"Test 6 failed: {result6}"

    # Test case 7: Same start time
    intervals7 = [[1, 3], [1, 4], [1, 5]]
    result7, count7 = find_max_overlap_count(intervals7)
    assert result7 == 1, f"Test 7 failed: {result7}"
    assert count7 == 3, f"Test 7 count failed: {count7}"

    # Test case 8: Multiple max points
    intervals8 = [[1, 3], [2, 4], [5, 7], [6, 8]]
    result8 = find_all_max_overlap_points(intervals8)
    assert 2 in result8 and 6 in result8, f"Test 8 failed: {result8}"

    print("All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    test_find_max_overlap()

    # Example usage
    intervals = [[1, 4], [2, 5], [9, 12], [5, 9], [5, 12]]
    print(f"Intervals: {intervals}")
    time, count = find_max_overlap_count(intervals)
    print(f"Maximum overlap at time {time} with {count} intervals")
