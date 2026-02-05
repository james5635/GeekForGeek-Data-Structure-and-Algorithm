"""
Sum of Digits using Recursion

Given a number, find the sum of its digits using recursion.

Approach:
- Extract the last digit using modulo 10 (n % 10)
- Add it to the sum of digits of the remaining number (n // 10)
- Base case: when n < 10, return n (single digit)

Time Complexity: O(log n) - number of digits
Space Complexity: O(log n) - recursion stack depth
"""


def sum_of_digits(n: int) -> int:
    """
    Calculate sum of digits using recursion.

    Args:
        n: Integer number (handles negative numbers)

    Returns:
        Sum of all digits
    """
    n = abs(n)  # Handle negative numbers

    # Base case: single digit
    if n < 10:
        return n

    # Recursive case: last digit + sum of remaining digits
    return (n % 10) + sum_of_digits(n // 10)


def main():
    """Test cases for sum of digits."""
    test_cases = [
        12345,  # 1+2+3+4+5 = 15
        45632,  # 4+5+6+3+2 = 20
        0,  # 0
        9,  # 9
        1000,  # 1+0+0+0 = 1
        -12345,  # Should handle negatives: 15
    ]

    print("Sum of Digits using Recursion")
    print("=" * 50)

    for num in test_cases:
        result = sum_of_digits(num)
        print(f"Number: {num}")
        print(f"Sum of digits: {result}")
        print("-" * 30)


if __name__ == "__main__":
    main()
