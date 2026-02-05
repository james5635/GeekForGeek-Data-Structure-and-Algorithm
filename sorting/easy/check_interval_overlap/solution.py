"""
Check Interval Overlap

Problem Description:
    Given a set of time intervals in any order, merge all overlapping intervals
    into one and output the result which should have only mutually exclusive
    intervals. Also, check if any two intervals overlap.

Algorithm:
    - Sort intervals by start time
    - Initialize result with first interval
    - For each subsequent interval:
        - If it overlaps with last interval in result, merge them
        - Otherwise, add it to result
    - Two intervals [a, b] and [c, d] overlap if: c <= b

Time Complexity: O(n log n)
    - Sorting intervals: O(n log n)
    - Merging: O(n)

Space Complexity: O(n)
    - For storing merged intervals
"""


def merge_overlapping_intervals(intervals):
    """
    Merge all overlapping intervals.

    Args:
        intervals: List of [start, end] intervals

    Returns:
        list: List of merged intervals
    """
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        # Check if current overlaps with last
        if current[0] <= last[1]:
            # Merge: extend the end time if needed
            last[1] = max(last[1], current[1])
        else:
            # No overlap, add current to result
            merged.append(current)

    return merged


def has_overlapping_intervals(intervals):
    """
    Check if any two intervals overlap.

    Args:
        intervals: List of [start, end] intervals

    Returns:
        bool: True if any overlap exists
    """
    if not intervals or len(intervals) < 2:
        return False

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] <= intervals[i - 1][1]:
            return True

    return False


def count_overlapping_pairs(intervals):
    """
    Count number of overlapping pairs.

    Args:
        intervals: List of [start, end] intervals

    Returns:
        int: Number of overlapping pairs
    """
    if not intervals or len(intervals) < 2:
        return 0

    intervals.sort(key=lambda x: x[0])
    count = 0

    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[j][0] <= intervals[i][1]:
                count += 1
            else:
                break  # No need to check further for this i

    return count


def insert_interval(intervals, new_interval):
    """
    Insert a new interval into existing intervals, merging if necessary.

    Args:
        intervals: List of [start, end] intervals
        new_interval: [start, end] interval to insert

    Returns:
        list: Updated list of intervals
    """
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


if __name__ == "__main__":
    # Test Case 1: Overlapping intervals
    intervals1 = [[1, 3], [2, 4], [5, 7], [6, 8]]
    print(f"Intervals: {intervals1}")
    print(f"Has overlap: {has_overlapping_intervals(intervals1.copy())}")
    print(f"Merged: {merge_overlapping_intervals(intervals1.copy())}")
    print(f"Overlapping pairs: {count_overlapping_pairs(intervals1.copy())}")
    print()

    # Test Case 2: Non-overlapping intervals
    intervals2 = [[1, 3], [4, 6], [7, 9]]
    print(f"Intervals: {intervals2}")
    print(f"Has overlap: {has_overlapping_intervals(intervals2.copy())}")
    print(f"Merged: {merge_overlapping_intervals(intervals2.copy())}")
    print()

    # Test Case 3: Nested intervals
    intervals3 = [[1, 10], [2, 3], [4, 5], [6, 7]]
    print(f"Intervals: {intervals3}")
    print(f"Has overlap: {has_overlapping_intervals(intervals3.copy())}")
    print(f"Merged: {merge_overlapping_intervals(intervals3.copy())}")
    print()

    # Test Case 4: Single interval
    intervals4 = [[1, 5]]
    print(f"Intervals: {intervals4}")
    print(f"Has overlap: {has_overlapping_intervals(intervals4.copy())}")
    print()

    # Test Case 5: Empty intervals
    intervals5 = []
    print(f"Intervals: {intervals5}")
    print(f"Has overlap: {has_overlapping_intervals(intervals5.copy())}")
    print()

    # Test Case 6: Insert interval
    intervals6 = [[1, 3], [6, 9]]
    new_interval = [2, 5]
    print(f"Original: {intervals6}")
    print(f"Insert: {new_interval}")
    print(f"Result: {insert_interval(intervals6, new_interval)}")
    print()

    # Test Case 7: Multiple overlapping
    intervals7 = [[1, 4], [2, 5], [3, 6], [7, 8], [8, 10]]
    print(f"Intervals: {intervals7}")
    print(f"Has overlap: {has_overlapping_intervals(intervals7.copy())}")
    print(f"Merged: {merge_overlapping_intervals(intervals7.copy())}")
    print()

    # Test Case 8: Touching intervals
    intervals8 = [[1, 3], [3, 5], [5, 7]]
    print(f"Intervals (touching): {intervals8}")
    print(f"Has overlap: {has_overlapping_intervals(intervals8.copy())}")
    print(f"Merged: {merge_overlapping_intervals(intervals8.copy())}")
