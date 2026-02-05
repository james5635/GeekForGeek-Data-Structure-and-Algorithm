"""
Check if Strings Are Rotations of Each Other

Given two strings s1 and s2 of equal length, determine whether s2 is a rotation of s1.
A string is said to be a rotation of another if it can be obtained by shifting
some leading characters of the original string to its end.

Approach: Using KMP Algorithm - O(n) Time and O(n) Space
If s2 is a rotation of s1, then s2 must be a substring of s1+s1.
"""


def compute_lps_array(pat):
    """
    Compute Longest Prefix Suffix array for KMP algorithm.

    Args:
        pat: Pattern string

    Returns:
        LPS array
    """
    n = len(pat)
    lps = [0] * n
    pat_len = 0
    i = 1

    while i < n:
        if pat[i] == pat[pat_len]:
            pat_len += 1
            lps[i] = pat_len
            i += 1
        else:
            if pat_len != 0:
                pat_len = lps[pat_len - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def are_rotations(s1, s2):
    """
    Check if s2 is a rotation of s1 using KMP algorithm.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if s2 is a rotation of s1, False otherwise
    """
    if len(s1) != len(s2):
        return False

    txt = s1 + s1
    pat = s2
    n = len(txt)
    m = len(pat)

    lps = compute_lps_array(pat)

    i = j = 0
    while i < n:
        if pat[j] == txt[i]:
            j += 1
            i += 1

        if j == m:
            return True

        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False


def main():
    """Test cases for string rotations."""
    test_cases = [
        ("abcd", "cdab", True),
        ("aab", "aba", True),
        ("abcd", "acbd", False),
        ("hello", "lohel", True),
        ("abc", "cba", False),
    ]

    print("=" * 50)
    print("Check String Rotations")
    print("=" * 50)

    for s1, s2, expected in test_cases:
        result = are_rotations(s1, s2)
        status = "✓" if result == expected else "✗"
        print(f"\nS1: '{s1}', S2: '{s2}'")
        print(f"Are rotations: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
