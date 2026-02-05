"""
Count Pairs with Given Sum

Problem: Given an array of integers and a target sum, count the number of pairs
of elements whose sum equals the target sum.

Approach: Use a hash map to store frequency of elements. For each element,
check how many times (target - element) has appeared before and add to count.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - hash map stores element frequencies
"""


def count_pairs_with_sum(arr, target):
    """
    Count pairs with given sum.

    Args:
        arr: List of integers
        target: Target sum

    Returns:
        Number of pairs with sum equal to target
    """
    freq = {}
    count = 0

    for num in arr:
        complement = target - num
        if complement in freq:
            count += freq[complement]
        freq[num] = freq.get(num, 0) + 1

    return count


if __name__ == "__main__":
    # Test Case 1: Multiple pairs
    arr1 = [1, 5, 7, -1, 5]
    target1 = 6
    print(f"Array: {arr1}, Target: {target1}")
    print(f"Count of pairs: {count_pairs_with_sum(arr1, target1)}")
    print()

    # Test Case 2: No pairs
    arr2 = [1, 2, 3, 4]
    target2 = 10
    print(f"Array: {arr2}, Target: {target2}")
    print(f"Count of pairs: {count_pairs_with_sum(arr2, target2)}")
    print()

    # Test Case 3: Duplicate pairs
    arr3 = [1, 1, 1, 1]
    target3 = 2
    print(f"Array: {arr3}, Target: {target3}")
    print(f"Count of pairs: {count_pairs_with_sum(arr3, target3)}")
    print()

    # Test Case 4: Single element
    arr4 = [5]
    target4 = 10
    print(f"Array: {arr4}, Target: {target4}")
    print(f"Count of pairs: {count_pairs_with_sum(arr4, target4)}")
    print()

    # Test Case 5: Empty array
    arr5 = []
    target5 = 5
    print(f"Array: {arr5}, Target: {target5}")
    print(f"Count of pairs: {count_pairs_with_sum(arr5, target5)}")
    print()

    # Test Case 6: Negative numbers
    arr6 = [-1, -2, 3, 5, 4, 1]
    target6 = 4
    print(f"Array: {arr6}, Target: {target6}")
    print(f"Count of pairs: {count_pairs_with_sum(arr6, target6)}")
