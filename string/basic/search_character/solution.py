"""
Search Character in String
===========================

Problem Description:
--------------------
Given a string and a character, search for the character in the string.
Return the first index where the character appears, or -1 if not found.

Approaches:
-----------
1. Linear search: Iterate through string
2. Using find() method: Built-in string method
3. Using index() with exception handling

Time Complexity: O(n) where n is the length of string
Space Complexity: O(1)

Reference: https://www.geeksforgeeks.org/dsa/program-to-search-a-character-in-a-string/
"""


def search_character_linear(s: str, char: str) -> int:
    """Search character using linear search."""
    if len(char) != 1:
        raise ValueError("char must be a single character")

    for i in range(len(s)):
        if s[i] == char:
            return i
    return -1


def search_character_find(s: str, char: str) -> int:
    """Search character using find method."""
    if len(char) != 1:
        raise ValueError("char must be a single character")
    return s.find(char)


def search_character_all(s: str, char: str) -> list:
    """Find all occurrences of character."""
    if len(char) != 1:
        raise ValueError("char must be a single character")

    indices = []
    for i in range(len(s)):
        if s[i] == char:
            indices.append(i)
    return indices


def test_search_character():
    """Test cases for character search."""
    test_cases = [
        ("hello world", "o", 4),
        ("python", "p", 0),
        ("python", "z", -1),
        ("", "a", -1),
        ("aaa", "a", 0),
        ("test", "t", 0),
        ("spaces here", " ", 6),
    ]

    print("Testing search_character_linear:")
    for i, (s, char, expected) in enumerate(test_cases, 1):
        result = search_character_linear(s, char)
        status = "✓" if result == expected else "✗"
        print(
            f"  Test {i}: {status} '{char}' in '{s}' -> {result} (expected: {expected})"
        )

    print("\nTesting search_character_find:")
    for i, (s, char, expected) in enumerate(test_cases, 1):
        result = search_character_find(s, char)
        status = "✓" if result == expected else "✗"
        print(
            f"  Test {i}: {status} '{char}' in '{s}' -> {result} (expected: {expected})"
        )

    print("\nTesting search_character_all:")
    all_test_cases = [
        ("hello", "l", [2, 3]),
        ("banana", "a", [1, 3, 5]),
        ("test", "z", []),
    ]
    for i, (s, char, expected) in enumerate(all_test_cases, 1):
        result = search_character_all(s, char)
        status = "✓" if result == expected else "✗"
        print(
            f"  Test {i}: {status} All '{char}' in '{s}' -> {result} (expected: {expected})"
        )


if __name__ == "__main__":
    test_search_character()
