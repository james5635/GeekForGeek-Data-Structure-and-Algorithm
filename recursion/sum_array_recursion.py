"""
Sum of Array Elements using Recursion
https://www.geeksforgeeks.org/dsa/sum-array-elements-using-recursion/

Given an array of integers, find the sum of array elements using recursion.

Examples:
Input: arr = [1, 2, 3]
Output: 6
Explanation: 1 + 2 + 3 = 6

Time Complexity: O(n), where n is the length of the array
Space Complexity: O(n), due to recursive function calls stored in the call stack
"""


def sum_array_recursive(arr, n=None):
    """
    Calculate sum of array elements using recursion.

    Args:
        arr: List of integers
        n: Number of elements to consider (defaults to len(arr))

    Returns:
        Sum of the first n elements
    """
    # Initialize n on first call
    if n is None:
        n = len(arr)

    # Base case: if no elements, sum is 0
    if n <= 0:
        return 0

    # Recursive case: sum of n elements = sum of (n-1) elements + nth element
    return sum_array_recursive(arr, n - 1) + arr[n - 1]


def sum_array_helper(arr):
    """
    Helper function to calculate sum of entire array.

    Args:
        arr: List of integers

    Returns:
        Sum of all elements in the array
    """
    return sum_array_recursive(arr, len(arr))


def main():
    """Test the sum_array_recursive function with various inputs."""
    test_cases = [[1, 2, 3], [15, 12, 13, 10], [5], [], [1, 2, 3, 4, 5]]

    print("=" * 50)
    print("Sum of Array Elements using Recursion")
    print("=" * 50)

    for arr in test_cases:
        result = sum_array_helper(arr)
        print(f"\nArray: {arr}")
        print(f"Sum: {result}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
