"""
Meeting Rooms - Check if a person can attend all meetings

Problem Description:
    Given a 2D array arr[][] where arr[i][0] represents the starting time
    and arr[i][1] represents the ending time of the ith meeting.
    Determine whether it is possible for a person to attend all meetings
    without any overlaps. A person can attend only one meeting at any given time.

    Note: A person can attend a meeting if its starting time is the same as
    the previous meeting's ending time.

Example:
    Input: arr = [[2, 4], [1, 2], [7, 8], [5, 6], [6, 8]]
    Output: False
    Explanation: The third and fifth meetings overlap (6-8 and 6-8)

Time Complexity: O(n log n) - Due to sorting
Space Complexity: O(1) - Constant extra space (if sorting in-place)
"""

from typing import List


def can_attend_all_meetings(arr: List[List[int]]) -> bool:
    """
    Check if a person can attend all meetings without overlap.

    Args:
        arr: List of [start_time, end_time] pairs representing meetings

    Returns:
        True if all meetings can be attended, False otherwise
    """
    if not arr or len(arr) <= 1:
        return True

    # Sort meetings by start time
    arr.sort(key=lambda x: x[0])

    # Check for overlaps
    for i in range(len(arr) - 1):
        # If current meeting ends after next meeting starts, there's overlap
        if arr[i][1] > arr[i + 1][0]:
            return False

    return True


if __name__ == "__main__":
    # Test Case 1: Overlapping meetings
    meetings = [[2, 4], [1, 2], [7, 8], [5, 6], [6, 8]]
    print("Test 1:")
    print(f"Meetings: {meetings}")
    result = can_attend_all_meetings(meetings)
    print(f"Can attend all: {result}")
    print()

    # Test Case 2: Non-overlapping meetings
    meetings = [[1, 4], [10, 15], [7, 10]]
    print("Test 2:")
    print(f"Meetings: {meetings}")
    result = can_attend_all_meetings(meetings)
    print(f"Can attend all: {result}")
    print()

    # Test Case 3: Adjacent meetings (should be allowed)
    meetings = [[1, 5], [5, 10], [10, 15]]
    print("Test 3:")
    print(f"Meetings: {meetings}")
    result = can_attend_all_meetings(meetings)
    print(f"Can attend all: {result}")
    print()

    # Test Case 4: Single meeting
    meetings = [[1, 5]]
    print("Test 4:")
    print(f"Meetings: {meetings}")
    result = can_attend_all_meetings(meetings)
    print(f"Can attend all: {result}")
    print()

    # Test Case 5: Empty meetings
    meetings = []
    print("Test 5:")
    print(f"Meetings: {meetings}")
    result = can_attend_all_meetings(meetings)
    print(f"Can attend all: {result}")
    print()

    # Test Case 6: Complete overlap
    meetings = [[1, 10], [2, 3], [4, 5]]
    print("Test 6:")
    print(f"Meetings: {meetings}")
    result = can_attend_all_meetings(meetings)
    print(f"Can attend all: {result}")
    print()

    # Test Case 7: Same start time
    meetings = [[1, 5], [1, 3], [4, 6]]
    print("Test 7:")
    print(f"Meetings: {meetings}")
    result = can_attend_all_meetings(meetings)
    print(f"Can attend all: {result}")
