"""
Product Array Puzzle

Given an array arr[] of n integers, construct a Product Array prod[]
such that prod[i] is equal to the product of all elements of arr[] except arr[i].

Approaches:
1. Naive: O(n²) - Calculate product for each element by iterating
2. Better: O(n) with prefix/suffix arrays
3. Optimal: O(n) time, O(1) extra space (output array doesn't count)
"""


def product_array_naive(arr):
    """
    Naive approach: For each element, calculate product of all others.

    Time Complexity: O(n²)
    Space Complexity: O(1) excluding output (O(n) for output)

    Algorithm:
    - For each position i:
      - Multiply all elements except arr[i]
    - Store result in output array

    Args:
        arr: List of integers

    Returns:
        Product array where prod[i] = product of all except arr[i]
    """
    n = len(arr)
    if n == 0:
        return []
    if n == 1:
        return [1]

    result = [1] * n

    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= arr[j]
        result[i] = product

    return result


def product_array_prefix_suffix(arr):
    """
    Better approach: Use prefix and suffix products.

    Time Complexity: O(n)
    Space Complexity: O(n) - for prefix and suffix arrays

    Algorithm:
    - prefix[i] = product of all elements from 0 to i-1
    - suffix[i] = product of all elements from i+1 to n-1
    - result[i] = prefix[i] * suffix[i]

    Args:
        arr: List of integers

    Returns:
        Product array
    """
    n = len(arr)
    if n == 0:
        return []
    if n == 1:
        return [1]

    # Calculate prefix products
    prefix = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * arr[i - 1]

    # Calculate suffix products
    suffix = [1] * n
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * arr[i + 1]

    # Result is product of prefix and suffix
    result = [prefix[i] * suffix[i] for i in range(n)]

    return result


def product_array_optimal(arr):
    """
    Optimal approach: O(1) extra space (excluding output).

    Time Complexity: O(n)
    Space Complexity: O(1) extra (output array doesn't count)

    Algorithm:
    - First pass: result[i] contains product of elements before i
    - Second pass: Multiply by product of elements after i
    - Use a running variable for suffix product

    Args:
        arr: List of integers

    Returns:
        Product array
    """
    n = len(arr)
    if n == 0:
        return []
    if n == 1:
        return [1]

    result = [1] * n

    # First pass: result[i] = product of elements before i
    for i in range(1, n):
        result[i] = result[i - 1] * arr[i - 1]

    # Second pass: multiply by product of elements after i
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix_product
        suffix_product *= arr[i]

    return result


def product_array_with_division(arr):
    """
    Alternative: Using total product and division.

    Time Complexity: O(n)
    Space Complexity: O(1) excluding output

    Note:
    - Doesn't work if array contains 0
    - Generally not allowed in interview constraints

    Args:
        arr: List of integers (no zeros)

    Returns:
        Product array
    """
    n = len(arr)
    if n == 0:
        return []
    if n == 1:
        return [1]

    # Check for zeros
    if 0 in arr:
        raise ValueError("Array contains zero, division method not applicable")

    total_product = 1
    for num in arr:
        total_product *= num

    return [total_product // num for num in arr]


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # (array, expected_product_array)
        ([10, 3, 5, 6, 2], [180, 600, 360, 300, 900]),
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([5], [1]),  # Single element
        ([2, 3], [3, 2]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([-1, 2, -3, 4], [-24, 12, -8, 6]),  # With negatives
    ]

    print("=" * 70)
    print("Product Array Puzzle")
    print("=" * 70)

    for i, (arr, expected) in enumerate(test_cases, 1):
        naive_result = product_array_naive(arr.copy())
        prefix_result = product_array_prefix_suffix(arr.copy())
        optimal_result = product_array_optimal(arr.copy())

        match_naive = naive_result == expected
        match_prefix = prefix_result == expected
        match_optimal = optimal_result == expected

        print(f"\nTest {i}:")
        print(f"  Input:    {arr}")
        print(f"  Expected: {expected}")
        print(f"  Naive O(n²):        {naive_result} {'✓' if match_naive else '✗'}")
        print(f"  Prefix-Suffix O(n): {prefix_result} {'✓' if match_prefix else '✗'}")
        print(f"  Optimal O(n) O(1):  {optimal_result} {'✓' if match_optimal else '✗'}")

    print("\n" + "=" * 70)
    print("\nAlgorithm Explanation:")
    print("\n1. Naive Approach O(n²):")
    print("   - For each position i:")
    print("     - Multiply all elements except arr[i]")
    print("   - Store result")
    print("   - Time: O(n²), Space: O(1) extra")
    print("\n2. Prefix-Suffix Approach O(n) O(n):")
    print("   - prefix[i] = product of arr[0..i-1]")
    print("   - suffix[i] = product of arr[i+1..n-1]")
    print("   - result[i] = prefix[i] × suffix[i]")
    print("   - Time: O(n), Space: O(n)")
    print("\n3. Optimal Approach O(n) O(1):")
    print("   - First pass (left to right):")
    print("     - result[i] = product of elements before i")
    print("   - Second pass (right to left):")
    print("     - Multiply result[i] by suffix product")
    print("     - Update suffix product")
    print("   - Time: O(n), Space: O(1) extra")
    print(
        "\nKey Insight: result[i] = (product of left elements) × (product of right elements)"
    )
    print("=" * 70)
