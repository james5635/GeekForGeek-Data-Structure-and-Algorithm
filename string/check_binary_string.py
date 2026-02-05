"""
Check for Binary String
Given a string s, check if it is a binary string (contains only '0' and '1').

Time Complexity: O(n), where n is the length of the string
Auxiliary Space: O(1)
"""


def is_binary(s: str) -> bool:
    """
    Check if the given string is a binary string.

    Args:
        s: Input string to check

    Returns:
        True if string contains only '0' and '1', False otherwise
    """
    for char in s:
        if char != "0" and char != "1":
            return False
    return True


def main():
    """Test the binary string checker with various inputs."""
    test_cases = [
        ("01010101010", True),
        ("geeks101", False),
        ("111000", True),
        ("", True),  # Empty string is considered binary
        ("01201", False),
        ("1010102", False),
    ]

    print("Check for Binary String")
    print("=" * 40)

    for s, expected in test_cases:
        result = is_binary(s)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status} | Input: '{s}' | Expected: {expected} | Got: {result}")


if __name__ == "__main__":
    main()
