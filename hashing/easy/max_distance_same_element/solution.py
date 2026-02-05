"""
Maximum Distance Between Two Occurrences of Same Element

Problem: Given an array with repeated elements, find the maximum distance
between two occurrences of the same element.

Example:
    Input: arr[] = {3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2}
    Output: 10
    Explanation: Maximum distance for 2 is 11-1 = 10
                 (first occurrence at index 1 and last at index 11)

Approach:
    Use a hash map to store the first occurrence of each element.
    For subsequent occurrences, calculate distance and update max if needed.

Time Complexity: O(n) where n is the size of the array
Space Complexity: O(n) for storing first occurrences
"""


def max_distance(arr):
    """
    Find maximum distance between two occurrences of same element.

    Args:
        arr: List of integers

    Returns:
        int: Maximum distance between two same elements, 0 if no repeats
    """
    if not arr or len(arr) < 2:
        return 0

    # Dictionary to store first occurrence of each element
    first_occurrence = {}
    max_dist = 0

    for i, num in enumerate(arr):
        if num in first_occurrence:
            # Calculate distance from first occurrence
            distance = i - first_occurrence[num]
            max_dist = max(max_dist, distance)
        else:
            # Store first occurrence
            first_occurrence[num] = i

    return max_dist


def max_distance_with_last(arr):
    """
    Alternative approach that also tracks last occurrence.
    Returns both the element and the maximum distance.

    Args:
        arr: List of integers

    Returns:
        tuple: (element_with_max_distance, max_distance)
    """
    if not arr or len(arr) < 2:
        return None, 0

    first_occurrence = {}
    max_dist = 0
    max_element = None

    for i, num in enumerate(arr):
        if num in first_occurrence:
            distance = i - first_occurrence[num]
            if distance > max_dist:
                max_dist = distance
                max_element = num
        else:
            first_occurrence[num] = i

    return max_element, max_dist


def max_distance_all_pairs(arr):
    """
    Find all pairs of elements that have maximum distance.

    Args:
        arr: List of integers

    Returns:
        dict: Dictionary with elements as keys and (first_idx, last_idx, distance) as values
    """
    if not arr:
        return {}

    first_occurrence = {}
    element_distances = {}

    for i, num in enumerate(arr):
        if num in first_occurrence:
            distance = i - first_occurrence[num]
            element_distances[num] = (first_occurrence[num], i, distance)
        else:
            first_occurrence[num] = i

    return element_distances


if __name__ == "__main__":
    # Test Case 1: Standard case
    arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
    print(f"Test 1: {max_distance(arr)}")  # Expected: 10

    # Test Case 2: All unique elements
    arr = [1, 2, 3, 4, 5]
    print(f"Test 2: {max_distance(arr)}")  # Expected: 0

    # Test Case 3: All same elements
    arr = [5, 5, 5, 5, 5]
    print(f"Test 3: {max_distance(arr)}")  # Expected: 4

    # Test Case 4: Two elements with same max distance
    arr = [1, 2, 3, 1, 2, 3]
    print(f"Test 4: {max_distance(arr)}")  # Expected: 3

    # Test Case 5: Empty array
    arr = []
    print(f"Test 5: {max_distance(arr)}")  # Expected: 0

    # Test Case 6: Single element
    arr = [1]
    print(f"Test 6: {max_distance(arr)}")  # Expected: 0

    # Test Case 7: Element with max distance identification
    arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
    element, dist = max_distance_with_last(arr)
    print(
        f"Test 7: Element={element}, Distance={dist}"
    )  # Expected: Element=2, Distance=10

    # Test Case 8: All pairs
    arr = [1, 2, 1, 3, 2]
    pairs = max_distance_all_pairs(arr)
    print(f"Test 8: {pairs}")  # Expected: {1: (0, 2, 2), 2: (1, 4, 3)}
