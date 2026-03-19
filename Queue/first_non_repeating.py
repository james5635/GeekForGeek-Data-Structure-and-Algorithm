"""
First Non Repeating Character in a Stream
==========================================
Given a stream of characters, find the first non-repeating character
at each position when reading left to right.
"""

from collections import deque


def firstNonRepeating_naive(s: str) -> str:
    """
    Naive Approach: O(n²) time
    For each position, scan the prefix to find the first character
    that appears exactly once.
    """
    result = []
    for i in range(len(s)):
        freq = {}
        for j in range(i + 1):
            freq[s[j]] = freq.get(s[j], 0) + 1

        found = "#"
        for j in range(i + 1):
            if freq[s[j]] == 1:
                found = s[j]
                break
        result.append(found)
    return "".join(result)


def firstNonRepeating_queue(s: str) -> str:
    """
    Better Approach: O(n) time using Queue and Frequency Array
    Maintain a queue of characters in order of appearance,
    and a frequency array. The front of the queue is always
    the first non-repeating character if queue is not empty.
    """
    freq = [0] * 26
    q = deque()
    result = []

    for ch in s:
        idx = ord(ch) - ord("a")
        freq[idx] += 1
        q.append(ch)

        while q and freq[ord(q[0]) - ord("a")] > 1:
            q.popleft()

        result.append(q[0] if q else "#")

    return "".join(result)


def firstNonRepeating(s: str) -> str:
    """
    Expected Approach: O(n) time and O(1) space
    Using Frequency and Last Occurrence Array

    Maintain:
    - freq[]: frequency of each character
    - index[]: position of last occurrence (or -1 if removed from consideration)

    The first non-repeating character is the one with minimum index
    among all characters with frequency == 1.

    Optimization: Since we only need minimum index, we can use
    a sliding window approach - when freq becomes 2, we mark that
    character as unavailable.
    """
    freq = [0] * 26
    result = []
    answer_index = [float("inf")] * 26

    for i, ch in enumerate(s):
        idx = ord(ch) - ord("a")
        freq[idx] += 1

        if freq[idx] == 1:
            answer_index[idx] = i
        elif freq[idx] == 2:
            answer_index[idx] = float("inf")

        min_idx = min(answer_index)
        if min_idx == float("inf"):
            result.append("#")
        else:
            result.append(s[min_idx])

    return "".join(result)


if __name__ == "__main__":
    test_cases = ["aabc", "abcabc", "aabccbdd", "aaaa", "a", "abcd", "bbaac"]

    print("First Non Repeating Character in a Stream")
    print("=" * 50)

    for s in test_cases:
        naive = firstNonRepeating_naive(s)
        queue_ans = firstNonRepeating_queue(s)
        expected = firstNonRepeating(s)

        print(f"\nInput: '{s}'")
        print(f"  Naive:     {naive}")
        print(f"  Queue:     {queue_ans}")
        print(f"  Expected:  {expected}")

        if naive == queue_ans == expected:
            print("  ✓ All approaches match")
        else:
            print("  ✗ Mismatch detected")

    print("\n" + "=" * 50)
    print("\nComplexity Analysis:")
    print("  Naive:     O(n²) time")
    print("  Queue:     O(n) time, O(26) = O(1) space")
    print("  Expected:  O(n) time, O(26) = O(1) space")
