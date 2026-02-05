"""
nCr using Recursion - Calculate combinations using recursive approach

Given two integers n and r, compute the value of nCr (number of ways to choose
r elements from a set of n elements) using recursion.

Approach: Mathematical Transformation (O(r) Time and O(r) Space)
- Uses the relation: nCr = nCr-1 * (n - r + 1) / r
- More efficient than Pascal's rule approach

Examples:
    Input: n = 5, r = 2
    Output: 10

    Input: n = 6, r = 3
    Output: 20
"""


def nCr(n: int, r: int) -> int:
    """
    Calculate nCr (combinations) using recursion.

    Args:
        n: Total number of items
        r: Number of items to choose

    Returns:
        Number of combinations

    Time Complexity: O(r)
    Space Complexity: O(r) due to recursion stack
    """
    # Base Case 1: If r = 0, then nCr = 1
    if r == 0:
        return 1

    # Base Case 2: If r = 1, then nCr = n
    if r == 1:
        return n

    # Recursive relation: nCr = nCr-1 * (n - r + 1) / r
    return nCr(n, r - 1) * (n - r + 1) // r


def nCr_pascal(n: int, r: int) -> int:
    """
    Alternative: Calculate nCr using Pascal's Rule.

    Uses the relation: nCr = (n-1)C(r-1) + (n-1)Cr
    Less efficient but demonstrates recursive thinking.

    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    # Base Case 1: If r = 0 or r = n, then nCr = 1
    if r == 0 or r == n:
        return 1

    # Base Case 2: If r = 1, then nCr = n
    if r == 1:
        return n

    # Recursive relation: nCr = (n-1)C(r-1) + (n-1)Cr
    return nCr_pascal(n - 1, r - 1) + nCr_pascal(n - 1, r)


def main():
    """Test the nCr function with various inputs."""
    print("=" * 60)
    print("nCr Calculation using Recursion")
    print("=" * 60)

    test_cases = [
        (5, 2),
        (3, 1),
        (6, 3),
        (10, 5),
        (20, 10),
    ]

    print("\nUsing Mathematical Transformation (O(r)):")
    print("-" * 60)
    for n, r in test_cases:
        result = nCr(n, r)
        print(f"{n}C{r} = {result}")

    print("\nUsing Pascal's Rule (O(2^n)):")
    print("-" * 60)
    for n, r in test_cases[:4]:  # Only test smaller cases due to exponential time
        result = nCr_pascal(n, r)
        print(f"{n}C{r} = {result}")

    print("\n" + "=" * 60)
    print("Complexity Analysis:")
    print("=" * 60)
    print("Mathematical Approach:")
    print("  Time: O(r), Space: O(r)")
    print("Pascal's Rule Approach:")
    print("  Time: O(2^n), Space: O(n)")


if __name__ == "__main__":
    main()
