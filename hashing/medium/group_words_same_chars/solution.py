"""
Group Words with Same Set of Characters

Problem: Given a list of words, group words that have the same set of characters.
Two words have the same set if they contain exactly the same characters (order
doesn't matter, frequency doesn't matter).

Approach: Use sorted characters as key in hash map. Words with same sorted
characters belong to same group.

Time Complexity: O(n * m log m) where n = words, m = max word length
Space Complexity: O(n * m) for storing groups
"""

from collections import defaultdict


def group_words_same_chars(words):
    """
    Group words with same set of characters.

    Args:
        words: List of words

    Returns:
        List of lists containing grouped words
    """
    groups = defaultdict(list)

    for word in words:
        # Use sorted characters as key
        key = "".join(sorted(word.lower()))
        groups[key].append(word)

    return list(groups.values())


def group_words_by_char_set(words):
    """
    Group words by their character set (ignoring frequency).

    Args:
        words: List of words

    Returns:
        List of lists containing grouped words
    """
    groups = defaultdict(list)

    for word in words:
        # Use set of characters as key (order doesn't matter, freq doesn't matter)
        key = frozenset(word.lower())
        groups[key].append(word)

    return list(groups.values())


def group_words_by_char_frequency(words):
    """
    Group words with same character frequency distribution.

    Args:
        words: List of words

    Returns:
        List of lists containing grouped words
    """
    groups = defaultdict(list)

    for word in words:
        # Count frequency of each character
        freq = defaultdict(int)
        for char in word.lower():
            freq[char] += 1

        # Create key from sorted frequency tuples
        key = tuple(sorted(freq.items()))
        groups[key].append(word)

    return list(groups.values())


def are_anagrams(word1, word2):
    """
    Check if two words are anagrams of each other.

    Args:
        word1: First word
        word2: Second word

    Returns:
        True if anagrams, False otherwise
    """
    return sorted(word1.lower()) == sorted(word2.lower())


def get_anagram_groups(words):
    """
    Get groups of anagrams (same chars with same frequency).

    Args:
        words: List of words

    Returns:
        Dictionary with sorted word as key and list of anagrams as value
    """
    groups = defaultdict(list)

    for word in words:
        key = "".join(sorted(word.lower()))
        groups[key].append(word)

    return dict(groups)


if __name__ == "__main__":
    # Test Case 1: Basic anagram grouping
    words1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Words: {words1}")
    print(f"Groups (sorted chars): {group_words_same_chars(words1)}")
    print()

    # Test Case 2: Same character set, different frequency
    words2 = ["aaa", "aa", "a", "bbb", "bb"]
    print(f"Words: {words2}")
    print(f"Groups (sorted chars): {group_words_same_chars(words2)}")
    print(f"Groups (char set only): {group_words_by_char_set(words2)}")
    print()

    # Test Case 3: Mixed case
    words3 = ["Listen", "Silent", "Triangle", "Integral", "abc"]
    print(f"Words: {words3}")
    print(f"Groups: {group_words_same_chars(words3)}")
    print()

    # Test Case 4: Empty list
    words4 = []
    print(f"Words: {words4}")
    print(f"Groups: {group_words_same_chars(words4)}")
    print()

    # Test Case 5: Single word
    words5 = ["hello"]
    print(f"Words: {words5}")
    print(f"Groups: {group_words_same_chars(words5)}")
    print()

    # Test Case 6: No anagrams
    words6 = ["abc", "def", "ghi"]
    print(f"Words: {words6}")
    print(f"Groups: {group_words_same_chars(words6)}")
    print()

    # Test Case 7: Anagram check
    print(f"Are 'listen' and 'silent' anagrams? {are_anagrams('listen', 'silent')}")
    print(f"Are 'hello' and 'world' anagrams? {are_anagrams('hello', 'world')}")
    print()

    # Test Case 8: Frequency-based grouping
    words8 = ["aab", "baa", "aba", "abc", "bca", "cba"]
    print(f"Words: {words8}")
    print(f"Groups by frequency: {group_words_by_char_frequency(words8)}")
    print()

    # Test Case 9: Anagram dictionary
    words9 = ["cat", "tac", "act", "dog", "god"]
    print(f"Words: {words9}")
    print(f"Anagram groups: {get_anagram_groups(words9)}")
