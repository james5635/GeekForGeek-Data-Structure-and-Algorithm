"""
Binary to Gray Code using Recursion

Given a binary number as a decimal number, convert it to its equivalent Gray Code.
In Gray Code, consecutive numbers differ by only one bit.

Examples:
- Binary: 1001 -> Gray: 1101
- Binary: 11 -> Gray: 10

Approach:
1. If n == 0, return 0 (base case)
2. Take last digit (a) and second last digit (b)
3. If a and b are opposite bits (XOR), append 1 to result
4. If a and b are same, append 0 to result
5. Recursively process n/10

Formula:
- If last two bits differ: 1 + 10 * binary_to_gray(n/10)
- If last two bits same: 10 * binary_to_gray(n/10)

Time Complexity: O(log n) - Traverse through all digits
Auxiliary Space: O(log n) - Due to recursive call stack
"""


def binary_to_gray(n):
    """
    Convert binary number to Gray code using recursion.

    Args:
        n: Binary number represented as decimal (e.g., 1011 is 1011)

    Returns:
        int: Gray code as decimal representation
    """
    # Base case: if n is 0
    if not n:
        return 0

    # Taking last digit
    a = n % 10

    # Taking second last digit
    b = int(n / 10) % 10

    # If last digits are opposite bits (XOR operation)
    if (a and not b) or (not a and b):
        return 1 + 10 * binary_to_gray(int(n / 10))

    # If last two bits are same
    return 10 * binary_to_gray(int(n / 10))


def binary_to_gray_str(binary_str):
    """
    Alternative implementation using string representation for larger numbers.

    Args:
        binary_str: Binary number as string

    Returns:
        str: Gray code as string
    """
    if len(binary_str) == 0:
        return ""

    # First bit of Gray code is same as first bit of binary
    gray = binary_str[0]

    # Compute remaining bits using XOR
    for i in range(1, len(binary_str)):
        # XOR of current and previous bit
        xor_result = str(int(binary_str[i - 1]) ^ int(binary_str[i]))
        gray += xor_result

    return gray


def main():
    # Test Case 1
    binary1 = 1001
    gray1 = binary_to_gray(binary1)
    print(f"Binary: {binary1}")
    print(f"Gray Code: {gray1}")
    print(f"Expected: 1101")
    print()

    # Test Case 2
    binary2 = 11
    gray2 = binary_to_gray(binary2)
    print(f"Binary: {binary2}")
    print(f"Gray Code: {gray2}")
    print(f"Expected: 10")
    print()

    # Test Case 3 - Using string method for larger number
    binary3_str = "1011101"
    gray3_str = binary_to_gray_str(binary3_str)
    print(f"Binary: {binary3_str}")
    print(f"Gray Code: {gray3_str}")
    print(f"Expected: 1110011")
    print()

    # Test Case 4 - Single digit
    binary4 = 1
    gray4 = binary_to_gray(binary4)
    print(f"Binary: {binary4}")
    print(f"Gray Code: {gray4}")
    print(f"Expected: 1")
    print()

    # Test Case 5 - Using string method
    binary5_str = "1000"
    gray5_str = binary_to_gray_str(binary5_str)
    print(f"Binary: {binary5_str}")
    print(f"Gray Code: {gray5_str}")
    print(f"Expected: 1100")


if __name__ == "__main__":
    main()
