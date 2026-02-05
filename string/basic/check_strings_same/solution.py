"""
Check if Two Strings are Same
==============================

Problem Description:
--------------------
Given two strings, check if they are the same (equal).

Approaches:
-----------
1. Direct comparison: Use == operator
2. Character by character: Compare each character
3. Using all() and zip: Check all pairs match

Time Complexity: O(n) where n is the length of shorter string
Space Complexity: O(1)

Reference: https://www.geeksforgeeks.org/dsa/program-to-check-if-two-strings-are-same-or-not/
"""


def are_strings_same_direct(s1: str, s2: str) -> bool:
    """Check if strings are same using direct comparison."""
    return s1 == s2


def are_strings_same_manual(s1: str, s2: str) -> bool:
    """Check if strings are same by comparing character by character."""
    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def are_strings_same_zip(s1: str, s2: str) -> bool:
    """Check if strings are same using zip."""
    if len(s1) != len(s2):
        return False
    return all(c1 == c2 for c1, c2 in zip(s1, s2))


def test_are_strings_same():
    """Test cases for string comparison."""
    test_cases = [
        ("hello", "hello", True),
        ("hello", "world", False),
        ("Hello", "hello", False),
        ("", "", True),
        ("a", "a", True),
        ("ab", "abc", False),
        ("abc", "ab", False),
        ("python", "python", True),
        ("test ", "test", False),
    ]

    functions = [
        ("Direct comparison", are_strings_same_direct),
        ("Manual comparison", are_strings_same_manual),
        ("Zip comparison", are_strings_same_zip),
    ]

    for func_name, func in functions:
        print(f"\nTesting {func_name}:")
        for i, (s1, s2, expected) in enumerate(test_cases, 1):
            result = func(s1, s2)
            status = "✓" if result == expected else "✗"
            print(
                f"  Test {i}: {status} '{s1}' vs '{s2}' -> {result} (expected: {expected})"
            )


if __name__ == "__main__":
    test_are_strings_same()
