"""
Check if String is Interleaving of Two Strings

Given three strings s1, s2, and s3, check whether s3 is an interleaving of s1 and s2.
An interleaving contains all characters of s1 and s2 in the same order.

Approach 1: Two Pointer - O(m+n) Time and O(1) Space
Approach 2: Dynamic Programming - O(m*n) Time and O(m*n) Space
The DP approach handles all cases correctly including when characters match both strings.
"""


def is_interleaved_greedy(s1, s2, s3):
    """
    Greedy approach - works for simple cases but fails for complex ones.

    Args:
        s1, s2: Input strings
        s3: String to check

    Returns:
        True if s3 is interleaving, False otherwise
    """
    if len(s1) + len(s2) != len(s3):
        return False

    i = j = 0

    for k in range(len(s3)):
        if i < len(s1) and s1[i] == s3[k]:
            i += 1
        elif j < len(s2) and s2[j] == s3[k]:
            j += 1
        else:
            return False

    return True


def is_interleaved_dp(s1, s2, s3):
    """
    Dynamic Programming approach - handles all cases correctly.
    dp[i][j] = True if s3[0:i+j] is an interleaving of s1[0:i] and s2[0:j]

    Args:
        s1, s2: Input strings
        s3: String to check

    Returns:
        True if s3 is interleaving, False otherwise
    """
    if len(s1) + len(s2) != len(s3):
        return False

    m, n = len(s1), len(s2)

    # dp[i][j] represents whether s3[0:i+j] is formed by interleaving s1[0:i] and s2[0:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty strings
    dp[0][0] = True

    # Fill first row: s3 formed only from s2
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    # Fill first column: s3 formed only from s1
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    # Fill rest of the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # s3[i+j-1] can come from either s1[i-1] or s2[j-1]
            from_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
            from_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
            dp[i][j] = from_s1 or from_s2

    return dp[m][n]


def is_interleaved(s1, s2, s3):
    """Use DP approach as it handles all cases correctly."""
    return is_interleaved_dp(s1, s2, s3)


def main():
    """Test cases for interleaving check."""
    test_cases = [
        ("AB", "C", "ACB", True),
        ("AXY", "BBZ", "BBAZXY", True),
        ("AB", "CD", "ACBG", False),
        ("aab", "axy", "aaxaby", True),
        ("aab", "axy", "abaaxy", False),
    ]

    print("=" * 50)
    print("Check Interleaving")
    print("=" * 50)

    for s1, s2, s3, expected in test_cases:
        result = is_interleaved(s1, s2, s3)
        status = "✓" if result == expected else "✗"
        print(f"\nS1: '{s1}', S2: '{s2}'")
        print(f"S3: '{s3}'")
        print(f"Is Interleaved: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
