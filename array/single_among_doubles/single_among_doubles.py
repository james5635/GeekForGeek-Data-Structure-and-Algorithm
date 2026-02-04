"""
Single Among Doubles

Find the element that appears only once (all others appear exactly twice).

Approaches:
1. Using XOR operation - O(n) time, O(1) space

Key Insight:
- XOR of a number with itself is 0
- XOR of a number with 0 is the number itself
- XOR is associative and commutative
"""


def find_single_xor(arr):
    """
    Find single element using XOR operation.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Properties of XOR:
    1. a ^ a = 0 (XOR of same number is 0)
    2. a ^ 0 = a (XOR with 0 is the number)
    3. a ^ b = b ^ a (Commutative)
    4. (a ^ b) ^ c = a ^ (b ^ c) (Associative)

    Algorithm:
    - XOR all elements together
    - Pairs will cancel out (a ^ a = 0)
    - Single element remains (0 ^ x = x)

    Args:
        arr: List of integers where every element appears twice except one

    Returns:
        The element that appears only once
    """
    result = 0
    for num in arr:
        result ^= num
    return result


def find_single_hashset(arr):
    """
    Alternative approach using HashSet.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Algorithm:
    - Use set to track seen elements
    - If element seen before, remove it
    - If element not seen, add it
    - Remaining element is the single one

    Args:
        arr: List of integers where every element appears twice except one

    Returns:
        The element that appears only once
    """
    seen = set()
    for num in arr:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)
    return seen.pop()


def find_single_sorting(arr):
    """
    Alternative approach using sorting.

    Time Complexity: O(n log n)
    Space Complexity: O(1) or O(n) depending on sort

    Algorithm:
    - Sort the array
    - Check adjacent pairs
    - Element without pair is the single one

    Args:
        arr: List of integers where every element appears twice except one

    Returns:
        The element that appears only once
    """
    sorted_arr = sorted(arr)
    n = len(sorted_arr)

    # Check pairs
    for i in range(0, n - 1, 2):
        if sorted_arr[i] != sorted_arr[i + 1]:
            return sorted_arr[i]

    # If not found in pairs, it's the last element
    return sorted_arr[-1]


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [2, 3, 5, 4, 5, 3, 4],
        [1, 2, 1, 2, 3],
        [7],
        [1, 1, 2],
        [5, 5, 6, 6, 7, 8, 8],
        [-1, -1, -2, -2, -3],
        [0, 0, 1],
    ]

    print("=" * 70)
    print("Single Among Doubles - Find Element Appearing Once")
    print("=" * 70)
    print("\nGiven an array where every element appears twice except one,")
    print("find the element that appears only once.\n")

    for i, arr in enumerate(test_cases, 1):
        xor_result = find_single_xor(arr)
        hashset_result = find_single_hashset(arr)
        sorting_result = find_single_sorting(arr)

        match = "✓" if xor_result == hashset_result == sorting_result else "✗"

        print(f"Test {i}: arr = {arr}")
        print(f"  XOR Approach O(n):      {xor_result}")
        print(f"  HashSet Approach O(n):  {hashset_result}")
        print(f"  Sorting O(n log n):     {sorting_result} {match}")
        print()

    print("=" * 70)
    print("\nXOR Approach Explanation:")
    print("  XOR properties:")
    print("    - a ^ a = 0 (same numbers cancel out)")
    print("    - a ^ 0 = a (keeps the number)")
    print("  When we XOR all elements:")
    print("    - Pairs become 0 (a ^ a = 0)")
    print("    - Single element remains (0 ^ x = x)")
    print("\nExample: [2, 3, 5, 4, 5, 3, 4]")
    print("  2 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4")
    print("  = 2 ^ (3 ^ 3) ^ (5 ^ 5) ^ (4 ^ 4)")
    print("  = 2 ^ 0 ^ 0 ^ 0 = 2")
    print("=" * 70)
