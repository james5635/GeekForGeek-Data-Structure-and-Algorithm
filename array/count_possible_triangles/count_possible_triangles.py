"""
Count Possible Triangles

Given an array of positive integers, count the number of possible triangles
that can be formed using three different elements as sides.

Triangle Inequality: For sides a, b, c (where a ≤ b ≤ c):
  a + b > c must be true

Approaches:
1. Naive: Try all triplets - O(n³) time, O(1) space
2. Better: Sort + Binary Search - O(n² log n) time, O(1) space
3. Optimal: Sort + Two Pointers - O(n²) time, O(1) space
"""

from bisect import bisect_left


def count_triangles_naive(arr):
    """
    Naive approach: Try all possible triplets.

    Time Complexity: O(n³)
    Space Complexity: O(1)

    Algorithm:
    - Check all combinations of three elements
    - Verify triangle inequality: a + b > c

    Args:
        arr: List of positive integers (side lengths)

    Returns:
        Count of possible triangles
    """
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check triangle inequality
                if (
                    arr[i] + arr[j] > arr[k]
                    and arr[i] + arr[k] > arr[j]
                    and arr[j] + arr[k] > arr[i]
                ):
                    count += 1

    return count


def count_triangles_binary_search(arr):
    """
    Better approach: Sort + Binary Search.

    Time Complexity: O(n² log n)
    Space Complexity: O(1)

    Algorithm:
    - Sort the array
    - Fix two sides (i and j), binary search for valid third side
    - For sorted array, if arr[i] + arr[j] > arr[k], then all elements
      between j+1 and k-1 also form valid triangles

    Args:
        arr: List of positive integers (side lengths)

    Returns:
        Count of possible triangles
    """
    n = len(arr)
    if n < 3:
        return 0

    arr = sorted(arr)
    count = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            # Find rightmost k such that arr[i] + arr[j] > arr[k]
            # Using bisect to find the insertion point
            sum_ij = arr[i] + arr[j]
            # Find first index where arr[k] >= sum_ij
            k = bisect_left(arr, sum_ij, j + 1, n)
            # All elements from j+1 to k-1 form valid triangles
            count += k - j - 1

    return count


def count_triangles_two_pointers(arr):
    """
    Optimal approach: Sort + Two Pointers.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Algorithm:
    - Sort the array
    - Fix the largest side (k from end)
    - Use two pointers (i=0, j=k-1) to find valid pairs
    - If arr[i] + arr[j] > arr[k], all elements between i and j-1
      also form valid triangles with arr[j] and arr[k]

    Key Insight:
    For sorted array, if arr[i] + arr[j] > arr[k], then for any
    index m where i ≤ m < j, we have arr[m] + arr[j] > arr[k]

    Args:
        arr: List of positive integers (side lengths)

    Returns:
        Count of possible triangles
    """
    n = len(arr)
    if n < 3:
        return 0

    arr = sorted(arr)
    count = 0

    # Fix the largest side
    for k in range(n - 1, 1, -1):
        i = 0
        j = k - 1

        while i < j:
            if arr[i] + arr[j] > arr[k]:
                # All elements from i to j-1 form valid triangles
                # with arr[j] and arr[k]
                count += j - i
                j -= 1
            else:
                i += 1

    return count


def count_triangles_brute_optimized(arr):
    """
    Alternative: Sort + Check with early termination.

    Time Complexity: O(n³) worst case, but faster in practice
    Space Complexity: O(1)
    """
    n = len(arr)
    if n < 3:
        return 0

    arr = sorted(arr)
    count = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] > arr[k]:
                    count += 1
                else:
                    break  # No need to check further (array is sorted)

    return count


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [4, 6, 3, 7],
        [10, 21, 22, 100, 101, 200, 300],
        [1, 2, 3],
        [2, 2, 3],
        [1, 1, 1, 1],
        [5, 5, 5, 5, 5],
        [1, 2, 3, 4, 5],
        [10, 20, 30],
    ]

    print("=" * 70)
    print("Count Possible Triangles")
    print("=" * 70)
    print("\nCount triangles where sum of any two sides > third side.\n")

    for i, arr in enumerate(test_cases, 1):
        naive_result = count_triangles_naive(arr)
        binary_search_result = count_triangles_binary_search(arr)
        two_pointer_result = count_triangles_two_pointers(arr)

        match = (
            "✓" if naive_result == binary_search_result == two_pointer_result else "✗"
        )

        print(f"Test {i}: arr = {arr}")
        print(f"  Naive O(n³):              {naive_result}")
        print(f"  Binary Search O(n²logn):  {binary_search_result}")
        print(f"  Two Pointers O(n²):       {two_pointer_result} {match}")
        print()

    print("=" * 70)
    print("\nTwo Pointers Approach Explanation:")
    print("  1. Sort the array")
    print("  2. Fix largest side (k from end to start)")
    print("  3. Use i=0, j=k-1 pointers")
    print("  4. If arr[i] + arr[j] > arr[k]:")
    print("     - All i to j-1 are valid with arr[j], arr[k]")
    print("     - Add (j-i) to count, decrement j")
    print("  5. Else increment i")
    print("\n  Time: O(n²), Space: O(1)")
    print("=" * 70)
