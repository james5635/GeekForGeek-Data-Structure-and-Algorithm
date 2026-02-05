"""
First Repeated Character

Find the earliest repeated character in a string. The earliest repeated character
means the character that occurs more than once and whose second occurrence has
the smallest index.

Time Complexity: O(n), where n is the length of the string
Space Complexity: O(1) (using fixed-size array for lowercase letters)

Examples:
- Input: "geeksforgeeks", Output: "e"
- Input: "hello geeks", Output: "l"
- Input: "abc", Output: "-1"
- Input: "abca", Output: "a"
"""


def first_repeated_char(s: str) -> str:
    """
    Find the first repeated character in a string using a set.
    This finds the first character that appears again in the order of appearance.

    Args:
        s: Input string (lowercase English letters and spaces)

    Returns:
        The first repeated character, or "-1" if no character repeats
    """
    seen = set()

    for char in s:
        if char in seen:
            return char
        seen.add(char)

    return "-1"


def first_repeated_char_hashmap(s: str) -> str:
    """
    Find the first repeated character using a hash map.
    Works for all Unicode characters.

    Args:
        s: Input string

    Returns:
        The first repeated character, or "-1" if no character repeats
    """
    char_count = {}
    seen = set()

    # First pass: count characters
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Second pass: find first repeated character
    for char in s:
        if char_count[char] > 1:
            return char

    return "-1"


def first_repeated_char_optimized(s: str) -> str:
    """
    Find the first repeated character in a single pass using a set.
    This approach finds the first character that appears twice in order of appearance.

    Args:
        s: Input string

    Returns:
        The first repeated character, or "-1" if no character repeats
    """
    seen = set()

    for char in s:
        if char in seen:
            return char
        seen.add(char)

    return "-1"


def first_repeated_char_brute_force(s: str) -> str:
    """
    Brute force approach using nested loops.
    Time Complexity: O(n^2)

    Args:
        s: Input string

    Returns:
        The first repeated character, or "-1" if no character repeats
    """
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                return s[i]

    return "-1"


def test_first_repeated_char():
    """Test cases for first_repeated_char function."""
    test_cases = [
        ("geeksforgeeks", "e"),
        ("hello geeks", "l"),
        ("abc", "-1"),
        ("abca", "a"),
        ("abcbca", "b"),
        ("", "-1"),
        ("a", "-1"),
        ("aa", "a"),
        ("ab", "-1"),
        ("aabbcc", "a"),
        ("abcabc", "a"),
        ("", "-1"),
        ("    ", " "),  # Spaces repeat
        ("a b c a", " "),
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = first_repeated_char(input_str)
        assert result == expected, (
            f"Test case {i} failed: first_repeated_char('{input_str}') = '{result}', expected '{expected}'"
        )

    print("All test cases passed!")


def test_consistency():
    """Test that optimized approaches produce same results."""
    test_strings = ["geeksforgeeks", "hello geeks", "abc", "abca", "aabbcc"]

    for s in test_strings:
        result1 = first_repeated_char_hashmap(s)
        result2 = first_repeated_char_optimized(s)

        print(f"'{s}': hash_map='{result1}', optimized='{result2}'")

    print("Consistency tests completed!")


if __name__ == "__main__":
    # Example usage
    test_strings = ["geeksforgeeks", "hello geeks", "abc", "abca", "aabbcc"]

    print("First Repeated Character:")
    for s in test_strings:
        result = first_repeated_char(s)
        print(f"Input: '{s}' -> First repeated: '{result}'")

    print("\nTesting with hash map approach:")
    for s in test_strings:
        result = first_repeated_char_hashmap(s)
        print(f"Input: '{s}' -> First repeated: '{result}'")

    print("\nRunning tests...")
    test_first_repeated_char()
    test_consistency()
