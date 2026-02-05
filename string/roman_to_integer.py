"""
Roman to Integer

Given a Roman numeral, convert it to an integer.

Approach: Single Pass - O(n) Time and O(1) Space
Process from left to right, subtracting when a smaller numeral precedes a larger one.
"""


def roman_to_integer(s):
    """
    Convert Roman numeral to integer.

    Args:
        s: Roman numeral string

    Returns:
        Integer value
    """
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    result = 0
    n = len(s)

    for i in range(n):
        # If current value is less than next, subtract it
        if i < n - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
            result -= roman_values[s[i]]
        else:
            result += roman_values[s[i]]

    return result


def main():
    """Test cases for Roman to Integer conversion."""
    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
    ]

    print("=" * 50)
    print("Roman to Integer")
    print("=" * 50)

    for roman, expected in test_cases:
        result = roman_to_integer(roman)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: '{roman}'")
        print(f"Output: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
