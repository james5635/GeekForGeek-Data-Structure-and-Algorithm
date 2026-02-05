"""
Remove All Occurrences of Character

Problem Description:
Remove all occurrences of a specific character from a string.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) - New string is created

Implementation:
- Use string replace() method with empty string
- Alternative: Use list comprehension to filter characters
"""


def remove_all_occurrences(original: str, char: str) -> str:
    """
    Remove all occurrences of a specific character from a string.

    Args:
        original: Original string
        char: Character to remove

    Returns:
        New string with all occurrences of character removed
    """
    return original.replace(char, "")


def remove_all_occurrences_filter(original: str, char: str) -> str:
    """
    Remove all occurrences using list comprehension (alternative method).

    Args:
        original: Original string
        char: Character to remove

    Returns:
        New string with all occurrences of character removed
    """
    return "".join(c for c in original if c != char)


def main():
    """Test cases for remove_all_occurrences functions."""
    test_cases = [
        ("hello", "l", "heo"),
        ("hello", "h", "ello"),
        ("hello", "o", "hell"),
        ("hello", "x", "hello"),
        ("aaaaa", "a", ""),
        ("abcabc", "a", "bcbc"),
        ("abcabc", "b", "acac"),
        ("abcabc", "c", "abab"),
        ("", "a", ""),
        ("hello", "", "hello"),
    ]

    print("Testing remove_all_occurrences function:")
    for i, (original, char, expected) in enumerate(test_cases):
        result = remove_all_occurrences(original, char)
        status = "✓" if result == expected else "✗"
        print(f"Test {i + 1}: {status} '{original}' remove '{char}' -> '{result}'")

    print("\nTesting remove_all_occurrences_filter function:")
    for i, (original, char, expected) in enumerate(test_cases):
        result = remove_all_occurrences_filter(original, char)
        status = "✓" if result == expected else "✗"
        print(f"Test {i + 1}: {status} '{original}' remove '{char}' -> '{result}'")


if __name__ == "__main__":
    main()
