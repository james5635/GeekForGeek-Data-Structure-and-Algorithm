"""
Palindrome String

Problem: Check if a given string is a palindrome.
A palindrome reads the same forwards and backwards.

Examples:
- Input: "abba", Output: True
- Input: "abc", Output: False
- Input: "racecar", Output: True

Time Complexity: O(n) where n is length of string
Space Complexity: O(1) or O(n) depending on implementation
"""


def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome using two pointers.

    Args:
        s: Input string to check

    Returns:
        True if palindrome, False otherwise
    """
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_slice(s: str) -> bool:
    """
    Check if string is palindrome using slicing.

    Args:
        s: Input string

    Returns:
        True if palindrome, False otherwise
    """
    return s == s[::-1]


def is_palindrome_recursive(s: str) -> bool:
    """
    Recursive approach to check palindrome.

    Args:
        s: Input string

    Returns:
        True if palindrome, False otherwise
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("abba", True),
        ("abc", False),
        ("racecar", True),
        ("a", True),
        ("", True),
        ("ab", False),
        ("aa", True),
        ("level", True),
        ("python", False),
        ("madam", True),
    ]

    print("=" * 60)
    print("Palindrome String - Test Results")
    print("=" * 60)

    for s, expected in test_cases:
        result = is_palindrome(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: '{s}' | Expected: {expected} | Got: {result} | {status}")

    print("=" * 60)

    # Compare implementations
    print("\nComparing all implementations:")
    print("-" * 60)
    for s, expected in test_cases[:7]:
        r1 = is_palindrome(s)
        r2 = is_palindrome_slice(s)
        r3 = is_palindrome_recursive(s)
        all_match = r1 == r2 == r3 == expected
        status = "PASS" if all_match else "FAIL"
        print(
            f"Input: '{s}' | Two-pointer: {r1} | Slice: {r2} | Recursive: {r3} | {status}"
        )
