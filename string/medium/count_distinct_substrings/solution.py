"""
Count Distinct Substrings

Count the number of distinct substrings of a string.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""


def count_distinct_substrings(s: str) -> int:
    """
    Count the number of distinct substrings of a string.

    A substring is a contiguous sequence of characters within a string.
    For a string of length n, there are n*(n+1)/2 possible substrings,
    but some may be duplicates.

    Args:
        s: Input string

    Returns:
        Number of distinct substrings
    """
    n = len(s)
    substrings = set()

    # Generate all possible substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(s[i:j])

    return len(substrings)


def count_distinct_substrings_optimized(s: str) -> int:
    """
    Optimized version using suffix automaton (conceptual implementation).
    This is a simplified version for understanding the concept.
    """

    class SuffixAutomaton:
        def __init__(self):
            self.states = []
            self.last = 0
            self._add_state(0)  # Initial state

        def _add_state(self, length):
            state = {"length": length, "link": -1, "transitions": {}}
            self.states.append(state)
            return len(self.states) - 1

        def extend(self, c):
            p = self.last
            cur = self._add_state(self.states[p]["length"] + 1)

            while p >= 0 and c not in self.states[p]["transitions"]:
                self.states[p]["transitions"][c] = cur
                p = self.states[p]["link"]

            if p == -1:
                self.states[cur]["link"] = 0
            else:
                q = self.states[p]["transitions"][c]
                if self.states[p]["length"] + 1 == self.states[q]["length"]:
                    self.states[cur]["link"] = q
                else:
                    clone = self._add_state(self.states[p]["length"] + 1)
                    self.states[clone]["transitions"] = self.states[q][
                        "transitions"
                    ].copy()
                    self.states[clone]["link"] = self.states[q]["link"]

                    while p >= 0 and self.states[p]["transitions"].get(c) == q:
                        self.states[p]["transitions"][c] = clone
                        p = self.states[p]["link"]

                    self.states[q]["link"] = self.states[cur]["link"] = clone

            self.last = cur

        def count_distinct_substrings(self):
            count = 0
            for i in range(1, len(self.states)):
                count += (
                    self.states[i]["length"]
                    - self.states[self.states[i]["link"]]["length"]
                )
            return count

    if not s:
        return 0

    sa = SuffixAutomaton()
    for c in s:
        sa.extend(c)

    return sa.count_distinct_substrings()


def count_distinct_substrings_hash(s: str) -> int:
    """
    Version using rolling hash for better performance.
    """
    n = len(s)
    distinct_hashes = set()
    base = 257
    mod = 10**9 + 7

    # Precompute powers
    power = [1] * (n + 1)
    for i in range(1, n + 1):
        power[i] = (power[i - 1] * base) % mod

    # Compute prefix hashes
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = (prefix[i] * base + ord(s[i])) % mod

    # Generate all substring hashes
    for i in range(n):
        for j in range(i + 1, n + 1):
            # Hash of substring s[i:j]
            substring_hash = (prefix[j] - prefix[i] * power[j - i] % mod + mod) % mod
            distinct_hashes.add(substring_hash)

    return len(distinct_hashes)


def count_distinct_substrings_suffix_array(s: str) -> int:
    """
    Version using suffix array and LCP array.
    """

    def build_suffix_array(s):
        n = len(s)
        k = 1
        rank = [ord(c) for c in s] + [-1]
        tmp = [0] * n
        sa = list(range(n))

        def cmp(i, j):
            if rank[i] != rank[j]:
                return rank[i] - rank[j]
            if i + k < n and j + k < n:
                return rank[i + k] - rank[j + k]
            return (j + k - n) - (i + k - n)

        while k <= n:
            sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
            tmp[sa[0]] = 0
            for i in range(1, n):
                tmp[sa[i]] = tmp[sa[i - 1]] + (cmp(sa[i - 1], sa[i]) > 0)
            rank = tmp + [0]
            k *= 2

        return sa

    def build_lcp_array(s, sa):
        n = len(s)
        rank = [0] * n
        for i, suffix in enumerate(sa):
            rank[suffix] = i

        lcp = [0] * (n - 1)
        h = 0
        for i in range(n):
            if rank[i] > 0:
                j = sa[rank[i] - 1]
                while i + h < n and j + h < n and s[i + h] == s[j + h]:
                    h += 1
                lcp[rank[i] - 1] = h
                if h > 0:
                    h -= 1

        return lcp

    if not s:
        return 0

    n = len(s)
    sa = build_suffix_array(s)
    lcp = build_lcp_array(s, sa)

    # Total substrings = n*(n+1)/2
    # Distinct substrings = Total substrings - sum of LCP array
    total_substrings = n * (n + 1) // 2
    distinct_substrings = total_substrings - sum(lcp)

    return distinct_substrings


def test_count_distinct_substrings():
    """Test cases for counting distinct substrings."""
    test_cases = [
        ("", 0),
        ("a", 1),
        ("aa", 2),  # "a", "aa"
        ("ab", 3),  # "a", "b", "ab"
        ("abc", 6),  # "a", "b", "c", "ab", "bc", "abc"
        ("aaa", 3),  # "a", "aa", "aaa"
        ("aba", 5),  # "a", "b", "ab", "ba", "aba"
        ("abab", 7),  # "a", "b", "ab", "ba", "aba", "bab", "abab"
        ("abcab", 12),
        ("banana", 15),
        ("abracadabra", 54),
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = count_distinct_substrings(input_str)
        assert result == expected, (
            f"Test case {i} failed: Expected {expected}, got {result}"
        )

    print("All test cases passed!")


if __name__ == "__main__":
    test_count_distinct_substrings()

    # Example usage
    s = "abab"
    result = count_distinct_substrings(s)
    print(f"Number of distinct substrings in '{s}': {result}")
