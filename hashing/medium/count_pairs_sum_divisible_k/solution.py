"""
Count Pairs Sum Divisible by K

Problem Description:
Given an array A[] and positive integer K, the task is to count the total
number of pairs in the array whose sum is divisible by K.

Examples:
Input: A[] = {2, 2, 1, 7, 5, 3}, K = 4
Output: 5
Explanation: Pairs with sum divisible by 4 are:
(2, 2), (1, 7), (7, 5), (1, 3), (5, 3)

Input: A[] = {5, 9, 36, 74, 52, 31, 42}, K = 3
Output: 7

Approach:
Use hashing to store frequency of remainders when divided by K.
- For each element, calculate remainder = arr[i] % K
- Elements with remainder r can pair with elements having remainder (K - r) % K
- Special case: elements with remainder 0 can pair among themselves

Time Complexity: O(N)
Space Complexity: O(K)
"""


def count_pairs_divisible_by_k(arr, k):
    """
    Count pairs whose sum is divisible by k.

    Args:
        arr: List of integers
        k: Positive integer divisor

    Returns:
        Count of pairs with sum divisible by k
    """
    if not arr or k <= 0:
        return 0

    # Frequency array for remainders
    freq = [0] * k

    # Count remainders
    for num in arr:
        freq[num % k] += 1

    count = 0

    # Pairs with remainder 0 can pair among themselves
    count += (freq[0] * (freq[0] - 1)) // 2

    # Pairs with complementary remainders
    for i in range(1, (k // 2) + 1):
        if i != k - i:
            count += freq[i] * freq[k - i]

    # If k is even, handle middle element separately
    if k % 2 == 0:
        count += (freq[k // 2] * (freq[k // 2] - 1)) // 2

    return count


def test_count_pairs_divisible_by_k():
    """Test cases for count_pairs_divisible_by_k function."""
    # Test Case 1: Example from problem
    arr1 = [2, 2, 1, 7, 5, 3]
    k1 = 4
    result1 = count_pairs_divisible_by_k(arr1, k1)
    print(f"Test 1: arr={arr1}, k={k1}")
    print(f"Result: {result1}, Expected: 5, {'PASS' if result1 == 5 else 'FAIL'}")
    print()

    # Test Case 2: Another example
    arr2 = [5, 9, 36, 74, 52, 31, 42]
    k2 = 3
    result2 = count_pairs_divisible_by_k(arr2, k2)
    print(f"Test 2: arr={arr2}, k={k2}")
    print(f"Result: {result2}, Expected: 7, {'PASS' if result2 == 7 else 'FAIL'}")
    print()

    # Test Case 3: Empty array
    arr3 = []
    k3 = 5
    result3 = count_pairs_divisible_by_k(arr3, k3)
    print(f"Test 3: arr={arr3}, k={k3}")
    print(f"Result: {result3}, Expected: 0, {'PASS' if result3 == 0 else 'FAIL'}")
    print()

    # Test Case 4: Single element
    arr4 = [5]
    k4 = 5
    result4 = count_pairs_divisible_by_k(arr4, k4)
    print(f"Test 4: arr={arr4}, k={k4}")
    print(f"Result: {result4}, Expected: 0, {'PASS' if result4 == 0 else 'FAIL'}")
    print()

    # Test Case 5: All elements divisible by k
    arr5 = [2, 4, 6, 8]
    k5 = 2
    result5 = count_pairs_divisible_by_k(arr5, k5)
    print(f"Test 5: arr={arr5}, k={k5}")
    print(f"Result: {result5}, Expected: 6, {'PASS' if result5 == 6 else 'FAIL'}")
    print()

    # Test Case 6: No pairs divisible
    arr6 = [1, 2, 3]
    k6 = 10
    result6 = count_pairs_divisible_by_k(arr6, k6)
    print(f"Test 6: arr={arr6}, k={k6}")
    print(f"Result: {result6}, Expected: 0, {'PASS' if result6 == 0 else 'FAIL'}")
    print()


if __name__ == "__main__":
    test_count_pairs_divisible_by_k()
