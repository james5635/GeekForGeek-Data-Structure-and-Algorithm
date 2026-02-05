"""
Word Break Problem

Given a string s and a dictionary of words, check if s can be segmented
into a sequence of valid words from the dictionary.

Approach: Bottom-Up DP - O(n*m*k) Time and O(n) Space
Use DP array where dp[i] = True if s[0:i] can be segmented.
"""


def word_break(s, dictionary):
    """
    Check if string can be segmented using dictionary words.

    Args:
        s: Input string
        dictionary: List of valid words

    Returns:
        True if can be segmented, False otherwise
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for word in dictionary:
            start = i - len(word)
            if start >= 0 and dp[start] and s[start:i] == word:
                dp[i] = True
                break

    return dp[n]


def main():
    """Test cases for word break problem."""
    test_cases = [
        ("ilike", ["i", "like", "gfg"], True),
        ("ilikegfg", ["i", "like", "man", "india", "gfg"], True),
        ("ilikemangoes", ["i", "like", "gfg"], False),
        ("catsanddog", ["cat", "cats", "and", "sand", "dog"], True),
        ("catsandog", ["cat", "cats", "and", "sand", "dog"], False),
    ]

    print("=" * 50)
    print("Word Break Problem")
    print("=" * 50)

    for s, dictionary, expected in test_cases:
        result = word_break(s, dictionary)
        status = "✓" if result == expected else "✗"
        print(f"\nString: '{s}'")
        print(f"Dictionary: {dictionary}")
        print(f"Can Segment: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
