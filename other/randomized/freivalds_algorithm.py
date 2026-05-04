import random


def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    """Multiply two matrices."""
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result


def freivalds_algorithm(
    A: list[list[int]], B: list[list[int]], C: list[list[int]], k: int = 5
) -> bool:
    """Verify if A * B = C using Freivald's randomized algorithm.

    Returns True if likely A*B=C, False if definitely A*B!=C.
    """
    n = len(A)

    for _ in range(k):
        r = [random.randint(0, 1) for _ in range(n)]

        br = [sum(B[i][j] * r[j] for j in range(n)) for i in range(n)]
        ab_r = [sum(A[i][j] * br[j] for j in range(n)) for i in range(n)]
        c_r = [sum(C[i][j] * r[j] for j in range(n)) for i in range(n)]

        if any(ab_r[i] != c_r[i] for i in range(n)):
            return False

    return True


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C_correct = matrix_multiply(A, B)
    C_wrong = [[19, 22], [43, 50]]

    print(f"A = {A}")
    print(f"B = {B}")
    print(f"A*B (correct) = {C_correct}")
    print(f"Freivalds (correct C): {freivalds_algorithm(A, B, C_correct)}")
    print(f"Freivalds (wrong C):   {freivalds_algorithm(A, B, C_wrong)}")
