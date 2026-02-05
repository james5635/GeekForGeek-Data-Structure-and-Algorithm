"""
Insert Character in String

Problem Description:
Insert a character at a specific position in a string.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) - New string is created

Implementation:
- Use string slicing to insert character at desired position
- Handle edge cases (position out of bounds)
"""


def insert_character(original: str, char: str, position: int) -> str:
    """
    Insert a character at a specific position in a string.

    Args:
        original: Original string
        char: Character to insert
        position: Position to insert (0-indexed)

    Returns:
        New string with character inserted
    """
    if position < 0:
        position = 0
    elif position > len(original):
        position = len(original)

    return original[:position] + char + original[position:]


def main():
    """Test cases for insert_character function."""
    test_cases = [
        ("hello", "x", 0, "xhello"),
        ("hello", "x", 2, "hexllo"),
        ("hello", "x", 5, "hellox"),
        ("hello", "x", 10, "hellox"),
        ("hello", "x", -1, "xhello"),
        ("", "a", 0, "a"),
        ("", "a", 5, "a"),
        ("abc", "d", 1, "adbc"),
        ("abc", "d", 3, "abcd"),
    ]

    print("Testing insert_character function:")
    for i, (original, char, position, expected) in enumerate(test_cases):
        result = insert_character(original, char, position)
        status = "✓" if result == expected else "✗"
        print(
            f"Test {i + 1}: {status} '{original}' + '{char}' at {position} -> '{result}'"
        )


if __name__ == "__main__":
    main()
