"""
How to Insert a Character in a String
GeeksforGeeks: https://www.geeksforgeeks.org/dsa/how-to-insert-a-character-in-a-string/

Given a string s, a character c and an integer position pos, the task is to
insert the character c into the string s at the specified position pos.

Examples:
Input: s = "Geeks", c = 'A', pos = 3
Output: GeeAks

Input: s = "HelloWorld", c = '!', pos = 5
Output: Hello!World

Time Complexity: O(n) where n is the length of the string
"""


def insert_char_builtin(s, c, pos):
    """
    Insert a character at specified position using string slicing.

    Args:
        s: Input string
        c: Character to insert
        pos: Position to insert at

    Returns:
        str: New string with character inserted
    """
    return s[:pos] + c + s[pos:]


def insert_char_manual(s, c, pos):
    """
    Insert a character at specified position using custom method.

    Args:
        s: Input string
        c: Character to insert
        pos: Position to insert at

    Returns:
        str: New string with character inserted
    """
    res = ""
    for i in range(len(s)):
        # Insert the character at the given position
        if i == pos:
            res += c

        # Insert the original characters
        res += s[i]

    # If the given pos is beyond the length, append the character at the end
    if pos >= len(s):
        res += c

    return res


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("Geeks", "A", 3),
        ("HelloWorld", "!", 5),
        ("abc", "X", 0),  # Insert at beginning
        ("abc", "Z", 3),  # Insert at end
        ("test", "@", 10),  # Position beyond length
    ]

    print("Insert Character in String Demonstration")
    print("=" * 50)

    for s, c, pos in test_cases:
        result_builtin = insert_char_builtin(s, c, pos)
        result_manual = insert_char_manual(s, c, pos)

        print(f"\nOriginal String: '{s}'")
        print(f"Character to insert: '{c}'")
        print(f"Position: {pos}")
        print(f"  Slicing method: '{result_builtin}'")
        print(f"  Manual method: '{result_manual}'")
        print(f"  Match: {result_builtin == result_manual}")
