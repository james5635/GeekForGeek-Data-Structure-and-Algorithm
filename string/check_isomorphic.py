"""
Check if Two Strings Are Isomorphic

Given two strings s1 and s2, determine if they are isomorphic.
Two strings are isomorphic if characters in s1 can be replaced to get s2
with each character mapping to a unique character.

Approach: Using HashMap and Set - O(n) Time and O(1) Space
Use a map to store character mappings and a set to track used characters.
"""


def are_isomorphic(s1, s2):
    """
    Check if two strings are isomorphic.

    Args:
        s1, s2: Input strings

    Returns:
        True if isomorphic, False otherwise
    """
    if len(s1) != len(s2):
        return False

    m1 = {}  # Character mapping from s1 to s2
    set2 = set()  # Already mapped characters in s2

    for c1, c2 in zip(s1, s2):
        if c1 in m1:
            if m1[c1] != c2:
                return False
        else:
            if c2 in set2:
                return False
            m1[c1] = c2
            set2.add(c2)

    return True


def main():
    """Test cases for isomorphic strings."""
    test_cases = [
        ("aab", "xxy", True),
        ("aab", "xyz", False),
        ("abc", "xxz", False),
        ("paper", "title", True),
        ("foo", "bar", False),
        ("ab", "aa", False),
    ]

    print("=" * 50)
    print("Check Isomorphic Strings")
    print("=" * 50)

    for s1, s2, expected in test_cases:
        result = are_isomorphic(s1, s2)
        status = "✓" if result == expected else "✗"
        print(f"\nS1: '{s1}', S2: '{s2}'")
        print(f"Isomorphic: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
