"""
Two Sum - Check if Pair Exists

Check if there exists a pair with given sum.

Approaches:
1. Naive: Check all pairs - O(n²) time, O(1) space
2. Better: Sort + Binary Search - O(n log n) time, O(1) or O(n) space
3. Better: Sort + Two Pointer - O(n log n) time, O(1) or O(n) space
4. Optimal: HashSet - O(n) time, O(n) space
"""


def two_sum_naive(arr, target):
    """
    Naive approach: Check all pairs.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: List of integers
        target: Target sum

    Returns:
        True if pair exists, False otherwise
    """
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return True
    return False


def two_sum_sort_binary_search(arr, target):
    """
    Better approach: Sort and use binary search.

    Time Complexity: O(n log n)
    Space Complexity: O(1) or O(n) depending on sort

    Algorithm:
    - Sort the array
    - For each element, binary search for (target - element)

    Args:
        arr: List of integers
        target: Target sum

    Returns:
        True if pair exists, False otherwise
    """
    sorted_arr = sorted(arr)
    n = len(sorted_arr)

    for i in range(n):
        complement = target - sorted_arr[i]
        # Binary search for complement in remaining array
        left, right = i + 1, n - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_arr[mid] == complement:
                return True
            elif sorted_arr[mid] < complement:
                left = mid + 1
            else:
                right = mid - 1

    return False


def two_sum_sort_two_pointer(arr, target):
    """
    Better approach: Sort and use two pointers.

    Time Complexity: O(n log n)
    Space Complexity: O(1) or O(n) depending on sort

    Algorithm:
    - Sort the array
    - Use two pointers from both ends
    - If sum < target, move left pointer right
    - If sum > target, move right pointer left
    - If sum == target, found!

    Args:
        arr: List of integers
        target: Target sum

    Returns:
        True if pair exists, False otherwise
    """
    sorted_arr = sorted(arr)
    left, right = 0, len(sorted_arr) - 1

    while left < right:
        current_sum = sorted_arr[left] + sorted_arr[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False


def two_sum_hashset(arr, target):
    """
    Optimal approach: Using HashSet.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Algorithm:
    - Use set to store seen elements
    - For each element, check if (target - element) is in set
    - If yes, pair exists; else add current element to set

    Args:
        arr: List of integers
        target: Target sum

    Returns:
        True if pair exists, False otherwise
    """
    seen = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)

    return False


def two_sum_hashset_with_indices(arr, target):
    """
    HashSet approach that also returns the pair indices.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Returns:
        Tuple of indices (i, j) or None
    """
    seen = {}  # value -> index

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i

    return None


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 4, 45, 6, 10, -8], 16, True),  # 6 + 10 = 16
        ([1, 2, 4, 3, 2], 6, True),  # 2 + 4 = 6 or 3 + 3 (but 3 appears once)
        ([1, 2, 3, 4, 5], 10, False),  # No pair sums to 10
        ([5, 5], 10, True),  # 5 + 5 = 10
        ([-1, -2, -3, 4, 5], 2, True),  # -1 + 3 (no 3), -2 + 4 = 2
        ([0, 0], 0, True),  # 0 + 0 = 0
        ([1], 2, False),  # Single element
        ([], 5, False),  # Empty array
    ]

    print("=" * 70)
    print("Two Sum - Check if Pair Exists")
    print("=" * 70)

    for i, (arr, target, expected) in enumerate(test_cases, 1):
        naive = two_sum_naive(arr, target)
        sort_bs = two_sum_sort_binary_search(arr, target)
        sort_tp = two_sum_sort_two_pointer(arr, target)
        hashset = two_sum_hashset(arr, target)

        all_match = naive == sort_bs == sort_tp == hashset == expected

        print(f"\nTest {i}: arr = {arr}, target = {target}")
        print(f"  Expected:               {expected}")
        print(f"  Naive O(n²):            {naive}")
        print(f"  Sort + Binary Search:   {sort_bs}")
        print(f"  Sort + Two Pointer:     {sort_tp}")
        print(f"  HashSet O(n):           {hashset} {'✓' if all_match else '✗'}")

        # Show pair if found
        pair = two_sum_hashset_with_indices(arr, target)
        if pair:
            print(
                f"  Pair found: arr[{pair[0]}] + arr[{pair[1]}] = {arr[pair[0]]} + {arr[pair[1]]} = {target}"
            )

    print("\n" + "=" * 70)
    print("\nApproach Summary:")
    print("  1. Naive:         O(n²) time, O(1) space - Simple")
    print("  2. Sort + BS:     O(n log n) time, O(1) space - Requires sorted")
    print("  3. Sort + 2 Ptr:  O(n log n) time, O(1) space - Efficient with sorting")
    print("  4. HashSet:       O(n) time, O(n) space - Fastest, uses extra space")
    print("=" * 70)
