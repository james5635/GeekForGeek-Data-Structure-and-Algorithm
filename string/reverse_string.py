"""
Reverse a String
GeeksforGeeks: https://www.geeksforgeeks.org/dsa/reverse-a-string/

Given a string s, the task is to reverse the string. Reversing a string means
rearranging the characters such that the first character becomes the last,
the second character becomes second last and so on.

Examples:
Input: s = "GeeksforGeeks"
Output: "skeeGrofskeeG"

Input: s = "abdcfe"
Output: "efcdba"

Time Complexity: O(n)
"""


def reverse_string_slicing(s):
    """
    Reverse a string using slicing [::-1].
    Most efficient method in Python.

    Args:
        s: Input string

    Returns:
        str: Reversed string
    """
    return s[::-1]


def reverse_string_two_pointers(s):
    """
    Reverse a string using two pointers approach.

    Args:
        s: Input string

    Returns:
        str: Reversed string
    """
    # Convert string to a list for mutability
    chars = list(s)
    left = 0
    right = len(s) - 1

    # Swap characters from both ends
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


def reverse_string_backward_traversal(s):
    """
    Reverse a string using backward traversal.

    Args:
        s: Input string

    Returns:
        str: Reversed string
    """
    res = []
    # Traverse on s in backward direction
    for i in range(len(s) - 1, -1, -1):
        res.append(s[i])

    return "".join(res)


def reverse_string_recursive(s):
    """
    Reverse a string using recursion.

    Args:
        s: Input string

    Returns:
        str: Reversed string
    """
    # Base case
    if len(s) <= 1:
        return s

    # Recursive case: reverse the substring and append first character
    return reverse_string_recursive(s[1:]) + s[0]


if __name__ == "__main__":
    # Test cases
    test_strings = ["GeeksforGeeks", "abdcfe", "hello", "Python", "a", ""]

    print("String Reversal Demonstration")
    print("=" * 50)

    for s in test_strings:
        result_slicing = reverse_string_slicing(s)
        result_two_pointers = reverse_string_two_pointers(s)
        result_backward = reverse_string_backward_traversal(s)
        result_recursive = reverse_string_recursive(s)

        print(f"\nOriginal: '{s}'")
        print(f"  Slicing [::-1]: '{result_slicing}'")
        print(f"  Two Pointers:   '{result_two_pointers}'")
        print(f"  Backward:       '{result_backward}'")
        print(f"  Recursive:      '{result_recursive}'")
        print(
            f"  All match: {result_slicing == result_two_pointers == result_backward == result_recursive}"
        )
