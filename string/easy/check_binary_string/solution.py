"""
Check for Binary String

Problem: Given a string, check if it is a binary string or not.
A binary string is a string that contains only characters '0' and '1'.

Examples:
- Input: "01010101010", Output: True
- Input: "geeks101", Output: False

Time Complexity: O(n) where n is length of string
Space Complexity: O(1)
"""


def is_binary_string(s: str) -> bool:
    """
    Check if the given string is a binary string.

    Args:
        s: Input string to check

    Returns:
        True if string contains only '0' and '1', False otherwise
    """
    for char in s:
        if char not in "01":
            return False
    return True


def is_binary_string_set(s: str) -> bool:
    """
    Alternative implementation using set comparison.

    Args:
        s: Input string to check

    Returns:
        True if string contains only '0' and '1', False otherwise
    """
    return set(s).issubset({"0", "1"})


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("01010101010", True),
        ("geeks101", False),
        ("1111", True),
        ("0000", True),
        ("", True),  # Empty string is technically binary
        ("012", False),
        ("10", True),
        ("binary", False),
    ]

    print("=" * 50)
    print("Check for Binary String - Test Results")
    print("=" * 50)

    for s, expected in test_cases:
        result = is_binary_string(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: '{s}' | Expected: {expected} | Got: {result} | {status}")

    print("=" * 50)

    # Test alternative implementation
    print("\nTesting set-based implementation:")
    for s, expected in test_cases[:4]:
        result = is_binary_string_set(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: '{s}' | Expected: {expected} | Got: {result} | {status}")
