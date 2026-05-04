"""N Queen Problem using Branch and Bound."""

from __future__ import annotations


class NQueenBranchBound:
    """Solve N-Queens problem using Branch and Bound with bitmask tracking."""

    def __init__(self, n: int) -> None:
        self.n = n
        self.solutions: list[list[int]] = []
        self.occupied_cols: set[int] = set()
        self.occupied_diag_main: set[int] = set()
        self.occupied_diag_anti: set[int] = set()

    def _is_safe(self, row: int, col: int) -> bool:
        return (
            col not in self.occupied_cols
            and (row + col) not in self.occupied_diag_main
            and (row - col) not in self.occupied_diag_anti
        )

    def _solve(self, row: int, board: list[int]) -> None:
        if row == self.n:
            self.solutions.append(board[:])
            return

        for col in range(self.n):
            if self._is_safe(row, col):
                self.occupied_cols.add(col)
                self.occupied_diag_main.add(row + col)
                self.occupied_diag_anti.add(row - col)
                board.append(col)

                self._solve(row + 1, board)

                board.pop()
                self.occupied_cols.remove(col)
                self.occupied_diag_main.remove(row + col)
                self.occupied_diag_anti.remove(row - col)

    def solve(self) -> list[list[int]]:
        """Find all solutions to the N-Queens problem.

        Returns:
            List of solutions, where each solution is a list of column positions.
        """
        self.solutions = []
        self._solve(0, [])
        return self.solutions

    def print_board(self, solution: list[int]) -> str:
        """Return a string representation of the board."""
        lines = []
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                line += "Q " if solution[row] == col else ". "
            lines.append(line.strip())
        return "\n".join(lines)


def n_queen_branch_bound(n: int) -> list[list[int]]:
    """Solve N-Queens problem using Branch and Bound.

    Args:
        n: Size of the board and number of queens.

    Returns:
        List of all valid queen placements.
    """
    solver = NQueenBranchBound(n)
    return solver.solve()


if __name__ == "__main__":
    n = 4
    solutions = n_queen_branch_bound(n)
    solver = NQueenBranchBound(n)
    print(f"Found {len(solutions)} solutions for {n}-Queens:")
    for i, sol in enumerate(solutions):
        print(f"\nSolution {i + 1}:")
        print(solver.print_board(sol))
