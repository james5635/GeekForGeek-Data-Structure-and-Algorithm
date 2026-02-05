"""
Distinct Quadruplets with Sum Equal to Given Value
===================================================

Problem:
    Given an array and a target sum, find all distinct quadruplets
    (unique sets of four elements) that sum to the target.
    Similar to 4Sum but with emphasis on distinct quadruplets.

Approach:
    Sort the array first.
    Use two nested loops for first two elements.
    Use two-pointer technique for remaining elements.
    Skip duplicates at each level.

Time Complexity: O(n^3) where n is the array length
Space Complexity: O(1) extra space (excluding output)
"""


def find_distinct_quadruplets(arr, target):
    """
    Find all distinct quadruplets with sum equal to target.

    Args:
        arr: Input array of integers
        target: Target sum value

    Returns:
        List of distinct quadruplets (each as a tuple) that sum to target
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


def count_distinct_quadruplets(arr, target):
    """
    Count the number of distinct quadruplets with given sum.
    """
    return len(find_distinct_quadruplets(arr, target))


if __name__ == "__main__":
    # Test Case 1: Basic case with multiple quadruplets
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 18
    result = find_distinct_quadruplets(arr, target)
    print(f"Test 1: {result}")
    # Expected: [(1, 2, 7, 8), (1, 3, 6, 8), (1, 4, 5, 8), (1, 4, 6, 7),
    #           (2, 3, 5, 8), (2, 3, 6, 7), (2, 4, 5, 7), (3, 4, 5, 6)]

    # Test Case 2: Array with many duplicates
    arr = [1, 1, 1, 1, 2, 2, 2, 2]
    target = 6
    result = find_distinct_quadruplets(arr, target)
    print(f"Test 2: {result}")  # Expected: [(1, 1, 2, 2)]

    # Test Case 3: No quadruplet exists
    arr = [1, 2, 3, 4]
    target = 50
    result = find_distinct_quadruplets(arr, target)
    print(f"Test 3: {result}")  # Expected: []

    # Test Case 4: All elements same
    arr = [2, 2, 2, 2, 2, 2]
    target = 8
    result = find_distinct_quadruplets(arr, target)
    print(f"Test 4: {result}")  # Expected: [(2, 2, 2, 2)]

    # Test Case 5: With negative numbers
    arr = [-3, -2, -1, 0, 1, 2, 3, 4]
    target = 2
    result = find_distinct_quadruplets(arr, target)
    print(f"Test 5: {result}")
    # Expected: [(-3, -2, 3, 4), (-3, -1, 2, 4), (-3, 0, 1, 4), (-3, 0, 2, 3),
    #           (-2, -1, 1, 4), (-2, -1, 2, 3), (-2, 0, 1, 3), (-1, 0, 1, 2)]

    # Test Case 6: Small array
    arr = [1, 2, 3]
    target = 10
    result = find_distinct_quadruplets(arr, target)
    print(f"Test 6: {result}")  # Expected: []

    # Test Case 7: Count quadruplets
    arr = [0, 1, 2, 3, 4, 5]
    target = 10
    count = count_distinct_quadruplets(arr, target)
    print(f"Test 7: Count = {count}")  # Expected: 1 (0, 1, 4, 5) or similar
