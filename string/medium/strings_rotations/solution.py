"""
Strings Rotations of Each Other

Check if two strings are rotations of each other.

Time Complexity: O(n)
Space Complexity: O(n)
"""


def are_rotations(s1: str, s2: str) -> bool:
    """
    Check if two strings are rotations of each other.

    A string s2 is a rotation of s1 if s2 can be obtained by
    moving some leading characters of s1 to the end.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if s2 is a rotation of s1, False otherwise
    """
    # Check if lengths are equal
    if len(s1) != len(s2):
        return False

    # Check if s2 is a substring of s1 + s1
    concatenated = s1 + s1
    return s2 in concatenated


def are_rotations_naive(s1: str, s2: str) -> bool:
    """
    Naive approach: check all possible rotations.
    """
    if len(s1) != len(s2):
        return False

    n = len(s1)
    for i in range(n):
        # Check rotation at position i
        is_rotation = True
        for j in range(n):
            if s1[(i + j) % n] != s2[j]:
                is_rotation = False
                break
        if is_rotation:
            return True

    return False


def are_rotations_optimized(s1: str, s2: str) -> bool:
    """
    Optimized version using KMP algorithm for substring search.
    """

    def kmp_search(pattern: str, text: str) -> bool:
        """KMP algorithm to check if pattern exists in text."""
        if not pattern:
            return True

        # Build LPS array
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # Search for pattern
        i = 0  # index for text
        j = 0  # index for pattern

        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1

                if j == len(pattern):
                    return True
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return False

    if len(s1) != len(s2):
        return False

    return kmp_search(s2, s1 + s1)


def test_are_rotations():
    """Test cases for strings rotation."""
    test_cases = [
        ("ABCD", "CDAB", True),
        ("ABCD", "CDBA", False),
        ("waterbottle", "erbottlewat", True),
        ("", "", True),
        ("a", "a", True),
        ("ab", "ba", True),
        ("ab", "ab", True),
        ("ab", "abc", False),
        ("abcde", "cdeab", True),
        ("abcde", "abced", False),
        ("aaaa", "aaaa", True),
        ("abc", "def", False),
    ]

    for i, (s1, s2, expected) in enumerate(test_cases):
        result = are_rotations(s1, s2)
        assert result == expected, (
            f"Test case {i} failed: Expected {expected}, got {result}"
        )

    print("All test cases passed!")


if __name__ == "__main__":
    test_are_rotations()

    # Example usage
    s1 = "ABCD"
    s2 = "CDAB"
    result = are_rotations(s1, s2)
    print(f"Are '{s1}' and '{s2}' rotations of each other? {result}")
