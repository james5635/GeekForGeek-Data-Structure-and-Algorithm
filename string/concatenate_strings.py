"""
Concatenate Two Strings
GeeksforGeeks: https://www.geeksforgeeks.org/python/python-string-concatenation/

String concatenation in Python allows us to combine two or more strings into one.

Examples:
Input: s1 = "Hello", s2 = "World"
Output: "HelloWorld" or "Hello World"

Time Complexity: O(n) where n is the total length of strings
"""


def concatenate_using_plus(s1, s2):
    """
    Concatenate two strings using + operator.

    Args:
        s1: First string
        s2: Second string

    Returns:
        str: Concatenated string
    """
    return s1 + s2


def concatenate_using_join(s1, s2, separator=""):
    """
    Concatenate two strings using join() method.

    Args:
        s1: First string
        s2: Second string
        separator: Separator between strings (default: "")

    Returns:
        str: Concatenated string
    """
    return separator.join([s1, s2])


def concatenate_using_fstring(s1, s2, separator=""):
    """
    Concatenate two strings using f-string.

    Args:
        s1: First string
        s2: Second string
        separator: Separator between strings (default: "")

    Returns:
        str: Concatenated string
    """
    return f"{s1}{separator}{s2}"


def concatenate_using_format(s1, s2, separator=""):
    """
    Concatenate two strings using format() method.

    Args:
        s1: First string
        s2: Second string
        separator: Separator between strings (default: "")

    Returns:
        str: Concatenated string
    """
    return "{}{}{}".format(s1, separator, s2)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("Hello", "World"),
        ("Geeks", "forGeeks"),
        ("", "test"),
        ("abc", ""),
        ("Python", "Programming"),
    ]

    print("String Concatenation Demonstration")
    print("=" * 50)

    for s1, s2 in test_cases:
        result_plus = concatenate_using_plus(s1, s2)
        result_join = concatenate_using_join(s1, s2)
        result_fstring = concatenate_using_fstring(s1, s2)
        result_format = concatenate_using_format(s1, s2)

        # With space separator
        result_plus_space = concatenate_using_plus(s1 + " ", s2)
        result_join_space = concatenate_using_join(s1, s2, " ")

        print(f"\nString 1: '{s1}'")
        print(f"String 2: '{s2}'")
        print(f"  Using + operator: '{result_plus}'")
        print(f"  Using join(): '{result_join}'")
        print(f"  Using f-string: '{result_fstring}'")
        print(f"  Using format(): '{result_format}'")
        print(f"  With space (+): '{result_plus_space}'")
        print(f"  With space (join): '{result_join_space}'")
