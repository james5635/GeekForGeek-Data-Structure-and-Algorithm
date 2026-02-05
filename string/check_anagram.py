"""
Check if Two Strings are Anagrams of Each Other
Two strings are anagrams if they contain the same characters with same frequencies.

Approach: Frequency array or sorting
Time Complexity: O(n), where n is length of strings
Auxiliary Space: O(1) for frequency array approach
"""

from collections import defaultdict


def are_anagrams_sorting(s1: str, s2: str) -> bool:
    """
    Check anagram using sorting approach.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if strings are anagrams, False otherwise
    """
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


def are_anagrams_frequency(s1: str, s2: str) -> bool:
    """
    Check anagram using frequency array (most efficient).
    """
    if len(s1) != len(s2):
        return False

    # For lowercase a-z
    freq = [0] * 26

    # Count frequency in s1
    for char in s1:
        freq[ord(char) - ord("a")] += 1

    # Subtract frequency using s2
    for char in s2:
        freq[ord(char) - ord("a")] -= 1

    # Check if all frequencies are zero
    for count in freq:
        if count != 0:
            return False

    return True


def are_anagrams_hashmap(s1: str, s2: str) -> bool:
    """
    Check anagram using hash map/dictionary.
    """
    if len(s1) != len(s2):
        return False

    char_count = defaultdict(int)

    # Count characters in s1
    for char in s1:
        char_count[char] += 1

    # Decrement count for characters in s2
    for char in s2:
        char_count[char] -= 1

    # Check if all counts are zero
    for count in char_count.values():
        if count != 0:
            return False

    return True


def main():
    """Test the anagram checker with various inputs."""
    test_cases = [
        ("geeks", "kseeg", True),
        ("allergy", "allergyy", False),
        ("listen", "silent", True),
        ("triangle", "integral", True),
        ("abc", "def", False),
        ("aabbcc", "abcabc", True),
        ("", "", True),
        ("a", "a", True),
        ("ab", "ba", True),
    ]

    print("Check if Two Strings are Anagrams")
    print("=" * 60)

    for s1, s2, expected in test_cases:
        result1 = are_anagrams_sorting(s1, s2)
        result2 = are_anagrams_frequency(s1, s2)
        result3 = are_anagrams_hashmap(s1, s2)

        all_pass = all(r == expected for r in [result1, result2, result3])
        status = "✓ PASS" if all_pass else "✗ FAIL"

        print(f"{status} | s1: '{s1}', s2: '{s2}'")
        print(f"       | Expected: {expected}")
        print(f"       | Sorting: {result1}, Frequency: {result2}, HashMap: {result3}")
        print()


if __name__ == "__main__":
    main()
