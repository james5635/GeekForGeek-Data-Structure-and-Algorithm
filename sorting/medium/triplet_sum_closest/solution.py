"""
Find a Triplet in an Array Whose Sum is Closest to a Given Number

Problem Description:
    Given an array and a target number, find a triplet whose sum is
    closest to the target. Return the sum of the triplet.

Time Complexity: O(n²)
- Sorting: O(n log n)
- Two nested loops: O(n²)

Space Complexity: O(1) auxiliary
- Sorting may use O(log n) to O(n)
- Only using a few pointers

Example:
    Input: arr = [-1, 2, 1, -4], target = 1
    Output: 2
    Explanation: The triplet [-1, 2, 1] has sum = 2, which is closest to 1
                 Other triplets: [-1, 2, -4] = -3, [2, 1, -4] = -1, [-1, 1, -4] = -4

    Input: arr = [1, 2, 3, 4, 5], target = 10
    Output: 10
    Explanation: [1, 4, 5] or [2, 3, 5] both sum to 10

Approach:
    1. Sort the array
    2. Initialize closest_sum to a large value
    3. For each i from 0 to n-3:
       - Use two pointers: left = i+1, right = n-1
       - While left < right:
         - Calculate current_sum = arr[i] + arr[left] + arr[right]
         - If |current_sum - target| < |closest_sum - target|:
           - Update closest_sum = current_sum
         - If current_sum == target: return target (exact match)
         - If current_sum < target: left++ (need larger sum)
         - If current_sum > target: right-- (need smaller sum)
"""

from typing import List, Tuple, Optional


def three_sum_closest(arr: List[int], target: int) -> int:
    """
    Find triplet sum closest to target.

    Args:
        arr: List of integers
        target: Target number

    Returns:
        Sum of triplet closest to target

    Raises:
        ValueError: If array has fewer than 3 elements
    """
    if not arr or len(arr) < 3:
        raise ValueError("Array must contain at least 3 elements")

    arr.sort()
    n = len(arr)

    # Initialize with first three elements
    closest_sum = arr[0] + arr[1] + arr[2]

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            # If exact match found
            if current_sum == target:
                return target

            # Update closest if current is closer
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            # Move pointers based on comparison
            if current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum


def three_sum_closest_with_triplet(
    arr: List[int], target: int
) -> Tuple[int, Tuple[int, int, int]]:
    """
    Find triplet sum closest to target, also return the triplet.

    Args:
        arr: List of integers
        target: Target number

    Returns:
        Tuple of (closest_sum, triplet)
    """
    if not arr or len(arr) < 3:
        raise ValueError("Array must contain at least 3 elements")

    arr.sort()
    n = len(arr)

    closest_sum = arr[0] + arr[1] + arr[2]
    closest_triplet = (arr[0], arr[1], arr[2])

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
                closest_triplet = (arr[i], arr[left], arr[right])

            if current_sum == target:
                return target, (arr[i], arr[left], arr[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum, closest_triplet


def three_sum_closest_brute_force(arr: List[int], target: int) -> int:
    """
    Brute force approach for verification (O(n³)).

    Args:
        arr: List of integers
        target: Target number

    Returns:
        Closest sum
    """
    if len(arr) < 3:
        raise ValueError("Array must contain at least 3 elements")

    n = len(arr)
    closest_sum = arr[0] + arr[1] + arr[2]

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                current_sum = arr[i] + arr[j] + arr[k]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

    return closest_sum


def three_sum_closest_all_solutions(
    arr: List[int], target: int
) -> List[Tuple[int, Tuple[int, int, int]]]:
    """
    Find all triplets with the closest sum to target.

    Args:
        arr: List of integers
        target: Target number

    Returns:
        List of (sum, triplet) with closest distance to target
    """
    if not arr or len(arr) < 3:
        return []

    arr.sort()
    n = len(arr)

    closest_sum = arr[0] + arr[1] + arr[2]
    solutions = []

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            current_diff = abs(current_sum - target)
            closest_diff = abs(closest_sum - target)

            if current_diff < closest_diff:
                closest_sum = current_sum
                solutions = [(current_sum, (arr[i], arr[left], arr[right]))]
            elif current_diff == closest_diff and current_sum == closest_sum:
                # Check for duplicate
                triplet = (arr[i], arr[left], arr[right])
                if (closest_sum, triplet) not in solutions:
                    solutions.append((closest_sum, triplet))

            if current_sum < target:
                left += 1
            else:
                right -= 1

    return solutions


# Test cases
def test_three_sum_closest():
    """Test cases for three_sum_closest function."""
    # Test case 1: Basic example
    arr1 = [-1, 2, 1, -4]
    target1 = 1
    result1 = three_sum_closest(arr1.copy(), target1)
    assert result1 == 2, f"Test 1 failed: {result1}"

    # Test case 2: Exact match exists
    arr2 = [1, 2, 3, 4, 5]
    target2 = 10
    result2 = three_sum_closest(arr2.copy(), target2)
    assert result2 == 10, f"Test 2 failed: {result2}"

    # Test case 3: All negative numbers
    arr3 = [-5, -4, -3, -2, -1]
    target3 = -10
    result3 = three_sum_closest(arr3.copy(), target3)
    assert result3 == -10, f"Test 3 failed: {result3}"  # -5 + -4 + -1 = -10

    # Test case 4: All positive numbers
    arr4 = [1, 2, 3, 4, 5]
    target4 = 100
    result4 = three_sum_closest(arr4.copy(), target4)
    assert result4 == 12, f"Test 4 failed: {result4}"  # 3 + 4 + 5 = 12 (closest to 100)

    # Test case 5: Mixed with duplicates
    arr5 = [0, 0, 0, 0]
    target5 = 1
    result5 = three_sum_closest(arr5.copy(), target5)
    assert result5 == 0, f"Test 5 failed: {result5}"

    # Test case 6: Large difference
    arr6 = [1, 1, 1, 100, 100]
    target6 = 3
    result6 = three_sum_closest(arr6.copy(), target6)
    assert result6 == 3, f"Test 6 failed: {result6}"

    # Test case 7: Get triplet as well
    arr7 = [-1, 2, 1, -4]
    target7 = 1
    sum7, triplet7 = three_sum_closest_with_triplet(arr7.copy(), target7)
    assert sum7 == 2, f"Test 7 failed: {sum7}"
    assert sum(triplet7) == sum7, f"Test 7 triplet sum failed"

    # Test case 8: Array too small
    try:
        three_sum_closest([1, 2], 3)
        assert False, "Test 8 failed: should raise error"
    except ValueError:
        pass

    # Test case 9: Compare with brute force
    import random

    arr9 = [random.randint(-50, 50) for _ in range(15)]
    target9 = random.randint(-30, 30)
    result9a = three_sum_closest(arr9.copy(), target9)
    result9b = three_sum_closest_brute_force(arr9.copy(), target9)
    assert result9a == result9b, f"Test 9 failed: {result9a} != {result9b}"

    # Test case 10: Zero target
    arr10 = [-2, -1, 0, 1, 2]
    target10 = 0
    result10 = three_sum_closest(arr10.copy(), target10)
    assert result10 == 0, f"Test 10 failed: {result10}"  # -1 + 0 + 1 = 0

    print("All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    test_three_sum_closest()

    # Example usage
    arr = [-1, 2, 1, -4]
    target = 1
    print(f"Array: {arr}")
    print(f"Target: {target}")

    closest = three_sum_closest(arr.copy(), target)
    print(f"Closest sum: {closest}")

    closest_with_triplet = three_sum_closest_with_triplet(arr.copy(), target)
    print(f"Closest sum: {closest_with_triplet[0]}, Triplet: {closest_with_triplet[1]}")
