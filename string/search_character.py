"""
Program to Search a Character in a String
GeeksforGeeks: https://www.geeksforgeeks.org/dsa/program-to-search-a-character-in-a-string/

Given a character ch and a string s, the task is to find the index of the first
occurrence of the character in the string. If the character is not present in the
string, return -1.

Examples:
Input: s = "geeksforgeeks", ch = 'k'
Output: 3
Explanation: The character 'k' is present at index 3 and 11 in "geeksforgeeks",
but it first appears at index 3.

Input: s = "geeksforgeeks", ch = 'z'
Output: -1
Explanation: The character 'z' is not present in "geeksforgeeks".

Time Complexity: O(n) Time
Auxiliary Space: O(1) Space
"""


def find_char(s, ch):
    """
    Find the first occurrence of a character in a string.

    Args:
        s: Input string
        ch: Character to search for

    Returns:
        int: Index of first occurrence, -1 if not found
    """
    n = len(s)
    for i in range(n):
        # If the current character is equal to ch, return the current index
        if s[i] == ch:
            return i

    # If we did not find any occurrence of ch, return -1
    return -1


def find_char_builtin(s, ch):
    """
    Find the first occurrence using built-in find() method.

    Args:
        s: Input string
        ch: Character to search for

    Returns:
        int: Index of first occurrence, -1 if not found
    """
    return s.find(ch)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("geeksforgeeks", "k"),
        ("geeksforgeeks", "z"),
        ("hello world", "o"),
        ("python", "p"),
        ("python", "n"),
        ("", "a"),
    ]

    print("Character Search in String Demonstration")
    print("=" * 50)

    for s, ch in test_cases:
        index_manual = find_char(s, ch)
        index_builtin = find_char_builtin(s, ch)

        print(f"\nString: '{s}'")
        print(f"Character to find: '{ch}'")
        print(f"  Manual method: {index_manual}")
        print(f"  Built-in method: {index_builtin}")
        print(f"  Match: {index_manual == index_builtin}")
