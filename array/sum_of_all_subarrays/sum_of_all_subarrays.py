"""
Sum of All Subarrays

Calculate the sum of all possible subarrays of a given array.

Approaches:
1. Naive: Generate all subarrays and sum - O(n²) time, O(1) space
2. Optimal: Use contribution formula - O(n) time, O(1) space
   Formula: arr[i] appears in (i+1) * (n-i) subarrays
"""


def sum_of_subarrays_naive(arr):
    """
    Naive approach: Generate all subarrays and calculate their sum.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Algorithm:
    - For each starting index i
    - Extend subarray to the right, accumulating sum
    - Add each subarray sum to total

    Args:
        arr: List of integers

    Returns:
        Sum of all subarrays
    """
    n = len(arr)
    total_sum = 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            total_sum += current_sum

    return total_sum


def sum_of_subarrays_optimal(arr):
    """
    Optimal approach: Use element contribution formula.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insight:
    Each element arr[i] appears in (i+1) * (n-i) subarrays:
    - (i+1) choices for starting index (0 to i)
    - (n-i) choices for ending index (i to n-1)

    So contribution of arr[i] = arr[i] * (i+1) * (n-i)

    Args:
        arr: List of integers

    Returns:
        Sum of all subarrays
    """
    n = len(arr)
    total_sum = 0

    for i in range(n):
        # Contribution of arr[i] to all subarrays
        contribution = arr[i] * (i + 1) * (n - i)
        total_sum += contribution

    return total_sum


def sum_of_subarrays_formula_derived(arr):
    """
    Alternative optimal approach with the same formula.

    This version explicitly shows the mathematical derivation.
    """
    n = len(arr)
    result = 0

    for i in range(n):
        # Number of subarrays where arr[i] is included
        # = (number of ways to choose start) * (number of ways to choose end)
        # = (i+1) * (n-i)
        count = (i + 1) * (n - i)
        result += arr[i] * count

    return result


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 3],
        [1, 2, 3, 4],
        [5],
        [],
        [1, 1, 1],
        [-1, 2, -3, 4],
        [10, 20, 30],
    ]

    print("=" * 70)
    print("Sum of All Subarrays - Test Cases")
    print("=" * 70)
    print("\nSubarrays are contiguous parts of the array.")
    print("For [1, 2, 3], subarrays are: [1], [1,2], [1,2,3], [2], [2,3], [3]")
    print("Sum = 1 + 3 + 6 + 2 + 5 + 3 = 20\n")

    for i, arr in enumerate(test_cases, 1):
        naive_result = sum_of_subarrays_naive(arr)
        optimal_result = sum_of_subarrays_optimal(arr)
        formula_result = sum_of_subarrays_formula_derived(arr)

        match = "✓" if naive_result == optimal_result == formula_result else "✗"

        print(f"Test {i}: arr = {arr}")
        print(f"  Naive O(n²):        {naive_result}")
        print(f"  Optimal O(n):       {optimal_result}")
        print(f"  Formula Derived:    {formula_result} {match}")
        print()

    print("=" * 70)
    print("\nFormula Explanation:")
    print("  For element at index i, it appears in (i+1) * (n-i) subarrays")
    print("  - (i+1): Number of choices for start index (0 to i)")
    print("  - (n-i): Number of choices for end index (i to n-1)")
    print("=" * 70)
