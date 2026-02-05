"""
Find Subarray Sum Divisible by K

Problem Description:
Given an array arr[] and an integer k, count all subarrays whose sum is divisible by k.

Examples:
Input: arr[] = [4, 5, 0, -2, -3, 1], k = 5
Output: 7
Explanation: Subarrays with sum divisible by 5 are:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Input: arr[] = [2, 2, 2, 2, 2], k = 2
Output: 15 (all subarrays)

Approach:
Use prefix sum with hashing:
- If prefix_sum[j] % k == prefix_sum[i] % k, then subarray (i+1 to j) sum is divisible by k
- Use hashmap to store frequency of each remainder
- For each prefix sum, add the count of previous occurrences of same remainder

Time Complexity: O(N)
Space Complexity: O(K)
"""


def count_subarrays_divisible_by_k(arr, k):
    """
    Count subarrays with sum divisible by k.

    Args:
        arr: List of integers
        k: Positive integer divisor

    Returns:
        Count of subarrays with sum divisible by k
    """
    if not arr:
        return 0

    # Hash map to store frequency of remainders
    remainder_count = {0: 1}  # Empty subarray has sum 0
    prefix_sum = 0
    count = 0

    for num in arr:
        prefix_sum += num
        remainder = prefix_sum % k

        # If remainder is negative, convert to positive
        if remainder < 0:
            remainder += k

        # If this remainder was seen before, add its count
        if remainder in remainder_count:
            count += remainder_count[remainder]
            remainder_count[remainder] += 1
        else:
            remainder_count[remainder] = 1

    return count


def test_count_subarrays_divisible_by_k():
    """Test cases for count_subarrays_divisible_by_k function."""
    # Test Case 1: Example from problem
    arr1 = [4, 5, 0, -2, -3, 1]
    k1 = 5
    result1 = count_subarrays_divisible_by_k(arr1, k1)
    print(f"Test 1: arr={arr1}, k={k1}")
    print(f"Result: {result1}, Expected: 7, {'PASS' if result1 == 7 else 'FAIL'}")
    print()

    # Test Case 2: All elements same, all subarrays divisible
    arr2 = [2, 2, 2, 2, 2]
    k2 = 2
    result2 = count_subarrays_divisible_by_k(arr2, k2)
    # n*(n+1)/2 = 5*6/2 = 15
    print(f"Test 2: arr={arr2}, k={k2}")
    print(f"Result: {result2}, Expected: 15, {'PASS' if result2 == 15 else 'FAIL'}")
    print()

    # Test Case 3: Empty array
    arr3 = []
    k3 = 5
    result3 = count_subarrays_divisible_by_k(arr3, k3)
    print(f"Test 3: arr={arr3}, k={k3}")
    print(f"Result: {result3}, Expected: 0, {'PASS' if result3 == 0 else 'FAIL'}")
    print()

    # Test Case 4: No subarrays divisible
    arr4 = [1, 2, 3]
    k4 = 10
    result4 = count_subarrays_divisible_by_k(arr4, k4)
    print(f"Test 4: arr={arr4}, k={k4}")
    print(f"Result: {result4}, Expected: 0, {'PASS' if result4 == 0 else 'FAIL'}")
    print()

    # Test Case 5: Array with zero
    arr5 = [0, 0, 0]
    k5 = 5
    result5 = count_subarrays_divisible_by_k(arr5, k5)
    # All 6 subarrays: [0], [0], [0], [0,0], [0,0], [0,0,0]
    print(f"Test 5: arr={arr5}, k={k5}")
    print(f"Result: {result5}, Expected: 6, {'PASS' if result5 == 6 else 'FAIL'}")
    print()

    # Test Case 6: Negative numbers
    arr6 = [-1, -3]
    k6 = 5
    result6 = count_subarrays_divisible_by_k(arr6, k6)
    print(f"Test 6: arr={arr6}, k={k6}")
    print(f"Result: {result6}, Expected: 0, {'PASS' if result6 == 0 else 'FAIL'}")
    print()


if __name__ == "__main__":
    test_count_subarrays_divisible_by_k()
