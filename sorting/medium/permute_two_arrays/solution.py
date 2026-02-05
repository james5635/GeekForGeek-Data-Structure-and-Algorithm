"""
Permute Two Arrays such that Sum of Every Pair is Greater than or Equal to K

Given two arrays a[] and b[] of equal size and an integer k, determine whether
there exists any permutation of the arrays such that for every index i,
a[i] + b[i] >= k.

Algorithm:
1. Sort array a in ascending order
2. Sort array b in descending order
3. Check if a[i] + b[i] >= k for all i

Time Complexity: O(n log n) - Sorting dominates
Space Complexity: O(1) or O(n) depending on sort implementation
"""


def can_permute_for_sum(a, b, k):
    """
    Check if arrays can be permuted such that a[i] + b[i] >= k for all i.

    Args:
        a: First array of integers
        b: Second array of integers (same size as a)
        k: Target minimum sum

    Returns:
        bool: True if valid permutation exists, False otherwise
    """
    if len(a) != len(b):
        return False

    if not a:  # Empty arrays
        return True

    n = len(a)

    # Sort a in ascending order
    a_sorted = sorted(a)

    # Sort b in descending order
    b_sorted = sorted(b, reverse=True)

    # Check if all pairs satisfy the condition
    for i in range(n):
        if a_sorted[i] + b_sorted[i] < k:
            return False

    return True


def can_permute_for_sum_with_permutation(a, b, k):
    """
    Returns the actual permutation if one exists.

    Args:
        a: First array of integers
        b: Second array of integers
        k: Target minimum sum

    Returns:
        tuple: (success, permuted_a, permuted_b) or (False, None, None)
    """
    if len(a) != len(b):
        return False, None, None

    if not a:
        return True, [], []

    n = len(a)

    # Sort a in ascending order
    a_sorted = sorted(a)

    # Sort b in descending order
    b_sorted = sorted(b, reverse=True)

    # Check if all pairs satisfy the condition
    for i in range(n):
        if a_sorted[i] + b_sorted[i] < k:
            return False, None, None

    return True, a_sorted, b_sorted


def find_permutation_greedy(a, b, k):
    """
    Alternative: Use greedy approach with two pointers.

    Args:
        a: First array of integers
        b: Second array of integers
        k: Target minimum sum

    Returns:
        bool: True if valid permutation exists
    """
    if len(a) != len(b):
        return False

    n = len(a)

    # Sort both arrays
    a_sorted = sorted(a)
    b_sorted = sorted(b)

    # Use two pointers - try to pair smallest of a with largest of b
    used = [False] * n

    for i in range(n):
        # Find the smallest element in b that makes sum >= k with a[i]
        found = False
        for j in range(n - 1, -1, -1):
            if not used[j] and a_sorted[i] + b_sorted[j] >= k:
                used[j] = True
                found = True
                break

        if not found:
            return False

    return True


def test_can_permute_for_sum():
    """Test cases for permute two arrays algorithm."""
    # Test Case 1: Basic case from problem
    a = [2, 1, 3]
    b = [7, 8, 9]
    k = 10
    result = can_permute_for_sum(a, b, k)
    assert result is True, f"Test 1 failed: Expected True, got {result}"
    print("Test 1 passed: Basic case (true)")

    # Test Case 2: Case where it's not possible
    a = [1, 2, 2, 1]
    b = [3, 3, 3, 4]
    k = 5
    result = can_permute_for_sum(a, b, k)
    assert result is False, f"Test 2 failed: Expected False, got {result}"
    print("Test 2 passed: Not possible case")

    # Test Case 3: Exact match
    a = [5, 5, 5]
    b = [5, 5, 5]
    k = 10
    result = can_permute_for_sum(a, b, k)
    assert result is True, f"Test 3 failed: Expected True, got {result}"
    print("Test 3 passed: Exact match")

    # Test Case 4: Empty arrays
    a = []
    b = []
    k = 5
    result = can_permute_for_sum(a, b, k)
    assert result is True, f"Test 4 failed: Expected True, got {result}"
    print("Test 4 passed: Empty arrays")

    # Test Case 5: Single element - possible
    a = [3]
    b = [7]
    k = 10
    result = can_permute_for_sum(a, b, k)
    assert result is True, f"Test 5 failed: Expected True, got {result}"
    print("Test 5 passed: Single element (possible)")

    # Test Case 6: Single element - not possible
    a = [3]
    b = [6]
    k = 10
    result = can_permute_for_sum(a, b, k)
    assert result is False, f"Test 6 failed: Expected False, got {result}"
    print("Test 6 passed: Single element (not possible)")

    # Test Case 7: Large arrays
    a = list(range(1, 101))  # 1 to 100
    b = list(range(100, 0, -1))  # 100 to 1
    k = 101  # Smallest possible sum is 1+1=2, largest is 100+100=200
    result = can_permute_for_sum(a, b, k)
    assert result is True, f"Test 7 failed: Expected True for large arrays"
    print("Test 7 passed: Large arrays")

    # Test Case 8: With negative numbers
    a = [-5, -3, 0]
    b = [10, 8, 5]
    k = 5
    result = can_permute_for_sum(a, b, k)
    assert result is True, f"Test 8 failed: Expected True, got {result}"
    print("Test 8 passed: With negative numbers")

    # Test Case 9: Get actual permutation
    a = [2, 1, 3]
    b = [7, 8, 9]
    k = 10
    success, perm_a, perm_b = can_permute_for_sum_with_permutation(a, b, k)
    assert success is True, "Test 9a failed: Should find permutation"
    assert perm_a is not None and perm_b is not None, (
        "Test 9b failed: Should return permutations"
    )
    for i in range(len(perm_a)):
        assert perm_a[i] + perm_b[i] >= k, (
            f"Test 9c failed: Sum at {i} is {perm_a[i] + perm_b[i]} < {k}"
        )
    print("Test 9 passed: Get actual permutation")

    # Test Case 10: Verify greedy approach matches main approach
    test_cases = [
        ([2, 1, 3], [7, 8, 9], 10),
        ([1, 2, 2, 1], [3, 3, 3, 4], 5),
        ([5, 5, 5], [5, 5, 5], 10),
        ([1, 2, 3], [4, 5, 6], 7),
    ]

    for i, (a, b, k) in enumerate(test_cases, 10):
        result1 = can_permute_for_sum(a, b, k)
        result2 = find_permutation_greedy(a, b, k)
        assert result1 == result2, f"Test {i} failed: Methods disagree"
        print(f"Test {i} passed: Methods agree")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_can_permute_for_sum()

    # Example usage
    print("\nExample 1 (Possible):")
    a = [2, 1, 3]
    b = [7, 8, 9]
    k = 10
    result = can_permute_for_sum(a, b, k)
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"k = {k}")
    print(f"Can permute: {result}")

    if result:
        _, perm_a, perm_b = can_permute_for_sum_with_permutation(a, b, k)
        print(f"Permutation a: {perm_a}")
        print(f"Permutation b: {perm_b}")
        print("Pair sums:", [perm_a[i] + perm_b[i] for i in range(len(perm_a))])

    print("\nExample 2 (Not possible):")
    a = [1, 2, 2, 1]
    b = [3, 3, 3, 4]
    k = 5
    result = can_permute_for_sum(a, b, k)
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"k = {k}")
    print(f"Can permute: {result}")
