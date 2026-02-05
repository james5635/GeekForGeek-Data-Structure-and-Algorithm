"""
Find all Palindromic Partitions of a String
https://www.geeksforgeeks.org/dsa/given-a-string-print-all-possible-palindromic-partition/

Given a string s, find all possible ways to partition it such that every substring in the partition is a palindrome.

Approach: Backtracking with Memoization (Expected Approach)
Time Complexity: O(n^2 + 2^n * n)
Auxiliary Space: O(n^2), for the DP table
"""


def palindromes(s, dp):
    """
    Precompute all palindromic substrings in s using DP.

    Args:
        s: The input string
        dp: DP table to store if substring s[i..j] is a palindrome
    """
    n = len(s)

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check two-character substrings
    for i in range(n - 1):
        dp[i][i + 1] = s[i] == s[i + 1]

    # Check substrings of length 3 or more using bottom-up DP
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]


def backtrack(idx, s, curr, res, dp):
    """
    Recursive function to find all palindromic partitions.

    Args:
        idx: Current index
        s: The input string
        curr: Current partition being built
        res: Result list to store all valid partitions
        dp: DP table for palindrome lookup
    """
    # If we have reached the end of the string, store current partition
    if idx == len(s):
        res.append(list(curr))
        return

    # Try all substrings starting from index idx
    for i in range(idx, len(s)):
        # If s[idx..i] is a palindrome, we can include it
        if dp[idx][i]:
            # Choose the substring
            curr.append(s[idx : i + 1])
            # Explore further from next index
            backtrack(i + 1, s, curr, res, dp)
            # Undo the choice (backtrack)
            curr.pop()


def palin_parts(s):
    """
    Return all palindromic partitions of string s.

    Args:
        s: The input string

    Returns:
        List of all possible palindromic partitions
    """
    n = len(s)
    # DP table to store if substring s[i..j] is a palindrome
    dp = [[False] * n for _ in range(n)]

    # Precompute all palindromic substrings using DP
    palindromes(s, dp)

    # Final result
    res = []
    # Current partition
    curr = []

    # Begin backtracking from index 0
    backtrack(0, s, curr, res, dp)
    return res


def main():
    """
    Main function to demonstrate the algorithm.
    """
    # Test case 1
    print("Test Case 1:")
    s = "geeks"
    print(f'Input: s = "{s}"')
    result = palin_parts(s)
    print(f"Output:")
    for partition in result:
        print(f"  {partition}")
    print()

    # Test case 2
    print("Test Case 2:")
    s = "abcba"
    print(f'Input: s = "{s}"')
    result = palin_parts(s)
    print(f"Output:")
    for partition in result:
        print(f"  {partition}")
    print()

    # Test case 3
    print("Test Case 3:")
    s = "aab"
    print(f'Input: s = "{s}"')
    result = palin_parts(s)
    print(f"Output:")
    for partition in result:
        print(f"  {partition}")


if __name__ == "__main__":
    main()
