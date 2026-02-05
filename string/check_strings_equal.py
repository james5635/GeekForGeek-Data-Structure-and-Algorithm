"""
Check if Two Strings are Same or Not
GeeksforGeeks: https://www.geeksforgeeks.org/dsa/program-to-check-if-two-strings-are-same-or-not/

Given two strings, the task is to check if these two strings are identical (same) or not.
Consider case sensitivity.

Examples:
Input: s1 = "abc", s2 = "abc"
Output: Yes

Input: s1 = "", s2 = ""
Output: Yes

Input: s1 = "GeeksforGeeks", s2 = "Geeks"
Output: No

Time Complexity: O(n)
Auxiliary Space: O(1)
"""


def are_strings_same(s1, s2):
    """
    Check if two strings are identical using == operator.

    Args:
        s1: First string
        s2: Second string

    Returns:
        bool: True if strings are same, False otherwise
    """
    return s1 == s2


def are_strings_equal_manual(s1, s2):
    """
    Check if two strings are identical by manual comparison.

    Args:
        s1: First string
        s2: Second string

    Returns:
        bool: True if strings are same, False otherwise
    """
    # Compare lengths first
    if len(s1) != len(s2):
        return False

    # Compare character by character
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("abc", "abc"),
        ("", ""),
        ("GeeksforGeeks", "Geeks"),
        ("Hello", "hello"),  # Case sensitive
        ("Python", "Python"),
        ("Test", "Testing"),
    ]

    print("String Equality Check Demonstration")
    print("=" * 50)

    for s1, s2 in test_cases:
        result_operator = are_strings_same(s1, s2)
        result_manual = are_strings_equal_manual(s1, s2)

        print(f"\nString 1: '{s1}'")
        print(f"String 2: '{s2}'")
        print(f"  Using == operator: {'Yes' if result_operator else 'No'}")
        print(f"  Using manual method: {'Yes' if result_manual else 'No'}")
        print(f"  Match: {result_operator == result_manual}")
