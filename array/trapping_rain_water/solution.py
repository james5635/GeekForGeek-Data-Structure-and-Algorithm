"""
Trapping Rain Water Problem

Problem Description:
Given n non-negative integers representing an elevation map where the width of each bar
is 1, compute how much water it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water are being trapped.

Time Complexity: O(n) - two pointers approach
Space Complexity: O(1) - only using two pointers

Approaches:
1. Brute Force: For each element, find max on left and right, O(n^2)
2. Dynamic Programming: Precompute left and right max arrays, O(n) time, O(n) space
3. Two Pointers: Optimal solution, O(n) time, O(1) space
"""

from typing import List


def trap_two_pointers(height: List[int]) -> int:
    """
    Optimal solution using two pointers.

    Args:
        height: List of non-negative integers representing elevation map

    Returns:
        Total units of water trapped
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            # Water trapped at left depends on left_max
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            # Water trapped at right depends on right_max
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


def trap_dp(height: List[int]) -> int:
    """
    Dynamic programming approach with precomputed max arrays.
    Time: O(n), Space: O(n)
    """
    if not height:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water


def trap_stack(height: List[int]) -> int:
    """
    Stack-based approach.
    Time: O(n), Space: O(n)
    """
    if not height:
        return 0

    stack = []
    water = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(height[i], height[stack[-1]]) - height[top]
            water += distance * bounded_height
        stack.append(i)

    return water


if __name__ == "__main__":
    # Test Case 1: Standard example
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result1 = trap_two_pointers(height1)
    print(f"Input: {height1}")
    print(f"Water trapped: {result1}")
    print(f"Expected: 6")
    print(f"Pass: {result1 == 6}\n")

    # Test Case 2: No water can be trapped
    height2 = [1, 2, 3, 4, 5]
    result2 = trap_two_pointers(height2)
    print(f"Input: {height2}")
    print(f"Water trapped: {result2}")
    print(f"Expected: 0")
    print(f"Pass: {result2 == 0}\n")

    # Test Case 3: Single valley
    height3 = [3, 0, 3]
    result3 = trap_two_pointers(height3)
    print(f"Input: {height3}")
    print(f"Water trapped: {result3}")
    print(f"Expected: 3")
    print(f"Pass: {result3 == 3}\n")

    # Test Case 4: Empty array
    height4 = []
    result4 = trap_two_pointers(height4)
    print(f"Input: {height4}")
    print(f"Water trapped: {result4}")
    print(f"Expected: 0")
    print(f"Pass: {result4 == 0}\n")

    # Test Case 5: Single element
    height5 = [5]
    result5 = trap_two_pointers(height5)
    print(f"Input: {height5}")
    print(f"Water trapped: {result5}")
    print(f"Expected: 0")
    print(f"Pass: {result5 == 0}\n")

    # Test Case 6: Two elements
    height6 = [4, 2]
    result6 = trap_two_pointers(height6)
    print(f"Input: {height6}")
    print(f"Water trapped: {result6}")
    print(f"Expected: 0")
    print(f"Pass: {result6 == 0}\n")

    # Test Case 7: Large valley
    height7 = [4, 2, 0, 3, 2, 5]
    result7 = trap_two_pointers(height7)
    print(f"Input: {height7}")
    print(f"Water trapped: {result7}")
    print(f"Expected: 9")
    print(f"Pass: {result7 == 9}")
