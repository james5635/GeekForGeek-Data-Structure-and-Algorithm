"""
Fraction to Recurring Decimal

Problem Description:
    Given two integers a and b (b != 0), return the fraction a/b in string format.
    If the fractional part is repeating, enclose the repeating part in parentheses.

Approach:
    1. Handle sign separately
    2. Calculate the integral part
    3. For fractional part, use a hash map to track remainders and their positions
    4. If a remainder repeats, it means the decimal representation will repeat
    5. Insert parentheses around the repeating part

Time Complexity: O(max(log10(a), log10(b)))
Space Complexity: O(max(log10(a), log10(b)))
"""


def fraction_to_decimal(numerator: int, denominator: int) -> str:
    """
    Convert a fraction to its decimal string representation.

    Args:
        numerator: The numerator of the fraction
        denominator: The denominator of the fraction (non-zero)

    Returns:
        String representation of the fraction with repeating decimals in parentheses

    Raises:
        ZeroDivisionError: If denominator is zero
    """
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

    # Handle zero numerator
    if numerator == 0:
        return "0"

    result = []

    # Handle sign
    if (numerator < 0) ^ (denominator < 0):
        result.append("-")

    # Work with absolute values
    numerator = abs(numerator)
    denominator = abs(denominator)

    # Calculate integral part
    integral_part = numerator // denominator
    result.append(str(integral_part))

    remainder = numerator % denominator

    # If completely divisible
    if remainder == 0:
        return "".join(result)

    result.append(".")

    # Hash map to store remainder and its position in result
    remainder_map = {}

    while remainder != 0:
        # If remainder seen before, we have a repeating fraction
        if remainder in remainder_map:
            start_index = remainder_map[remainder]
            result.insert(start_index, "(")
            result.append(")")
            break

        # Store the position of this remainder
        remainder_map[remainder] = len(result)

        # Calculate next digit
        remainder *= 10
        digit = remainder // denominator
        result.append(str(digit))
        remainder = remainder % denominator

    return "".join(result)


def test_fraction_to_decimal():
    """Test cases for fraction to decimal conversion."""
    test_cases = [
        # (numerator, denominator, expected_result)
        (1, 2, "0.5"),
        (2, 1, "2"),
        (4, 2, "2"),
        (-1, 2, "-0.5"),
        (1, -2, "-0.5"),
        (-1, -2, "0.5"),
        (0, 5, "0"),
        (50, 22, "2.(27)"),
        (1, 3, "0.(3)"),
        (1, 6, "0.1(6)"),
        (1, 7, "0.(142857)"),
        (22, 7, "3.(142857)"),
        (1, 333, "0.(003)"),
        (1, 17, "0.(0588235294117647)"),
    ]

    print("Running test cases for Fraction to Decimal:")
    print("=" * 60)

    for i, (num, den, expected) in enumerate(test_cases, 1):
        result = fraction_to_decimal(num, den)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {i}: {num}/{den}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print(f"  Status:   {status}\n")

    # Test edge case - division by zero
    try:
        fraction_to_decimal(1, 0)
        print("ERROR: Should have raised ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"✓ Correctly raised ZeroDivisionError: {e}")


if __name__ == "__main__":
    # Example usage
    print("Example: 50/22 =", fraction_to_decimal(50, 22))
    print("Example: 1/3 =", fraction_to_decimal(1, 3))
    print()

    # Run tests
    test_fraction_to_decimal()
