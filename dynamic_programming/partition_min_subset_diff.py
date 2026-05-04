"""
Partition a set into two subsets such that the difference of subset sums is minimum.

Given an array arr[] of size n, the task is to divide it into two sets S1 and S2
such that the absolute difference between their sums is minimum.

The solution uses dynamic programming with space optimization.
We find all possible subset sums and then find the sum closest to half of total sum.

Time Complexity: O(n * sumTotal)
Space Complexity: O(sumTotal)
"""


def min_difference(arr):
    """
    Find the minimum difference between sums of two subsets.

    Args:
        arr: List of integers to partition

    Returns:
        Minimum absolute difference between two subset sums
    """
    sum_total = sum(arr)

    # DP array to track achievable subset sums
    dp = [False] * (sum_total + 1)
    dp[0] = True

    # Fill the DP array
    for num in arr:
        for sum_val in range(sum_total, num - 1, -1):
            dp[sum_val] = dp[sum_val] or dp[sum_val - num]

    # Find the minimum difference
    min_diff = sum_total
    for sum_val in range(sum_total // 2 + 1):
        if dp[sum_val]:
            min_diff = min(min_diff, abs((sum_total - sum_val) - sum_val))

    return min_diff


if __name__ == "__main__":
    # Test case 1
    arr1 = [1, 6, 11, 5]
    result1 = min_difference(arr1)
    print(f"Input: {arr1}")
    print(f"Minimum subset difference: {result1}")
    print(f"Expected: 1\n")

    # Test case 2
    arr2 = [1, 5, 11, 5]
    result2 = min_difference(arr2)
    print(f"Input: {arr2}")
    print(f"Minimum subset difference: {result2}")
    print(f"Expected: 0\n")

    # Test case 3
    arr3 = [3, 1, 4, 2, 2, 3]
    result3 = min_difference(arr3)
    print(f"Input: {arr3}")
    print(f"Minimum subset difference: {result3}")
