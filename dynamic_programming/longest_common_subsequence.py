"""
Longest Common Subsequence (LCS) - Dynamic Programming
Source: https://www.geeksforgeeks.org/dsa/longest-common-subsequence-dp-4/

Given two strings s1 and s2, find the length of the Longest Common Subsequence.
A subsequence is generated from the original string by deleting 0 or more characters,
without changing the relative order of the remaining characters.

Time Complexity: O(m * n) where m and n are lengths of the two strings
Space Complexity: O(m * n) for the DP table
"""


def lcs(s1: str, s2: str) -> int:
    """
    Find the length of the Longest Common Subsequence between two strings
    using bottom-up dynamic programming (tabulation).

    Args:
        s1: First input string
        s2: Second input string

    Returns:
        Length of the longest common subsequence
    """
    m = len(s1)
    n = len(s2)

    # Initialize DP table of size (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs_space_optimized(s1: str, s2: str) -> int:
    """
    Space-optimized version using a single 1D array.
    Reduces space complexity from O(m*n) to O(min(m,n)).

    Args:
        s1: First input string
        s2: Second input string

    Returns:
        Length of the longest common subsequence
    """
    m = len(s1)
    n = len(s2)

    dp = [0] * (n + 1)

    for i in range(1, m + 1):
        prev = dp[0]
        for j in range(1, n + 1):
            temp = dp[j]
            if s1[i - 1] == s2[j - 1]:
                dp[j] = 1 + prev
            else:
                dp[j] = max(dp[j - 1], dp[j])
            prev = temp

    return dp[n]


def get_lcs_string(s1: str, s2: str) -> str:
    """
    Reconstruct and return the actual Longest Common Subsequence string.

    Args:
        s1: First input string
        s2: Second input string

    Returns:
        The longest common subsequence string
    """
    m = len(s1)
    n = len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the LCS string
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(result))


if __name__ == "__main__":
    # Test case 1
    s1, s2 = "ABC", "ACD"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"LCS length: {lcs(s1, s2)}")  # Expected: 2
    print(f"LCS string: '{get_lcs_string(s1, s2)}'")  # Expected: "AC"
    print()

    # Test case 2
    s1, s2 = "AGGTAB", "GXTXAYB"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"LCS length: {lcs(s1, s2)}")  # Expected: 4
    print(f"LCS string: '{get_lcs_string(s1, s2)}'")  # Expected: "GTAB"
    print()

    # Test case 3
    s1, s2 = "ABC", "CBA"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"LCS length: {lcs(s1, s2)}")  # Expected: 1
    print()

    # Test case 4 - identical strings
    s1, s2 = "GEEKS", "GEEKS"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"LCS length: {lcs(s1, s2)}")  # Expected: 5
    print()

    # Test case 5 - no common subsequence
    s1, s2 = "ABC", "DEF"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"LCS length: {lcs(s1, s2)}")  # Expected: 0
    print()

    # Test case 6 - space optimized version
    s1, s2 = "AGGTAB", "GXTXAYB"
    print(f"Space optimized LCS length: {lcs_space_optimized(s1, s2)}")  # Expected: 4
    print()

    # Test case 7 - empty string
    s1, s2 = "", "ABC"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"LCS length: {lcs(s1, s2)}")  # Expected: 0
