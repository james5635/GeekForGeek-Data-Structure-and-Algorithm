from collections import deque


def prefix_suffix_lengths(s):
    n = len(s)
    result = []

    for length in range(1, n):
        prefix = deque(s[:length])
        suffix = deque(s[n - length :])

        if list(prefix) == list(suffix):
            result.append(length)

    return result


def prefix_suffix_optimized(s):
    n = len(s)
    result = []

    for length in range(1, n):
        if s[:length] == s[n - length :]:
            result.append(length)

    return result


if __name__ == "__main__":
    assert prefix_suffix_lengths("geeksforgeeks") == [5]
    assert prefix_suffix_optimized("geeksforgeeks") == [5]
    assert prefix_suffix_lengths("abab") == [2]
    assert prefix_suffix_optimized("abab") == [2]
    assert prefix_suffix_lengths("aaaa") == [1, 2, 3]
    assert prefix_suffix_optimized("aaaa") == [1, 2, 3]
    assert prefix_suffix_lengths("abcde") == []
    assert prefix_suffix_optimized("abcde") == []
    print("All tests passed!")
