"""
Factorial of a Number using Recursion
https://www.geeksforgeeks.org/dsa/program-for-factorial-of-a-number/

Given a non-negative integer n, compute the factorial of the number.
Factorial of n is defined as n * (n-1) * (n-2) * ... * 1
For n = 0, factorial is 1.

Time Complexity: O(n)
Space Complexity: O(n) - due to recursion stack
"""


def factorial(n):
    """
    Calculate factorial of n using recursion.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)


def main():
    """Test the factorial function with various inputs."""
    test_cases = [0, 1, 5, 4, 6]

    print("=" * 50)
    print("Factorial using Recursion")
    print("=" * 50)

    for num in test_cases:
        result = factorial(num)
        print(f"factorial({num}) = {result}")

    print("=" * 50)


if __name__ == "__main__":
    main()
