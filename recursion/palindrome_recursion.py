"""
Check for Palindrome using Recursion

Given a string, check if it is a palindrome using recursion.
A palindrome reads the same backward as forward.

Approach (Two Pointers):
- Use two pointers: left (start) and right (end)
- Base case: pointers meet or cross - palindrome confirmed
- If characters at pointers don't match - not a palindrome
- Recursively check inner substring by moving pointers inward

Time Complexity: O(n)
Space Complexity: O(n) - recursion stack space
"""


def is_palindrome_rec(s: str, left: int, right: int) -> bool:
    """
    Helper recursive function to check palindrome.

    Args:
        s: String to check
        left: Left pointer index
        right: Right pointer index

    Returns:
        True if palindrome, False otherwise
    """
    # Base case: pointers met or crossed
    if left >= right:
        return True

    # If mismatch found
    if s[left] != s[right]:
        return False

    # Recursive call with narrowed range
    return is_palindrome_rec(s, left + 1, right - 1)


def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome.

    Args:
        s: Input string

    Returns:
        True if palindrome, False otherwise
    """
    if not s:
        return True
    return is_palindrome_rec(s, 0, len(s) - 1)


def main():
    """Test cases for palindrome check."""
    test_cases = [
        "abba",  # True
        "abc",  # False
        "radar",  # True
        "racecar",  # True
        "hello",  # False
        "a",  # True (single char)
        "",  # True (empty string)
        "madam",  # True
        "python",  # False
        "level",  # True
    ]

    print("Palindrome Check using Recursion")
    print("=" * 50)

    for s in test_cases:
        result = is_palindrome(s)
        status = "✓ Palindrome" if result else "✗ Not Palindrome"
        print(f'"{s}" -> {status}')


if __name__ == "__main__":
    main()
