"""
Split Array into Three Equal Sum Subarrays

Determine if array can be split into three contiguous subarrays with equal sum.

Approaches:
1. Naive: Check all split points - O(n³) time, O(1) space
2. Optimal: Using prefix sum - O(n) time, O(1) space
"""


def can_split_three_equal_naive(arr):
    """
    Naive approach: Try all possible split points.

    Time Complexity: O(n³)
    Space Complexity: O(1)

    Algorithm:
    - Try all possible i and j where i < j
    - Calculate sum of three parts: [0,i], [i+1,j], [j+1,n-1]
    - Check if all three sums are equal

    Args:
        arr: List of integers

    Returns:
        True if array can be split, False otherwise
    """
    n = len(arr)
    if n < 3:
        return False

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            sum1 = sum(arr[0 : i + 1])
            sum2 = sum(arr[i + 1 : j + 1])
            sum3 = sum(arr[j + 1 : n])

            if sum1 == sum2 == sum3:
                return True

    return False


def can_split_three_equal_prefix(arr):
    """
    Better approach: Using prefix sum array.

    Time Complexity: O(n²)
    Space Complexity: O(n)

    Algorithm:
    - Precompute prefix sums
    - Try all split points using prefix sums for O(1) range sum

    Args:
        arr: List of integers

    Returns:
        True if array can be split, False otherwise
    """
    n = len(arr)
    if n < 3:
        return False

    # Compute prefix sum
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    total = prefix[n]

    # Total must be divisible by 3
    if total % 3 != 0:
        return False

    target = total // 3

    # Find first point where prefix sum = target
    for i in range(n - 2):
        if prefix[i + 1] == target:
            # Find second point where prefix sum = 2*target
            for j in range(i + 1, n - 1):
                if prefix[j + 1] == 2 * target:
                    return True

    return False


def can_split_three_equal_optimal(arr):
    """
    Optimal approach: Single pass using prefix sum.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - Calculate total sum
    - If not divisible by 3, return False
    - Track running sum, count how many times we hit target and 2*target
    - Need to hit target before 2*target, and 2*target before end

    Args:
        arr: List of integers

    Returns:
        True if array can be split, False otherwise
    """
    n = len(arr)
    if n < 3:
        return False

    total = sum(arr)

    # Total sum must be divisible by 3
    if total % 3 != 0:
        return False

    target = total // 3
    running_sum = 0
    count = 0  # Count of partitions found

    # We need two partitions, third is automatic
    for i in range(n - 1):  # Exclude last element for third partition
        running_sum += arr[i]

        if running_sum == target:
            count += 1
            running_sum = 0  # Reset for next partition

            if count == 2:
                # Found two partitions, third is remaining
                return True

    return False


def find_split_indices(arr):
    """
    Find the actual split indices.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Returns:
        Tuple (i, j) where array splits at i and j, or None
    """
    n = len(arr)
    if n < 3:
        return None

    total = sum(arr)

    if total % 3 != 0:
        return None

    target = total // 3
    running_sum = 0
    first_cut = -1

    for i in range(n - 1):
        running_sum += arr[i]

        if running_sum == target and first_cut == -1:
            first_cut = i
            running_sum = 0
        elif running_sum == target and first_cut != -1:
            return (first_cut, i)

    return None


def get_three_partitions(arr):
    """
    Get the actual three partitions.

    Returns:
        List of three subarrays or None
    """
    indices = find_split_indices(arr)
    if indices is None:
        return None

    i, j = indices
    return [arr[0 : i + 1], arr[i + 1 : j + 1], arr[j + 1 :]]


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 3, 4, 0, 4],  # Can split: [1,3], [4], [0,4] - all sum to 4
        [0, 0, 0, 0],  # Can split: multiple ways
        [1, 1, 1, 1, 1, 1],  # Can split: [1,1], [1,1], [1,1]
        [1, 2, 3, 4, 5],  # Cannot split: total = 15, not divisible by 3
        [3, 3, 3],  # Can split: [3], [3], [3]
        [1, 2],  # Cannot split: less than 3 elements
        [5, 5, 5, 5, 5, 5, 5, 5, 5],  # total=45, each=15: [5,5,5], [5,5,5], [5,5,5]
        [0, 1, -1, 0],  # Can split: [0], [1,-1], [0]
    ]

    print("=" * 70)
    print("Split Array into Three Equal Sum Subarrays")
    print("=" * 70)
    print("\nCheck if array can be split into three contiguous parts with equal sum.\n")

    for i, arr in enumerate(test_cases, 1):
        naive = can_split_three_equal_naive(arr)
        prefix = can_split_three_equal_prefix(arr)
        optimal = can_split_three_equal_optimal(arr)
        indices = find_split_indices(arr)
        partitions = get_three_partitions(arr)

        all_match = naive == prefix == optimal

        print(f"Test {i}: arr = {arr}")
        print(f"  Total sum: {sum(arr)}")
        print(f"  Naive O(n³):         {naive}")
        print(f"  Prefix O(n²):        {prefix}")
        print(f"  Optimal O(n):        {optimal} {'✓' if all_match else '✗'}")

        if indices:
            print(f"  Split indices:       {indices}")
            print(f"  Partitions:          {partitions}")
            if partitions:
                sums = [sum(p) for p in partitions]
                print(f"  Partition sums:      {sums}")
        print()

    print("=" * 70)
    print("\nOptimal Approach Explanation:")
    print("  1. Calculate total sum")
    print("  2. If not divisible by 3, return False")
    print("  3. Each partition should sum to total/3")
    print("  4. Traverse array, accumulate sum")
    print("  5. When sum equals target, we found a partition")
    print("  6. Need exactly 2 partitions, 3rd is automatic")
    print("=" * 70)
