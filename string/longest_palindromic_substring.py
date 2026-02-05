"""
Longest Palindromic Substring

Given a string s, find the longest substring which is a palindrome.

Approach: Expansion from Center - O(n^2) Time and O(1) Space
For each position, expand around center for both odd and even length palindromes.
"""


def get_longest_pal(s):
    """
    Find the longest palindromic substring.

    Args:
        s: Input string

    Returns:
        Longest palindromic substring
    """
    n = len(s)
    start, max_len = 0, 1

    for i in range(n):
        # Check for both odd and even length palindromes
        for j in range(2):
            low, high = i, i + j

            # Expand while it is a palindrome
            while low >= 0 and high < n and s[low] == s[high]:
                curr_len = high - low + 1
                if curr_len > max_len:
                    start = low
                    max_len = curr_len
                low -= 1
                high += 1

    return s[start : start + max_len]


def main():
    """Test cases for longest palindromic substring."""
    test_cases = [
        ("forgeeksskeegfor", "geeksskeeg"),
        ("Geeks", "ee"),
        ("abc", "a"),
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("a", "a"),
        ("aaaa", "aaaa"),
    ]

    print("=" * 50)
    print("Longest Palindromic Substring")
    print("=" * 50)

    for s, expected in test_cases:
        result = get_longest_pal(s)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: '{s}'")
        print(f"Output: '{result}'")
        print(f"Expected: '{expected}' {status}")


if __name__ == "__main__":
    main()
