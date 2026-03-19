from collections import deque


def generate_sequence(n, s):
    dq = deque()
    dq.append(0)
    for i in range(n):
        val = i + 1
        if s[i] == "F":
            dq.appendleft(val)
        else:
            dq.append(val)
    return list(dq)


if __name__ == "__main__":
    assert generate_sequence(5, "FBBFB") == [4, 1, 0, 2, 3, 5]
    assert generate_sequence(3, "FFF") == [3, 2, 1, 0]
    assert generate_sequence(3, "BBB") == [0, 1, 2, 3]
    assert generate_sequence(0, "") == [0]
    assert generate_sequence(1, "F") == [1, 0]
    assert generate_sequence(1, "B") == [0, 1]
    assert generate_sequence(4, "FBFB") == [4, 2, 1, 0, 3]

    print("All tests passed")
