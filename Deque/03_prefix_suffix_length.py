from collections import deque


def prefix_suffix_lengths_naive(s):
    """
    Find lengths of all prefixes that are also suffixes using naive comparison.

    Approach:
    - For each prefix length i (from 1 to n-1), compare:
      - prefix s[0:i] with suffix s[n-i:n]
    - If they match, add i to result

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(s)
    result = []

    for i in range(1, n):
        prefix = s[:i]
        suffix = s[n - i :]
        if prefix == suffix:
            result.append(i)

    return result


def prefix_suffix_lengths_lps(s):
    """
    Find lengths using LPS (Longest Proper Prefix which is also Suffix) concept.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(s)
    lps = [0] * n

    for i in range(1, n):
        j = lps[i - 1]
        while j > 0 and s[i] != s[j]:
            j = lps[j - 1]
        if s[i] == s[j]:
            j += 1
        lps[i] = j

    result = []
    length = lps[n - 1]

    while length > 0:
        result.append(length)
        length = lps[length - 1]

    return result[::-1]


def prefix_suffix_lengths_deque(s):
    """
    Find all prefix-suffix lengths using deque for character comparison.

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(s)
    result = []

    for i in range(1, n):
        prefix_deque = deque(s[:i])
        suffix_deque = deque(s[n - i :])

        match = True
        while prefix_deque and suffix_deque:
            if prefix_deque.popleft() != suffix_deque.pop():
                match = False
                break

        if match:
            result.append(i)

    return result


def main():
    print("=== Length of All Prefixes That Are Also Suffixes ===\n")

    test_cases = [
        ("ababababab", [2, 4, 6, 8]),
        ("geeksforgeeks", [5]),
        ("aaaaa", [1, 2, 3, 4]),
        ("abcd", []),
        ("aabaabaa", [2]),
        ("aaaa", [1, 2, 3]),
    ]

    print("--- Naive Approach ---")
    for s, expected in test_cases:
        result = prefix_suffix_lengths_naive(s)
        status = "✓" if result == expected else "✗"
        print(f'Input: "{s}"')
        print(
            f"Output: {' '.join(map(str, result))} (Expected: {' '.join(map(str, expected))}) {status}"
        )
        print()

    print("--- LPS (KMP) Approach ---")
    for s, expected in test_cases:
        result = prefix_suffix_lengths_lps(s)
        status = "✓" if result == expected else "✗"
        print(f'Input: "{s}" → Output: {" ".join(map(str, result))} {status}')


if __name__ == "__main__":
    main()
