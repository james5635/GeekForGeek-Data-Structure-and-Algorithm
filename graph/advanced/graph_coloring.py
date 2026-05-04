"""
Graph Coloring - Introduction and Applications

Graph coloring assigns colors to vertices such that no two adjacent
vertices share the same color. The minimum number of colors needed
is called the chromatic number.

Algorithms:
1. Greedy Coloring: Assign lowest available color to each vertex
   - Time: O(V + E), Uses at most (max_degree + 1) colors
   - Not always optimal

2. Backtracking (M-Coloring): Try all color assignments
   - Time: O(m^V) where m = number of colors
   - Always finds optimal if enough colors available

3. Welsh-Powell: Order vertices by degree descending, then greedy
   - Better results than basic greedy in practice

Applications:
- Schedule/timetable generation
- Register allocation in compilers
- Map coloring
- Sudoku solving
- Frequency assignment in mobile networks
"""

from typing import List, Dict, Optional, Tuple
from collections import defaultdict


def greedy_coloring(adj: List[List[int]]) -> Tuple[List[int], int]:
    """
    Greedy graph coloring algorithm.

    Assigns the lowest available color to each vertex in order.

    Args:
        adj: Adjacency list of undirected graph

    Returns:
        Tuple of (coloring, num_colors) where coloring[i] = color of vertex i
    """
    n = len(adj)
    color = [-1] * n
    color[0] = 0

    for u in range(1, n):
        # Find colors used by neighbors
        used_colors = set()
        for v in adj[u]:
            if color[v] != -1:
                used_colors.add(color[v])

        # Find lowest available color
        c = 0
        while c in used_colors:
            c += 1
        color[u] = c

    num_colors = max(color) + 1 if n > 0 else 0
    return color, num_colors


def welsh_powell_coloring(adj: List[List[int]]) -> Tuple[List[int], int]:
    """
    Welsh-Powell coloring: order by degree descending, then greedy.

    Args:
        adj: Adjacency list

    Returns:
        Tuple of (coloring, num_colors)
    """
    n = len(adj)
    # Sort vertices by degree (descending)
    vertices = sorted(range(n), key=lambda v: -len(adj[v]))

    color = [-1] * n

    for u in vertices:
        used_colors = set()
        for v in adj[u]:
            if color[v] != -1:
                used_colors.add(color[v])

        c = 0
        while c in used_colors:
            c += 1
        color[u] = c

    num_colors = max(color) + 1 if n > 0 else 0
    return color, num_colors


def is_safe_coloring(
    adj: List[List[int]], color: List[int], vertex: int, c: int
) -> bool:
    """Check if assigning color c to vertex is safe."""
    for neighbor in adj[vertex]:
        if color[neighbor] == c:
            return False
    return True


def m_coloring_backtracking(adj: List[List[int]], m: int) -> Optional[List[int]]:
    """
    Find a valid coloring using at most m colors via backtracking.

    Args:
        adj: Adjacency list
        m: Maximum number of colors

    Returns:
        Valid coloring, or None if not possible with m colors
    """
    n = len(adj)
    color = [0] * n

    def backtrack(v: int) -> bool:
        if v == n:
            return True

        for c in range(1, m + 1):
            if is_safe_coloring(adj, color, v, c):
                color[v] = c
                if backtrack(v + 1):
                    return True
                color[v] = 0

        return False

    if backtrack(0):
        # Convert to 0-indexed
        return [c - 1 for c in color]
    return None


def chromatic_number(adj: List[List[int]]) -> int:
    """
    Find the chromatic number (minimum colors needed).

    Uses binary search + backtracking for efficiency.

    Args:
        adj: Adjacency list

    Returns:
        Chromatic number
    """
    n = len(adj)
    if n == 0:
        return 0

    max_degree = max(len(neighbors) for neighbors in adj)

    # Binary search for minimum m
    low, high = 1, max_degree + 1
    result = high

    while low <= high:
        mid = (low + high) // 2
        if m_coloring_backtracking(adj, mid) is not None:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


def is_bipartite(adj: List[List[int]]) -> bool:
    """
    Check if graph is bipartite (2-colorable).

    Args:
        adj: Adjacency list

    Returns:
        True if bipartite
    """
    n = len(adj)
    color = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue

        color[start] = 0
        stack = [start]

        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    stack.append(v)
                elif color[v] == color[u]:
                    return False

    return True


def solve_sudoku_with_graph_coloring(
    board: List[List[int]],
) -> Optional[List[List[int]]]:
    """
    Solve Sudoku using graph coloring (backtracking approach).

    Each cell is a vertex, edges connect cells in same row/col/box.

    Args:
        board: 9x9 Sudoku board (0 = empty)

    Returns:
        Solved board, or None if unsolvable
    """
    n = 9

    def is_valid(board: List[List[int]], row: int, col: int, num: int) -> bool:
        # Check row
        if num in board[row]:
            return False
        # Check column
        if num in [board[r][col] for r in range(n)]:
            return False
        # Check 3x3 box
        box_r, box_c = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_r, box_r + 3):
            for c in range(box_c, box_c + 3):
                if board[r][c] == num:
                    return False
        return True

    def solve() -> bool:
        for r in range(n):
            for c in range(n):
                if board[r][c] == 0:
                    for num in range(1, 10):
                        if is_valid(board, r, c, num):
                            board[r][c] = num
                            if solve():
                                return True
                            board[r][c] = 0
                    return False
        return True

    if solve():
        return board
    return None


if __name__ == "__main__":
    # Example 1: Greedy coloring
    print("=== Example 1: Greedy Coloring ===")
    adj1 = [
        [1, 2],  # 0
        [0, 2, 3],  # 1
        [0, 1],  # 2
        [1, 4],  # 3
        [3],  # 4
    ]
    color1, num_colors1 = greedy_coloring(adj1)
    print(f"Greedy coloring: {color1}")
    print(f"Colors used: {num_colors1}")

    # Example 2: Welsh-Powell
    print("\n=== Example 2: Welsh-Powell ===")
    color2, num_colors2 = welsh_powell_coloring(adj1)
    print(f"Welsh-Powell coloring: {color2}")
    print(f"Colors used: {num_colors2}")

    # Example 3: M-Coloring
    print("\n=== Example 3: M-Coloring ===")
    result3 = m_coloring_backtracking(adj1, 3)
    if result3:
        print(f"3-coloring possible: {result3}")
    else:
        print("3-coloring not possible")

    # Example 4: Chromatic number
    print("\n=== Example 4: Chromatic Number ===")
    chi = chromatic_number(adj1)
    print(f"Chromatic number: {chi}")

    # Example 5: Bipartite check
    print("\n=== Example 5: Bipartite Check ===")
    bipartite_adj = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(f"Is bipartite: {is_bipartite(bipartite_adj)}")

    non_bipartite = [[1, 2], [0, 2], [0, 1]]  # Triangle
    print(f"Triangle is bipartite: {is_bipartite(non_bipartite)}")

    # Example 6: Sudoku
    print("\n=== Example 6: Sudoku Solver ===")
    sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    solved = solve_sudoku_with_graph_coloring(sudoku)
    if solved:
        print("Solved:")
        for row in solved:
            print(f"  {row}")
