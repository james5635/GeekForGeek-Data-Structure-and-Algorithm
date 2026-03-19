"""
Largest Permutation by Swapping Adjacent Elements

Approach: Given we can only insert at ends of a deque, we achieve lexicographically
largest permutation by:
1. Sort array in descending order
2. Take top k largest elements (k = ceil(n/2)) at front in descending order
3. Append remaining elements (the ones not in top k) in ascending order

Time Complexity: O(n log n) for sorting
Space Complexity: O(n)
"""

from collections import deque


def largest_permutation(arr):
    """
    Convert array to lexicographically largest permutation using deque.
    Strategy: Top k largest at front (descending), rest appended (ascending).
    """
    if not arr:
        return []

    if len(arr) <= 2:
        return sorted(arr, reverse=True)

    sorted_arr = sorted(arr, reverse=True)
    k = (len(arr) + 1) // 2

    dq = deque()
    for i in range(k):
        dq.append(sorted_arr[i])

    remaining = []
    for i in range(k, len(sorted_arr)):
        remaining.append(sorted_arr[i])
    remaining.sort()
    for num in remaining:
        dq.append(num)

    return list(dq)


def largest_permutation_v2(arr):
    """
    Alternative: Take largest from front, smallest from back of sorted array.
    This creates the lexicographically largest arrangement using deque.
    """
    if not arr:
        return []

    sorted_arr = sorted(arr, reverse=True)
    dq = deque()

    left, right = 0, len(sorted_arr) - 1
    take_from_left = True

    while left <= right:
        if take_from_left:
            dq.append(sorted_arr[left])
            left += 1
        else:
            dq.append(sorted_arr[right])
            right -= 1
        take_from_left = not take_from_left

    return list(dq)


def main():
    print("=== Largest Permutation by Inserting at Ends ===\n")

    test_cases = [
        ([3, 1, 2, 4], [4, 3, 1, 2]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 1, 2]),
        ([5, 4, 3, 2, 1], [5, 4, 3, 1, 2]),
        ([1], [1]),
        ([2, 1], [2, 1]),
        ([1, 2], [2, 1]),
        ([4, 2, 1, 3], [4, 3, 1, 2]),
        ([1, 3, 5, 2, 4], [5, 4, 3, 1, 2]),
    ]

    for i, (input_arr, expected) in enumerate(test_cases, 1):
        result = largest_permutation(input_arr.copy())
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: Input: {input_arr}")
        print(f"        Output: {result}")
        print(f"        Expected: {expected}")
        print(f"        Status: {status}\n")


if __name__ == "__main__":
    main()
