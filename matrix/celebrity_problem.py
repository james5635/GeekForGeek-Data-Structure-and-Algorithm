def knows(a, b, matrix):
    """
    Helper function to check if person a knows person b.
    matrix[i][j] = 1 means i knows j, else 0.
    """
    return matrix[a][b] == 1


def find_celebrity(n, matrix):
    """
    Find the celebrity in a party of n people.
    A celebrity is someone who is known by everyone but knows no one.
    Returns the index of the celebrity, or -1 if no celebrity exists.
    """
    # Step 1: Use elimination to find a potential celebrity
    celeb = 0
    for i in range(1, n):
        if knows(celeb, i, matrix):
            celeb = i

    # Step 2: Verify the potential celebrity
    for i in range(n):
        if i != celeb:
            # If celeb knows i or i does not know celeb, then celeb is not a celebrity
            if knows(celeb, i, matrix) or not knows(i, celeb, matrix):
                return -1
    return celeb


# Test cases
if __name__ == "__main__":
    # Example 1: Celebrity at index 2
    n1 = 4
    matrix1 = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
    print("Celebrity index:", find_celebrity(n1, matrix1))  # Expected: 2

    # Example 2: No celebrity
    n2 = 3
    matrix2 = [[0, 0, 1], [0, 0, 0], [0, 1, 0]]
    print("Celebrity index:", find_celebrity(n2, matrix2))  # Expected: -1

    # Example 3: Celebrity at index 0
    n3 = 3
    matrix3 = [[0, 0, 0], [1, 0, 0], [1, 0, 0]]
    print("Celebrity index:", find_celebrity(n3, matrix3))  # Expected: 0
