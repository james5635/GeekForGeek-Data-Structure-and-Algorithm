"""
Palindrome Substring Queries

Given a string s and a 2D list of queries, where each query consists of [left, right].
For each query, find whether the substring s[left:right+1] forms a palindrome.

Examples:
- s = "abaaabaaaba", queries = [[0,10], [5,8], [2,5], [5,9]]
  Output: [1, 0, 0, 1]

Time Complexity: O(n) preprocessing + O(1) per query using Manacher's algorithm
Space Complexity: O(n)
"""


def isPalindrome(s, start, end):
    """Check if a substring is a palindrome using two pointers"""
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def palQueriesBruteForce(s, queries):
    """
    Brute force approach - O(n * q) time
    """
    result = []
    for query in queries:
        start = query[0]
        end = query[1]

        # Check if the substring is a palindrome
        if isPalindrome(s, start, end):
            result.append(1)
        else:
            result.append(0)
    return result


# Manacher's Algorithm Implementation
def buildManacher(s):
    """
    Build modified string with sentinels and separators for Manacher's algorithm
    Returns the radius array p and modified string ms
    """
    # Build modified string with sentinels and separators
    ms = "@" + "#".join([""] + list(s)) + "#$"
    n = len(ms)
    p = [0] * n
    left = right = 0

    for i in range(1, n - 1):
        mirror = left + right - i

        # Initialize radius using mirror or boundary
        if i < right:
            p[i] = min(right - i, p[mirror])

        # Expand around i
        while ms[i + p[i] + 1] == ms[i - p[i] - 1]:
            p[i] += 1

        # Update left and right bounds
        if i + p[i] > right:
            left = i - p[i]
            right = i + p[i]

    return p, ms


def isPalindromeManacher(l, r, p):
    """
    Check if substring s[l:r+1] is a palindrome using Manacher's array
    """
    # Compute the center index in modified string
    mid = l + r + 2
    length = r - l + 1

    # Check if radius covers the length
    return p[mid] >= length


def palQueriesManacher(s, queries):
    """
    Optimized approach using Manacher's algorithm - O(n + q) time
    """
    p, ms = buildManacher(s)
    res = []
    for l, r in queries:
        res.append(1 if isPalindromeManacher(l, r, p) else 0)
    return res


# Test the functions
if __name__ == "__main__":
    test_cases = [
        ("abaaabaaaba", [[0, 10], [5, 8], [2, 5], [5, 9]]),
        ("abdcaaa", [[0, 1], [2, 2], [4, 6]]),
    ]

    print("Palindrome Substring Queries")
    print("=" * 40)

    for s, queries in test_cases:
        print(f"String: '{s}'")
        print(f"Queries: {queries}")

        # Brute force approach
        result_brute = palQueriesBruteForce(s, queries)
        print(f"Brute Force Result: {result_brute}")

        # Manacher's algorithm approach
        result_manacher = palQueriesManacher(s, queries)
        print(f"Manacher's Result:  {result_manacher}")

        # Show details for each query
        print("\nQuery Details:")
        for i, (l, r) in enumerate(queries):
            substring = s[l : r + 1]
            is_pal = result_manacher[i] == 1
            print(
                f"  [{l}, {r}]: '{substring}' -> {'Palindrome' if is_pal else 'Not Palindrome'}"
            )
        print()
