"""
Minimum Platforms Required (Railway/Bus Station)

Problem Description:
    Given arrival and departure times of all trains/buses that reach a station,
    find the minimum number of platforms required so that no train waits.

Time Complexity: O(n log n)
- Sorting arrival and departure times: O(n log n)
- Linear scan: O(n)

Space Complexity: O(n)
- Arrays for arrival and departure times: O(n)

Example:
    Input: arr = [900, 940, 950, 1100, 1500, 1800]
           dep = [910, 1200, 1120, 1130, 1900, 2000]
    Output: 3
    Explanation: Maximum 3 trains are present at a time:
                 - At 940: trains at 900, 940, 950
                 - Departures at 910 doesn't help as 950 arrives before 940 departs

Approach:
    1. Sort arrival and departure times
    2. Use two pointers to track current trains at platform
    3. If next arrival is before next departure, need new platform
    4. If next departure is before next arrival, free up a platform
"""

from typing import List


def find_min_platforms(arrival: List[int], departure: List[int]) -> int:
    """
    Find minimum number of platforms required.

    Args:
        arrival: List of arrival times (in HHMM format)
        departure: List of departure times (in HHMM format)

    Returns:
        Minimum number of platforms required
    """
    if not arrival or not departure:
        return 0

    n = len(arrival)

    # Sort arrival and departure times
    arrival.sort()
    departure.sort()

    platforms_needed = 0
    max_platforms = 0

    i = j = 0

    while i < n and j < n:
        if arrival[i] <= departure[j]:
            # A new train arrives, need a platform
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:
            # A train departs, free up a platform
            platforms_needed -= 1
            j += 1

    return max_platforms


def find_min_platforms_with_details(arrival: List[int], departure: List[int]) -> dict:
    """
    Find minimum platforms with additional details.

    Args:
        arrival: List of arrival times
        departure: List of departure times

    Returns:
        Dictionary with min_platforms and peak_time
    """
    if not arrival or not departure:
        return {"min_platforms": 0, "peak_time": None}

    n = len(arrival)
    arrival.sort()
    departure.sort()

    platforms_needed = 0
    max_platforms = 0
    peak_time = arrival[0]

    i = j = 0

    while i < n and j < n:
        if arrival[i] <= departure[j]:
            platforms_needed += 1
            if platforms_needed > max_platforms:
                max_platforms = platforms_needed
                peak_time = arrival[i]
            i += 1
        else:
            platforms_needed -= 1
            j += 1

    return {"min_platforms": max_platforms, "peak_time": peak_time}


def find_min_platforms_events(arrival: List[int], departure: List[int]) -> int:
    """
    Alternative implementation using event-based approach.

    Args:
        arrival: List of arrival times
        departure: List of departure times

    Returns:
        Minimum number of platforms required
    """
    if not arrival or not departure:
        return 0

    events = []

    # Create events: (time, type) where type 0 is arrival, 1 is departure
    for time in arrival:
        events.append((time, 0))
    for time in departure:
        events.append((time, 1))

    # Sort by time, but departures come before arrivals at same time
    events.sort(key=lambda x: (x[0], x[1]))

    platforms_needed = 0
    max_platforms = 0

    for time, event_type in events:
        if event_type == 0:  # Arrival
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
        else:  # Departure
            platforms_needed -= 1

    return max_platforms


# Test cases
def test_find_min_platforms():
    """Test cases for find_min_platforms function."""
    # Test case 1: Basic example
    arr1 = [900, 940, 950, 1100, 1500, 1800]
    dep1 = [910, 1200, 1120, 1130, 1900, 2000]
    result1 = find_min_platforms(arr1.copy(), dep1.copy())
    assert result1 == 3, f"Test 1 failed: {result1}"

    # Test case 2: All trains arrive at same time
    arr2 = [900, 900, 900, 900]
    dep2 = [910, 920, 930, 940]
    result2 = find_min_platforms(arr2.copy(), dep2.copy())
    assert result2 == 4, f"Test 2 failed: {result2}"

    # Test case 3: No overlap
    arr3 = [900, 1000, 1100, 1200]
    dep3 = [930, 1030, 1130, 1230]
    result3 = find_min_platforms(arr3.copy(), dep3.copy())
    assert result3 == 1, f"Test 3 failed: {result3}"

    # Test case 4: Complete overlap
    arr4 = [900, 905, 910, 915]
    dep4 = [1000, 1005, 1010, 1015]
    result4 = find_min_platforms(arr4.copy(), dep4.copy())
    assert result4 == 4, f"Test 4 failed: {result4}"

    # Test case 5: Empty arrays
    arr5 = []
    dep5 = []
    result5 = find_min_platforms(arr5, dep5)
    assert result5 == 0, f"Test 5 failed: {result5}"

    # Test case 6: Single train
    arr6 = [900]
    dep6 = [1000]
    result6 = find_min_platforms(arr6.copy(), dep6.copy())
    assert result6 == 1, f"Test 6 failed: {result6}"

    # Test case 7: Compare implementations
    arr7 = [900, 940, 950, 1100, 1500, 1800, 1850]
    dep7 = [910, 1200, 1120, 1130, 1900, 2000, 1950]
    result7a = find_min_platforms(arr7.copy(), dep7.copy())
    result7b = find_min_platforms_events(arr7.copy(), dep7.copy())
    assert result7a == result7b, f"Test 7 failed: {result7a} != {result7b}"

    # Test case 8: Same arrival and departure
    arr8 = [900, 910, 920]
    dep8 = [910, 920, 930]
    result8 = find_min_platforms(arr8.copy(), dep8.copy())
    assert result8 == 2, f"Test 8 failed: {result8}"

    print("All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    test_find_min_platforms()

    # Example usage
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]
    print(f"Arrival times: {arrival}")
    print(f"Departure times: {departure}")
    print(f"Minimum platforms needed: {find_min_platforms(arrival, departure)}")

    details = find_min_platforms_with_details(arrival, departure)
    print(
        f"Peak time: {details['peak_time']} with {details['min_platforms']} platforms"
    )
