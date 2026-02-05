"""
K-th Non-Repeating Character

Given a string str of length n and a number k, find the kth non-repeating character in the string.

Time Complexity: O(n), where n is the length of the string
Space Complexity: O(n) for the hash map (or O(1) if using fixed-size array for lowercase letters)

Examples:
- Input: str = "geeksforgeeks", k = 3, Output: "r"
- Input: str = "geeksforgeeks", k = 2, Output: "o"
- Input: str = "geeksforgeeks", k = 4, Output: "Less than k non-repeating characters"
"""


def kth_non_repeating_char(s: str, k: int) -> str:
    """
    Find the kth non-repeating character in a string.

    Args:
        s: Input string
        k: The position of non-repeating character to find (1-indexed)

    Returns:
        The kth non-repeating character as string, or error message if not found
    """
    # Count character frequencies
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find kth non-repeating character
    non_repeating_count = 0
    for char in s:
        if char_count[char] == 1:
            non_repeating_count += 1
            if non_repeating_count == k:
                return char

    return "Less than k non-repeating characters"


def kth_non_repeating_char_array(s: str, k: int) -> str:
    """
    Alternative implementation using array for lowercase English letters only.
    More space efficient for lowercase strings.

    Args:
        s: Input string (lowercase English letters only)
        k: The position of non-repeating character to find (1-indexed)

    Returns:
        The kth non-repeating character as string, or error message if not found
    """
    # For lowercase English letters only
    char_count = [0] * 26

    # Count character frequencies
    for char in s:
        if "a" <= char <= "z":
            char_count[ord(char) - ord("a")] += 1

    # Find kth non-repeating character
    non_repeating_count = 0
    for char in s:
        if "a" <= char <= "z" and char_count[ord(char) - ord("a")] == 1:
            non_repeating_count += 1
            if non_repeating_count == k:
                return char

    return "Less than k non-repeating characters"


def test_kth_non_repeating_char():
    """Test cases for kth_non_repeating_char function."""
    test_cases = [
        ("geeksforgeeks", 3, "r"),
        ("geeksforgeeks", 2, "o"),
        ("geeksforgeeks", 1, "f"),
        ("geeksforgeeks", 4, "Less than k non-repeating characters"),
        ("abcabcde", 1, "d"),
        ("abcabcde", 2, "e"),
        ("aaaa", 1, "Less than k non-repeating characters"),
        ("", 1, "Less than k non-repeating characters"),
        ("a", 1, "a"),
        ("ab", 2, "b"),
    ]

    for i, (input_str, k, expected) in enumerate(test_cases):
        result = kth_non_repeating_char(input_str, k)
        assert result == expected, (
            f"Test case {i} failed: kth_non_repeating_char('{input_str}', {k}) = '{result}', expected '{expected}'"
        )

    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    test_strings = [
        ("geeksforgeeks", 3),
        ("geeksforgeeks", 2),
        ("abcabcde", 1),
        ("aaaa", 1),
    ]

    print("K-th Non-Repeating Character Finder:")
    for s, k in test_strings:
        result = kth_non_repeating_char(s, k)
        print(f"String: '{s}', k={k} -> {result}")

    print("\nRunning tests...")
    test_kth_non_repeating_char()
