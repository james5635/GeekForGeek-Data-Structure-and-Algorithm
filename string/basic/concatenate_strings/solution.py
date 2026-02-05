"""
Concatenate Two Strings

Problem Description:
Concatenate (join) two strings together.

Time Complexity: O(n + m) where n and m are lengths of the strings
Space Complexity: O(n + m) - New string is created

Implementation:
- Use + operator to concatenate strings
- Alternative: Use join() method or f-strings
"""


def concatenate_strings(str1: str, str2: str) -> str:
    """
    Concatenate two strings using the + operator.

    Args:
        str1: First string
        str2: Second string

    Returns:
        Concatenated string
    """
    return str1 + str2


def concatenate_strings_join(str1: str, str2: str) -> str:
    """
    Concatenate two strings using join() method.

    Args:
        str1: First string
        str2: Second string

    Returns:
        Concatenated string
    """
    return "".join([str1, str2])


def concatenate_strings_fstring(str1: str, str2: str) -> str:
    """
    Concatenate two strings using f-string.

    Args:
        str1: First string
        str2: Second string

    Returns:
        Concatenated string
    """
    return f"{str1}{str2}"


def main():
    """Test cases for concatenate_strings functions."""
    test_cases = [
        ("hello", "world", "helloworld"),
        ("", "world", "world"),
        ("hello", "", "hello"),
        ("", "", ""),
        ("a", "b", "ab"),
        ("123", "456", "123456"),
        ("hello", " ", "hello "),
        (" ", "world", " world"),
        ("hello", " world", "hello world"),
    ]

    functions = [
        ("+ operator", concatenate_strings),
        ("join() method", concatenate_strings_join),
        ("f-string", concatenate_strings_fstring),
    ]

    for func_name, func in functions:
        print(f"\nTesting {func_name}:")
        for i, (str1, str2, expected) in enumerate(test_cases):
            result = func(str1, str2)
            status = "✓" if result == expected else "✗"
            print(f"Test {i + 1}: {status} '{str1}' + '{str2}' -> '{result}'")


if __name__ == "__main__":
    main()
