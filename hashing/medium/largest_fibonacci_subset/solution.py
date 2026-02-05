"""
Largest Fibonacci Subset

Problem Description:
Given an array arr[], find the largest subset from the array that contains
elements which are Fibonacci numbers.

Examples:
Input: arr[] = [1, 4, 3, 9, 10, 13, 7]
Output: [1, 3, 13]
Explanation: 1, 3, and 13 are the only Fibonacci numbers in the array

Input: arr[] = [0, 2, 8, 5, 2, 1, 4, 13, 23]
Output: [0, 2, 8, 5, 2, 1, 13]
Explanation: All these numbers are Fibonacci numbers

Approach:
Use Hash Set:
1. Find maximum element in array
2. Generate all Fibonacci numbers up to max element
3. Store Fibonacci numbers in hash set
4. Filter array to keep only Fibonacci numbers

Time Complexity: O(N + M) where M is max element
Space Complexity: O(N + M)
"""


def is_perfect_square(n):
    """Check if a number is a perfect square."""
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n


def is_fibonacci(n):
    """
    Check if a number is Fibonacci using mathematical property.
    N is Fibonacci if one of (5*N^2 + 4) or (5*N^2 - 4) is perfect square.
    """
    if n < 0:
        return False
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


def largest_fibonacci_subset_math(arr):
    """
    Find largest Fibonacci subset using mathematical formula.

    Args:
        arr: List of integers

    Returns:
        List of Fibonacci numbers from array
    """
    return [x for x in arr if is_fibonacci(x)]


def largest_fibonacci_subset_hash(arr):
    """
    Find largest Fibonacci subset using hash set approach.

    Args:
        arr: List of integers

    Returns:
        List of Fibonacci numbers from array
    """
    if not arr:
        return []

    max_val = max(arr)

    # Generate all Fibonacci numbers up to max_val
    fib_set = set()
    a, b = 0, 1

    while a <= max_val:
        fib_set.add(a)
        a, b = b, a + b

    # Filter array to keep only Fibonacci numbers
    return [x for x in arr if x in fib_set]


def count_fibonacci_in_range(low, high):
    """
    Count Fibonacci numbers in given range [low, high].

    Args:
        low: Lower bound (inclusive)
        high: Upper bound (inclusive)

    Returns:
        Count of Fibonacci numbers in range
    """
    count = 0
    a, b = 0, 1

    while a <= high:
        if a >= low:
            count += 1
        a, b = b, a + b

    return count


def test_largest_fibonacci_subset():
    """Test cases for largest Fibonacci subset."""
    # Test Case 1: Example from problem
    arr1 = [1, 4, 3, 9, 10, 13, 7]
    result1_math = largest_fibonacci_subset_math(arr1)
    result1_hash = largest_fibonacci_subset_hash(arr1)
    print(f"Test 1: arr={arr1}")
    print(f"Math approach: {result1_math}")
    print(f"Hash approach: {result1_hash}")
    print(f"Expected: [1, 3, 13]")
    print(f"{'PASS' if result1_hash == [1, 3, 13] else 'FAIL'}")
    print()

    # Test Case 2: Another example
    arr2 = [0, 2, 8, 5, 2, 1, 4, 13, 23]
    result2 = largest_fibonacci_subset_hash(arr2)
    print(f"Test 2: arr={arr2}")
    print(f"Result: {result2}")
    print(f"Expected: [0, 2, 8, 5, 2, 1, 13]")
    print(f"{'PASS' if result2 == [0, 2, 8, 5, 2, 1, 13] else 'FAIL'}")
    print()

    # Test Case 3: Empty array
    arr3 = []
    result3 = largest_fibonacci_subset_hash(arr3)
    print(f"Test 3: arr={arr3}")
    print(f"Result: {result3}, Expected: [], {'PASS' if result3 == [] else 'FAIL'}")
    print()

    # Test Case 4: No Fibonacci numbers
    arr4 = [4, 6, 7, 9, 10]
    result4 = largest_fibonacci_subset_hash(arr4)
    print(f"Test 4: arr={arr4}")
    print(f"Result: {result4}, Expected: [], {'PASS' if result4 == [] else 'FAIL'}")
    print()

    # Test Case 5: All Fibonacci numbers
    arr5 = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    result5 = largest_fibonacci_subset_hash(arr5)
    print(f"Test 5: arr={arr5}")
    print(f"Result: {result5}")
    print(f"Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21]")
    print(f"{'PASS' if result5 == arr5 else 'FAIL'}")
    print()

    # Test Case 6: Test is_fibonacci function
    fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    non_fib = [4, 6, 7, 9, 10, 11, 12, 14]
    print(f"Test 6: is_fibonacci function")
    print(f"Fibonacci numbers: {fib_numbers}")
    print(f"All recognized as Fibonacci: {all(is_fibonacci(x) for x in fib_numbers)}")
    print(f"Non-Fibonacci: {non_fib}")
    print(f"None recognized as Fibonacci: {not any(is_fibonacci(x) for x in non_fib)}")
    print()

    # Test Case 7: Count Fibonacci in range
    print(f"Test 7: Count Fibonacci in range")
    print(f"Count in [1, 100]: {count_fibonacci_in_range(1, 100)} (Expected: 11)")
    print(f"Count in [10, 100]: {count_fibonacci_in_range(10, 100)} (Expected: 5)")
    print()


if __name__ == "__main__":
    test_largest_fibonacci_subset()
