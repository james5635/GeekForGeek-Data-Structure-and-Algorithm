"""
4Sum Closest - Find Quadruplet with Sum Closest to Target
==========================================================

Problem:
    Given an array and a target value, find four elements such that their sum
    is closest to the target. Return the closest sum value (not the quadruplet).

Approach:
    Sort the array first.
    Use two nested loops to fix first two elements.
    Use two-pointer technique for remaining two elements.
    Track the closest sum found and update when a closer sum is found.

Time Complexity: O(n^3) where n is the array length
Space Complexity: O(1) - only using constant extra space
"""


def four_sum_closest(arr, target):
    """
    Find the sum of four elements closest to target.

    Args:
        arr: Input array of integers
        target: Target sum value

    Returns:
        Integer representing the closest sum to target
    """
    n = len(arr)
    if n < 4:
        return None

    arr = sorted(arr)
    closest_sum = arr[0] + arr[1] + arr[2] + arr[3]

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left, right = j + 1, n - 1

            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                # Update closest sum if current is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # If exact match found, return immediately
                if current_sum == target:
                    return target
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return closest_sum


def four_sum_closest_quadruplet(arr, target):
    """
    Find the quadruplet with sum closest to target.

    Returns:
        Tuple of (closest_sum, quadruplet)
    """
    n = len(arr)
    if n < 4:
        return None, None

    arr = sorted(arr)
    closest_sum = arr[0] + arr[1] + arr[2] + arr[3]
    closest_quadruplet = (arr[0], arr[1], arr[2], arr[3])

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left, right = j + 1, n - 1

            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    closest_quadruplet = (arr[i], arr[j], arr[left], arr[right])

                if current_sum == target:
                    return target, (arr[i], arr[j], arr[left], arr[right])
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return closest_sum, closest_quadruplet


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    result = four_sum_closest(arr, target)
    print(f"Test 1: Closest sum = {result}")  # Expected: 0 (exact match possible)

    # Test Case 2: Closest to target 3
    arr = [1, 2, 3, 4, 5]
    target = 10
    result, quadruplet = four_sum_closest_quadruplet(arr, target)
    print(f"Test 2: Closest sum = {result}, Quadruplet = {quadruplet}")
    # Expected: 10 (1+2+3+4) exact match

    # Test Case 3: No exact match
    arr = [1, 2, 4, 8, 16, 32]
    target = 50
    result, quadruplet = four_sum_closest_quadruplet(arr, target)
    print(f"Test 3: Closest sum = {result}, Quadruplet = {quadruplet}")
    # Expected: Closest sum to 50

    # Test Case 4: With negative numbers
    arr = [-3, -2, -1, 0, 1, 2, 3]
    target = 5
    result = four_sum_closest(arr, target)
    print(f"Test 4: Closest sum = {result}")
    # Expected: 5 or very close

    # Test Case 5: All same elements
    arr = [2, 2, 2, 2, 2]
    target = 10
    result = four_sum_closest(arr, target)
    print(f"Test 5: Closest sum = {result}")  # Expected: 8 (2+2+2+2)

    # Test Case 6: Small array
    arr = [1, 2, 3]
    target = 10
    result = four_sum_closest(arr, target)
    print(f"Test 6: {result}")  # Expected: None (not enough elements)

    # Test Case 7: Large numbers
    arr = [100, 200, 300, 400, 500]
    target = 1000
    result, quadruplet = four_sum_closest_quadruplet(arr, target)
    print(f"Test 7: Closest sum = {result}, Quadruplet = {quadruplet}")
    # Expected: 1000 exact or close
