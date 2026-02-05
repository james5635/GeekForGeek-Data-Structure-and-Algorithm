"""
Unique Triplets with Sum Equal to Given Value
==============================================

Problem:
    Given an array and a target sum, find all unique triplets (i, j, k)
    such that arr[i] + arr[j] + arr[k] = target and i, j, k are distinct.
    Each triplet should be unique (no duplicates).

Approach:
    Sort the array first.
    For each element, use two-pointer technique to find pairs that sum to target - current.
    Skip duplicates to ensure unique triplets.

Time Complexity: O(n^2) where n is the array length
Space Complexity: O(1) extra space (excluding output), O(k) for storing k triplets
"""


def find_unique_triplets_sum(arr, target):
    """
    Find all unique triplets with sum equal to target.

    Args:
        arr: Input array of integers
        target: Target sum value

    Returns:
        List of unique triplets (each as a tuple) that sum to target
    """
    n = len(arr)
    if n < 3:
        return []

    arr = sorted(arr)
    result = []

    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # Two pointers
        left, right = i + 1, n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                result.append((arr[i], arr[left], arr[right]))

                # Skip duplicates for second element
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                # Skip duplicates for third element
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result


def count_unique_triplets(arr, target):
    """
    Count the number of unique triplets with given sum.
    """
    return len(find_unique_triplets_sum(arr, target))


if __name__ == "__main__":
    # Test Case 1: Basic case with multiple triplets
    arr = [1, 2, 3, 4, 5, 6, 7]
    target = 12
    result = find_unique_triplets_sum(arr, target)
    print(
        f"Test 1: {result}"
    )  # Expected: [(1, 4, 7), (1, 5, 6), (2, 3, 7), (2, 4, 6), (3, 4, 5)]

    # Test Case 2: Array with duplicates
    arr = [1, 1, 2, 2, 3, 3, 4, 4]
    target = 6
    result = find_unique_triplets_sum(arr, target)
    print(f"Test 2: {result}")  # Expected: [(1, 1, 4), (1, 2, 3)]

    # Test Case 3: No triplet exists
    arr = [1, 2, 3]
    target = 100
    result = find_unique_triplets_sum(arr, target)
    print(f"Test 3: {result}")  # Expected: []

    # Test Case 4: Single triplet
    arr = [0, -1, 2, -3, 1]
    target = 0
    result = find_unique_triplets_sum(arr, target)
    print(f"Test 4: {result}")  # Expected: [(-3, 1, 2), (-1, 0, 1)]

    # Test Case 5: All same elements
    arr = [2, 2, 2, 2, 2]
    target = 6
    result = find_unique_triplets_sum(arr, target)
    print(f"Test 5: {result}")  # Expected: [(2, 2, 2)]

    # Test Case 6: Array with negative numbers
    arr = [-2, -1, 0, 1, 2, 3]
    target = 0
    result = find_unique_triplets_sum(arr, target)
    print(f"Test 6: {result}")  # Expected: [(-2, -1, 3), (-2, 0, 2), (-1, 0, 1)]

    # Test Case 7: Small array
    arr = [1, 2]
    target = 3
    result = find_unique_triplets_sum(arr, target)
    print(f"Test 7: {result}")  # Expected: []
