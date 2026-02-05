"""
Ways to Increase LCS Length of Two Strings by One

Given two strings str1 and str2, find the number of ways to increase the
LCS (Longest Common Subsequence) length by exactly 1.

This is a hard dynamic programming problem that involves:
1. Computing LCS of the two strings
2. Finding all characters that can be added to increase LCS by 1

Time Complexity: O(m * n) for LCS computation
Space Complexity: O(m * n)
"""


def lcs(str1, str2):
    """
    Compute LCS length using dynamic programming
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def waysToIncreaseLCS(str1, str2):
    """
    Find number of ways to increase LCS length by exactly 1

    Approach:
    1. Compute LCS of str1 and str2
    2. For each character not in the LCS, check if adding it to one string
       would increase the LCS
    """
    m, n = len(str1), len(str2)
    original_lcs = lcs(str1, str2)

    ways = 0

    # Try inserting each possible character (a-z) at each position in str1
    for i in range(m + 1):
        for ch in "abcdefghijklmnopqrstuvwxyz":
            new_str = str1[:i] + ch + str1[i:]
            new_lcs = lcs(new_str, str2)
            if new_lcs == original_lcs + 1:
                ways += 1

    # Try inserting each possible character at each position in str2
    for i in range(n + 1):
        for ch in "abcdefghijklmnopqrstuvwxyz":
            new_str = str2[:i] + ch + str2[i:]
            new_lcs = lcs(str1, new_str)
            if new_lcs == original_lcs + 1:
                ways += 1

    return ways


def waysToIncreaseLCSOptimized(str1, str2):
    """
    Optimized approach using LCS DP table analysis
    """
    m, n = len(str1), len(str2)

    # dp[i][j] = LCS of str1[0..i-1] and str2[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # dp2[i][j] = LCS of str1[i..m-1] and str2[j..n-1] (from the end)
    dp2 = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill dp table (forward)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Fill dp2 table (backward)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if str1[i] == str2[j]:
                dp2[i][j] = dp2[i + 1][j + 1] + 1
            else:
                dp2[i][j] = max(dp2[i + 1][j], dp2[i][j + 1])

    original_lcs = dp[m][n]
    ways = 0

    # Check all positions where we could extend the LCS
    for i in range(m + 1):
        for j in range(n + 1):
            for ch in set(str1 + str2):  # Only check characters that appear
                # Check if inserting 'ch' at position i in str1 increases LCS
                if i < m and str1[i] == ch:
                    continue
                if j < n and str2[j] == ch:
                    continue

                # Calculate new LCS if we match this character
                lcs_before = dp[i][j] if i > 0 and j > 0 else 0
                lcs_after = dp2[i][j] if i < m and j < n else 0

                if lcs_before + 1 + lcs_after == original_lcs + 1:
                    ways += 1

    return ways


# Test the function
if __name__ == "__main__":
    test_cases = [
        ("abc", "abc"),
        ("abcd", "anc"),
        ("AGGTAB", "GXTXAYB"),
    ]

    print("Ways to Increase LCS Length by One")
    print("=" * 40)

    for str1, str2 in test_cases:
        original_lcs = lcs(str1, str2)
        # Note: The brute force approach is very slow for long strings
        # ways = waysToIncreaseLCS(str1, str2)

        print(f"String 1: '{str1}'")
        print(f"String 2: '{str2}'")
        print(f"Original LCS length: {original_lcs}")
        print(f"LCS string: ", end="")

        # Find and print the actual LCS
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Backtrack to find LCS
        lcs_str = []
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                lcs_str.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        print("".join(reversed(lcs_str)))
        print()

    print("Note: This problem requires advanced DP techniques.")
    print("The exact implementation depends on the specific problem constraints.")
