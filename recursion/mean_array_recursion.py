"""
Mean of Array using Recursion

Given an array of numbers, calculate the mean (average) using recursion.
The mean is the sum of elements divided by the number of elements.

Approach:
- Base case: If array has only one element, return that element
- Recursive case: Calculate mean of first n-1 elements, then combine with nth element
  using formula: (mean(n-1) * (n-1) + arr[n-1]) / n

Time Complexity: O(n)
Auxiliary Space: O(n)
"""


def find_mean(arr):
    """
    Calculate the mean of an array using recursion.

    Args:
        arr: List of numbers

    Returns:
        float: Mean of the array
    """
    n = len(arr)

    # Base case: when there is only one element
    if n == 1:
        return float(arr[n - 1])
    else:
        # Recursive formula: mean(n) = (mean(n-1) * (n-1) + arr[n-1]) / n
        return (find_mean(arr[: n - 1]) * (n - 1) + arr[n - 1]) / n


def main():
    # Test Case 1
    arr1 = [1, 2, 3, 4, 5]
    mean1 = find_mean(arr1)
    print(f"Array: {arr1}")
    print(f"Mean: {mean1}")
    print(f"Expected: 3.0")
    print()

    # Test Case 2
    arr2 = [1, 2, 3]
    mean2 = find_mean(arr2)
    print(f"Array: {arr2}")
    print(f"Mean: {mean2}")
    print(f"Expected: 2.0")
    print()

    # Test Case 3 - Single element
    arr3 = [10]
    mean3 = find_mean(arr3)
    print(f"Array: {arr3}")
    print(f"Mean: {mean3}")
    print(f"Expected: 10.0")
    print()

    # Test Case 4 - With floating point results
    arr4 = [10, 20, 30]
    mean4 = find_mean(arr4)
    print(f"Array: {arr4}")
    print(f"Mean: {mean4}")
    print(f"Expected: 20.0")


if __name__ == "__main__":
    main()
