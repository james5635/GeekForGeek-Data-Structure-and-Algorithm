"""
First Non-Repeating Character

Find the first non-repeating character in a string.

Time Complexity: O(n)
Space Complexity: O(1) - Using constant space for character count (256 for ASCII)
"""


def first_non_repeating_character(s: str) -> str:
    """
    Returns the first non-repeating character in the string.
    If all characters are repeating, returns -1.

    Args:
        s: Input string

    Returns:
        First non-repeating character or -1 if none exists
    """
    # Count character frequencies
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char

    return -1


def first_non_repeating_character_optimized(s: str) -> str:
    """
    Optimized version using list for ASCII characters.
    """
    # For ASCII characters, we can use a fixed-size array
    count = [0] * 256

    # Count frequencies
    for char in s:
        count[ord(char)] += 1

    # Find first non-repeating character
    for char in s:
        if count[ord(char)] == 1:
            return char

    return -1


def test_first_non_repeating_character():
    """Test cases for first non-repeating character."""
    test_cases = [
        ("geeksforgeeks", "f"),
        ("abacabad", "c"),
        ("abacabaabacaba", -1),
        ("", -1),
        ("a", "a"),
        ("aaab", "b"),
        ("abcabcde", "d"),
        ("xxyyzz", -1),
        ("abcbad", "c"),
        ("test", "e"),
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = first_non_repeating_character(input_str)
        assert result == expected, (
            f"Test case {i} failed: Expected {expected}, got {result}"
        )

    print("All test cases passed!")


if __name__ == "__main__":
    test_first_non_repeating_character()

    # Example usage
    s = "geeksforgeeks"
    result = first_non_repeating_character(s)
    print(f"First non-repeating character in '{s}': {result}")
