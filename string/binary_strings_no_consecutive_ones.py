"""
Count Binary Strings with No Consecutive 1s

Given a positive integer N, count all possible distinct binary strings of length N
such that there are no consecutive 1's.

Approach: Dynamic Programming - O(n) Time and O(1) Space
Use DP where dp[i][0] = strings ending with 0, dp[i][1] = strings ending with 1.
"""


def count_binary_strings(n):
    """
    Count binary strings of length n with no consecutive 1s.

    Args:
        n: Length of binary strings

    Returns:
        Count of valid binary strings
    """
    if n == 0:
        return 0
    if n == 1:
        return 2

    # a = count ending with 0, b = count ending with 1
    a, b = 1, 1

    for _ in range(2, n + 1):
        # New strings ending with 0 = prev ending with 0 + prev ending with 1
        # New strings ending with 1 = prev ending with 0 only
        a, b = a + b, a

    return a + b


def generate_binary_strings(n):
    """
    Generate all binary strings of length n with no consecutive 1s.

    Args:
        n: Length of binary strings

    Returns:
        List of valid binary strings
    """
    result = []

    def generate(current):
        if len(current) == n:
            result.append(current)
            return

        # Always can add 0
        generate(current + "0")

        # Can add 1 only if last char is not 1
        if len(current) == 0 or current[-1] != "1":
            generate(current + "1")

    generate("")
    return result


def main():
    """Test cases for binary strings with no consecutive 1s."""
    test_cases = [
        (1, 2, ["0", "1"]),
        (2, 3, ["00", "01", "10"]),
        (3, 5, ["000", "001", "010", "100", "101"]),
        (4, 8, None),
    ]

    print("=" * 50)
    print("Binary Strings with No Consecutive 1s")
    print("=" * 50)

    for n, expected_count, expected_strings in test_cases:
        count = count_binary_strings(n)
        strings = generate_binary_strings(n)
        status = "✓" if count == expected_count else "✗"

        print(f"\nn = {n}")
        print(f"Count: {count}")
        print(f"Expected count: {expected_count} {status}")
        if expected_strings:
            print(f"Strings: {strings}")


if __name__ == "__main__":
    main()
