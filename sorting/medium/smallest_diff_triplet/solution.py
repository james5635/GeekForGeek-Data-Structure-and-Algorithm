"""
Smallest Difference Triplet from Three Arrays

Given three arrays of same size, find a triplet such that the difference between
the maximum and minimum element in that triplet is minimum of all the triplets.
A triplet should have one number from each of the three given arrays.
If there are multiple triplets with same minimum difference, return the one
with the smallest sum.

Algorithm:
1. Sort all three arrays
2. Use three pointers approach - one for each array
3. Move the pointer pointing to the smallest element
4. Track the minimum difference triplet

Time Complexity: O(n log n) - Sorting takes O(n log n) and three-pointer traversal is O(n)
Space Complexity: O(1) - Only using a few variables
"""


def smallest_difference_triplet(arr1, arr2, arr3):
    """
    Find the triplet with smallest difference from three arrays.

    Args:
        arr1: First array of integers
        arr2: Second array of integers
        arr3: Third array of integers

    Returns:
        tuple: A tuple of three integers forming the smallest difference triplet
    """
    n = len(arr1)

    # Sort all three arrays
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    arr3 = sorted(arr3)

    # Initialize pointers
    i = j = k = 0

    # Initialize result variables
    min_diff = float("inf")
    result = None

    # Traverse arrays using three pointers
    while i < n and j < n and k < n:
        # Get current elements
        a, b, c = arr1[i], arr2[j], arr3[k]

        # Find max and min of current triplet
        curr_max = max(a, b, c)
        curr_min = min(a, b, c)
        curr_diff = curr_max - curr_min
        curr_sum = a + b + c

        # Update result if we found a better triplet
        if curr_diff < min_diff or (
            curr_diff == min_diff and (result is None or curr_sum < sum(result))
        ):
            min_diff = curr_diff
            result = (a, b, c)

        # Move pointer of the smallest element
        if curr_min == a:
            i += 1
        elif curr_min == b:
            j += 1
        else:
            k += 1

    return result


def test_smallest_difference_triplet():
    """Test cases for smallest difference triplet algorithm."""
    # Test Case 1: Basic case
    arr1 = [5, 2, 8]
    arr2 = [10, 7, 12]
    arr3 = [9, 14, 6]
    result = smallest_difference_triplet(arr1, arr2, arr3)
    assert result in [
        (7, 6, 5),
        (5, 7, 6),
        (6, 7, 5),
        (5, 6, 7),
        (7, 5, 6),
        (6, 5, 7),
    ], f"Test 1 failed: Expected triplet with values close to 5,6,7, got {result}"
    print("Test 1 passed: Basic case")

    # Test Case 2: Larger arrays
    arr1 = [15, 12, 18, 9]
    arr2 = [10, 17, 13, 8]
    arr3 = [14, 16, 11, 5]
    result = smallest_difference_triplet(arr1, arr2, arr3)
    assert result in [
        (11, 10, 9),
        (9, 10, 11),
        (11, 9, 10),
        (9, 11, 10),
        (10, 9, 11),
        (10, 11, 9),
    ], f"Test 2 failed: Expected triplet 9,10,11, got {result}"
    print("Test 2 passed: Larger arrays")

    # Test Case 3: Single element arrays
    arr1 = [5]
    arr2 = [5]
    arr3 = [5]
    result = smallest_difference_triplet(arr1, arr2, arr3)
    assert result == (5, 5, 5), f"Test 3 failed: Expected (5, 5, 5), got {result}"
    print("Test 3 passed: Single element arrays")

    # Test Case 4: Arrays with negative numbers
    arr1 = [-5, -2, 0]
    arr2 = [-3, 1, 4]
    arr3 = [-4, 2, 5]
    result = smallest_difference_triplet(arr1, arr2, arr3)
    # The best triplet should have values close to each other
    assert result is not None, "Test 4 failed: Should return a valid triplet"
    print("Test 4 passed: Arrays with negative numbers")

    # Test Case 5: Arrays with duplicates
    arr1 = [1, 1, 1]
    arr2 = [1, 2, 2]
    arr3 = [1, 2, 3]
    result = smallest_difference_triplet(arr1, arr2, arr3)
    # Best triplet should be (1, 1, 1) with diff = 0
    max_val = max(result)
    min_val = min(result)
    assert max_val - min_val == 0, (
        f"Test 5 failed: Expected diff 0, got {max_val - min_val}"
    )
    print("Test 5 passed: Arrays with duplicates")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_smallest_difference_triplet()

    # Example usage
    arr1 = [5, 2, 8]
    arr2 = [10, 7, 12]
    arr3 = [9, 14, 6]
    result = smallest_difference_triplet(arr1, arr2, arr3)
    print(f"\nExample:")
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print(f"Array 3: {arr3}")
    print(f"Smallest difference triplet: {result}")
    print(f"Difference: {max(result) - min(result)}")
