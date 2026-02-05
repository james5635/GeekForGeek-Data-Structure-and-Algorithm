"""
Longest Consecutive Subsequence

Problem Description:
Given an array of integers, find the length of the longest subsequence such
that elements in the subsequence are consecutive integers.
The consecutive numbers can be in any order.

Examples:
Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The longest consecutive subsequence is [1, 2, 3, 4, 5, 6]

Input: arr[] = [1, 1, 1, 2, 2, 3]
Output: 3
Explanation: The subsequence [1, 2, 3] is the longest consecutive subsequence

Approach:
Use Hashing for O(N) solution:
1. Insert all elements into a hash set
2. For each element, check if it's the start of a sequence (element-1 not in set)
3. If it's a start, count consecutive elements
4. Track maximum length

Time Complexity: O(N)
Space Complexity: O(N)
"""


def longest_consecutive_subsequence(arr):
    """
    Find length of longest consecutive subsequence.

    Args:
        arr: List of integers

    Returns:
        Length of longest consecutive subsequence
    """
    if not arr:
        return 0

    # Create hash set of all elements
    elements = set(arr)
    max_length = 0

    for num in elements:
        # Check if this is the start of a sequence
        if num - 1 not in elements:
            current_num = num
            current_length = 1

            # Count consecutive elements
            while current_num + 1 in elements:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length


def find_longest_consecutive_subsequence(arr):
    """
    Find the actual longest consecutive subsequence.

    Args:
        arr: List of integers

    Returns:
        List containing the longest consecutive subsequence
    """
    if not arr:
        return []

    elements = set(arr)
    max_length = 0
    best_start = None

    for num in elements:
        if num - 1 not in elements:
            current_num = num
            current_length = 1

            while current_num + 1 in elements:
                current_num += 1
                current_length += 1

            if current_length > max_length:
                max_length = current_length
                best_start = num

    if best_start is not None:
        return list(range(best_start, best_start + max_length))
    return []


def longest_consecutive_sorted(arr):
    """
    Alternative approach using sorting.
    Time: O(N log N), Space: O(1) or O(N)

    Args:
        arr: List of integers

    Returns:
        Length of longest consecutive subsequence
    """
    if not arr:
        return 0

    arr = sorted(set(arr))  # Remove duplicates and sort
    n = len(arr)

    max_length = 1
    current_length = 1

    for i in range(1, n):
        if arr[i] == arr[i - 1] + 1:
            current_length += 1
            max_length = max(max_length, current_length)
        elif arr[i] != arr[i - 1]:  # Skip duplicates
            current_length = 1

    return max_length


def test_longest_consecutive():
    """Test cases for longest consecutive subsequence."""
    # Test Case 1: Example from problem
    arr1 = [2, 6, 1, 9, 4, 5, 3]
    result1 = longest_consecutive_subsequence(arr1)
    subsequence1 = find_longest_consecutive_subsequence(arr1)
    print(f"Test 1: arr={arr1}")
    print(f"Length: {result1}, Expected: 6")
    print(f"Subsequence: {subsequence1}")
    print(f"{'PASS' if result1 == 6 else 'FAIL'}")
    print()

    # Test Case 2: With duplicates
    arr2 = [1, 1, 1, 2, 2, 3]
    result2 = longest_consecutive_subsequence(arr2)
    print(f"Test 2: arr={arr2}")
    print(f"Length: {result2}, Expected: 3")
    print(f"{'PASS' if result2 == 3 else 'FAIL'}")
    print()

    # Test Case 3: Empty array
    arr3 = []
    result3 = longest_consecutive_subsequence(arr3)
    print(f"Test 3: arr={arr3}")
    print(f"Length: {result3}, Expected: 0")
    print(f"{'PASS' if result3 == 0 else 'FAIL'}")
    print()

    # Test Case 4: Single element
    arr4 = [5]
    result4 = longest_consecutive_subsequence(arr4)
    print(f"Test 4: arr={arr4}")
    print(f"Length: {result4}, Expected: 1")
    print(f"{'PASS' if result4 == 1 else 'FAIL'}")
    print()

    # Test Case 5: No consecutive elements
    arr5 = [1, 3, 5, 7]
    result5 = longest_consecutive_subsequence(arr5)
    print(f"Test 5: arr={arr5}")
    print(f"Length: {result5}, Expected: 1")
    print(f"{'PASS' if result5 == 1 else 'FAIL'}")
    print()

    # Test Case 6: Negative numbers
    arr6 = [-5, -4, -3, -2, -1, 0, 1]
    result6 = longest_consecutive_subsequence(arr6)
    print(f"Test 6: arr={arr6}")
    print(f"Length: {result6}, Expected: 7")
    print(f"{'PASS' if result6 == 7 else 'FAIL'}")
    print()

    # Test Case 7: Compare with sorted approach
    arr7 = [100, 4, 200, 1, 3, 2]
    result7_hash = longest_consecutive_subsequence(arr7)
    result7_sort = longest_consecutive_sorted(arr7)
    print(f"Test 7: arr={arr7}")
    print(f"Hashing approach: {result7_hash}, Sorted approach: {result7_sort}")
    print(f"Expected: 4 (sequence: 1, 2, 3, 4)")
    print(f"{'PASS' if result7_hash == 4 and result7_sort == 4 else 'FAIL'}")
    print()


if __name__ == "__main__":
    test_longest_consecutive()
