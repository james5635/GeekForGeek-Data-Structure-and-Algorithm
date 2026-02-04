"""
Only Repeating Element in Range [1, n-1]

Given an array of size n containing elements from 1 to n-1 with one element repeating,
find the only repeating element.

Approaches:
1. Sorting: O(n log n) time, O(1) or O(n) space
2. HashSet: O(n) time, O(n) space
3. Sum Formula: O(n) time, O(1) space
4. XOR: O(n) time, O(1) space
5. Floyd's Cycle Detection: O(n) time, O(1) space (treats array as linked list)
"""


def find_repeating_sorting(arr):
    """
    Approach 1: Sorting.

    Time Complexity: O(n log n)
    Space Complexity: O(1) if in-place, O(n) otherwise

    Algorithm:
    - Sort the array
    - Find adjacent duplicates

    Args:
        arr: List of integers from 1 to n-1 with one repeating

    Returns:
        The repeating element
    """
    sorted_arr = sorted(arr)
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] == sorted_arr[i + 1]:
            return sorted_arr[i]
    return -1


def find_repeating_hashset(arr):
    """
    Approach 2: HashSet.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Algorithm:
    - Use set to track seen elements
    - Return element already in set

    Args:
        arr: List of integers from 1 to n-1 with one repeating

    Returns:
        The repeating element
    """
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1


def find_repeating_sum(arr):
    """
    Approach 3: Sum Formula.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - Sum of 1..(n-1) = (n-1)*n/2
    - Actual sum - Expected sum = Repeating element

    Args:
        arr: List of integers from 1 to n-1 with one repeating

    Returns:
        The repeating element
    """
    n = len(arr)
    expected_sum = (n - 1) * n // 2
    actual_sum = sum(arr)
    return actual_sum - expected_sum


def find_repeating_xor(arr):
    """
    Approach 4: XOR.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - XOR all elements
    - XOR with 1 to n-1
    - Result is repeating element (others cancel out)

    Args:
        arr: List of integers from 1 to n-1 with one repeating

    Returns:
        The repeating element
    """
    n = len(arr)
    result = 0

    # XOR all array elements
    for num in arr:
        result ^= num

    # XOR with 1 to n-1
    for i in range(1, n):
        result ^= i

    return result


def find_repeating_floyd(arr):
    """
    Approach 5: Floyd's Cycle Detection (Tortoise and Hare).

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - Treat array as linked list where arr[i] points to index arr[i]
    - Since there's a duplicate, there must be a cycle
    - Use slow and fast pointers to find cycle
    - Find entry point of cycle (repeating element)

    Args:
        arr: List of integers from 1 to n-1 with one repeating

    Returns:
        The repeating element
    """
    # Phase 1: Find meeting point
    slow = arr[0]
    fast = arr[0]

    while True:
        slow = arr[slow]  # Move 1 step
        fast = arr[arr[fast]]  # Move 2 steps
        if slow == fast:
            break

    # Phase 2: Find entry point of cycle
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 3, 3, 4],  # n=5, range [1,4], repeating=3
        [1, 1],  # n=2, range [1,1], repeating=1
        [1, 2, 3, 4, 4],  # n=5, repeating=4
        [2, 2, 3, 4, 5],  # n=5, repeating=2
        [1, 2, 3, 4, 5, 6, 7, 8, 8, 9],  # n=10, repeating=8
    ]

    print("=" * 70)
    print("Only Repeating Element in Range [1, n-1]")
    print("=" * 70)
    print("\nArray contains elements 1 to n-1 with exactly one element repeating.\n")

    for i, arr in enumerate(test_cases, 1):
        n = len(arr)

        sorting_result = find_repeating_sorting(arr)
        hashset_result = find_repeating_hashset(arr)
        sum_result = find_repeating_sum(arr)
        xor_result = find_repeating_xor(arr)
        floyd_result = find_repeating_floyd(arr)

        all_match = (
            sorting_result == hashset_result == sum_result == xor_result == floyd_result
        )

        print(f"Test {i}: arr = {arr}, n = {n}, range = [1, {n - 1}]")
        print(f"  Sorting O(n log n):    {sorting_result}")
        print(f"  HashSet O(n):          {hashset_result}")
        print(f"  Sum Formula O(n):      {sum_result}")
        print(f"  XOR O(n):              {xor_result}")
        print(f"  Floyd's Cycle O(n):    {floyd_result} {'✓' if all_match else '✗'}")
        print()

    print("=" * 70)
    print("\nApproach Summary:")
    print("  1. Sorting:      Simple but slower, O(n log n)")
    print("  2. HashSet:      Fast but uses extra space, O(n)")
    print("  3. Sum Formula:  Fast, O(1) space, risk of overflow")
    print("  4. XOR:          Fast, O(1) space, no overflow")
    print("  5. Floyd's:      Fast, O(1) space, clever cycle detection")
    print("\nFloyd's Cycle Detection:")
    print("  - Treat array values as pointers to indices")
    print("  - Duplicate creates a cycle in this 'linked list'")
    print("  - Find cycle entry point (repeating element)")
    print("=" * 70)
