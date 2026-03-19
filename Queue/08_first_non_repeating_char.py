def first_non_repeating_naive(stream):
    result = []
    for i in range(len(stream)):
        non_rep = "#"
        for j in range(i + 1):
            repeated = False
            for k in range(i + 1):
                if stream[j] == stream[k] and j != k:
                    repeated = True
                    break
            if not repeated:
                non_rep = stream[j]
                break
        result.append(non_rep)
    return "".join(result)


def first_non_repeating_better(stream):
    from collections import deque

    freq = [0] * 26
    q = deque()
    result = []

    for ch in stream:
        freq[ord(ch) - ord("a")] += 1
        q.append(ch)
        while q and freq[ord(q[0]) - ord("a")] > 1:
            q.popleft()
        if q:
            result.append(q[0])
        else:
            result.append("#")
    return "".join(result)


def first_non_repeating_expected(stream):
    freq = [0] * 26
    first_pos = [-1] * 26

    for i, ch in enumerate(stream):
        idx = ord(ch) - ord("a")
        if freq[idx] == 0:
            first_pos[idx] = i
        freq[idx] += 1

    result = []
    for i, ch in enumerate(stream):
        min_idx = len(stream)
        for j in range(26):
            if freq[j] == 1 and first_pos[j] <= i and first_pos[j] < min_idx:
                min_idx = first_pos[j]
        if min_idx == len(stream):
            result.append("#")
        else:
            result.append(stream[min_idx])
    return "".join(result)


if __name__ == "__main__":
    stream1 = "aabc"
    print(f"Stream: {stream1}")
    print(f"Naive:    {first_non_repeating_naive(stream1)}")
    print(f"Better:   {first_non_repeating_better(stream1)}")
    print(f"Expected: {first_non_repeating_expected(stream1)}")
    print()

    stream2 = "aabcbcd"
    print(f"Stream: {stream2}")
    print(f"Naive:    {first_non_repeating_naive(stream2)}")
    print(f"Better:   {first_non_repeating_better(stream2)}")
    print(f"Expected: {first_non_repeating_expected(stream2)}")
    print()

    stream3 = "zz"
    print(f"Stream: {stream3}")
    print(f"Naive:    {first_non_repeating_naive(stream3)}")
    print(f"Better:   {first_non_repeating_better(stream3)}")
    print(f"Expected: {first_non_repeating_expected(stream3)}")
