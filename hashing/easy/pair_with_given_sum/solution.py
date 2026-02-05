"""
Pair with Given Sum

Problem: Given an array of integers and a target sum, check if there exists a pair
of elements in the array whose sum equals the target sum.

Approach: Use a hash set to store visited elements. For each element, check if
(target - element) exists in the set.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - hash set stores visited elements
"""


def has_pair_with_sum(arr, target):
    """
    Check if there exists a pair with given sum.

    Args:
        arr: List of integers
        target: Target sum

    Returns:
        True if pair exists, False otherwise
    """
    seen = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)

    return False


def find_pair_with_sum(arr, target):
    """
    Find the actual pair with given sum.

    Args:
        arr: List of integers
        target: Target sum

    Returns:
        Tuple of pair if exists, None otherwise
    """
    seen = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)

    return None


if __name__ == "__main__":
    # Test Case 1: Pair exists
    arr1 = [1, 4, 45, 6, 10, -8]
    target1 = 16
    print(f"Array: {arr1}, Target: {target1}")
    print(f"Has pair with sum: {has_pair_with_sum(arr1, target1)}")
    print(f"Pair: {find_pair_with_sum(arr1, target1)}")
    print()

    # Test Case 2: No pair exists
    arr2 = [1, 2, 3, 4, 5]
    target2 = 10
    print(f"Array: {arr2}, Target: {target2}")
    print(f"Has pair with sum: {has_pair_with_sum(arr2, target2)}")
    print()

    # Test Case 3: Pair with negative numbers
    arr3 = [-1, -2, 3, 5, 8]
    target3 = 6
    print(f"Array: {arr3}, Target: {target3}")
    print(f"Has pair with sum: {has_pair_with_sum(arr3, target3)}")
    print(f"Pair: {find_pair_with_sum(arr3, target3)}")
    print()

    # Test Case 4: Single element (no pair possible)
    arr4 = [5]
    target4 = 10
    print(f"Array: {arr4}, Target: {target4}")
    print(f"Has pair with sum: {has_pair_with_sum(arr4, target4)}")
    print()

    # Test Case 5: Same element used twice (should not count)
    arr5 = [5, 5]
    target5 = 10
    print(f"Array: {arr5}, Target: {target5}")
    print(f"Has pair with sum: {has_pair_with_sum(arr5, target5)}")
    print()

    # Test Case 6: Empty array
    arr6 = []
    target6 = 5
    print(f"Array: {arr6}, Target: {target6}")
    print(f"Has pair with sum: {has_pair_with_sum(arr6, target6)}")
