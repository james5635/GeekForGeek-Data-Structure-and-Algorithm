"""
4Sum - Find Four Elements that Sum to a Given Value
====================================================

Problem:
    Given an array and a target sum, find all unique quadruplets (i, j, k, l)
    such that arr[i] + arr[j] + arr[k] + arr[l] = target and all indices are distinct.
    Each quadruplet should be unique (no duplicates).

Approach:
    Sort the array first.
    Use two nested loops to fix first two elements.
    Use two-pointer technique for the remaining two elements.
    Skip duplicates at each level to ensure unique quadruplets.

Time Complexity: O(n^3) where n is the array length
Space Complexity: O(1) extra space (excluding output)
"""


def four_sum(arr, target):
    """
    Find all unique quadruplets with sum equal to target.

    Args:
        arr: Input array of integers
        target: Target sum value

    Returns:
        List of unique quadruplets (each as a tuple) that sum to target
    """
    n = len(arr)
    if n < 4:
        return []

    arr = sorted(arr)
    result = []

    for i in range(n - 3):
        # Skip duplicates for first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicates for second element
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            # Two pointers for remaining two elements
            left, right = j + 1, n - 1

            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if current_sum == target:
                    result.append((arr[i], arr[j], arr[left], arr[right]))

                    # Skip duplicates
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result


def has_four_sum(arr, target):
    """
    Check if there exists any quadruplet with given sum.
    """
    return len(four_sum(arr, target)) > 0


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    result = four_sum(arr, target)
    print(
        f"Test 1: {result}"
    )  # Expected: [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]

    # Test Case 2: Target = 4
    arr = [2, 2, 2, 2, 2]
    target = 8
    result = four_sum(arr, target)
    print(f"Test 2: {result}")  # Expected: [(2, 2, 2, 2)]

    # Test Case 3: No solution
    arr = [1, 2, 3, 4]
    target = 100
    result = four_sum(arr, target)
    print(f"Test 3: {result}")  # Expected: []

    # Test Case 4: With negative numbers
    arr = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0
    result = four_sum(arr, target)
    print(f"Test 4: {result}")  # Multiple solutions

    # Test Case 5: Large array
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 20
    result = four_sum(arr, target)
    print(
        f"Test 5: {result}"
    )  # Multiple solutions like (1, 2, 8, 9), (1, 3, 7, 9), etc.

    # Test Case 6: Small array
    arr = [1, 2, 3]
    target = 6
    result = four_sum(arr, target)
    print(f"Test 6: {result}")  # Expected: []

    # Test Case 7: Check existence
    arr = [1, 2, 3, 4, 5, 6]
    target = 10
    exists = has_four_sum(arr, target)
    print(f"Test 7: Has quadruplet? {exists}")  # Expected: True (1, 2, 3, 4)
