"""
Count Triplets with Given Sum

Problem Description:
Given an array arr[] and a target value, find the count of triplets present in
the given array having sum equal to the given target.

Examples:
Input: arr[] = [0, -1, 2, -3, 1], target = -2
Output: 2
Explanation: Triplets are:
(0, -3, 1) and (-1, 2, -3)

Input: arr[] = [1, -2, 1, 0, 5], target = 1
Output: 0

Approach:
Use hashing with two-pointer technique:
- Fix one element and use hash set to find pairs with required sum
- For each element arr[i], find pairs in arr[i+1:] that sum to (target - arr[i])
- Use hash set to store elements and check for complement

Time Complexity: O(N^2)
Space Complexity: O(N)
"""


def count_triplets_with_sum(arr, target):
    """
    Count triplets with sum equal to target.

    Args:
        arr: List of integers
        target: Target sum for triplets

    Returns:
        Count of triplets with sum equal to target
    """
    n = len(arr)
    if n < 3:
        return 0

    count = 0

    # Fix first element and find other two
    for i in range(n - 2):
        # Find pairs in arr[i+1:] with sum = target - arr[i]
        seen = set()
        required = target - arr[i]

        for j in range(i + 1, n):
            complement = required - arr[j]
            if complement in seen:
                count += 1
            seen.add(arr[j])

    return count


def count_triplets_sorted(arr, target):
    """
    Optimized version for sorted arrays using two-pointer technique.

    Args:
        arr: Sorted list of integers
        target: Target sum for triplets

    Returns:
        Count of triplets with sum equal to target
    """
    n = len(arr)
    if n < 3:
        return 0

    arr = sorted(arr)  # Ensure array is sorted
    count = 0

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                # Handle duplicates
                if arr[left] == arr[right]:
                    # All elements between left and right are same
                    num_elements = right - left + 1
                    count += (num_elements * (num_elements - 1)) // 2
                    break

                left_count = 1
                right_count = 1

                # Count duplicates on left
                while left + 1 < right and arr[left] == arr[left + 1]:
                    left += 1
                    left_count += 1

                # Count duplicates on right
                while right - 1 > left and arr[right] == arr[right - 1]:
                    right -= 1
                    right_count += 1

                count += left_count * right_count
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return count


def test_count_triplets():
    """Test cases for triplet counting functions."""
    # Test Case 1: Example from problem
    arr1 = [0, -1, 2, -3, 1]
    target1 = -2
    result1 = count_triplets_with_sum(arr1, target1)
    print(f"Test 1: arr={arr1}, target={target1}")
    print(f"Result: {result1}, Expected: 2, {'PASS' if result1 == 2 else 'FAIL'}")
    print()

    # Test Case 2: No triplets found
    arr2 = [1, -2, 1, 0, 5]
    target2 = 1
    result2 = count_triplets_with_sum(arr2, target2)
    print(f"Test 2: arr={arr2}, target={target2}")
    print(f"Result: {result2}, Expected: 0, {'PASS' if result2 == 0 else 'FAIL'}")
    print()

    # Test Case 3: All same elements
    arr3 = [1, 1, 1, 1]
    target3 = 3
    result3 = count_triplets_with_sum(arr3, target3)
    print(f"Test 3: arr={arr3}, target={target3}")
    print(f"Result: {result3}, Expected: 4, {'PASS' if result3 == 4 else 'FAIL'}")
    print()

    # Test Case 4: Empty array
    arr4 = []
    target4 = 5
    result4 = count_triplets_with_sum(arr4, target4)
    print(f"Test 4: arr={arr4}, target={target4}")
    print(f"Result: {result4}, Expected: 0, {'PASS' if result4 == 0 else 'FAIL'}")
    print()

    # Test Case 5: Less than 3 elements
    arr5 = [1, 2]
    target5 = 3
    result5 = count_triplets_with_sum(arr5, target5)
    print(f"Test 5: arr={arr5}, target={target5}")
    print(f"Result: {result5}, Expected: 0, {'PASS' if result5 == 0 else 'FAIL'}")
    print()

    # Test Case 6: Test sorted version
    arr6 = [-3, -1, -1, 0, 1, 2]
    target6 = -2
    result6 = count_triplets_sorted(arr6, target6)
    print(f"Test 6 (sorted): arr={arr6}, target={target6}")
    print(f"Result: {result6}, Expected: 4, {'PASS' if result6 == 4 else 'FAIL'}")
    print()


if __name__ == "__main__":
    test_count_triplets()
