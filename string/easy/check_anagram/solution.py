"""
Check Anagram

Problem: Given two strings, check whether two strings are anagram of each other.
Two strings are anagram if they contain the same characters with same frequency.

Examples:
- Input: s1 = "listen", s2 = "silent"
  Output: True
- Input: s1 = "hello", s2 = "world"
  Output: False

Time Complexity: O(n) where n is length of string
Space Complexity: O(1) - fixed size character set
"""

from collections import Counter


def is_anagram(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams using Counter.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if strings are anagrams, False otherwise
    """
    return Counter(s1) == Counter(s2)


def is_anagram_sort(s1: str, s2: str) -> bool:
    """
    Check anagram by sorting both strings.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if strings are anagrams
    """
    return sorted(s1) == sorted(s2)


def is_anagram_manual(s1: str, s2: str) -> bool:
    """
    Manual implementation using character count array.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if strings are anagrams
    """
    if len(s1) != len(s2):
        return False

    # Count characters (assuming lowercase English letters)
    count = [0] * 256

    for char in s1:
        count[ord(char)] += 1

    for char in s2:
        count[ord(char)] -= 1
        if count[ord(char)] < 0:
            return False

    return True


def is_anagram_dict(s1: str, s2: str) -> bool:
    """
    Check anagram using dictionary for character counts.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if strings are anagrams
    """
    if len(s1) != len(s2):
        return False

    char_count = {}

    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in s2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "a", True),
        ("ab", "ba", True),
        ("abc", "abd", False),
        ("triangle", "integral", True),
        ("schoolmaster", "theclassroom", True),
    ]

    print("=" * 70)
    print("Check Anagram - Test Results")
    print("=" * 70)

    for s1, s2, expected in test_cases:
        result = is_anagram(s1, s2)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"s1: '{s1}' | s2: '{s2}' | Expected: {expected} | Got: {result} | {status}"
        )

    print("=" * 70)

    # Compare all implementations
    print("\nComparing all implementations:")
    print("-" * 70)
    implementations = [
        ("Counter", is_anagram),
        ("Sort", is_anagram_sort),
        ("Manual", is_anagram_manual),
        ("Dict", is_anagram_dict),
    ]

    for s1, s2, expected in test_cases[:7]:
        results = [impl(s1, s2) for _, impl in implementations]
        all_match = all(r == expected for r in results)
        status = "PASS" if all_match else "FAIL"
        print(f"s1='{s1}', s2='{s2}' | {status}")
        for (name, _), result in zip(implementations, results):
            print(f"  {name}: {result}")
