"""
Palindrome String
Check if a given string is a palindrome (reads same forwards and backwards).

Approach: Two pointers from start and end
Time Complexity: O(n), where n is the length of the string
Auxiliary Space: O(1)
"""


def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome using two pointers.

    Args:
        s: Input string to check

    Returns:
        True if string is palindrome, False otherwise
    """
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_optimized(s: str) -> bool:
    """
    Optimized version using single loop.
    """
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


def is_palindrome_reversed(s: str) -> bool:
    """
    Using string reversal (Pythonic way).
    """
    return s == s[::-1]


def main():
    """Test the palindrome checker with various inputs."""
    test_cases = [
        ("abba", True),
        ("abc", False),
        ("racecar", True),
        ("hello", False),
        ("a", True),
        ("", True),
        ("madam", True),
        ("python", False),
    ]

    print("Palindrome String Checker")
    print("=" * 60)

    for s, expected in test_cases:
        result1 = is_palindrome(s)
        result2 = is_palindrome_optimized(s)
        result3 = is_palindrome_reversed(s)

        all_pass = all(r == expected for r in [result1, result2, result3])
        status = "✓ PASS" if all_pass else "✗ FAIL"

        print(f"{status} | Input: '{s}'")
        print(f"       | Expected: {expected}")
        print(
            f"       | Two Pointers: {result1}, Optimized: {result2}, Reversed: {result3}"
        )
        print()


if __name__ == "__main__":
    main()
