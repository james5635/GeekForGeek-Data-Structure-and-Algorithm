"""
Write your own Atoi()

Given a string s, convert it into integer format without utilizing any built-in functions.
Similar to C/C++ atoi() function.

Approach: Process string character by character - O(n) Time and O(1) Space
Skip whitespace, handle sign, read digits, check overflow.
"""

INT_MAX = 2**31 - 1
INT_MIN = -(2**31)


def my_atoi(s):
    """
    Convert string to integer (atoi implementation).

    Args:
        s: Input string representing a number

    Returns:
        Integer value of the string
    """
    sign = 1
    res = 0
    idx = 0
    n = len(s)

    # Ignore leading whitespaces
    while idx < n and s[idx] == " ":
        idx += 1

    # Store the sign of number
    if idx < n and (s[idx] == "+" or s[idx] == "-"):
        if s[idx] == "-":
            sign = -1
        idx += 1

    # Construct the number digit by digit
    while idx < n and "0" <= s[idx] <= "9":
        digit = ord(s[idx]) - ord("0")
        res = 10 * res + digit

        # Handle overflow and underflow
        if res > INT_MAX:
            return INT_MAX if sign == 1 else INT_MIN

        idx += 1

    return res * sign


def main():
    """Test cases for atoi implementation."""
    test_cases = [
        ("-123", -123),
        ("   -", 0),
        ("  1231231231311133", INT_MAX),
        ("-999999999999", INT_MIN),
        ("  -0012gfg4", -12),
        ("42", 42),
        ("   +42", 42),
    ]

    print("=" * 50)
    print("Atoi Implementation")
    print("=" * 50)

    for s, expected in test_cases:
        result = my_atoi(s)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: '{s}'")
        print(f"Output: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
