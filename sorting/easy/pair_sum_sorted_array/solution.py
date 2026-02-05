"""
Pair with Given Sum in Sorted Array (Two Sum II)

Problem Description:
    Given a 1-based indexed integer array arr[] that is sorted in non-decreasing order,
    along with an integer target. Find two elements in the array such that their sum
    is equal to target. Return the 1-based indices of the two elements in increasing order.
    If no such pair exists, return [-1, -1].

Example:
    Input: arr = [2, 7, 11, 15], target = 9
    Output: [1, 2]
    Explanation: arr[1] + arr[2] = 2 + 7 = 9

Time Complexity: O(n) - Linear time using two-pointer technique
Space Complexity: O(1) - Constant extra space
"""

from typing import List


def pair_sum_sorted(arr: List[int], target: int) -> List[int]:
    """
    Find pair with given sum in sorted array.

    Args:
        arr: Sorted array of integers (1-based indexing in output)
        target: Target sum

    Returns:
        List containing 1-based indices of the pair, or [-1, -1] if not found
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            # Return 1-based indices
            return [left + 1, right + 1]
        elif current_sum < target:
            # Need larger sum, move left pointer right
            left += 1
        else:
            # Need smaller sum, move right pointer left
            right -= 1

    return [-1, -1]


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr = [2, 7, 11, 15]
    target = 9
    print("Test 1:")
    print(f"Array: {arr}, Target: {target}")
    result = pair_sum_sorted(arr, target)
    print(f"Output: {result}")
    if result != [-1, -1]:
        print(
            f"Verification: arr[{result[0]}] + arr[{result[1]}] = {arr[result[0] - 1]} + {arr[result[1] - 1]} = {arr[result[0] - 1] + arr[result[1] - 1]}"
        )
    print()

    # Test Case 2: Different pair
    arr = [1, 3, 4, 6, 8, 11]
    target = 10
    print("Test 2:")
    print(f"Array: {arr}, Target: {target}")
    result = pair_sum_sorted(arr, target)
    print(f"Output: {result}")
    if result != [-1, -1]:
        print(
            f"Verification: arr[{result[0]}] + arr[{result[1]}] = {arr[result[0] - 1]} + {arr[result[1] - 1]} = {arr[result[0] - 1] + arr[result[1] - 1]}"
        )
    print()

    # Test Case 3: No pair exists
    arr = [1, 2, 3, 4, 5]
    target = 100
    print("Test 3:")
    print(f"Array: {arr}, Target: {target}")
    result = pair_sum_sorted(arr, target)
    print(f"Output: {result}")
    print()

    # Test Case 4: Pair at edges
    arr = [1, 2, 3, 4, 5]
    target = 6
    print("Test 4:")
    print(f"Array: {arr}, Target: {target}")
    result = pair_sum_sorted(arr, target)
    print(f"Output: {result}")
    if result != [-1, -1]:
        print(
            f"Verification: arr[{result[0]}] + arr[{result[1]}] = {arr[result[0] - 1]} + {arr[result[1] - 1]} = {arr[result[0] - 1] + arr[result[1] - 1]}"
        )
    print()

    # Test Case 5: Negative numbers
    arr = [-5, -2, 0, 3, 8]
    target = 1
    print("Test 5:")
    print(f"Array: {arr}, Target: {target}")
    result = pair_sum_sorted(arr, target)
    print(f"Output: {result}")
    if result != [-1, -1]:
        print(
            f"Verification: arr[{result[0]}] + arr[{result[1]}] = {arr[result[0] - 1]} + {arr[result[1] - 1]} = {arr[result[0] - 1] + arr[result[1] - 1]}"
        )
    print()

    # Test Case 6: Duplicate elements
    arr = [1, 2, 2, 3, 4]
    target = 4
    print("Test 6:")
    print(f"Array: {arr}, Target: {target}")
    result = pair_sum_sorted(arr, target)
    print(f"Output: {result}")
    if result != [-1, -1]:
        print(
            f"Verification: arr[{result[0]}] + arr[{result[1]}] = {arr[result[0] - 1]} + {arr[result[1] - 1]} = {arr[result[0] - 1] + arr[result[1] - 1]}"
        )
