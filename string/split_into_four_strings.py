"""
Split the Given String into Four Distinct Strings

Given a string, split it into four distinct non-empty strings.
If not possible, return empty list.

Approach: Backtracking - O(n^3) Time and O(1) Space
Try all possible ways to split the string into 4 parts.
"""


def split_into_four(s):
    """
    Split string into four distinct non-empty parts.

    Args:
        s: Input string

    Returns:
        List of 4 distinct strings or empty list
    """
    n = len(s)

    if n < 4:
        return []

    # Try all possible splits
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:]

                # Check if all are distinct
                parts = [s1, s2, s3, s4]
                if len(set(parts)) == 4:
                    return parts

    return []


def main():
    """Test cases for splitting into four strings."""
    test_cases = [
        ("abcd", ["a", "b", "c", "d"]),
        ("hello", ["h", "e", "l", "lo"]),
        ("aaaa", []),
        ("abcdef", ["a", "b", "c", "def"]),
        ("abc", []),
    ]

    print("=" * 50)
    print("Split into Four Distinct Strings")
    print("=" * 50)

    for s, expected in test_cases:
        result = split_into_four(s)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: '{s}'")
        print(f"Output: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
