"""
Check if Two Numbers are Equal

Problem: Check if two numbers are equal without using arithmetic
and comparison operators.

Example:
    Input: num1 = 10, num2 = 10
    Output: true

    Input: num1 = 10, num2 = 20
    Output: false

Approach 1: Using XOR operator
    - If two numbers are equal, their XOR is 0
    - If XOR is 0, numbers are equal

Approach 2: Using subtraction (not allowed per constraints, but shown for reference)

Approach 3: Using bitwise operations

Time Complexity: O(1)
Space Complexity: O(1)
"""


def are_equal_xor(num1, num2):
    """
    Check if two numbers are equal using XOR.
    If num1 == num2, then num1 ^ num2 == 0

    Args:
        num1: First number
        num2: Second number

    Returns:
        bool: True if numbers are equal, False otherwise
    """
    return (num1 ^ num2) == 0


def are_equal_bitwise(num1, num2):
    """
    Check if two numbers are equal using bitwise operations.

    Args:
        num1: First number
        num2: Second number

    Returns:
        bool: True if numbers are equal, False otherwise
    """
    # If numbers are equal, all bits will be same
    # XOR gives 0 when bits are same
    xor_result = num1 ^ num2

    # Check if all bits are 0
    return not xor_result


def are_equal_hash(num1, num2):
    """
    Check if two numbers are equal using a hash set approach.
    Store one number in a set and check if the other exists.

    Args:
        num1: First number
        num2: Second number

    Returns:
        bool: True if numbers are equal, False otherwise
    """
    num_set = {num1}
    return num2 in num_set


if __name__ == "__main__":
    # Test Case 1: Equal positive numbers
    num1, num2 = 10, 10
    print(f"Test 1 (XOR): {are_equal_xor(num1, num2)}")  # Expected: True
    print(f"Test 1 (Hash): {are_equal_hash(num1, num2)}")  # Expected: True

    # Test Case 2: Different positive numbers
    num1, num2 = 10, 20
    print(f"Test 2 (XOR): {are_equal_xor(num1, num2)}")  # Expected: False
    print(f"Test 2 (Hash): {are_equal_hash(num1, num2)}")  # Expected: False

    # Test Case 3: Equal negative numbers
    num1, num2 = -5, -5
    print(f"Test 3 (XOR): {are_equal_xor(num1, num2)}")  # Expected: True

    # Test Case 4: Zero
    num1, num2 = 0, 0
    print(f"Test 4 (XOR): {are_equal_xor(num1, num2)}")  # Expected: True

    # Test Case 5: Zero and non-zero
    num1, num2 = 0, 5
    print(f"Test 5 (XOR): {are_equal_xor(num1, num2)}")  # Expected: False

    # Test Case 6: Large numbers
    num1, num2 = 1000000, 1000000
    print(f"Test 6 (XOR): {are_equal_xor(num1, num2)}")  # Expected: True

    # Test Case 7: Same value different type
    num1, num2 = 5, 5.0
    print(f"Test 7 (XOR): {are_equal_xor(int(num1), int(num2))}")  # Expected: True
