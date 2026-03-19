from collections import deque


def approach1(s):
    n = len(s)
    result = []
    dq_prefix = deque()
    dq_suffix = deque()
    prefix = ""
    suffix = ""

    for i in range(n - 1):
        prefix += s[i]
        dq_prefix.append(prefix)
        suffix = s[-(i + 1)] + suffix
        dq_suffix.appendleft(suffix)

    while dq_prefix and dq_suffix:
        p = dq_prefix.popleft()
        sf = dq_suffix.pop()
        if p == sf:
            result.append(len(p))

    return result


def approach2(s):
    n = len(s)
    result = []
    for i in range(1, n):
        prefix = s[:i]
        suffix = s[n - i :]
        if prefix == suffix:
            result.append(i)
    return result


if __name__ == "__main__":
    test_cases = [
        ("ababababab", [2, 4, 6, 8]),
        ("abcab", [2]),
        ("aaaa", [1, 2, 3]),
        ("abcd", []),
        ("aabaabaa", [1, 2, 5]),
        ("abcabcabc", [3, 6]),
    ]

    for s, expected in test_cases:
        res1 = approach1(s)
        res2 = approach2(s)
        print(f'String: "{s}"')
        print(f"  Approach 1: {res1}")
        print(f"  Approach 2: {res2}")
        print(f"  Expected:   {expected}")
        assert res1 == expected
        assert res2 == expected
        print()

    print("All tests passed")
