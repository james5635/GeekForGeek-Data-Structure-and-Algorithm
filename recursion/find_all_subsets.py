"""
Find All Subsets using Backtracking

Given an integer array, find all the subsets of the array.
A subset is any selection of elements from an array where order doesn't matter.

Approach: Backtracking
- For each element, we have two choices: include it or exclude it
- Recursively explore both choices
- When we reach the end of array, add current subset to results

Examples:
    Input: [1, 2, 3]
    Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

    Input: [2, 4]
    Output: [[], [2], [2, 4], [4]]
"""


def subsetRecur(i: int, arr: list, res: list, subset: list) -> None:
    """
    Recursive function to find all subsets using backtracking.

    Args:
        i: Current index in array
        arr: Input array
        res: Result list to store all subsets
        subset: Current subset being built
    """
    # Base case: If we've processed all elements
    if i == len(arr):
        res.append(list(subset))  # Add copy of current subset
        return

    # Choice 1: Include the current element
    subset.append(arr[i])
    subsetRecur(i + 1, arr, res, subset)

    # Backtrack: Remove the element we just added
    subset.pop()

    # Choice 2: Exclude the current element
    subsetRecur(i + 1, arr, res, subset)


def subsets(arr: list) -> list:
    """
    Find all subsets of given array using backtracking.

    Args:
        arr: Input array of integers

    Returns:
        List of all subsets

    Time Complexity: O(n * 2^n)
    Space Complexity: O(n) for recursion stack
    """
    subset = []
    res = []
    subsetRecur(0, arr, res, subset)
    return res


def subsets_bit_manipulation(arr: list) -> list:
    """
    Alternative: Find all subsets using bit manipulation.

    For an array of size n, there are 2^n subsets.
    Each subset can be represented by a number from 0 to 2^n - 1
    where each bit indicates if an element is included.

    Time Complexity: O(n * 2^n)
    Space Complexity: O(1) auxiliary
    """
    n = len(arr)
    res = []

    # Loop through all possible subsets (0 to 2^n - 1)
    for i in range(1 << n):
        subset = []

        # Check each bit position
        for j in range(n):
            # If j-th bit is set, include arr[j]
            if i & (1 << j):
                subset.append(arr[j])

        res.append(subset)

    return res


def printSubsets(res: list) -> None:
    """Helper function to print subsets in a readable format."""
    print("[")
    for subset in res:
        print(f"  {subset}")
    print("]")


def main():
    """Test the subset functions."""
    print("=" * 60)
    print("Find All Subsets using Backtracking")
    print("=" * 60)

    test_cases = [[1, 2, 3], [2, 4], [1, 2, 3, 4]]

    for arr in test_cases:
        print(f"\nInput: {arr}")
        print("-" * 40)

        # Using backtracking
        print("Using Backtracking:")
        result_backtrack = subsets(arr)
        print(f"Total subsets: {len(result_backtrack)}")
        printSubsets(result_backtrack)

        # Using bit manipulation
        print("\nUsing Bit Manipulation:")
        result_bits = subsets_bit_manipulation(arr)
        print(f"Total subsets: {len(result_bits)}")
        printSubsets(result_bits)

    print("\n" + "=" * 60)
    print("Complexity Analysis:")
    print("=" * 60)
    print("Number of subsets for array of size n: 2^n")
    print("Backtracking Approach:")
    print("  Time: O(n * 2^n)")
    print("  Space: O(n) - recursion stack depth")
    print("Bit Manipulation Approach:")
    print("  Time: O(n * 2^n)")
    print("  Space: O(1) - no recursion stack needed")


if __name__ == "__main__":
    main()
