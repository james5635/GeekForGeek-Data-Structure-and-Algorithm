"""
Add n Binary Strings

Given n binary strings, find their sum which is also a binary string.

Approach: Bit-by-bit addition with carry - O(n * maxLen) Time and O(maxLen) Space
Add binary strings one by one using bit-by-bit addition.
"""


def trim_leading_zeros(s):
    """Remove leading zeros from binary string."""
    first_one = s.find("1")
    return s[first_one:] if first_one != -1 else "0"


def add_two_binary(s1, s2):
    """
    Add two binary strings.

    Args:
        s1, s2: Binary strings to add

    Returns:
        Sum as binary string
    """
    s1 = trim_leading_zeros(s1)
    s2 = trim_leading_zeros(s2)

    n, m = len(s1), len(s2)

    # Swap if s1 is shorter
    if n < m:
        s1, s2 = s2, s1
        n, m = m, n

    j = m - 1
    carry = 0
    result = []

    for i in range(n - 1, -1, -1):
        bit1 = int(s1[i])
        bit_sum = bit1 + carry

        if j >= 0:
            bit2 = int(s2[j])
            bit_sum += bit2
            j -= 1

        bit = bit_sum % 2
        carry = bit_sum // 2
        result.append(str(bit))

    if carry > 0:
        result.append("1")

    return "".join(result[::-1])


def add_binary_strings(arr):
    """
    Add n binary strings.

    Args:
        arr: List of binary strings

    Returns:
        Sum of all binary strings
    """
    res = "0"
    for binary_str in arr:
        res = add_two_binary(res, binary_str)
    return res


def main():
    """Test cases for adding binary strings."""
    test_cases = [
        (["1", "10", "11"], "110"),
        (["1101", "111"], "10100"),
        (["1", "1", "1"], "11"),
        (["0", "0"], "0"),
        (["1111", "1"], "10000"),
    ]

    print("=" * 50)
    print("Add n Binary Strings")
    print("=" * 50)

    for arr, expected in test_cases:
        result = add_binary_strings(arr)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: {arr}")
        print(f"Output: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
