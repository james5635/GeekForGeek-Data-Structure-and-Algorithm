"""
Reverse a String

Problem Description:
Given a string, reverse it completely.

Time Complexity: O(n)
Space Complexity: O(n) for the result string

Implementation:
- Use slicing to reverse the string
- Alternative implementations using two-pointer approach and built-in methods
"""


def reverse_string(s: str) -> str:
    """
    Reverse a string using slicing.

    Args:
        s: Input string

    Returns:
        Reversed string
    """
    return s[::-1]


def reverse_string_two_pointer(s: str) -> str:
    """
    Reverse a string using two-pointer approach.

    Args:
        s: Input string

    Returns:
        Reversed string
    """
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


def reverse_string_builtin(s: str) -> str:
    """
    Reverse a string using built-in reversed() function.

    Args:
        s: Input string

    Returns:
        Reversed string
    """
    return "".join(reversed(s))


def test_reverse_string():
    """Test cases for reverse_string functions."""
    test_cases = [
        ("hello", "olleh"),
        ("", ""),
        ("a", "a"),
        ("racecar", "racecar"),
        ("Python", "nohtyP"),
        ("12345", "54321"),
        ("Hello, World!", "!dlroW ,olleH"),
        ("  spaces  ", "  secaps  "),
        ("abc123", "321cba"),
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        # Test slicing method
        result1 = reverse_string(input_str)
        assert result1 == expected, (
            f"Test case {i} failed (slicing): input='{input_str}', expected='{expected}', got='{result1}'"
        )

        # Test two-pointer method
        result2 = reverse_string_two_pointer(input_str)
        assert result2 == expected, (
            f"Test case {i} failed (two-pointer): input='{input_str}', expected='{expected}', got='{result2}'"
        )

        # Test builtin method
        result3 = reverse_string_builtin(input_str)
        assert result3 == expected, (
            f"Test case {i} failed (builtin): input='{input_str}', expected='{expected}', got='{result3}'"
        )

        print(f"Test case {i} passed: '{input_str}' -> '{expected}'")


if __name__ == "__main__":
    test_reverse_string()
    print("\nAll test cases passed!")
