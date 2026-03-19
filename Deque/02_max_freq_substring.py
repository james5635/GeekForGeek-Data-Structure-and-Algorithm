from collections import deque, defaultdict


def max_freq_substring_sliding_window(s, k):
    """
    Find the substring of length K with maximum frequency using sliding window + hashmap.

    Approach:
    - Use a sliding window of size k
    - Count frequency of each substring in a hashmap
    - Track the substring with maximum frequency

    Time Complexity: O(n)
    Space Complexity: O(n)

    Args:
        s: Input string
        k: Length of substring

    Returns:
        Substring with maximum frequency
    """
    if not s or k <= 0 or k > len(s):
        return ""

    freq_map = defaultdict(int)
    n = len(s)

    for i in range(n - k + 1):
        substring = s[i : i + k]
        freq_map[substring] += 1

    max_freq = max(freq_map.values())

    for substring, freq in freq_map.items():
        if freq == max_freq:
            return substring

    return ""


def max_freq_substring_all(s, k):
    """
    Return all substrings with maximum frequency (first one alphabetically).
    """
    if not s or k <= 0 or k > len(s):
        return []

    freq_map = defaultdict(int)
    n = len(s)

    for i in range(n - k + 1):
        substring = s[i : i + k]
        freq_map[substring] += 1

    if not freq_map:
        return []

    max_freq = max(freq_map.values())
    result = [sub for sub, freq in freq_map.items() if freq == max_freq]

    return sorted(result)


def main():
    print("=== Substring of Length K with Maximum Frequency ===\n")

    test_cases = [
        ("bbbbbaaaaabbabababa", 5, "babab"),
        ("heisagoodboy", 5, "heisa"),
        ("aaaaa", 2, "aa"),
        ("abcdef", 3, "abc"),
        ("aabbccddee", 2, "aa"),
        ("abcabcabc", 3, "abc"),
    ]

    for s, k, expected in test_cases:
        result = max_freq_substring_sliding_window(s, k)
        print(f'Input: str = "{s}", K = {k}')
        print(f"Output: {result} (Expected: {expected})")
        print()

    print("--- All substrings with max frequency ---")
    for s, k, _ in test_cases:
        results = max_freq_substring_all(s, k)
        print(f'str = "{s}", K = {k} → {results}')


if __name__ == "__main__":
    main()
