"""
Rearrange Array such that arr[i] = i

Given an array of elements of length N, ranging from 0 to N-1.
All elements may not be present in the array.
If element is not present, there will be -1 present in the array.
Rearrange the array such that arr[i] = i, and if i is not present, put -1 there.

Approaches:
1. Naive: O(n²) - For each i from 0 to n-1, search i in array
2. Optimal: O(n) - Place elements at their correct positions
"""


def rearrange_naive(arr):
    """
    Naive approach: For each index i, search for i in array.

    Time Complexity: O(n²)
    Space Complexity: O(1) - modifies array in-place

    Algorithm:
    - For each position i from 0 to n-1:
      - Search if i exists in array
      - If found, put i at position i
      - If not found, put -1 at position i

    Args:
        arr: List of integers with some elements missing (-1 for missing)

    Returns:
        Modified array with arr[i] = i or -1
    """
    n = len(arr)
    result = [-1] * n

    for i in range(n):
        # Search for i in array
        for j in range(n):
            if arr[j] == i:
                result[i] = i
                break

    return result


def rearrange_optimal(arr):
    """
    Optimal approach: Place elements at their correct positions.

    Time Complexity: O(n)
    Space Complexity: O(1) - modifies array in-place

    Algorithm:
    - Traverse array and for each element arr[i]:
      - While arr[i] is valid (0 <= arr[i] < n) and arr[i] != i:
        - Swap arr[i] with arr[arr[i]]
    - After placing all elements, replace remaining with -1

    Key Insight:
    - An element x should be at position x
    - Keep swapping until arr[i] = i or out of range

    Args:
        arr: List of integers (modified in-place)

    Returns:
        Modified array with arr[i] = i or -1
    """
    n = len(arr)

    for i in range(n):
        # Keep swapping until arr[i] is at correct position or invalid
        while 0 <= arr[i] < n and arr[i] != i:
            # Check if target position already has the correct element
            target = arr[i]
            if arr[target] == target:
                break

            # Swap arr[i] with arr[target]
            arr[i], arr[target] = arr[target], arr[i]

    # Replace any remaining misplaced elements with -1
    for i in range(n):
        if arr[i] != i:
            arr[i] = -1

    return arr


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Format: (input_array, expected_output)
        # Input has: -1, -1, 6, 1, 9, 3, 2, -1, 4, -1
        # Valid values in range [0,9]: 6, 1, 9, 3, 2, 4
        # So positions 0, 5, 7, 8 should be -1
        ([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1], [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]),
        ([19, 7, 0, 3, 18], [0, -1, -1, 3, -1]),  # 0 and 3 are valid (in range 0-4)
        ([-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]),
        ([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]),
        ([4, 3, 2, 1, 0], [0, 1, 2, 3, 4]),
        ([-1, 0], [0, -1]),
    ]

    print("=" * 70)
    print("Rearrange Array such that arr[i] = i")
    print("=" * 70)

    for i, (arr, expected) in enumerate(test_cases, 1):
        arr_copy1 = arr.copy()
        arr_copy2 = arr.copy()

        naive_result = rearrange_naive(arr_copy1)
        optimal_result = rearrange_optimal(arr_copy2)

        match_naive = naive_result == expected
        match_optimal = optimal_result == expected

        print(f"\nTest {i}:")
        print(f"  Input:    {arr}")
        print(f"  Expected: {expected}")
        print(f"  Naive O(n²):     {naive_result} {'✓' if match_naive else '✗'}")
        print(f"  Optimal O(n):    {optimal_result} {'✓' if match_optimal else '✗'}")

    print("\n" + "=" * 70)
    print("\nAlgorithm Explanation:")
    print("\n1. Naive Approach O(n²):")
    print("   - For each position i from 0 to n-1")
    print("   - Search the entire array for value i")
    print("   - If found, place it at position i")
    print("   - Otherwise, place -1")
    print("\n2. Optimal Approach O(n):")
    print("   - Traverse array and for each element arr[i]:")
    print("   - While arr[i] is valid (0 <= arr[i] < n) and arr[i] != i:")
    print("     - Swap arr[i] with arr[arr[i]] to place it at correct position")
    print("   - After all swaps, replace misplaced elements with -1")
    print("\nKey Insight: An element x belongs at position x")
    print("=" * 70)
