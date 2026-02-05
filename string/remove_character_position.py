"""
Remove a Character from a Given Position
GeeksforGeeks: https://www.geeksforgeeks.org/dsa/remove-a-character-from-a-given-position/

Given a string and a position (0-based indexing), remove the character at the given position.

Examples:
Input: s = "abcde", pos = 1
Output: s = "acde"

Input: s = "a", pos = 0
Output: s = ""

Time Complexity: O(n)
Auxiliary Space: O(1)
"""


def remove_char_at_position_builtin(s, pos):
    """
    Remove character at specified position using string slicing.

    Args:
        s: Input string
        pos: Position of character to remove

    Returns:
        str: New string with character removed
    """
    if pos < 0 or pos >= len(s):
        return s
    return s[:pos] + s[pos + 1 :]


def remove_char_at_position_manual(s, pos):
    """
    Remove character at specified position using custom method.

    Args:
        s: Input string
        pos: Position of character to remove

    Returns:
        str: New string with character removed
    """
    # Check for valid position
    if pos < 0 or pos >= len(s):
        return s

    # Convert string to list for mutable operations
    s_list = list(s)

    # Shift characters to the left from the position
    for i in range(pos, len(s) - 1):
        s_list[i] = s_list[i + 1]

    # Remove the last character
    s_list.pop()

    return "".join(s_list)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("abcde", 1),
        ("a", 0),
        ("hello", 0),  # Remove first character
        ("hello", 4),  # Remove last character
        ("test", 10),  # Invalid position
        ("test", -1),  # Invalid position
    ]

    print("Remove Character at Position Demonstration")
    print("=" * 50)

    for s, pos in test_cases:
        result_builtin = remove_char_at_position_builtin(s, pos)
        result_manual = remove_char_at_position_manual(s, pos)

        print(f"\nOriginal String: '{s}'")
        print(f"Position to remove: {pos}")
        print(f"  Slicing method: '{result_builtin}'")
        print(f"  Manual method: '{result_manual}'")
        print(f"  Match: {result_builtin == result_manual}")
