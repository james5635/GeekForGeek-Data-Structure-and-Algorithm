"""
Check if Two Strings are Isomorphic

Problem Description:
Two strings str1 and str2 are called isomorphic if there is a one-to-one mapping
possible for every character of str1 to every character of str2. All occurrences
of a character must be replaced with another character while preserving the
order of characters. No two characters may map to the same character.

Time Complexity: O(n) where n is the length of the strings
Space Complexity: O(1) - Using fixed size dictionaries (256 possible characters)

Implementation:
- Use two dictionaries to track character mappings
- Check if mapping is consistent in both directions
"""


def are_strings_isomorphic(str1: str, str2: str) -> bool:
    """
    Check if two strings are isomorphic.

    Args:
        str1: First string
        str2: Second string

    Returns:
        True if strings are isomorphic, False otherwise
    """
    if len(str1) != len(str2):
        return False

    # Dictionaries to store character mappings
    char_map = {}  # str1 -> str2
    reverse_map = {}  # str2 -> str1

    for i in range(len(str1)):
        char1 = str1[i]
        char2 = str2[i]

        # Check if char1 is already mapped
        if char1 in char_map:
            if char_map[char1] != char2:
                return False
        else:
            # Check if char2 is already mapped to another character
            if char2 in reverse_map:
                return False
            char_map[char1] = char2
            reverse_map[char2] = char1

    return True


def main():
    """Test cases for are_strings_isomorphic function."""
    test_cases = [
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("ab", "aa", False),
        ("aab", "xxy", True),
        ("aab", "xyz", False),
        ("", "", True),
        ("a", "b", True),
        ("abc", "def", True),
        ("abc", "dee", False),
    ]

    print("Testing are_strings_isomorphic function:")
    for i, (str1, str2, expected) in enumerate(test_cases):
        result = are_strings_isomorphic(str1, str2)
        status = "✓" if result == expected else "✗"
        print(f"Test {i + 1}: {status} '{str1}' vs '{str2}' -> {result}")


if __name__ == "__main__":
    main()
