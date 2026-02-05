"""
String Permutations using Recursion

Given a string, generate all permutations of the string in lexicographically
sorted order. A permutation is the rearrangement of all the elements.

Approach: Backtracking with Swap
- Use recursion and backtracking to generate all permutations
- For each index, swap with all elements to its right and recurse
- Backtrack by swapping back to original state

Examples:
    Input: "ABC"
    Output: ABC ACB BAC BCA CAB CBA

    Input: "XY"
    Output: XY YX
"""


def recurPermute(index: int, s: list, ans: list) -> None:
    """
    Recursive function to generate all permutations.

    Args:
        index: Current index being processed
        s: List of characters (mutable)
        ans: List to store all permutations
    """
    # Base Case: If we've processed all characters
    if index == len(s):
        ans.append("".join(s))
        return

    # Swap current index with all possible indices and recurse
    for i in range(index, len(s)):
        # Swap
        s[index], s[i] = s[i], s[index]
        # Recurse to next index
        recurPermute(index + 1, s, ans)
        # Backtrack: swap back
        s[index], s[i] = s[i], s[index]


def findPermutation(s: str) -> list:
    """
    Find all unique permutations of a given string.

    Args:
        s: Input string

    Returns:
        List of all permutations sorted lexicographically

    Time Complexity: O(n * n!)
    Space Complexity: O(n!)
    """
    ans = []
    recurPermute(0, list(s), ans)
    ans.sort()  # Sort the resultant list
    return ans


def findPermutationUnique(s: str) -> list:
    """
    Find all unique permutations (handles duplicates).

    Args:
        s: Input string (may contain duplicates)

    Returns:
        List of unique permutations
    """
    ans = set()

    def backtrack(index, chars):
        if index == len(chars):
            ans.add("".join(chars))
            return

        for i in range(index, len(chars)):
            chars[index], chars[i] = chars[i], chars[index]
            backtrack(index + 1, chars)
            chars[index], chars[i] = chars[i], chars[index]

    backtrack(0, list(s))
    return sorted(list(ans))


def main():
    """Test the permutation functions."""
    print("=" * 60)
    print("String Permutations using Recursion")
    print("=" * 60)

    test_cases = ["ABC", "XY", "AAA", "AAB"]

    for s in test_cases:
        print(f"\nInput: '{s}'")
        print("-" * 40)

        # All permutations
        result = findPermutation(s)
        print(f"All permutations ({len(result)} total):")
        print("  " + " ".join(result))

        # Unique permutations
        unique_result = findPermutationUnique(s)
        if len(unique_result) != len(result):
            print(f"Unique permutations ({len(unique_result)} total):")
            print("  " + " ".join(unique_result))

    print("\n" + "=" * 60)
    print("Complexity Analysis:")
    print("=" * 60)
    print("Time Complexity: O(n * n!)")
    print("  - There are n! permutations")
    print("  - Creating each string takes O(n) time")
    print("Space Complexity: O(n!)")
    print("  - To store all n! permutations")


if __name__ == "__main__":
    main()
