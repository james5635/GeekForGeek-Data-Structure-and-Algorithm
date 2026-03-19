def matrixChainOrder(p, n):
    """
    Matrix Chain Multiplication using Dynamic Programming
    Args:
        p: List of dimensions where matrix i has dimensions p[i-1] x p[i] for i=1..n
        n: Number of matrices (length of p is n+1)
    Returns:
        Minimum number of scalar multiplications needed
    """
    # Create a 2D DP table to store results of subproblems
    # dp[i][j] = Minimum number of scalar multiplications needed to compute
    #            the product of matrices from i to j (inclusive)
    dp = [[0] * n for _ in range(n)]

    # cost is zero when multiplying one matrix
    for i in range(1, n):
        dp[i][i] = 0

    # L is chain length
    for L in range(2, n):  # L from 2 to n-1
        for i in range(1, n - L + 1):
            j = i + L - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                # q = cost/scalar multiplications
                q = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < dp[i][j]:
                    dp[i][j] = q

    return dp[1][n - 1]


def test_matrixChainOrder():
    # Test case 1
    # p[] = {40, 20, 30, 10, 30}
    # Matrices: A1:40x20, A2:20x30, A3:30x10, A4:10x30
    p1 = [40, 20, 30, 10, 30]
    n1 = len(p1)
    print(f"Test 1 - Dimensions: {p1}")
    result1 = matrixChainOrder(p1, n1)
    print(f"Minimum multiplications: {result1}")
    print(f"Expected: 26000")
    print()

    # Test case 2
    # p[] = {10, 20, 30, 40, 30}
    # Matrices: A1:10x20, A2:20x30, A3:30x40, A4:40x30
    p2 = [10, 20, 30, 40, 30]
    n2 = len(p2)
    print(f"Test 2 - Dimensions: {p2}")
    result2 = matrixChainOrder(p2, n2)
    print(f"Minimum multiplications: {result2}")
    print(f"Expected: 30000")
    print()

    # Test case 3
    # p[] = {10, 20, 30}
    # Matrices: A1:10x20, A2:20x30
    p3 = [10, 20, 30]
    n3 = len(p3)
    print(f"Test 3 - Dimensions: {p3}")
    result3 = matrixChainOrder(p3, n3)
    print(f"Minimum multiplications: {result3}")
    print(f"Expected: 6000")
    print()


if __name__ == "__main__":
    test_matrixChainOrder()
