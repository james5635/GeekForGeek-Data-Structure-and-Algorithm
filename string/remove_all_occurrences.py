"""
Remove All Occurrences of a Character in a String
GeeksforGeeks: https://www.geeksforgeeks.org/dsa/remove-all-occurrences-of-a-character-in-a-string/

Given a string and a character, remove all the occurrences of the character in the string.

Examples:
Input: s = "geeksforgeeks", c = 'e'
Output: s = "gksforgks"

Input: s = "geeksforgeeks", c = 'g'
Output: s = "eeksforeeks"

Input: s = "geeksforgeeks", c = 'k'
Output: s = "geesforgees"

Time Complexity: O(n) where n is length of input string
Auxiliary Space: O(1)
"""


def remove_all_occurrences_builtin(s, c):
    """
    Remove all occurrences of a character using replace() method.

    Args:
        s: Input string
        c: Character to remove

    Returns:
        str: New string with all occurrences removed
    """
    return s.replace(c, "")


def remove_all_occurrences_manual(s, c):
    """
    Remove all occurrences of a character using custom method.

    Args:
        s: Input string
        c: Character to remove

    Returns:
        str: New string with all occurrences removed
    """
    result = []
    for char in s:
        if char != c:
            result.append(char)
    return "".join(result)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("geeksforgeeks", "e"),
        ("geeksforgeeks", "g"),
        ("geeksforgeeks", "k"),
        ("ababca", "a"),
        ("hello world", "l"),
        ("python", "z"),  # Character not in string
    ]

    print("Remove All Occurrences of Character Demonstration")
    print("=" * 50)

    for s, c in test_cases:
        result_builtin = remove_all_occurrences_builtin(s, c)
        result_manual = remove_all_occurrences_manual(s, c)

        print(f"\nOriginal String: '{s}'")
        print(f"Character to remove: '{c}'")
        print(f"  Built-in method: '{result_builtin}'")
        print(f"  Manual method: '{result_manual}'")
        print(f"  Match: {result_builtin == result_manual}")
