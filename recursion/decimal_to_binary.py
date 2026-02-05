"""
Decimal to Binary Conversion using Recursion

Given a decimal number as input, convert it to its equivalent binary number.

Approach:
- Recursively divide the decimal number by 2
- Prepend remainders to build binary string from MSB to LSB
- Uses string concatenation to handle large numbers

Time Complexity: O(log n)
Space Complexity: O(log n) due to recursion stack
"""


def dec_to_bin_rec(n: int) -> str:
    """
    Helper recursive function to convert decimal to binary.

    Args:
        n: Decimal number to convert

    Returns:
        Binary string representation
    """
    if n > 1:
        return dec_to_bin_rec(n // 2) + str(n % 2)
    return str(n)


def decimal_to_binary(n: int) -> str:
    """
    Convert decimal number to binary string.

    Args:
        n: Decimal number (non-negative)

    Returns:
        Binary string representation
    """
    if n < 0:
        return "-" + dec_to_bin_rec(-n)
    return dec_to_bin_rec(n)


def main():
    """Test cases for decimal to binary conversion."""
    test_cases = [
        7,  # Expected: 111
        10,  # Expected: 1010
        0,  # Expected: 0
        1,  # Expected: 1
        255,  # Expected: 11111111
        1048576,  # Expected: 100000000000000000000
    ]

    print("Decimal to Binary Conversion using Recursion")
    print("=" * 50)

    for decimal in test_cases:
        binary = decimal_to_binary(decimal)
        print(f"Decimal: {decimal}")
        print(f"Binary:  {binary}")
        print("-" * 30)


if __name__ == "__main__":
    main()
