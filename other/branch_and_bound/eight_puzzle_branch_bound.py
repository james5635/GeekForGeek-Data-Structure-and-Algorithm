"""8 Puzzle Problem using Branch and Bound."""

from __future__ import annotations

import copy
import heapq
from typing import Tuple

Matrix = Tuple[Tuple[int, ...], ...]


def _get_blanks(matrix: Matrix) -> Tuple[int, int]:
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                return i, j
    return -1, -1


def _calculate_cost(matrix: Matrix, target: Matrix, level: int) -> int:
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] != 0 and matrix[i][j] != target[i][j]:
                misplaced += 1
    return misplaced + level


def _move(matrix: Matrix, x1: int, y1: int, x2: int, y2: int) -> Matrix:
    new_matrix = [list(row) for row in matrix]
    new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1]
    return tuple(tuple(row) for row in new_matrix)


class PuzzleNode:
    """Represents a state in the 8-puzzle search space."""

    def __init__(
        self,
        matrix: Matrix,
        target: Matrix,
        level: int,
        parent: "PuzzleNode | None" = None,
    ) -> None:
        self.matrix = matrix
        self.level = level
        self.cost = _calculate_cost(matrix, target, level)
        self.parent = parent

    def __lt__(self, other: "PuzzleNode") -> bool:
        return self.cost < other.cost


def _is_solvable(matrix: Matrix) -> bool:
    flat = [val for row in matrix for val in row if val != 0]
    inversions = sum(
        1
        for i in range(len(flat))
        for j in range(i + 1, len(flat))
        if flat[i] > flat[j]
    )
    return inversions % 2 == 0


def eight_puzzle_branch_bound(initial: Matrix, target: Matrix) -> list[Matrix]:
    """Solve 8 Puzzle using Branch and Bound.

    Args:
        initial: Initial 3x3 matrix state.
        target: Target 3x3 matrix state.

    Returns:
        List of matrices representing the solution path, or empty list if unsolvable.
    """
    if not _is_solvable(initial):
        return []

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    root = PuzzleNode(initial, target, 0)
    pq: list[PuzzleNode] = [root]
    visited: set[Matrix] = set()

    while pq:
        heapq.heapify(pq)
        current = heapq.heappop(pq)

        if current.matrix == target:
            path: list[Matrix] = []
            node: PuzzleNode | None = current
            while node is not None:
                path.append(node.matrix)
                node = node.parent
            path.reverse()
            return path

        visited.add(current.matrix)
        blank_x, blank_y = _get_blanks(current.matrix)

        for dx, dy in moves:
            new_x, new_y = blank_x + dx, blank_y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_matrix = _move(current.matrix, blank_x, blank_y, new_x, new_y)
                if new_matrix not in visited:
                    child = PuzzleNode(new_matrix, target, current.level + 1, current)
                    heapq.heappush(pq, child)

    return []


if __name__ == "__main__":
    initial_state = (
        (1, 2, 3),
        (5, 6, 0),
        (7, 8, 4),
    )
    target_state = (
        (1, 2, 3),
        (5, 8, 6),
        (0, 7, 4),
    )
    solution = eight_puzzle_branch_bound(initial_state, target_state)
    if solution:
        print(f"Solution found in {len(solution) - 1} moves:")
        for i, step in enumerate(solution):
            print(f"Step {i}:")
            for row in step:
                print(row)
            print()
    else:
        print("No solution exists.")
