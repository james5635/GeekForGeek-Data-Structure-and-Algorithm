"""
Find All Triplets with Zero Sum

Problem Description:
Given an array arr[], find all possible indices {i, j, k} of triplet
{arr[i], arr[j], arr[k]} such that their sum is equal to zero.
Indices in a triplet should be distinct and in sorted order (i < j < k).

Examples:
Input: arr[] = [0, -1, 2, -3, 1]
Output: [[0, 1, 4], [2, 3, 4]]
Explanation:
- arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
- arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0

Input: arr[] = [1, -2, 1, 0, 5]
Output: [[0, 1, 2]]
Explanation: arr[0] + arr[1] + arr[2] = 1 + (-2) + 1 = 0

Approach:
Use sorting and two-pointer technique:
- Sort the array first
- Fix one element, use two pointers to find pair with sum = -fixed element
- Skip duplicates to avoid duplicate triplets

Time Complexity: O(N^2)
Space Complexity: O(1) excluding output
"""


def find_triplets_with_zero_sum(arr):
    """
    Find all unique triplets with sum equal to zero.

    Args:
        arr: List of integers

    Returns:
        List of triplets (indices) with sum zero
    """
    n = len(arr)
    if n < 3:
        return []

    # Store original indices before sorting
    indexed_arr = [(arr[i], i) for i in range(n)]
    indexed_arr.sort(key=lambda x: x[0])

    result = []

    for i in range(n - 2):
        # Skip duplicate values for first element
        if i > 0 and indexed_arr[i][0] == indexed_arr[i - 1][0]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            current_sum = (
                indexed_arr[i][0] + indexed_arr[left][0] + indexed_arr[right][0]
            )

            if current_sum == 0:
                # Get original indices and sort them
                triplet_indices = sorted(
                    [indexed_arr[i][1], indexed_arr[left][1], indexed_arr[right][1]]
                )
                result.append(triplet_indices)

                # Move pointers and skip duplicates
                left += 1
                right -= 1

                while left < right and indexed_arr[left][0] == indexed_arr[left - 1][0]:
                    left += 1
                while (
                    left < right and indexed_arr[right][0] == indexed_arr[right + 1][0]
                ):
                    right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result


def find_triplets_hashing(arr):
    """
    Alternative approach using hashing.
    Returns values instead of indices.

    Args:
        arr: List of integers

    Returns:
        List of unique triplets (values) with sum zero
    """
    n = len(arr)
    if n < 3:
        return []

    result = set()

    for i in range(n - 2):
        seen = set()
        for j in range(i + 1, n):
            complement = -(arr[i] + arr[j])
            if complement in seen:
                triplet = tuple(sorted([arr[i], arr[j], complement]))
                result.add(triplet)
            seen.add(arr[j])

    return [list(triplet) for triplet in result]


def test_find_triplets_zero_sum():
    """Test cases for finding triplets with zero sum."""
    # Test Case 1: Example from problem
    arr1 = [0, -1, 2, -3, 1]
    result1 = find_triplets_with_zero_sum(arr1)
    print(f"Test 1: arr={arr1}")
    print(f"Result: {result1}")
    print(f"Expected: [[0, 1, 4], [2, 3, 4]]")
    print(f"{'PASS' if result1 == [[0, 1, 4], [2, 3, 4]] else 'FAIL'}")
    print()

    # Test Case 2: Another example
    arr2 = [1, -2, 1, 0, 5]
    result2 = find_triplets_with_zero_sum(arr2)
    print(f"Test 2: arr={arr2}")
    print(f"Result: {result2}")
    print(f"Expected: [[0, 1, 2]]")
    print(f"{'PASS' if result2 == [[0, 1, 2]] else 'FAIL'}")
    print()

    # Test Case 3: No triplets
    arr3 = [2, 3, 1, 0, 5]
    result3 = find_triplets_with_zero_sum(arr3)
    print(f"Test 3: arr={arr3}")
    print(f"Result: {result3}")
    print(f"Expected: []")
    print(f"{'PASS' if result3 == [] else 'FAIL'}")
    print()

    # Test Case 4: Empty array
    arr4 = []
    result4 = find_triplets_with_zero_sum(arr4)
    print(f"Test 4: arr={arr4}")
    print(f"Result: {result4}, Expected: [], {'PASS' if result4 == [] else 'FAIL'}")
    print()

    # Test Case 5: Less than 3 elements
    arr5 = [1, -1]
    result5 = find_triplets_with_zero_sum(arr5)
    print(f"Test 5: arr={arr5}")
    print(f"Result: {result5}, Expected: [], {'PASS' if result5 == [] else 'FAIL'}")
    print()

    # Test Case 6: Multiple zeros
    arr6 = [0, 0, 0, 0]
    result6 = find_triplets_with_zero_sum(arr6)
    print(f"Test 6: arr={arr6}")
    print(f"Result: {result6}")
    print(f"Note: Should contain one triplet of zeros")
    print()


if __name__ == "__main__":
    test_find_triplets_zero_sum()
