"""
Make Two Strings Anagram without Deletion

Given two strings, find the minimum number of character operations
(replace, insert, add) required to make two strings anagrams of each other.
Unlike the standard anagram problem, we cannot delete characters - we can
only add or replace.

Examples:
- "abc", "bca" -> 0 (already anagrams)
- "abc", "def" -> 6 (replace all or add missing)
- "aabb", "abab" -> 0 (already anagrams with same chars)

Time Complexity: O(n) where n is the length of longer string
Space Complexity: O(1) for fixed character set
"""

from collections import Counter


def minOperationsToAnagram(s1, s2):
    """
    Find minimum operations to make s1 and s2 anagrams
    Operations allowed: add characters to either string
    """
    # Count characters in both strings
    count1 = Counter(s1)
    count2 = Counter(s2)

    operations = 0

    # Get all unique characters
    all_chars = set(s1) | set(s2)

    for char in all_chars:
        freq1 = count1.get(char, 0)
        freq2 = count2.get(char, 0)

        # Add the difference to operations
        operations += abs(freq1 - freq2)

    return operations


def minOperationsToAnagramReplaceOnly(s1, s2):
    """
    Find minimum replacements to make s1 and s2 anagrams
    Only replacement operation is allowed
    """
    if len(s1) != len(s2):
        return -1  # Cannot make anagrams with different lengths using only replace

    # Count characters in both strings
    count1 = Counter(s1)
    count2 = Counter(s2)

    replacements = 0

    # For each character, calculate how many need to be replaced
    for char in set(s1) | set(s2):
        freq1 = count1.get(char, 0)
        freq2 = count2.get(char, 0)

        # We need to replace characters where frequencies differ
        if freq1 > freq2:
            replacements += freq1 - freq2

    return replacements


def minOperationsNoDeletion(s1, s2):
    """
    Minimum operations (add/change) to make strings anagrams
    without deleting any characters
    """
    m, n = len(s1), len(s2)

    # Count frequency of each character
    count1 = [0] * 26
    count2 = [0] * 26

    for char in s1:
        count1[ord(char) - ord("a")] += 1

    for char in s2:
        count2[ord(char) - ord("a")] += 1

    operations = 0

    # Calculate operations needed
    for i in range(26):
        if count1[i] > count2[i]:
            # Need to add (count1[i] - count2[i]) of char[i] to s2
            operations += count1[i] - count2[i]
        elif count2[i] > count1[i]:
            # Need to add (count2[i] - count1[i]) of char[i] to s1
            operations += count2[i] - count1[i]

    return operations


def canMakeAnagram(s1, s2):
    """
    Check if it's possible to make anagrams without deletion
    (always possible by adding characters)
    """
    return True  # Always possible by adding characters


# Test the functions
if __name__ == "__main__":
    test_cases = [
        ("abc", "bca"),
        ("abc", "def"),
        ("aabb", "abab"),
        ("hello", "world"),
        ("anagram", "nagaram"),
        ("abc", "abcd"),
        ("aabbcc", "abc"),
    ]

    print("Make Two Strings Anagram without Deletion")
    print("=" * 50)

    for s1, s2 in test_cases:
        ops_add = minOperationsToAnagram(s1, s2)
        ops_replace = minOperationsToAnagramReplaceOnly(s1, s2)
        ops_no_del = minOperationsNoDeletion(s1, s2)

        print(f"String 1: '{s1}'")
        print(f"String 2: '{s2}'")
        print(f"  Min operations (add allowed): {ops_add}")
        print(f"  Min operations (replace only): {ops_replace}")
        print(f"  Min operations (no deletion): {ops_no_del}")
        print()

    print("Operations explanation:")
    print("- 'add allowed': Can add characters to either string")
    print("- 'replace only': Can only replace existing characters")
    print("- 'no deletion': Standard anagram transformation")
