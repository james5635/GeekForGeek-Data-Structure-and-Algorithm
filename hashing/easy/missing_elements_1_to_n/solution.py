"""
Find Missing Elements from 1 to N

Problem: Given an array of size n containing numbers from 1 to n with some
numbers missing, find all missing numbers.

Approach: Use hash set to track present elements, then check 1 to n.
Alternative: Mark indices as negative to track presence (O(1) space).

Time Complexity: O(n) - two passes through array/range
Space Complexity: O(n) for hash set, O(1) for marking approach
"""


def find_missing_elements_hash(arr, n):
    """
    Find missing elements from 1 to n using hash set.

    Args:
        arr: List of integers (some from 1 to n)
        n: Upper bound

    Returns:
        List of missing elements from 1 to n
    """
    present = set(arr)
    missing = []

    for i in range(1, n + 1):
        if i not in present:
            missing.append(i)

    return missing


def find_missing_elements_marking(arr, n):
    """
    Find missing elements by marking indices (modifies array).

    Args:
        arr: List of integers (some from 1 to n)
        n: Upper bound

    Returns:
        List of missing elements from 1 to n
    """
    # Mark presence by making element at index negative
    for num in arr:
        idx = abs(num) - 1
        if 0 <= idx < n:
            arr[idx] = -abs(arr[idx])

    missing = []
    for i in range(n):
        if arr[i] > 0:
            missing.append(i + 1)

    return missing


def find_missing_elements_sum(arr, n):
    """
    Find single missing element using sum formula.

    Args:
        arr: List of integers (n-1 elements from 1 to n)
        n: Upper bound

    Returns:
        The single missing element
    """
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


if __name__ == "__main__":
    # Test Case 1: Multiple missing
    arr1 = [1, 3, 5, 6]
    n1 = 6
    print(f"Array: {arr1}, n: {n1}")
    print(f"Missing elements: {find_missing_elements_hash(arr1.copy(), n1)}")
    print()

    # Test Case 2: Single missing
    arr2 = [1, 2, 4, 5]
    n2 = 5
    print(f"Array: {arr2}, n: {n2}")
    print(f"Missing element (sum): {find_missing_elements_sum(arr2, n2)}")
    print(f"Missing elements: {find_missing_elements_hash(arr2.copy(), n2)}")
    print()

    # Test Case 3: None missing
    arr3 = [1, 2, 3, 4, 5]
    n3 = 5
    print(f"Array: {arr3}, n: {n3}")
    print(f"Missing elements: {find_missing_elements_hash(arr3.copy(), n3)}")
    print()

    # Test Case 4: Only 1 missing
    arr4 = [2, 3, 4, 5]
    n4 = 5
    print(f"Array: {arr4}, n: {n4}")
    print(f"Missing elements: {find_missing_elements_hash(arr4.copy(), n4)}")
    print()

    # Test Case 5: Only n missing
    arr5 = [1, 2, 3, 4]
    n5 = 5
    print(f"Array: {arr5}, n: {n5}")
    print(f"Missing element (sum): {find_missing_elements_sum(arr5, n5)}")
    print()

    # Test Case 6: With duplicates
    arr6 = [1, 2, 2, 4]
    n6 = 5
    print(f"Array: {arr6}, n: {n6}")
    print(f"Missing elements: {find_missing_elements_hash(arr6.copy(), n6)}")
    print(
        f"Missing elements (marking): {find_missing_elements_marking(arr6.copy(), n6)}"
    )
