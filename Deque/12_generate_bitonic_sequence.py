from collections import deque


def generate_bitonic_deque(n, l, r):
    if n <= 0:
        return []

    dq = deque([r - 1])
    dec_val = r - 2
    inc_val = r

    for i in range(n - 1):
        if i % 2 == 0:
            dq.append(dec_val)
            dec_val -= 1
        else:
            dq.appendleft(inc_val)
            inc_val -= 1

    return list(dq)


def generate_bitonic_precalc(n, l, r):
    if n <= 0:
        return []

    dq = deque([r - 1])
    dec_val = r - 2
    inc_val = r

    for i in range(n - 1):
        if i % 2 == 0:
            dq.append(dec_val)
            dec_val -= 1
        else:
            dq.appendleft(inc_val)
            inc_val -= 1

    return list(dq)


if __name__ == "__main__":
    print(generate_bitonic_deque(5, 3, 10))
    print(generate_bitonic_deque(1, 3, 10))
    print(generate_bitonic_deque(2, 3, 10))
    print(generate_bitonic_deque(4, 1, 5))
    print(generate_bitonic_deque(7, 2, 10))

    print()
    print(generate_bitonic_precalc(5, 3, 10))
    print(generate_bitonic_precalc(1, 3, 10))
    print(generate_bitonic_precalc(2, 3, 10))
    print(generate_bitonic_precalc(4, 1, 5))
    print(generate_bitonic_precalc(7, 2, 10))
