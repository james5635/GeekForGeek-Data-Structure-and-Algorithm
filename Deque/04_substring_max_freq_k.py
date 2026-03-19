from collections import deque, defaultdict


def naive(s, k):
    freq = defaultdict(int)
    n = len(s)
    for i in range(n - k + 1):
        sub = s[i : i + k]
        freq[sub] += 1
    max_freq = 0
    result = ""
    for sub, count in freq.items():
        if count > max_freq:
            max_freq = count
            result = sub
    return result


def efficient(s, k):
    dq = deque()
    freq = defaultdict(int)
    n = len(s)

    for i in range(n):
        dq.append(s[i])
        if len(dq) == k:
            key = "".join(dq)
            freq[key] += 1
            dq.popleft()

    max_freq = 0
    result = ""
    for sub, count in freq.items():
        if count > max_freq:
            max_freq = count
            result = sub
    return result


if __name__ == "__main__":
    test_cases = [
        ("bbbbbaaaaabbabababa", 5),
        ("abcabcabc", 3),
        ("abcdefg", 4),
        ("aaaaaa", 3),
        ("ababab", 2),
    ]

    for s, k in test_cases:
        res_naive = naive(s, k)
        res_efficient = efficient(s, k)
        print(f'String: "{s}", k={k}')
        print(f'  Naive:    "{res_naive}"')
        print(f'  Efficient: "{res_efficient}"')
        assert res_naive == res_efficient
        print()

    print("All tests passed")
