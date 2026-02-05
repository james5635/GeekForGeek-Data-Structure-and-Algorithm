"""
Anagram Substring Search (Search for all permutations)

Given a text txt and a pattern pat, find all occurrences of pat and its anagrams in txt.

Approach: Sliding Window with Character Count - O(n) Time and O(1) Space
Use frequency arrays to compare pattern with each window of text.
"""


def search_anagram(pat, txt):
    """
    Find all starting indices of anagrams of pat in txt.

    Args:
        pat: Pattern string
        txt: Text string

    Returns:
        List of starting indices
    """
    # Convert to lowercase for case-insensitive search
    pat = pat.lower()
    txt = txt.lower()

    n, m = len(txt), len(pat)

    if m > n:
        return []

    # Character frequency arrays
    pat_count = [0] * 26
    window_count = [0] * 26

    # Initialize frequency arrays
    for i in range(m):
        pat_count[ord(pat[i]) - ord("a")] += 1
        window_count[ord(txt[i]) - ord("a")] += 1

    result = []

    # Check first window
    if pat_count == window_count:
        result.append(0)

    # Slide the window
    for i in range(m, n):
        # Remove leftmost character of previous window
        window_count[ord(txt[i - m]) - ord("a")] -= 1
        # Add new character
        window_count[ord(txt[i]) - ord("a")] += 1

        if pat_count == window_count:
            result.append(i - m + 1)

    return result


def main():
    """Test cases for anagram substring search."""
    test_cases = [
        ("ABCD", "BACDGABCDA", [0, 5, 6]),
        ("AABA", "AAABABAA", [0, 1, 4]),
        ("abc", "abcabcabc", [0, 1, 2, 3, 4, 5, 6]),  # All windows are anagrams
        ("test", "testtest", [0, 1, 2, 3, 4]),  # All overlapping windows
        ("ab", "abba", [0, 2]),  # Non-overlapping anagrams
    ]

    print("=" * 50)
    print("Anagram Substring Search")
    print("=" * 50)

    for pat, txt, expected in test_cases:
        result = search_anagram(pat, txt)
        status = "✓" if result == expected else "✗"
        print(f"\nPattern: '{pat}'")
        print(f"Text: '{txt}'")
        print(f"Output: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
