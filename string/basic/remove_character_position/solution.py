"""
Remove Character at Position

Problem Description:
Remove a character from a given position in a string.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) - New string is created

Implementation:
- Use string slicing to remove character at desired position
- Handle edge cases (position out of bounds)
"""


def remove_character_at_position(original: str, position: int) -> str:
    """
    Remove a character from a given position in a string.

    Args:
        original: Original string
        position: Position of character to remove (0-indexed)

    Returns:
        New string with character removed
    """
    if position < 0 or position >= len(original):
        return original

    return original[:position] + original[position + 1 :]


def main():
    """Test cases for remove_character_at_position function."""
    test_cases = [
        ("hello", 0, "ello"),
        ("hello", 2, "helo"),
        ("hello", 4, "hell"),
        ("hello", 5, "hello"),
        ("hello", -1, "hello"),
        ("a", 0, ""),
        ("", 0, ""),
        ("abcde", 2, "abde"),
        ("abcde", 4, "abcd"),
    ]

    print("Testing remove_character_at_position function:")
    for i, (original, position, expected) in enumerate(test_cases):
        result = remove_character_at_position(original, position)
        status = "✓" if result == expected else "✗"
        print(f"Test {i + 1}: {status} '{original}' at {position} -> '{result}'")


if __name__ == "__main__":
    main()
