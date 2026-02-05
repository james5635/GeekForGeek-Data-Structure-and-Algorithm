"""
Check for Duplicates Within K Distance

Problem: Given an unsorted array that may contain duplicates, check if the array
contains any duplicate elements within a distance of k (i.e., if there are two
identical elements at indices i and j where |i - j| <= k).

Example:
    Input: arr[] = {1, 2, 3, 4, 1, 2, 3, 4}, k = 3
    Output: false
    Explanation: All duplicates are more than k distance away.

    Input: arr[] = {1, 2, 3, 1, 4, 5}, k = 3
    Output: true
    Explanation: Element 1 repeats at index 0 and index 3 (distance = 3 <= k)

Approach:
    Use a hash set to keep track of elements in the current window of size k.
    Slide the window through the array and check for duplicates.

Time Complexity: O(n) where n is the size of the array
Space Complexity: O(k) for maintaining the window of size k
"""


def check_duplicates_within_k(arr, k):
    """
    Check if there are any duplicate elements within k distance.

    Args:
        arr: List of integers
        k: Maximum allowed distance between duplicates

    Returns:
        bool: True if duplicates exist within k distance, False otherwise
    """
    if not arr or k <= 0:
        return False

    # Set to store elements in current window of size k
    window = set()

    for i, num in enumerate(arr):
        # If element already in window, duplicate found within k distance
        if num in window:
            return True

        # Add current element to window
        window.add(num)

        # Remove element that's now outside the window (distance > k)
        if i >= k:
            window.remove(arr[i - k])

    return False


def check_duplicates_within_k_with_indices(arr, k):
    """
    Find all duplicate pairs within k distance with their indices.

    Args:
        arr: List of integers
        k: Maximum allowed distance between duplicates

    Returns:
        list: List of tuples (element, index1, index2, distance)
    """
    if not arr or k <= 0:
        return []

    # Dictionary to store element and its recent index
    element_indices = {}
    duplicates = []

    for i, num in enumerate(arr):
        if num in element_indices:
            # Check all previous occurrences within k distance
            for prev_idx in element_indices[num]:
                distance = i - prev_idx
                if distance <= k:
                    duplicates.append((num, prev_idx, i, distance))

        # Add current index to the list
        if num not in element_indices:
            element_indices[num] = []
        element_indices[num].append(i)

        # Remove indices that are now outside k distance for future checks
        element_indices[num] = [idx for idx in element_indices[num] if i - idx < k]

    return duplicates


def first_duplicate_within_k(arr, k):
    """
    Find the first pair of duplicates within k distance.

    Args:
        arr: List of integers
        k: Maximum allowed distance between duplicates

    Returns:
        tuple: (element, index1, index2) or None if no duplicate found
    """
    if not arr or k <= 0:
        return None

    window = {}

    for i, num in enumerate(arr):
        if num in window:
            return (num, window[num], i)

        window[num] = i

        # Remove oldest element when window exceeds size k
        if i >= k:
            oldest_element = arr[i - k]
            if window.get(oldest_element) == i - k:
                del window[oldest_element]

    return None


if __name__ == "__main__":
    # Test Case 1: No duplicates within k distance
    arr = [1, 2, 3, 4, 1, 2, 3, 4]
    k = 3
    print(f"Test 1: {check_duplicates_within_k(arr, k)}")  # Expected: False

    # Test Case 2: Duplicates within k distance
    arr = [1, 2, 3, 1, 4, 5]
    k = 3
    print(f"Test 2: {check_duplicates_within_k(arr, k)}")  # Expected: True

    # Test Case 3: Duplicates exactly at k distance
    arr = [1, 2, 3, 4, 1]
    k = 4
    print(f"Test 3: {check_duplicates_within_k(arr, k)}")  # Expected: True

    # Test Case 4: k = 1 (adjacent duplicates)
    arr = [1, 1, 2, 3]
    k = 1
    print(f"Test 4: {check_duplicates_within_k(arr, k)}")  # Expected: True

    # Test Case 5: No duplicates at all
    arr = [1, 2, 3, 4, 5]
    k = 3
    print(f"Test 5: {check_duplicates_within_k(arr, k)}")  # Expected: False

    # Test Case 6: Empty array
    arr = []
    k = 3
    print(f"Test 6: {check_duplicates_within_k(arr, k)}")  # Expected: False

    # Test Case 7: Single element
    arr = [1]
    k = 3
    print(f"Test 7: {check_duplicates_within_k(arr, k)}")  # Expected: False

    # Test Case 8: Find all duplicates
    arr = [1, 2, 1, 3, 2, 1]
    k = 3
    duplicates = check_duplicates_within_k_with_indices(arr, k)
    print(f"Test 8: {duplicates}")
    # Expected: [(1, 0, 2, 2), (2, 1, 4, 3), (1, 2, 5, 3)]

    # Test Case 9: First duplicate
    arr = [1, 2, 3, 1, 2]
    k = 3
    first_dup = first_duplicate_within_k(arr, k)
    print(f"Test 9: {first_dup}")  # Expected: (1, 0, 3)
