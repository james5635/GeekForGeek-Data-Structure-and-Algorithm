"""
Check if Two Strings are K-Anagrams
Two strings are k-anagrams if they can become anagrams by changing at most k characters.

Approach: Count character frequency differences
Time Complexity: O(n), where n is length of strings
Auxiliary Space: O(1) for fixed size frequency array
"""

from collections import defaultdict


def are_k_anagrams_map(s1: str, s2: str, k: int) -> bool:
    """
    Check k-anagram using hash map approach.

    Args:
        s1: First string
        s2: Second string
        k: Maximum allowed character changes

    Returns:
        True if strings are k-anagrams, False otherwise
    """
    if len(s1) != len(s2):
        return False

    char_count = defaultdict(int)

    # Count frequency in s1
    for char in s1:
        char_count[char] += 1

    # Decrement for characters in s2
    for char in s2:
        if char_count[char] > 0:
            char_count[char] -= 1

    # Sum remaining differences
    diff_count = sum(char_count.values())

    return diff_count <= k


def are_k_anagrams_array(s1: str, s2: str, k: int) -> bool:
    """
    Check k-anagram using frequency array (more efficient).
    """
    if len(s1) != len(s2):
        return False

    MAX_CHAR = 26
    freq = [0] * MAX_CHAR

    # Store occurrence of all characters
    for char in s1:
        freq[ord(char) - ord("a")] += 1

    # Count differences
    count = 0
    for char in s2:
        if freq[ord(char) - ord("a")] > 0:
            freq[ord(char) - ord("a")] -= 1
        else:
            count += 1

        if count > k:
            return False

    return count <= k


def main():
    """Test the k-anagram checker with various inputs."""
    test_cases = [
        ("anagram", "grammar", 3, True),
        ("anagram", "grammar", 2, True),
        ("geeks", "eggkf", 1, False),
        ("geeks", "eggkf", 2, True),
        ("fodr", "gork", 2, True),
        ("fodr", "gork", 1, False),
        ("abc", "def", 3, True),
        ("abc", "def", 2, False),
        ("aabb", "bbaa", 0, True),
        ("hello", "world", 3, True),
    ]

    print("Check if Two Strings are K-Anagrams")
    print("=" * 60)

    for s1, s2, k, expected in test_cases:
        result1 = are_k_anagrams_map(s1, s2, k)
        result2 = are_k_anagrams_array(s1, s2, k)

        all_pass = result1 == expected and result2 == expected
        status = "✓ PASS" if all_pass else "✗ FAIL"

        print(f"{status} | s1: '{s1}', s2: '{s2}', k: {k}")
        print(f"       | Expected: {expected}")
        print(f"       | HashMap: {result1}, Array: {result2}")
        print()


if __name__ == "__main__":
    main()
