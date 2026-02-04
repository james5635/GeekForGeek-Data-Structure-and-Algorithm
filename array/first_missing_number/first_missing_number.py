"""
First Missing Positive Number

Given an unsorted integer array, find the smallest missing positive integer.

Approaches:
1. Naive: O(n log n) - Sort then scan
2. Better: O(n) space with hash set
3. Optimal: O(1) space - Cyclic sort / place at index
"""


def first_missing_positive_naive(arr):
    """
    Naive approach: Sort then scan for first missing positive.

    Time Complexity: O(n log n) - for sorting
    Space Complexity: O(1) or O(n) depending on sort

    Algorithm:
    - Sort the array
    - Traverse and find first positive integer
    - Check if each consecutive positive integer is present
    - Return first missing

    Args:
        arr: List of integers

    Returns:
        Smallest missing positive integer
    """
    if not arr:
        return 1

    arr_sorted = sorted(arr)

    missing = 1
    for num in arr_sorted:
        if num == missing:
            missing += 1
        elif num > missing:
            break

    return missing


def first_missing_positive_hash(arr):
    """
    Better approach: Use hash set for O(n) time.

    Time Complexity: O(n)
    Space Complexity: O(n) - for hash set

    Algorithm:
    - Store all elements in a hash set
    - Check integers starting from 1
    - Return first integer not in set

    Args:
        arr: List of integers

    Returns:
        Smallest missing positive integer
    """
    if not arr:
        return 1

    elements = set(arr)

    missing = 1
    while missing in elements:
        missing += 1

    return missing


def first_missing_positive_cyclic(arr):
    """
    Optimal approach: Cyclic sort - place each element at its index.

    Time Complexity: O(n)
    Space Complexity: O(1) - modifies array in-place

    Algorithm:
    - For each element, if it's in valid range (1 to n):
      - Swap it to its correct position (element x goes to index x-1)
    - After placing all, find first index where arr[i] != i+1
    - Return i+1

    Args:
        arr: List of integers (modified in-place)

    Returns:
        Smallest missing positive integer
    """
    n = len(arr)
    if n == 0:
        return 1

    for i in range(n):
        # Place arr[i] at its correct position if possible
        while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
            # Swap arr[i] with arr[arr[i] - 1]
            correct_idx = arr[i] - 1
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]

    # Find first index where arr[i] != i + 1
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    # All 1 to n are present, return n+1
    return n + 1


def first_missing_positive_partition(arr):
    """
    Alternative optimal: Partition then cyclic sort.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - First partition: move all positive numbers to front
    - Then apply cyclic sort only on positive part
    - Find first missing

    Args:
        arr: List of integers

    Returns:
        Smallest missing positive integer
    """
    n = len(arr)
    if n == 0:
        return 1

    # Partition: move positive numbers to front
    j = 0
    for i in range(n):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    # Now arr[j..n-1] contains positive numbers
    # Work only with positive part
    positive_start = j
    positive_count = n - j

    # Mark presence by making index negative
    for i in range(positive_start, n):
        val = abs(arr[i])
        if 1 <= val <= positive_count:
            idx = positive_start + val - 1
            if arr[idx] > 0:
                arr[idx] = -arr[idx]

    # Find first positive position
    for i in range(positive_start, n):
        if arr[i] > 0:
            return i - positive_start + 1

    return positive_count + 1


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # (array, expected)
        ([1, 2, 0], 3),  # 3 is missing
        ([3, 4, -1, 1], 2),  # 2 is missing
        ([7, 8, 9, 11, 12], 1),  # 1 is missing
        ([1, 2, 3], 4),  # All present, return 4
        ([-1, -2, -3], 1),  # All negative, 1 is missing
        ([0], 1),  # Single zero
        ([1], 2),  # Single one
        ([2], 1),  # Single two
        ([-5, 3, 2, 1], 4),  # Mixed with negative
        ([1, 1, 1], 2),  # Duplicates
    ]

    print("=" * 70)
    print("First Missing Positive Number")
    print("=" * 70)

    for i, (arr, expected) in enumerate(test_cases, 1):
        # Test naive
        result_naive = first_missing_positive_naive(arr.copy())

        # Test hash
        result_hash = first_missing_positive_hash(arr.copy())

        # Test cyclic sort
        result_cyclic = first_missing_positive_cyclic(arr.copy())

        # Test partition
        result_partition = first_missing_positive_partition(arr.copy())

        match_naive = result_naive == expected
        match_hash = result_hash == expected
        match_cyclic = result_cyclic == expected
        match_partition = result_partition == expected

        print(f"\nTest {i}:")
        print(f"  Input:    {arr}")
        print(f"  Expected: {expected}")
        print(f"  Naive O(n log n):  {result_naive} {'✓' if match_naive else '✗'}")
        print(f"  Hash O(n) O(n):    {result_hash} {'✓' if match_hash else '✗'}")
        print(f"  Cyclic O(n) O(1):  {result_cyclic} {'✓' if match_cyclic else '✗'}")
        print(
            f"  Partition O(n):    {result_partition} {'✓' if match_partition else '✗'}"
        )

    print("\n" + "=" * 70)
    print("\nAlgorithm Explanation:")
    print("\n1. Naive Approach O(n log n):")
    print("   - Sort the array")
    print("   - Traverse from 1, checking if each exists")
    print("   - Return first missing")
    print("   - Time: O(n log n), Space: O(1) or O(n)")
    print("\n2. Hash Set Approach O(n) O(n):")
    print("   - Store all elements in hash set")
    print("   - Check integers 1, 2, 3, ... until not found")
    print("   - Time: O(n), Space: O(n)")
    print("\n3. Cyclic Sort Approach O(n) O(1):")
    print("   - Place each positive number x at index x-1")
    print("   - After placing, find first index where arr[i] ≠ i+1")
    print("   - Return i+1")
    print("   - Time: O(n), Space: O(1)")
    print("\n4. Partition + Marking O(n) O(1):")
    print("   - Move positive numbers to front")
    print("   - Use sign to mark presence")
    print("   - Find first unmarked position")
    print("   - Time: O(n), Space: O(1)")
    print("\nKey Insight: For array of size n, answer must be in range [1, n+1]")
    print("=" * 70)
