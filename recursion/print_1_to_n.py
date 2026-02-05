"""
Print 1 to n without using Loops (Using Recursion)
https://www.geeksforgeeks.org/dsa/print-1-to-n-without-using-loops/

Given an integer n, print numbers from 1 to n using recursion.

Examples:
Input: n = 3
Output: 1 2 3

Time Complexity: O(n)
Space Complexity: O(n) - due to recursion stack
"""


def print_1_to_n(n):
    """
    Print numbers from 1 to n using recursion.
    Uses tail recursion pattern: recursive call first, then print.

    Args:
        n: Positive integer
    """
    # Base case: stop when n reaches 0
    if n == 0:
        return

    # Recursive call first (goes all the way to 1)
    print_1_to_n(n - 1)

    # Print after recursion unwinds (prints 1, 2, 3, ... n)
    print(n, end=" ")


def print_1_to_n_list(n):
    """
    Return numbers from 1 to n as a list using recursion.

    Args:
        n: Positive integer

    Returns:
        List of integers from 1 to n
    """
    if n == 0:
        return []

    result = print_1_to_n_list(n - 1)
    result.append(n)
    return result


def main():
    """Test the print_1_to_n function with various inputs."""
    test_cases = [3, 5, 10, 1]

    print("=" * 50)
    print("Print 1 to n using Recursion")
    print("=" * 50)

    for num in test_cases:
        print(f"\nn = {num}")
        print("Output: ", end="")
        print_1_to_n(num)
        print()  # New line after output
        print(f"As list: {print_1_to_n_list(num)}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
