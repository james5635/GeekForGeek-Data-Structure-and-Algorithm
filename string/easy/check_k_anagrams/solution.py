"""
Check K-Anagrams

Problem: Two strings are called k-anagrams if both of the following conditions are true:
1. Both have same number of characters
2. Two strings can become anagrams by changing at most k characters

Examples:
- Input: str1 = "anagram", str2 = "grammar", k = 3
  Output: True (change 'gram' in str2 to 'anag' to make anagram)
- Input: str1 = "geeks", str2 = "eggkf", k = 1
  Output: False (need to change more than 1 character)

Time Complexity: O(n) where n is length of string
Space Complexity: O(1) - fixed size character set
"""

from collections import Counter


def are_k_anagrams(str1: str, str2: str, k: int) -> bool:
    """
    Check if two strings are k-anagrams.

    Args:
        str1: First string
        str2: Second string
        k: Maximum number of changes allowed

    Returns:
        True if strings are k-anagrams, False otherwise
    """
    if len(str1) != len(str2):
        return False

    # Count characters in both strings
    count1 = Counter(str1)
    count2 = Counter(str2)

    # Count differences
    changes_needed = 0

    # Count characters that need to be changed
    for char in count1:
        if count1[char] > count2.get(char, 0):
            changes_needed += count1[char] - count2.get(char, 0)

    return changes_needed <= k


def are_k_anagrams_manual(str1: str, str2: str, k: int) -> bool:
    """
    Manual implementation without Counter.

    Args:
        str1: First string
        str2: Second string
        k: Maximum changes allowed

    Returns:
        True if strings are k-anagrams
    """
    if len(str1) != len(str2):
        return False

    # Create frequency array
    freq = [0] * 26

    # Count characters in str1
    for char in str1:
        freq[ord(char) - ord("a")] += 1

    # Subtract characters in str2
    for char in str2:
        freq[ord(char) - ord("a")] -= 1

    # Count positive differences (characters to change)
    changes_needed = sum(f for f in freq if f > 0)

    return changes_needed <= k


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("anagram", "grammar", 3, True),
        ("geeks", "eggkf", 1, False),
        ("geeks", "eggkf", 2, True),
        ("aab", "bbc", 1, False),
        ("aab", "bbc", 2, True),
        ("abc", "abc", 0, True),
        ("abc", "def", 3, True),
        ("abc", "def", 2, False),
        ("", "", 0, True),
        ("a", "b", 1, True),
        ("a", "b", 0, False),
    ]

    print("=" * 70)
    print("Check K-Anagrams - Test Results")
    print("=" * 70)

    for str1, str2, k, expected in test_cases:
        result = are_k_anagrams(str1, str2, k)
        status = "PASS" if result == expected else "FAIL"
        print(f"str1: '{str1}' | str2: '{str2}' | k: {k}")
        print(f"Expected: {expected} | Got: {result} | {status}")
        print("-" * 70)

    print("=" * 70)

    # Compare implementations
    print("\nComparing implementations:")
    print("-" * 70)
    for str1, str2, k, expected in test_cases[:8]:
        r1 = are_k_anagrams(str1, str2, k)
        r2 = are_k_anagrams_manual(str1, str2, k)
        all_match = r1 == r2 == expected
        status = "PASS" if all_match else "FAIL"
        print(
            f"str1='{str1}', str2='{str2}', k={k} | Counter: {r1} | Manual: {r2} | {status}"
        )
