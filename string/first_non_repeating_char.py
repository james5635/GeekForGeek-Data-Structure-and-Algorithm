"""
First Non-Repeating Character of Given String

Given a string s of lowercase English letters, find the first non-repeating character.
If there is no such character, return '$'.

Approach: Using Frequency Array (Two Traversal) - O(2*n) Time and O(MAX_CHAR) Space
"""

MAX_CHAR = 26


def first_non_repeating_char(s):
    """
    Find the first non-repeating character in a string.

    Args:
        s: Input string containing lowercase English letters

    Returns:
        First non-repeating character or '$' if all repeat
    """
    freq = [0] * MAX_CHAR

    for c in s:
        freq[ord(c) - ord("a")] += 1

    for c in s:
        if freq[ord(c) - ord("a")] == 1:
            return c

    return "$"


def main():
    """Test cases for first non-repeating character."""
    test_cases = [
        ("geeksforgeeks", "f"),
        ("racecar", "e"),
        ("aabbccc", "$"),
        ("abcdef", "a"),
        ("aabb", "$"),
    ]

    print("=" * 50)
    print("First Non-Repeating Character")
    print("=" * 50)

    for s, expected in test_cases:
        result = first_non_repeating_char(s)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: '{s}'")
        print(f"Output: '{result}'")
        print(f"Expected: '{expected}' {status}")


if __name__ == "__main__":
    main()
