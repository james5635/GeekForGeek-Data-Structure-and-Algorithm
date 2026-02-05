"""
Print n to 1 without using Loops (Using Recursion)
https://www.geeksforgeeks.org/dsa/print-n-to-1-without-loop/

Given an integer n, print numbers from n to 1 using recursion.

Examples:
Input: n = 3
Output: 3 2 1

Time Complexity: O(n)
Space Complexity: O(n) - due to recursion stack
"""


def print_n_to_1(n):
    """
    Print numbers from n to 1 using recursion.
    Uses head recursion pattern: print first, then recursive call.

    Args:
        n: Positive integer
    """
    # Base case: stop when n reaches 0
    if n == 0:
        return

    # Print first (prints n, n-1, n-2, ... 1)
    print(n, end=" ")

    # Then make recursive call
    print_n_to_1(n - 1)


def print_n_to_1_list(n):
    """
    Return numbers from n to 1 as a list using recursion.

    Args:
        n: Positive integer

    Returns:
        List of integers from n to 1
    """
    if n == 0:
        return []

    result = [n]
    result.extend(print_n_to_1_list(n - 1))
    return result


def main():
    """Test the print_n_to_1 function with various inputs."""
    test_cases = [3, 5, 10, 1]

    print("=" * 50)
    print("Print n to 1 using Recursion")
    print("=" * 50)

    for num in test_cases:
        print(f"\nn = {num}")
        print("Output: ", end="")
        print_n_to_1(num)
        print()  # New line after output
        print(f"As list: {print_n_to_1_list(num)}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
