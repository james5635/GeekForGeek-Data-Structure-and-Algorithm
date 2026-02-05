"""
Find the Length of a String
GeeksforGeeks: https://www.geeksforgeeks.org/dsa/find-the-length-of-a-string/

Given a string s, the task is to find the length of the string.

Examples:
Input: s = "abc"
Output: 3

Input: s = "GeeksforGeeks"
Output: 13

Input: s = ""
Output: 0

Time Complexity: O(n), where n is the length of the string
Auxiliary Space: O(1)
"""


def get_length(s):
    """
    Calculate length of a string by traversing each character.

    Args:
        s: Input string

    Returns:
        int: Length of the string
    """
    cnt = 0
    for c in s:
        cnt += 1
    return cnt


def get_length_builtin(s):
    """
    Calculate length using Python's built-in len() function.

    Args:
        s: Input string

    Returns:
        int: Length of the string
    """
    return len(s)


if __name__ == "__main__":
    # Test cases
    test_strings = ["abc", "GeeksforGeeks", "", "Hello World", "Python"]

    print("String Length Algorithm Demonstration")
    print("=" * 50)

    for s in test_strings:
        length_manual = get_length(s)
        length_builtin = get_length_builtin(s)

        print(f"\nInput: '{s}'")
        print(f"  Manual method: {length_manual}")
        print(f"  Built-in method: {length_builtin}")
        print(f"  Match: {length_manual == length_builtin}")
