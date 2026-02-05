"""
Multiply Two Strings

Given two numbers as strings, find their product as a string.

Approach: Elementary School Multiplication - O(n*m) Time and O(n+m) Space
Multiply digit by digit from right to left, handling carries.
"""


def multiply_strings(num1, num2):
    """
    Multiply two numbers represented as strings.

    Args:
        num1, num2: Number strings to multiply

    Returns:
        Product as string
    """
    if num1 == "0" or num2 == "0":
        return "0"

    n, m = len(num1), len(num2)
    result = [0] * (n + m)

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            digit1 = ord(num1[i]) - ord("0")
            digit2 = ord(num2[j]) - ord("0")

            pos1, pos2 = i + j, i + j + 1
            mul = digit1 * digit2 + result[pos2]

            result[pos2] = mul % 10
            result[pos1] += mul // 10

    # Convert to string
    result_str = ""
    for num in result:
        if not (len(result_str) == 0 and num == 0):
            result_str += str(num)

    return result_str if result_str else "0"


def main():
    """Test cases for multiplying strings."""
    test_cases = [
        ("2", "3", "6"),
        ("123", "456", "56088"),
        ("99", "99", "9801"),
        ("0", "123", "0"),
        ("123456789", "987654321", "121932631112635269"),
    ]

    print("=" * 50)
    print("Multiply Two Strings")
    print("=" * 50)

    for num1, num2, expected in test_cases:
        result = multiply_strings(num1, num2)
        status = "✓" if result == expected else "✗"
        print(f"\nNum1: {num1}")
        print(f"Num2: {num2}")
        print(f"Output: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
