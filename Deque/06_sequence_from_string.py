from collections import deque


def generate_sequence_by_positions(n, s):
    """
    Generate sequence by inserting positions using deque.

    Approach:
    - Initialize deque with positions 0 to n-1
    - Process string S character by character:
      - 'F' (Front): Pop from front, output position
      - 'B' (Back): Pop from back, output position
    - After processing all characters in S, output remaining elements from front

    Time Complexity: O(n + |S|)
    Space Complexity: O(n)

    Args:
        n: Number of positions (0 to n-1)
        s: String of 'F' and 'B' characters

    Returns:
        List of positions in order
    """
    if n <= 0:
        return []

    result = []
    dq = deque(range(n))

    for char in s:
        if char == "F":
            result.append(dq.popleft())
        elif char == "B":
            result.append(dq.pop())

    while dq:
        result.append(dq.popleft())

    return result


def generate_sequence_with_all_positions(n, s):
    """
    Generate sequence including all positions (0 to n-1).

    For each character in S:
    - 'F': take from front
    - 'B': take from back
    Then output remaining in order.

    This gives a permutation of 0 to n-1.
    """
    if n <= 0:
        return []

    result = []
    dq = deque(range(n))

    for char in s:
        if char == "F":
            result.append(dq.popleft())
        elif char == "B":
            result.append(dq.pop())

    while dq:
        result.append(dq.popleft())

    return result


def generate_sequence_simple(n, s):
    """
    Simple approach using list and index pointers.
    """
    if n <= 0:
        return []

    positions = list(range(n))
    front = 0
    back = n - 1
    result = []

    for char in s:
        if char == "F":
            result.append(positions[front])
            front += 1
        elif char == "B":
            result.append(positions[back])
            back -= 1

    for i in range(front, back + 1):
        result.append(positions[i])

    return result


def main():
    print("=== Generate Sequence by Inserting Positions ===\n")

    test_cases = [
        (5, "FBBFB", [0, 4, 3, 1, 2]),
        (6, "BBBBBB", [5, 4, 3, 2, 1, 0]),
        (4, "FFBB", [0, 1, 3, 2]),
        (3, "FBF", [0, 2, 1]),
        (7, "BFFBFF", [6, 0, 1, 5, 2, 3, 4]),
    ]

    for n, s, expected in test_cases:
        result = generate_sequence_by_positions(n, s)
        status = "✓" if result == expected else "✗"
        print(f'Input: N={n}, S="{s}"')
        print(
            f"Output: {' '.join(map(str, result))} (Expected: {' '.join(map(str, expected))}) {status}"
        )
        print()

    print("--- Simple Approach ---")
    for n, s, expected in test_cases:
        result = generate_sequence_simple(n, s)
        status = "✓" if result == expected else "✗"
        print(f'N={n}, S="{s}" → {" ".join(map(str, result))} {status}')


if __name__ == "__main__":
    main()
