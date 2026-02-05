"""
Reverse a String

Problem Description:
Reverse a given string.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) - New string is created

Implementation:
- Use slicing with step -1
- Alternative: Use reversed() function or manual iteration
"""


def reverse_string_slicing(s: str) -> str:
    """
    Reverse a string using slicing.

    Args:
        s: Input string

    Returns:
        Reversed string
    """
    return s[::-1]


def reverse_string_reversed(s: str) -> str:
    """
    Reverse a string using reversed() function.

    Args:
        s: Input string

    Returns:
        Reversed string
    """
    return "".join(reversed(s))


def reverse_string_manual(s: str) -> str:
    """
    Reverse a string using manual iteration.

    Args:
        s: Input string

    Returns:
        Reversed string
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


def reverse_string_two_pointers(s: str) -> str:
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


def main():
    """Test cases for reverse_string functions."""
    test_cases = [
        ("hello", "olleh"),
        ("", ""),
        ("a", "a"),
        ("abc", "cba"),
        ("12345", "54321"),
        ("racecar", "racecar"),
        ("Hello World", "dlroW olleH"),
        ("!@#$%", "%$#@!"),
    ]

    functions = [
        ("Slicing", reverse_string_slicing),
        ("reversed()", reverse_string_reversed),
        ("Manual", reverse_string_manual),
        ("Two pointers", reverse_string_two_pointers),
    ]

    for func_name, func in functions:
        print(f"\nTesting {func_name}:")
        for i, (input_str, expected) in enumerate(test_cases):
            result = func(input_str)
            status = "✓" if result == expected else "✗"
            print(f"Test {i + 1}: {status} '{input_str}' -> '{result}'")


if __name__ == "__main__":
    main()
