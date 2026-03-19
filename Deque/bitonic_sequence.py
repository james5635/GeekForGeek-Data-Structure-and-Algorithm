"""
Generate Bitonic Sequence

Approach:
- A bitonic sequence increases to a peak and then decreases
- Start from a value in range [l, r], increase by 1 until reaching r
- Then decrease from r-1 down to l
- Use deque: appendleft for increasing, append for decreasing

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque


def generate_bitonic(n, l, r):
    """
    Generate bitonic sequence of length n with range [l, r].
    Sequence starts at some value in [l, r], increases to r, then decreases.
    """
    if n <= 0:
        return []

    if n == 1:
        return [l]

    dq = deque()
    curr = l
    dq.append(curr)

    while curr < r and len(dq) < n:
        curr += 1
        dq.append(curr)

    curr = r - 1
    while curr >= l and len(dq) < n:
        dq.append(curr)
        curr -= 1

    return list(dq)


def generate_bitonic_v2(n, l, r):
    """
    Alternative: Start from peak and expand to both sides.
    """
    if n == 0:
        return []
    if n == 1:
        return [l]

    dq = deque([r])
    curr = r - 1
    left_vals = []
    right_vals = []

    while curr >= l and len(left_vals) + len(right_vals) < n - 1:
        left_vals.append(curr)
        curr -= 1

    while curr >= l and len(left_vals) + len(right_vals) < n - 1:
        right_vals.append(curr)
        curr -= 1

    i, j = 0, len(right_vals) - 1
    while i < len(left_vals) and j >= 0 and len(dq) < n:
        dq.appendleft(left_vals[i])
        dq.append(right_vals[j])
        i += 1
        j -= 1

    while i < len(left_vals) and len(dq) < n:
        dq.appendleft(left_vals[i])
        i += 1

    while j >= 0 and len(dq) < n:
        dq.append(right_vals[j])
        j -= 1

    return list(dq)


def main():
    print("=== Generate Bitonic Sequence ===\n")

    test_cases = [
        (5, 3, 10, [3, 4, 5, 6, 7]),
        (7, 2, 5, [2, 3, 4, 5, 4, 3, 2]),
        (1, 1, 5, [1]),
        (2, 1, 3, [1, 2]),
        (3, 1, 3, [1, 2, 3]),
        (4, 1, 3, [1, 2, 3, 2]),
        (10, 1, 5, [1, 2, 3, 4, 5, 4, 3, 2, 1]),
    ]

    for n, l, r, expected in test_cases:
        result = generate_bitonic(n, l, r)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: n={n}, l={l}, r={r}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Status: {status}\n")


if __name__ == "__main__":
    main()
