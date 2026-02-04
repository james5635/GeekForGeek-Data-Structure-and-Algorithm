"""
Missing Number

Find the missing number in a range [1, n] where one number is missing.

Approaches:
1. Naive: Linear search - O(n²) time
2. Better: Hashing - O(n) time, O(n) space
3. Optimal 1: Sum formula - O(n) time, O(1) space
4. Optimal 2: XOR - O(n) time, O(1) space
"""


def find_missing_naive(arr):
    """
    Naive approach: Linear search for each number.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Algorithm:
    - For each number from 1 to n, check if it exists in array
    - Return the missing number

    Args:
        arr: List of integers from 1 to n with one missing

    Returns:
        The missing number
    """
    n = len(arr) + 1  # One number is missing

    for num in range(1, n + 1):
        found = False
        for element in arr:
            if element == num:
                found = True
                break
        if not found:
            return num

    return -1


def find_missing_hashing(arr):
    """
    Better approach: Using HashSet.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Algorithm:
    - Put all elements in a set
    - Check which number from 1 to n is not in the set

    Args:
        arr: List of integers from 1 to n with one missing

    Returns:
        The missing number
    """
    n = len(arr) + 1
    elements = set(arr)

    for num in range(1, n + 1):
        if num not in elements:
            return num

    return -1


def find_missing_sum(arr):
    """
    Optimal approach 1: Using sum formula.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Formula:
    Sum of 1 to n = n * (n + 1) / 2
    Missing number = Expected sum - Actual sum

    Args:
        arr: List of integers from 1 to n with one missing

    Returns:
        The missing number
    """
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


def find_missing_xor(arr):
    """
    Optimal approach 2: Using XOR.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - XOR all numbers from 1 to n
    - XOR all elements in array
    - Result is the missing number (pairs cancel out)

    Args:
        arr: List of integers from 1 to n with one missing

    Returns:
        The missing number
    """
    n = len(arr) + 1

    # XOR all numbers from 1 to n
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i

    # XOR all elements in array
    xor_arr = 0
    for num in arr:
        xor_arr ^= num

    # Missing number
    return xor_all ^ xor_arr


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 4, 5],  # Missing 3
        [1, 3],  # Missing 2
        [2, 3, 4, 5],  # Missing 1
        [1, 2, 3, 4],  # Missing 5
        [1],  # Missing 2
        [2],  # Missing 1
    ]

    print("=" * 70)
    print("Missing Number - Find Missing Number in Range [1, n]")
    print("=" * 70)

    for i, arr in enumerate(test_cases, 1):
        naive_result = find_missing_naive(arr)
        hash_result = find_missing_hashing(arr)
        sum_result = find_missing_sum(arr)
        xor_result = find_missing_xor(arr)

        all_match = naive_result == hash_result == sum_result == xor_result

        print(f"\nTest {i}: arr = {arr}, n = {len(arr) + 1}")
        print(f"  Naive O(n²):        {naive_result}")
        print(f"  Hashing O(n):       {hash_result}")
        print(f"  Sum Formula O(n):   {sum_result}")
        print(f"  XOR O(n):           {xor_result} {'✓' if all_match else '✗'}")

    print("\n" + "=" * 70)
    print("\nApproach Explanations:")
    print("\n1. Sum Formula:")
    print("   Expected sum = n*(n+1)/2")
    print("   Missing = Expected - Actual")
    print("   Risk: Integer overflow for very large n")
    print("\n2. XOR:")
    print("   XOR 1..n XOR XOR arr[] = missing number")
    print("   No overflow risk, works with large numbers")
    print("=" * 70)
