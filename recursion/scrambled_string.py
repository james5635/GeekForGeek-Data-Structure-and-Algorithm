"""
Check if a string is a scrambled form of another string
https://www.geeksforgeeks.org/dsa/check-if-a-string-is-a-scrambled-form-of-another-string/

Given two strings s1 and s2 of equal length, determine if s2 is a scrambled version of s1.
A scrambled string is formed by recursively splitting the string into two non-empty substrings
and rearranging them randomly.

Approach: Top-Down DP (Memoization) - O(n^4) time and O(n^3) space
"""


def scramble_recur(i1, i2, length, s1, s2, dp):
    """
    Recursive function with memoization to check if s2 is a scrambled form of s1.

    Args:
        i1: Start index in s1
        i2: Start index in s2
        length: Length of substring to consider
        s1: First string
        s2: Second string
        dp: Memoization table

    Returns:
        True if s2[i2:i2+length] is a scrambled form of s1[i1:i1+length]
    """
    # For single character, compare the two characters
    if length == 1:
        return s1[i1] == s2[i2]

    # If value is computed, return it
    if dp[i1][i2][length] != -1:
        return dp[i1][i2][length]

    ans = False

    for len_ in range(1, length):
        # Check if s2[i2, i2+len-1] is scrambled version of s1[i1, i1+len-1]
        # and s2[i2+len, i2+length-1] is scrambled version of s1[i1+len, i1+length-1]
        val1 = scramble_recur(i1, i2, len_, s1, s2, dp) and scramble_recur(
            i1 + len_, i2 + len_, length - len_, s1, s2, dp
        )

        # Check if s2[i2+length-len+1, i2+length] is scrambled version of s1[i1, i1+len-1]
        # and s2[i2, i2+length-len] is scrambled version of s1[i1+len, i1+length-1]
        val2 = scramble_recur(
            i1, i2 + length - len_, len_, s1, s2, dp
        ) and scramble_recur(i1 + len_, i2, length - len_, s1, s2, dp)

        # If any version is scrambled
        if val1 or val2:
            ans = True
            break

    # Memoize the value and return it
    dp[i1][i2][length] = ans
    return ans


def is_scramble(s1, s2):
    """
    Check if s2 is a scrambled form of s1.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if s2 is a scrambled form of s1, False otherwise
    """
    # Strings of non-equal length can't be scramble strings
    if len(s1) != len(s2):
        return False

    n = len(s1)

    # Empty strings are scramble strings
    if n == 0:
        return True

    # Equal strings are scramble strings
    if s1 == s2:
        return True

    # Create a 3D array for memoization
    dp = [[[-1] * (n + 1) for _ in range(n)] for _ in range(n)]

    return scramble_recur(0, 0, n, s1, s2, dp)


def main():
    """
    Main function to demonstrate the algorithm.
    """
    # Test case 1
    print("Test Case 1:")
    s1 = "coder"
    s2 = "ocder"
    print(f's1 = "{s1}"')
    print(f's2 = "{s2}"')
    print(f"Output: {'Yes' if is_scramble(s1, s2) else 'No'}")
    print()

    # Test case 2
    print("Test Case 2:")
    s1 = "abcde"
    s2 = "caebd"
    print(f's1 = "{s1}"')
    print(f's2 = "{s2}"')
    print(f"Output: {'Yes' if is_scramble(s1, s2) else 'No'}")
    print()

    # Test case 3
    print("Test Case 3:")
    s1 = "great"
    s2 = "rgeat"
    print(f's1 = "{s1}"')
    print(f's2 = "{s2}"')
    print(f"Output: {'Yes' if is_scramble(s1, s2) else 'No'}")
    print()

    # Test case 4
    print("Test Case 4:")
    s1 = "abcd"
    s2 = "bdac"
    print(f's1 = "{s1}"')
    print(f's2 = "{s2}"')
    print(f"Output: {'Yes' if is_scramble(s1, s2) else 'No'}")


if __name__ == "__main__":
    main()
