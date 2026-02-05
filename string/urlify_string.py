"""
URLify a Given String (Replace Spaces with %20)
Given a string, replace all spaces with '%20'.

Time Complexity: O(n), where n is the length of the string
Auxiliary Space: O(n), for the output string
"""


def urlify(s: str) -> str:
    """
    Replace all spaces in the string with '%20'.

    Args:
        s: Input string

    Returns:
        URLified string with spaces replaced by '%20'
    """
    result = []

    for char in s:
        if char == " ":
            result.append("%")
            result.append("2")
            result.append("0")
        else:
            result.append(char)

    return "".join(result)


def urlify_builtin(s: str) -> str:
    """
    Using Python's built-in replace() method.
    """
    return s.replace(" ", "%20")


def main():
    """Test the URLify function with various inputs."""
    test_cases = [
        ("i love programming", "i%20love%20programming"),
        ("ab cd", "ab%20cd"),
        ("hello world python", "hello%20world%20python"),
        ("nospaces", "nospaces"),
        ("  leading", "%20%20leading"),
        ("trailing  ", "trailing%20%20"),
        ("", ""),
        ("   ", "%20%20%20"),
    ]

    print("URLify a Given String (Replace Spaces with %20)")
    print("=" * 60)

    for input_str, expected in test_cases:
        result = urlify(input_str)
        builtin_result = urlify_builtin(input_str)

        all_pass = result == expected and builtin_result == expected
        status = "✓ PASS" if all_pass else "✗ FAIL"

        print(f"{status} | Input: '{input_str}'")
        print(f"       | Expected: '{expected}'")
        print(f"       | Manual: '{result}', Built-in: '{builtin_result}'")
        print()


if __name__ == "__main__":
    main()
