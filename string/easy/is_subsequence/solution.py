"""
Is Subsequence

Problem: Given two strings str1 and str2, find if str1 is a subsequence of str2.
A subsequence is a sequence that appears in the same relative order,
but not necessarily contiguous.

Examples:
- Input: str1 = "AXY", str2 = "ADXCPY"
  Output: True (A, X, Y appear in order)
- Input: str1 = "AXY", str2 = "YADXCP"
  Output: False (order not maintained)

Time Complexity: O(n) where n is length of str2
Space Complexity: O(1)
"""


def is_subsequence(str1: str, str2: str) -> bool:
    """
    Check if str1 is a subsequence of str2.

    Args:
        str1: Potential subsequence
        str2: Main string

    Returns:
        True if str1 is subsequence of str2, False otherwise
    """
    m, n = len(str1), len(str2)
    i, j = 0, 0

    while i < m and j < n:
        if str1[i] == str2[j]:
            i += 1
        j += 1

    # If we matched all characters of str1
    return i == m


def is_subsequence_recursive(
    str1: str, str2: str, m: int = None, n: int = None
) -> bool:
    """
    Recursive approach to check subsequence.

    Args:
        str1: Potential subsequence
        str2: Main string
        m: Length of str1 (for recursion)
        n: Length of str2 (for recursion)

    Returns:
        True if str1 is subsequence of str2
    """
    if m is None:
        m, n = len(str1), len(str2)

    # Base cases
    if m == 0:
        return True
    if n == 0:
        return False

    # If last characters match, check remaining
    if str1[m - 1] == str2[n - 1]:
        return is_subsequence_recursive(str1, str2, m - 1, n - 1)

    # If last characters don't match, ignore last char of str2
    return is_subsequence_recursive(str1, str2, m, n - 1)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("AXY", "ADXCPY", True),
        ("AXY", "YADXCP", False),
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("", "anything", True),
        ("abc", "", False),
        ("a", "a", True),
        ("abc", "abc", True),
        ("ace", "abcde", True),
        ("aec", "abcde", False),
        ("hello", "hello world", True),
    ]

    print("=" * 70)
    print("Is Subsequence - Test Results")
    print("=" * 70)

    for str1, str2, expected in test_cases:
        result = is_subsequence(str1, str2)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"str1: '{str1}' | str2: '{str2}' | Expected: {expected} | Got: {result} | {status}"
        )

    print("=" * 70)

    # Compare implementations
    print("\nComparing implementations:")
    print("-" * 70)
    for str1, str2, expected in test_cases[:8]:
        r1 = is_subsequence(str1, str2)
        r2 = is_subsequence_recursive(str1, str2)
        all_match = r1 == r2 == expected
        status = "PASS" if all_match else "FAIL"
        print(
            f"str1='{str1}', str2='{str2}' | Iterative: {r1} | Recursive: {r2} | {status}"
        )
