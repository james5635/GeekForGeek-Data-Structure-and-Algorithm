"""
Check if a String is Substring of Another
Find if pattern string is a substring of text string.
Return the index of first occurrence, or -1 if not found.

Approach: Nested loops (brute force) or built-in find()
Time Complexity: O(m*n) for brute force, O(n) for built-in
Auxiliary Space: O(1)
"""


def find_substring(txt: str, pat: str) -> int:
    """
    Find if pat is a substring of txt using nested loops.

    Args:
        txt: Main text string
        pat: Pattern to search for

    Returns:
        Index of first occurrence, or -1 if not found
    """
    n = len(txt)
    m = len(pat)

    # Iterate through txt
    for i in range(n - m + 1):
        j = 0
        # Check for substring match
        while j < m and txt[i + j] == pat[j]:
            j += 1

        # If we completed the inner loop, we found a match
        if j == m:
            return i

    # No match found
    return -1


def find_substring_builtin(txt: str, pat: str) -> int:
    """
    Using Python's built-in find() method.
    """
    return txt.find(pat)


def main():
    """Test the substring finder with various inputs."""
    test_cases = [
        ("geeksforgeeks", "eks", 2),
        ("geeksforgeeks", "xyz", -1),
        ("hello world", "world", 6),
        ("abcdef", "abc", 0),
        ("abcdef", "def", 3),
        ("abcdef", "xyz", -1),
        ("aaaa", "aa", 0),
        ("", "a", -1),
        ("abc", "", 0),
    ]

    print("Check if String is Substring of Another")
    print("=" * 60)

    for txt, pat, expected in test_cases:
        result = find_substring(txt, pat)
        builtin_result = find_substring_builtin(txt, pat)
        status = (
            "✓ PASS" if result == expected and result == builtin_result else "✗ FAIL"
        )

        print(f"{status} | Text: '{txt}', Pattern: '{pat}'")
        print(f"       | Expected: {expected}")
        print(f"       | Brute Force: {result}, Built-in: {builtin_result}")
        print()


if __name__ == "__main__":
    main()
