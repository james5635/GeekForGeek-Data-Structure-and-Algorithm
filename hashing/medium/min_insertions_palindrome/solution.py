"""
Minimum Insertions to Form Longest Palindrome

Problem: Given a string, find the minimum number of insertions needed to make it
a palindrome. We can remove characters but want to minimize insertions needed.

Approach: The minimum insertions = length of string - length of longest palindromic
subsequence. Find LPS using dynamic programming or hash-based approach.

Time Complexity: O(n^2) - LPS using DP, or O(n) with optimized approach
Space Complexity: O(n^2) for DP table, O(n) for optimized
"""

from collections import Counter


def min_insertions_to_palindrome(s):
    """
    Find minimum insertions needed to make string a palindrome.

    Args:
        s: Input string

    Returns:
        Minimum number of insertions needed
    """
    n = len(s)
    if n <= 1:
        return 0

    # LPS[i][j] = length of longest palindromic subsequence in s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # All single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill table for substrings of length 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    lps_length = dp[0][n - 1]
    return n - lps_length


def get_min_insertions_chars(s):
    """
    Get the characters that need to be inserted to form palindrome.

    Args:
        s: Input string

    Returns:
        List of characters to insert
    """
    n = len(s)
    if n <= 1:
        return []

    # Build LPS using DP
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2 if length > 2 else 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # Reconstruct LPS
    lps = []
    i, j = 0, n - 1
    while i <= j:
        if s[i] == s[j]:
            if i == j:
                lps.append(s[i])
            else:
                lps.extend([s[i], s[j]])
            i += 1
            j -= 1
        elif dp[i + 1][j] > dp[i][j - 1]:
            i += 1
        else:
            j -= 1

    # Characters not in LPS need to be inserted
    char_count = Counter(s)
    lps_count = Counter(lps)

    insertions = []
    for char, count in char_count.items():
        needed = count - lps_count.get(char, 0)
        insertions.extend([char] * needed)

    return insertions


def min_insertions_optimized(s):
    """
    Optimized approach using character frequency analysis.
    This gives an approximation for some cases.

    Args:
        s: Input string

    Returns:
        Approximate minimum insertions
    """
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2 == 1)

    # At least (odd_count - 1) characters need to be paired
    return max(0, odd_count - 1)


if __name__ == "__main__":
    # Test Case 1: Already palindrome
    s1 = "abba"
    print(f"String: '{s1}'")
    print(f"Min insertions: {min_insertions_to_palindrome(s1)}")
    print()

    # Test Case 2: Needs insertions
    s2 = "abcd"
    print(f"String: '{s2}'")
    print(f"Min insertions: {min_insertions_to_palindrome(s2)}")
    print()

    # Test Case 3: Single character
    s3 = "a"
    print(f"String: '{s3}'")
    print(f"Min insertions: {min_insertions_to_palindrome(s3)}")
    print()

    # Test Case 4: Two different characters
    s4 = "ab"
    print(f"String: '{s4}'")
    print(f"Min insertions: {min_insertions_to_palindrome(s4)}")
    print()

    # Test Case 5: Mixed case
    s5 = "geeks"
    print(f"String: '{s5}'")
    print(f"Min insertions: {min_insertions_to_palindrome(s5)}")
    print()

    # Test Case 6: Empty string
    s6 = ""
    print(f"String: '{s6}'")
    print(f"Min insertions: {min_insertions_to_palindrome(s6)}")
    print()

    # Test Case 7: Repeated characters
    s7 = "aaaa"
    print(f"String: '{s7}'")
    print(f"Min insertions: {min_insertions_to_palindrome(s7)}")
    print()

    # Test Case 8: Complex string
    s8 = "abcdeba"
    print(f"String: '{s8}'")
    print(f"Min insertions: {min_insertions_to_palindrome(s8)}")
    print()

    # Test Case 9: Characters to insert
    s9 = "abc"
    print(f"String: '{s9}'")
    print(f"Min insertions: {min_insertions_to_palindrome(s9)}")
    print(f"Chars to insert: {get_min_insertions_chars(s9)}")
