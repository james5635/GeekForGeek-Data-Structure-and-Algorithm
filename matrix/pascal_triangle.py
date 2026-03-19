def generate_pascal_triangle(n):
    """
    Generate the first n rows of Pascal's triangle.
    Returns a list of lists representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        row = [1]  # First element is always 1
        # Calculate middle elements
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle


def print_pascal_triangle(n):
    """
    Print the first n rows of Pascal's triangle.
    """
    triangle = generate_pascal_triangle(n)
    for row in triangle:
        print(" ".join(map(str, row)))


# Test cases
if __name__ == "__main__":
    print("First 5 rows of Pascal's triangle:")
    print_pascal_triangle(5)
    # Expected:
    # 1
    # 1 1
    # 1 2 1
    # 1 3 3 1
    # 1 4 6 4 1

    print("\nFirst 1 row of Pascal's triangle:")
    print_pascal_triangle(1)
    # Expected:
    # 1

    print("\nFirst 0 rows of Pascal's triangle:")
    print_pascal_triangle(0)
    # Expected: (nothing printed)
