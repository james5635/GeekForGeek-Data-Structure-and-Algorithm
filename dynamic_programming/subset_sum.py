"""
Subset Sum Problem (DP-25)

Given an array of non-negative integers and a target sum, determine if there exists
a subset of the array whose sum equals the target sum.

This implementation uses the space-optimized dynamic programming approach.

Time Complexity: O(n * sum)
Space Complexity: O(sum)

Source: https://www.geeksforgeeks.org/dsa/subset-sum-problem-dp-25/
"""


def is_subset_sum(arr, target_sum):
    """
    Check if there is a subset of arr with sum equal to target_sum.

    Args:
        arr: List of non-negative integers
        target_sum: The target sum to find

    Returns:
        bool: True if a subset with the target sum exists, False otherwise
    """
    n = len(arr)
    prev = [False] * (target_sum + 1)
    curr = [False] * (target_sum + 1)

    prev[0] = True

    for i in range(1, n + 1):
        for j in range(target_sum + 1):
            if j < arr[i - 1]:
                curr[j] = prev[j]
            else:
                curr[j] = prev[j] or prev[j - arr[i - 1]]
        prev = curr.copy()

    return prev[target_sum]


if __name__ == "__main__":
    print("=== Subset Sum Problem ===\n")

    arr = [3, 34, 4, 12, 5, 2]
    target = 9
    result = is_subset_sum(arr, target)
    print(f"Input: arr = {arr}, sum = {target}")
    print(f"Output: {result}")
    print(
        f"Explanation: {'There is a subset (4, 5) with sum 9' if result else 'No subset found'}\n"
    )

    arr = [3, 34, 4, 12, 5, 2]
    target = 30
    result = is_subset_sum(arr, target)
    print(f"Input: arr = {arr}, sum = {target}")
    print(f"Output: {result}")
    print(f"Explanation: {'Subset found' if result else 'No subset adds up to 30'}\n")

    arr = [1, 5, 3, 7, 4]
    target = 12
    result = is_subset_sum(arr, target)
    print(f"Input: arr = {arr}, sum = {target}")
    print(f"Output: {result}")
    print(f"Explanation: {'Subset found' if result else 'No subset found'}\n")

    arr = [1, 2, 3]
    target = 0
    result = is_subset_sum(arr, target)
    print(f"Input: arr = {arr}, sum = {target}")
    print(f"Output: {result}")
    print(f"Explanation: Empty subset always sums to 0\n")

    arr = [2, 3, 7, 8, 10]
    target = 15
    result = is_subset_sum(arr, target)
    print(f"Input: arr = {arr}, sum = {target}")
    print(f"Output: {result}")
    print(f"Explanation: {'Subset found' if result else 'No subset found'}\n")
