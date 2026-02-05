"""
N Queen Problem
https://www.geeksforgeeks.org/dsa/n-queen-problem-backtracking-3/

Given an integer n, place n queens on an n × n chessboard such that no two queens attack each other.

Approach: Backtracking with Column and Diagonal Hashing (Optimized)
Time Complexity: O(n!)
Auxiliary Space: O(n)
"""


def place_queens(i, cols, left_diagonal, right_diagonal, cur, result):
    """
    Recursive function to place queens on the board.

    Args:
        i: Current row index
        cols: Array to mark occupied columns
        left_diagonal: Array to mark occupied left diagonals
        right_diagonal: Array to mark occupied right diagonals
        cur: Current solution being built
        result: List to store all valid solutions
    """
    n = len(cols)

    # Base case: If all queens are placed
    if i == n:
        result.append(cur[:])
        return

    # Consider the row and try placing queen in all columns one by one
    for j in range(n):
        # Check if the queen can be placed
        if cols[j] or right_diagonal[i + j] or left_diagonal[i - j + n - 1]:
            continue

        # Mark the cell occupied
        cols[j] = 1
        right_diagonal[i + j] = 1
        left_diagonal[i - j + n - 1] = 1
        cur.append(j + 1)

        place_queens(i + 1, cols, left_diagonal, right_diagonal, cur, result)

        # Remove the queen from current cell (backtrack)
        cur.pop()
        cols[j] = 0
        right_diagonal[i + j] = 0
        left_diagonal[i - j + n - 1] = 0


def n_queen(n):
    """
    Find all solutions to the N-Queens problem.

    Args:
        n: Size of the chessboard (n x n)

    Returns:
        List of all valid solutions where each solution is a list of column positions
    """
    # Arrays to mark occupied cells
    cols = [0] * n
    left_diagonal = [0] * (2 * n)
    right_diagonal = [0] * (2 * n)
    cur = []
    result = []

    # Place queens
    place_queens(0, cols, left_diagonal, right_diagonal, cur, result)

    return result


def print_board(solution, n):
    """
    Helper function to print the board for a solution.
    """
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[row] == col + 1:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()


def main():
    """
    Main function to demonstrate the algorithm.
    """
    # Test case 1: n = 4
    print("Test Case 1: n = 4")
    n = 4
    result = n_queen(n)
    print(f"Number of solutions: {len(result)}")
    print(f"Solutions (column positions for each row):")
    for i, sol in enumerate(result):
        print(f"  Solution {i + 1}: {sol}")
        print(f"  Board representation:")
        print_board(sol, n)

    # Test case 2: n = 3 (no solution)
    print("Test Case 2: n = 3")
    n = 3
    result = n_queen(n)
    print(f"Number of solutions: {len(result)}")
    if not result:
        print("No solution exists for n = 3")
    print()

    # Test case 3: n = 5
    print("Test Case 3: n = 5")
    n = 5
    result = n_queen(n)
    print(f"Number of solutions: {len(result)}")
    print(f"First solution: {result[0] if result else 'None'}")


if __name__ == "__main__":
    main()
