"""
Check Interleaving

Check whether two strings are interleaving of each other.

Time Complexity: O(m*n)
Space Complexity: O(m*n) where m and n are lengths of the strings
"""


def are_interleaving(a: str, b: str, c: str) -> bool:
    """
    Check if string c is formed by interleaving strings a and b.

    An interleaving of two strings preserves the relative order of characters
    from each string but allows them to be interleaved with each other.

    Args:
        a: First string
        b: Second string
        c: Target string to check

    Returns:
        True if c is an interleaving of a and b, False otherwise
    """
    m, n = len(a), len(b)

    # Check if total length matches
    if len(c) != m + n:
        return False

    # DP table: dp[i][j] = True if c[0:i+j] is formed by interleaving a[0:i] and b[0:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty strings
    dp[0][0] = True

    # Fill first row (only string a contributes)
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and a[i - 1] == c[i - 1]

    # Fill first column (only string b contributes)
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and b[j - 1] == c[j - 1]

    # Fill the rest of the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Current character of c can come from either a[i-1] or b[j-1]
            dp[i][j] = (dp[i - 1][j] and a[i - 1] == c[i + j - 1]) or (
                dp[i][j - 1] and b[j - 1] == c[i + j - 1]
            )

    return dp[m][n]


def are_interleaving_optimized(a: str, b: str, c: str) -> bool:
    """
    Space-optimized version using only O(n) space.
    """
    m, n = len(a), len(b)

    if len(c) != m + n:
        return False

    # Use the shorter string for space optimization
    if n > m:
        return are_interleaving_optimized(b, a, c)

    # DP array of size n+1
    dp = [False] * (n + 1)
    dp[0] = True

    # Initialize first row
    for j in range(1, n + 1):
        dp[j] = dp[j - 1] and b[j - 1] == c[j - 1]

    # Fill the DP table
    for i in range(1, m + 1):
        # Update first column
        dp[0] = dp[0] and a[i - 1] == c[i - 1]

        for j in range(1, n + 1):
            dp[j] = (dp[j] and a[i - 1] == c[i + j - 1]) or (
                dp[j - 1] and b[j - 1] == c[i + j - 1]
            )

    return dp[n]


def are_interleaving_recursive(
    a: str, b: str, c: str, i: int = 0, j: int = 0, k: int = 0, memo: dict = None
) -> bool:
    """
    Recursive approach with memoization.
    """
    if memo is None:
        memo = {}

    # Base case: all strings processed
    if k == len(c):
        return i == len(a) and j == len(b)

    # Check if result is already computed
    key = (i, j, k)
    if key in memo:
        return memo[key]

    result = False

    # If current character matches with a[i], move forward in a
    if i < len(a) and a[i] == c[k]:
        result = are_interleaving_recursive(a, b, c, i + 1, j, k + 1, memo)

    # If current character matches with b[j], move forward in b
    if not result and j < len(b) and b[j] == c[k]:
        result = are_interleaving_recursive(a, b, c, i, j + 1, k + 1, memo)

    memo[key] = result
    return result


def test_are_interleaving():
    """Test cases for interleaving strings."""
    test_cases = [
        ("abc", "def", "adbcef", True),
        ("abc", "def", "abdecf", True),
        ("abc", "def", "abcdef", True),
        ("abc", "def", "defabc", True),
        ("abc", "def", "aebdcf", False),
        ("", "", "", True),
        ("", "abc", "abc", True),
        ("abc", "", "abc", True),
        ("ab", "cd", "abcd", True),
        ("ab", "cd", "acbd", True),
        ("ab", "cd", "adcb", False),
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
    ]

    for i, (a, b, c, expected) in enumerate(test_cases):
        result = are_interleaving(a, b, c)
        assert result == expected, (
            f"Test case {i} failed: Expected {expected}, got {result}"
        )

    print("All test cases passed!")


if __name__ == "__main__":
    test_are_interleaving()

    # Example usage
    a, b, c = "abc", "def", "adbcef"
    result = are_interleaving(a, b, c)
    print(f"Is '{c}' an interleaving of '{a}' and '{b}'? {result}")
