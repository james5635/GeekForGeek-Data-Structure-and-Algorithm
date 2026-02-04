"""
Duplicate Within K Distance

Check if array contains duplicate elements within k distance.

Approaches:
1. Naive: Check all pairs within k distance - O(n*k) time, O(1) space
2. Optimal: Use HashSet to track last k elements - O(n) time, O(k) space
"""


def has_duplicate_naive(arr, k):
    """
    Naive approach: Check all pairs within k distance.

    Time Complexity: O(n*k)
    Space Complexity: O(1)

    Args:
        arr: List of integers
        k: Maximum distance between duplicates

    Returns:
        True if duplicate exists within k distance, False otherwise
    """
    n = len(arr)
    for i in range(n):
        # Check only next k elements
        for j in range(i + 1, min(i + k + 1, n)):
            if arr[i] == arr[j]:
                return True
    return False


def has_duplicate_optimal(arr, k):
    """
    Optimal approach: Use HashSet to track last k elements.

    Time Complexity: O(n)
    Space Complexity: O(k)

    We maintain a window of last k elements using a set.
    If we find a duplicate in the window, return True.

    Args:
        arr: List of integers
        k: Maximum distance between duplicates

    Returns:
        True if duplicate exists within k distance, False otherwise
    """
    seen = set()

    for i in range(len(arr)):
        # If element already in window, duplicate found
        if arr[i] in seen:
            return True

        # Add current element to window
        seen.add(arr[i])

        # Remove element that is now k+1 distance away
        if i >= k:
            seen.remove(arr[i - k])

    return False


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # (array, k, expected_result)
        ([1, 2, 3, 4, 1, 2, 3, 4], 3, True),  # 1 repeats within distance 4
        ([1, 2, 3, 1, 4, 5], 3, True),  # 1 repeats at distance 3
        ([1, 2, 3, 4, 5], 3, False),  # No duplicates
        ([1, 2, 3, 4, 4], 3, True),  # 4 repeats at distance 1
        ([1, 1, 1, 1], 1, True),  # Multiple duplicates
        ([1], 1, False),  # Single element
        ([], 1, False),  # Empty array
        ([1, 2, 3, 4, 5, 1], 5, True),  # 1 at distance exactly 5
        ([1, 2, 3, 4, 5, 1], 4, False),  # 1 at distance 5, k=4
    ]

    print("=" * 60)
    print("Duplicate Within K Distance - Test Cases")
    print("=" * 60)

    for i, (arr, k, expected) in enumerate(test_cases, 1):
        arr_copy = arr.copy()
        naive_result = has_duplicate_naive(arr_copy, k)
        optimal_result = has_duplicate_optimal(arr_copy, k)

        status_naive = "✓" if naive_result == expected else "✗"
        status_optimal = "✓" if optimal_result == expected else "✗"

        print(f"\nTest {i}: arr={arr}, k={k}")
        print(f"  Expected: {expected}")
        print(f"  Naive O(n*k): {naive_result} {status_naive}")
        print(f"  Optimal O(n): {optimal_result} {status_optimal}")

    print("\n" + "=" * 60)
