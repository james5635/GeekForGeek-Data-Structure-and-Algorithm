"""
Smallest Difference Triplet
============================

Problem:
    Given three sorted arrays, find a triplet (one element from each array)
    such that the difference between the maximum and minimum element in the triplet
    is minimum.

Approach:
    Use three pointers starting at the beginning of each array.
    Calculate the difference between max and min of current triplet.
    Move the pointer pointing to the smallest element (to potentially reduce difference).
    Keep track of the minimum difference found.

Time Complexity: O(n1 + n2 + n3) where n1, n2, n3 are sizes of the three arrays
Space Complexity: O(1) - only using a constant amount of extra space
"""


def smallest_difference_triplet(arr1, arr2, arr3):
    """
    Find triplet with smallest difference from three sorted arrays.

    Args:
        arr1: First sorted array
        arr2: Second sorted array
        arr3: Third sorted array

    Returns:
        Tuple of three elements forming the triplet with minimum difference
    """
    n1, n2, n3 = len(arr1), len(arr2), len(arr3)

    if n1 == 0 or n2 == 0 or n3 == 0:
        return None

    # Initialize pointers
    i, j, k = 0, 0, 0

    # Track minimum difference and result
    min_diff = float("inf")
    result = None

    while i < n1 and j < n2 and k < n3:
        # Get current elements
        a, b, c = arr1[i], arr2[j], arr3[k]

        # Find min and max of current triplet
        current_min = min(a, b, c)
        current_max = max(a, b, c)
        current_diff = current_max - current_min

        # Update result if current difference is smaller
        if current_diff < min_diff:
            min_diff = current_diff
            result = (a, b, c)

        # If difference is 0, we found the optimal solution
        if min_diff == 0:
            break

        # Move pointer of the array with smallest element
        if current_min == a:
            i += 1
        elif current_min == b:
            j += 1
        else:
            k += 1

    return result


def smallest_difference_triplet_value(arr1, arr2, arr3):
    """
    Return only the minimum difference value.
    """
    triplet = smallest_difference_triplet(arr1, arr2, arr3)
    if triplet is None:
        return None
    return max(triplet) - min(triplet)


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr1 = [1, 4, 10]
    arr2 = [2, 15, 20]
    arr3 = [10, 12]
    result = smallest_difference_triplet(arr1, arr2, arr3)
    print(f"Test 1: {result}")  # Expected: (10, 15, 10) or similar with diff 5

    # Test Case 2: Arrays with close values
    arr1 = [20, 24, 100]
    arr2 = [2, 19, 22, 79, 800]
    arr3 = [10, 12, 23, 24, 119]
    result = smallest_difference_triplet(arr1, arr2, arr3)
    print(f"Test 2: {result}")  # Expected: (24, 22, 23) with diff 2

    # Test Case 3: Same values
    arr1 = [5, 10, 15]
    arr2 = [5, 10, 15]
    arr3 = [5, 10, 15]
    result = smallest_difference_triplet(arr1, arr2, arr3)
    print(f"Test 3: {result}")  # Expected: (5, 5, 5) with diff 0

    # Test Case 4: Empty array
    arr1 = []
    arr2 = [1, 2, 3]
    arr3 = [4, 5, 6]
    result = smallest_difference_triplet(arr1, arr2, arr3)
    print(f"Test 4: {result}")  # Expected: None

    # Test Case 5: Single element arrays
    arr1 = [10]
    arr2 = [15]
    arr3 = [12]
    result = smallest_difference_triplet(arr1, arr2, arr3)
    print(f"Test 5: {result}")  # Expected: (10, 15, 12) with diff 5

    # Test Case 6: Large difference values
    arr1 = [1, 100, 1000]
    arr2 = [2, 101, 1001]
    arr3 = [3, 102, 1002]
    result = smallest_difference_triplet(arr1, arr2, arr3)
    print(f"Test 6: {result}")  # Expected: (100, 101, 102) or (1, 2, 3)
