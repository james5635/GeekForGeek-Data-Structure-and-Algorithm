"""
Palindrome Substring Queries

Problem Description:
    Given a string s and multiple queries, each query specifies a substring
    [left, right]. For each query, determine if the substring is a palindrome.

Approaches:
    1. Naive: Check each query independently - O(q * n)
    2. Rolling Hash (Rabin-Karp): Precompute prefix hashes - O(n + q)
    3. Manacher's Algorithm: Linear time palindrome detection - O(n + q)

Time Complexity (Optimal): O(n + q) for preprocessing + query
Space Complexity: O(n)
"""

from typing import List


class RollingHash:
    """Rolling hash for efficient substring comparison."""

    def __init__(self, s: str):
        self.s = s
        self.n = len(s)
        self.base = 31
        self.mod = 10**9 + 7

        # Precompute prefix hashes and powers
        self.prefix_hash = [0] * (self.n + 1)
        self.power = [1] * (self.n + 1)

        for i in range(self.n):
            self.prefix_hash[i + 1] = (
                self.prefix_hash[i] * self.base + ord(s[i])
            ) % self.mod
            self.power[i + 1] = (self.power[i] * self.base) % self.mod

    def get_hash(self, left: int, right: int) -> int:
        """Get hash of substring s[left..right] (inclusive)."""
        # Convert to [left, right+1) for calculation
        right = right + 1
        hash_val = (
            self.prefix_hash[right] - self.prefix_hash[left] * self.power[right - left]
        ) % self.mod
        return hash_val if hash_val >= 0 else hash_val + self.mod


def palindrome_queries_naive(s: str, queries: List[List[int]]) -> List[int]:
    """
    Answer palindrome queries using naive approach.

    Time Complexity: O(q * n) where q = number of queries
    Space Complexity: O(1)
    """

    def is_palindrome(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    return [1 if is_palindrome(l, r) else 0 for l, r in queries]


def palindrome_queries_rolling_hash(s: str, queries: List[List[int]]) -> List[int]:
    """
    Answer palindrome queries using rolling hash.

    Time Complexity: O(n + q) for preprocessing and queries
    Space Complexity: O(n)
    """
    n = len(s)

    # Forward hash
    forward_hash = RollingHash(s)
    # Reverse hash
    reverse_hash = RollingHash(s[::-1])

    result = []
    for left, right in queries:
        # Get hash of forward substring
        forward_h = forward_hash.get_hash(left, right)

        # Map to reversed string indices
        rev_left = n - 1 - right
        rev_right = n - 1 - left
        reverse_h = reverse_hash.get_hash(rev_left, rev_right)

        result.append(1 if forward_h == reverse_h else 0)

    return result


def build_manacher(s: str) -> List[int]:
    """
    Build Manacher's array for palindrome detection.

    Returns array where p[i] is the radius of longest palindrome centered at i.
    """
    # Transform string: "abc" -> "#a#b#c#"
    t = "#".join("^{}$".format(s))
    n = len(t)
    p = [0] * n
    center = right = 0

    for i in range(1, n - 1):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])

        # Expand around center
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        # Update center and right boundary
        if i + p[i] > right:
            center = i
            right = i + p[i]

    return p


def palindrome_queries_manacher(s: str, queries: List[List[int]]) -> List[int]:
    """
    Answer palindrome queries using Manacher's algorithm.

    Time Complexity: O(n + q)
    Space Complexity: O(n)
    """
    p = build_manacher(s)
    result = []

    for left, right in queries:
        length = right - left + 1
        # Center in transformed string
        center = left + right + 2
        # Check if palindrome radius covers the substring
        result.append(1 if p[center] >= length else 0)

    return result


def test_palindrome_queries():
    """Test cases for palindrome substring queries."""
    test_cases = [
        # (string, queries, expected_result)
        ("abaaabaaaba", [[0, 10], [5, 8], [2, 5], [5, 9]], [1, 0, 0, 1]),
        ("abdcaaa", [[0, 1], [2, 2], [4, 6]], [0, 1, 1]),
        ("aaaa", [[0, 3], [1, 2], [0, 0]], [1, 1, 1]),
        ("abcba", [[0, 4], [1, 3], [0, 2]], [1, 1, 0]),
        ("a", [[0, 0]], [1]),
        ("ab", [[0, 1], [0, 0], [1, 1]], [0, 1, 1]),
    ]

    print("Running test cases for Palindrome Substring Queries:")
    print("=" * 60)

    for i, (s, queries, expected) in enumerate(test_cases, 1):
        result_naive = palindrome_queries_naive(s, queries)
        result_hash = palindrome_queries_rolling_hash(s, queries)
        result_manacher = palindrome_queries_manacher(s, queries)

        status_naive = "✓" if result_naive == expected else "✗"
        status_hash = "✓" if result_hash == expected else "✗"
        status_manacher = "✓" if result_manacher == expected else "✗"

        print(f"Test {i}: s = '{s}'")
        print(f"  Queries: {queries}")
        print(f"  Expected: {expected}")
        print(f"  Naive:    {result_naive} {status_naive}")
        print(f"  Rolling Hash: {result_hash} {status_hash}")
        print(f"  Manacher: {result_manacher} {status_manacher}\n")


if __name__ == "__main__":
    # Example usage
    s = "abaaabaaaba"
    queries = [[0, 10], [5, 8], [2, 5], [5, 9]]

    print(f"String: {s}")
    print(f"Queries: {queries}")
    print(f"\nResults:")
    results = palindrome_queries_manacher(s, queries)
    for (l, r), res in zip(queries, results):
        substring = s[l : r + 1]
        is_pal = "is" if res == 1 else "is not"
        print(f"  Substring '{substring}' [{l}, {r}] {is_pal} a palindrome")

    print()

    # Run tests
    test_palindrome_queries()
