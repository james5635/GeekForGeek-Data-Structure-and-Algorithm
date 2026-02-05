"""
Check if One String is Subsequence of Another
Check if s1 is a subsequence of s2 (can be derived by deleting some elements
without changing the order of remaining elements).

Approach: Two pointers (iterative) or recursion
Time Complexity: O(n), where n is length of s2
Auxiliary Space: O(1) for iterative, O(n) for recursion
"""

from typing import Optional


def is_subsequence_iterative(s1: str, s2: str) -> bool:
    """
    Check if s1 is a subsequence of s2 using two pointers.

    Args:
        s1: Potential subsequence
        s2: Main string

    Returns:
        True if s1 is subsequence of s2, False otherwise
    """
    m = len(s1)
    n = len(s2)

    if m > n:
        return False

    i = j = 0
    while i < m and j < n:
        if s1[i] == s2[j]:
            i += 1
        j += 1

    # If i reached end of s1, all characters were found
    return i == m


def is_subsequence_recursive(
    s1: str, s2: str, m: Optional[int] = None, n: Optional[int] = None
) -> bool:
    """
    Recursive approach to check subsequence.
    """
    if m is None:
        m = len(s1)
    if n is None:
        n = len(s2)

    # Base cases
    if m == 0:
        return True
    if n == 0:
        return False

    # If last characters match
    if s1[m - 1] == s2[n - 1]:
        return is_subsequence_recursive(s1, s2, m - 1, n - 1)

    # If last characters don't match
    return is_subsequence_recursive(s1, s2, m, n - 1)


def main():
    """Test the subsequence checker with various inputs."""
    test_cases = [
        ("AXY", "ADXCPY", True),
        ("AXY", "YADXCP", False),
        ("gksrek", "geeksforgeeks", True),
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("", "abc", True),
        ("abc", "", False),
        ("a", "a", True),
        ("hello", "hello world", True),
    ]

    print("Check if One String is Subsequence of Another")
    print("=" * 60)

    for s1, s2, expected in test_cases:
        result_iter = is_subsequence_iterative(s1, s2)
        result_rec = is_subsequence_recursive(s1, s2)

        all_pass = result_iter == expected and result_rec == expected
        status = "✓ PASS" if all_pass else "✗ FAIL"

        print(f"{status} | s1: '{s1}', s2: '{s2}'")
        print(f"       | Expected: {expected}")
        print(f"       | Iterative: {result_iter}, Recursive: {result_rec}")
        print()


if __name__ == "__main__":
    main()
