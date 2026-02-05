"""
Print All Permutations of a Given String

Given a string s, return all permutations in lexicographically sorted order.

Approach: Backtracking - O(n * n!) Time and O(n!) Space
Use recursion to generate all permutations by swapping characters.
Handles duplicates by skipping repeated characters at each position.
"""


def find_permutations(s):
    """
    Find all unique permutations of string.

    Args:
        s: Input string

    Returns:
        List of all unique permutations sorted
    """

    def backtrack(start):
        if start == len(chars):
            result.append("".join(chars))
            return

        used = set()  # Track characters used at this position to avoid duplicates
        for i in range(start, len(chars)):
            if chars[i] in used:
                continue
            used.add(chars[i])
            chars[start], chars[i] = chars[i], chars[start]
            backtrack(start + 1)
            chars[start], chars[i] = chars[i], chars[start]  # Backtrack

    result = []
    chars = list(s)
    backtrack(0)
    result.sort()
    return result


def main():
    """Test cases for string permutations."""
    test_cases = [
        ("ABC", ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]),
        ("XY", ["XY", "YX"]),
        ("AAB", ["AAB", "ABA", "BAA"]),
    ]

    print("=" * 50)
    print("String Permutations")
    print("=" * 50)

    for s, expected in test_cases:
        result = find_permutations(s)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: '{s}'")
        print(f"Output: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
