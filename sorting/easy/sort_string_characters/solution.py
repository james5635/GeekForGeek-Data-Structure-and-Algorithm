"""
Sort String Characters

Problem Description:
    Given a string consisting of lowercase English alphabets, sort the
    characters of the string in alphabetical order. The string may contain
    duplicate characters.

Algorithm:
    - Counting Sort approach (optimal for lowercase English letters):
        1. Count frequency of each character (26 possible characters)
        2. Build result string by appending characters in order of their count
    - Alternative: Convert to list, sort, and join (less efficient)

Time Complexity: O(n + k)
    - n: length of string
    - k: number of unique characters (26 for lowercase English)
    - Effectively O(n) for fixed character set

Space Complexity: O(n + k)
    - For count array and result string
"""


def sort_string_counting(s):
    """
    Sort string characters using counting sort (optimal for limited alphabet).

    Args:
        s: Input string containing lowercase English letters

    Returns:
        str: Sorted string
    """
    if not s:
        return s

    # Count frequency of each character (26 lowercase English letters)
    count = [0] * 26

    for char in s:
        count[ord(char) - ord("a")] += 1

    # Build result string
    result = []
    for i in range(26):
        result.append(chr(i + ord("a")) * count[i])

    return "".join(result)


def sort_string_builtin(s):
    """
    Sort string using Python's built-in sort.

    Args:
        s: Input string

    Returns:
        str: Sorted string
    """
    return "".join(sorted(s))


def sort_string_inplace(s):
    """
    Sort string by converting to list and sorting (modifies in place concept).

    Args:
        s: Input string

    Returns:
        str: Sorted string
    """
    char_list = list(s)
    char_list.sort()
    return "".join(char_list)


def sort_by_frequency(s):
    """
    Sort characters by frequency (most frequent first).

    Args:
        s: Input string

    Returns:
        str: String sorted by character frequency
    """
    from collections import Counter

    if not s:
        return s

    # Count frequency
    freq = Counter(s)

    # Sort by frequency (descending), then by character (ascending)
    sorted_chars = sorted(s, key=lambda x: (-freq[x], x))

    return "".join(sorted_chars)


if __name__ == "__main__":
    # Test Case 1: Random string
    s1 = "geeksforgeeks"
    print(f"Original: '{s1}'")
    print(f"Counting sort: '{sort_string_counting(s1)}'")
    print(f"Built-in sort: '{sort_string_builtin(s1)}'")
    print()

    # Test Case 2: Already sorted
    s2 = "abcde"
    print(f"Original: '{s2}'")
    print(f"Sorted: '{sort_string_counting(s2)}'")
    print()

    # Test Case 3: Reverse sorted
    s3 = "edcba"
    print(f"Original: '{s3}'")
    print(f"Sorted: '{sort_string_counting(s3)}'")
    print()

    # Test Case 4: Single character
    s4 = "z"
    print(f"Original: '{s4}'")
    print(f"Sorted: '{sort_string_counting(s4)}'")
    print()

    # Test Case 5: Empty string
    s5 = ""
    print(f"Original: '{s5}'")
    print(f"Sorted: '{sort_string_counting(s5)}'")
    print()

    # Test Case 6: All same characters
    s6 = "aaaa"
    print(f"Original: '{s6}'")
    print(f"Sorted: '{sort_string_counting(s6)}'")
    print()

    # Test Case 7: Sort by frequency
    s7 = "tree"
    print(f"Original: '{s7}'")
    print(f"By frequency: '{sort_by_frequency(s7)}'")
    print()

    # Test Case 8: Long string
    s8 = "pythonprogramming"
    print(f"Original: '{s8}'")
    print(f"Sorted: '{sort_string_counting(s8)}'")
