"""
Check if String is Substring of Another

Problem: Given two strings str1 and str2, check if str1 is a substring of str2.

Examples:
- Input: str1 = "for", str2 = "geeksforgeeks"
  Output: True
- Input: str1 = "practice", str2 = "geeksforgeeks"
  Output: False

Time Complexity: O(n * m) where n and m are lengths of strings
Space Complexity: O(1)
"""


def is_substring(str1: str, str2: str) -> bool:
    """
    Check if str1 is a substring of str2.

    Args:
        str1: Substring to search for
        str2: Main string to search in

    Returns:
        True if str1 is substring of str2, False otherwise
    """
    n, m = len(str2), len(str1)

    if m > n:
        return False

    if m == 0:
        return True

    for i in range(n - m + 1):
        if str2[i : i + m] == str1:
            return True

    return False


def is_substring_builtin(str1: str, str2: str) -> bool:
    """
    Using Python's 'in' operator.

    Args:
        str1: Substring to search for
        str2: Main string

    Returns:
        True if str1 is substring of str2
    """
    return str1 in str2


def is_substring_find(str1: str, str2: str) -> bool:
    """
    Using string find method.

    Args:
        str1: Substring to search for
        str2: Main string

    Returns:
        True if str1 is substring of str2
    """
    return str2.find(str1) != -1


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("for", "geeksforgeeks", True),
        ("practice", "geeksforgeeks", False),
        ("abc", "abc", True),
        ("", "anything", True),  # Empty string is substring of any string
        ("xyz", "", False),
        ("hello", "hello world", True),
        ("world", "hello world", True),
        ("test", "testing", True),
        ("aaa", "aaaa", True),
        ("abc", "def", False),
    ]

    print("=" * 70)
    print("Check if String is Substring of Another - Test Results")
    print("=" * 70)

    for str1, str2, expected in test_cases:
        result = is_substring(str1, str2)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"str1: '{str1}' | str2: '{str2}' | Expected: {expected} | Got: {result} | {status}"
        )

    print("=" * 70)

    # Compare implementations
    print("\nComparing implementations:")
    print("-" * 70)
    for str1, str2, expected in test_cases[:6]:
        r1 = is_substring(str1, str2)
        r2 = is_substring_builtin(str1, str2)
        r3 = is_substring_find(str1, str2)
        all_match = r1 == r2 == r3 == expected
        status = "PASS" if all_match else "FAIL"
        print(
            f"str1='{str1}', str2='{str2}' | Manual: {r1} | 'in': {r2} | find(): {r3} | {status}"
        )
