"""
3Sum Zero - Find Triplets with Sum Equal to Zero
=================================================

Problem:
    Given an array, find all unique triplets (i, j, k) such that
    arr[i] + arr[j] + arr[k] = 0 and i, j, k are distinct.
    This is a special case of the 3Sum problem with target = 0.

Approach:
    Sort the array.
    Fix one element and use two-pointer technique to find pairs that sum to negative of fixed.
    Skip duplicates to ensure unique triplets.

Time Complexity: O(n^2) where n is the array length
Space Complexity: O(1) extra space (excluding output), O(k) for storing k triplets
"""


def three_sum_zero(arr):
    """
    Find all unique triplets with sum equal to zero.

    Args:
        arr: Input array of integers

    Returns:
        List of unique triplets (each as a tuple) that sum to zero
    """
    n = len(arr)
    if n < 3:
        return []

    arr = sorted(arr)
    result = []

    for i in range(n - 2):
        # Skip positive numbers (can't form sum = 0)
        if arr[i] > 0:
            break

        # Skip duplicates
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == 0:
                result.append((arr[i], arr[left], arr[right]))

                # Skip duplicates
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result


def has_three_sum_zero(arr):
    """
    Check if there exists any triplet with sum zero.
    """
    return len(three_sum_zero(arr)) > 0


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr = [-1, 0, 1, 2, -1, -4]
    result = three_sum_zero(arr)
    print(f"Test 1: {result}")  # Expected: [(-1, -1, 2), (-1, 0, 1)]

    # Test Case 2: No triplet
    arr = [1, 2, 3, 4, 5]
    result = three_sum_zero(arr)
    print(f"Test 2: {result}")  # Expected: []

    # Test Case 3: All zeros
    arr = [0, 0, 0, 0]
    result = three_sum_zero(arr)
    print(f"Test 3: {result}")  # Expected: [(0, 0, 0)]

    # Test Case 4: Multiple solutions
    arr = [-2, 0, 1, 1, 2]
    result = three_sum_zero(arr)
    print(f"Test 4: {result}")  # Expected: [(-2, 0, 2), (-2, 1, 1)]

    # Test Case 5: Large numbers
    arr = [-100, -50, 0, 50, 100, 150]
    result = three_sum_zero(arr)
    print(f"Test 5: {result}")  # Expected: [(-100, 0, 100), (-50, 0, 50)]

    # Test Case 6: Two elements only
    arr = [-1, 1]
    result = three_sum_zero(arr)
    print(f"Test 6: {result}")  # Expected: []

    # Test Case 7: Check existence
    arr = [3, -1, -2, 4, 5]
    exists = has_three_sum_zero(arr)
    print(f"Test 7: Has triplet? {exists}")  # Expected: True (-1, -2, 3)
