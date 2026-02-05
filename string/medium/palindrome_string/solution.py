"""
Palindrome String

Check if a string is a palindrome.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome reads the same forwards and backwards.
    This implementation ignores case and non-alphanumeric characters.

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = "".join(char.lower() for char in s if char.isalnum())

    # Check palindrome using two pointers
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_simple(s: str) -> bool:
    """
    Simple version that checks exact match (case-sensitive, considers all characters).
    """
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_recursive(s: str, left: int = 0, right: int = None) -> bool:
    """
    Recursive approach to check palindrome.
    """
    if right is None:
        right = len(s) - 1

    # Base case
    if left >= right:
        return True

    # If characters don't match
    if s[left] != s[right]:
        return False

    # Recursive call
    return is_palindrome_recursive(s, left + 1, right - 1)


def is_palindrome_using_reverse(s: str) -> bool:
    """
    Using Python's string reversal.
    """
    return s == s[::-1]


def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring.

    Args:
        s: Input string

    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""

    start, max_len = 0, 1

    def expand_around_center(left: int, right: int) -> None:
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_len = right - left + 1
            if current_len > max_len:
                start = left
                max_len = current_len
            left -= 1
            right += 1

    for i in range(len(s)):
        # Odd length palindromes
        expand_around_center(i, i)
        # Even length palindromes
        expand_around_center(i, i + 1)

    return s[start : start + max_len]


def count_palindromic_substrings(s: str) -> int:
    """
    Count all palindromic substrings in the given string.
    """
    n = len(s)
    count = 0

    for center in range(2 * n - 1):
        left = center // 2
        right = left + (center % 2)

        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    return count


def min_insertions_to_make_palindrome(s: str) -> int:
    """
    Minimum insertions to make a string palindrome.
    Uses dynamic programming approach.
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Fill the DP table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


def test_is_palindrome():
    """Test cases for palindrome checking."""
    test_cases = [
        ("racecar", True),
        ("RaceCar", True),  # Case insensitive
        ("A man, a plan, a canal: Panama", True),  # Ignores punctuation
        ("hello", False),
        ("", True),  # Empty string is palindrome
        ("a", True),
        ("ab", False),
        ("aba", True),
        ("abba", True),
        ("abcba", True),
        ("abccba", True),
        ("12321", True),
        ("123321", True),
        ("Was it a car or a cat I saw?", True),
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = is_palindrome(input_str)
        assert result == expected, (
            f"Test case {i} failed: Expected {expected}, got {result}"
        )

    print("All palindrome test cases passed!")


def test_longest_palindromic_substring():
    """Test cases for longest palindromic substring."""
    test_cases = [
        ("babad", ["bab", "aba"]),  # Either "bab" or "aba" is correct
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),
        ("", [""]),
        ("forgeeksskeegfor", ["geeksskeeg"]),
        ("abacdfgdcaba", ["aba", "aca"]),
    ]

    for i, (input_str, expected_options) in enumerate(test_cases):
        result = longest_palindromic_substring(input_str)
        assert result in expected_options, (
            f"Test case {i} failed: Expected one of {expected_options}, got {result}"
        )

    print("All longest palindromic substring test cases passed!")


if __name__ == "__main__":
    test_is_palindrome()
    test_longest_palindromic_substring()

    # Example usage
    s = "A man, a plan, a canal: Panama"
    result = is_palindrome(s)
    print(f"Is '{s}' a palindrome? {result}")

    s2 = "babad"
    longest_pal = longest_palindromic_substring(s2)
    print(f"Longest palindromic substring in '{s2}': {longest_pal}")
