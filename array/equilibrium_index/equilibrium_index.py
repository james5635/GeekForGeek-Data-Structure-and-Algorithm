"""
Equilibrium Index

Find an index where sum of elements on left equals sum on right.

Approaches:
1. Naive: Check all indices - O(n²) time, O(1) space
2. Better: Prefix/Suffix arrays - O(n) time, O(n) space
3. Optimal: Running sum - O(n) time, O(1) space
"""


def equilibrium_index_naive(arr):
    """
    Naive approach: Check each index by calculating left and right sums.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Algorithm:
    - For each index, calculate sum of left elements
    - Calculate sum of right elements
    - Return index if sums are equal

    Args:
        arr: List of integers

    Returns:
        Equilibrium index or -1 if not found
    """
    n = len(arr)

    for i in range(n):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i + 1 :])

        if left_sum == right_sum:
            return i

    return -1


def equilibrium_index_prefix_suffix(arr):
    """
    Better approach: Using prefix and suffix sum arrays.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Algorithm:
    - Precompute prefix sums (sum from start to i)
    - Precompute suffix sums (sum from i to end)
    - Check where prefix[i-1] == suffix[i+1]

    Args:
        arr: List of integers

    Returns:
        Equilibrium index or -1 if not found
    """
    n = len(arr)
    if n == 0:
        return -1

    # Compute prefix sums
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    # Compute suffix sums
    suffix = [0] * n
    suffix[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] + arr[i]

    # Check each index
    for i in range(n):
        left_sum = prefix[i - 1] if i > 0 else 0
        right_sum = suffix[i + 1] if i < n - 1 else 0

        if left_sum == right_sum:
            return i

    return -1


def equilibrium_index_optimal(arr):
    """
    Optimal approach: Single pass with running sum.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - Calculate total sum first
    - Traverse array, maintaining left sum
    - At each index, right sum = total - left - arr[i]
    - Check if left == right

    Args:
        arr: List of integers

    Returns:
        Equilibrium index or -1 if not found
    """
    n = len(arr)
    if n == 0:
        return -1

    total_sum = sum(arr)
    left_sum = 0

    for i in range(n):
        # Right sum = total - left - current
        right_sum = total_sum - left_sum - arr[i]

        if left_sum == right_sum:
            return i

        left_sum += arr[i]

    return -1


def find_all_equilibrium_indices(arr):
    """
    Find all equilibrium indices.

    Time Complexity: O(n)
    Space Complexity: O(1) (excluding output)

    Args:
        arr: List of integers

    Returns:
        List of all equilibrium indices
    """
    n = len(arr)
    if n == 0:
        return []

    total_sum = sum(arr)
    left_sum = 0
    indices = []

    for i in range(n):
        right_sum = total_sum - left_sum - arr[i]

        if left_sum == right_sum:
            indices.append(i)

        left_sum += arr[i]

    return indices


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [-7, 1, 5, 2, -4, 3, 0],
        [1, 2, 3],
        [1, 2, 3, 0, 3, 2, 1],
        [0, 0, 0, 0],
        [1],
        [],
        [2, 2, 2],
        [-1, -1, -1, -1, -1],
    ]

    print("=" * 70)
    print("Equilibrium Index")
    print("=" * 70)
    print("\nFind index where left sum equals right sum.\n")

    for i, arr in enumerate(test_cases, 1):
        naive_result = equilibrium_index_naive(arr)
        prefix_result = equilibrium_index_prefix_suffix(arr)
        optimal_result = equilibrium_index_optimal(arr)
        all_indices = find_all_equilibrium_indices(arr)

        match = "✓" if naive_result == prefix_result == optimal_result else "✗"

        print(f"Test {i}: arr = {arr}")
        print(f"  Naive O(n²):        Index {naive_result}")
        print(f"  Prefix/Suffix O(n): Index {prefix_result}")
        print(f"  Optimal O(1):       Index {optimal_result}")
        print(f"  All indices:        {all_indices if all_indices else 'None'} {match}")
        print()

    print("=" * 70)
    print("\nOptimal Approach Explanation:")
    print("  1. Calculate total sum of array")
    print("  2. Traverse array, maintaining running left sum")
    print("  3. At index i: right_sum = total - left - arr[i]")
    print("  4. If left_sum == right_sum, we found equilibrium")
    print("\n  Time: O(n), Space: O(1)")
    print("=" * 70)
