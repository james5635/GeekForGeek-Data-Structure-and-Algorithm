"""
Total Number of Spanning Trees in a Graph

A spanning tree of a connected undirected graph is a subgraph that:
- Includes all vertices
- Is connected
- Has no cycles (exactly V-1 edges)

For complete graph K_n, the number of spanning trees is n^(n-2) (Cayley's formula).

For general graphs, use Kirchhoff's Matrix Tree Theorem:
1. Build the Laplacian matrix L = D - A (degree matrix - adjacency matrix)
2. Remove any row and corresponding column from L
3. The determinant of the resulting (V-1) x (V-1) matrix = number of spanning trees

Time Complexity: O(V^3) for determinant calculation
Space Complexity: O(V^2)
"""

from typing import List


def count_spanning_trees_complete(n: int) -> int:
    """
    Count spanning trees in a complete graph K_n using Cayley's formula.

    Number of spanning trees = n^(n-2)

    Args:
        n: Number of vertices

    Returns:
        Number of spanning trees
    """
    if n <= 1:
        return 0 if n <= 0 else 1
    return n ** (n - 2)


def count_spanning_trees_general(num_vertices: int, edges: List[List[int]]) -> int:
    """
    Count spanning trees using Kirchhoff's Matrix Tree Theorem.

    Args:
        num_vertices: Number of vertices
        edges: List of undirected edges

    Returns:
        Number of spanning trees
    """
    # Build Laplacian matrix
    laplacian = [[0] * num_vertices for _ in range(num_vertices)]

    for u, v in edges:
        laplacian[u][u] += 1
        laplacian[v][v] += 1
        laplacian[u][v] -= 1
        laplacian[v][u] -= 1

    # Remove last row and column (any row/column works)
    n = num_vertices - 1
    minor = [row[:n] for row in laplacian[:n]]

    # Calculate determinant using Gaussian elimination
    return int(round(_determinant(minor)))


def _determinant(matrix: List[List[float]]) -> float:
    """
    Calculate determinant using Gaussian elimination with partial pivoting.

    Args:
        matrix: Square matrix

    Returns:
        Determinant value
    """
    n = len(matrix)
    if n == 0:
        return 1.0
    if n == 1:
        return matrix[0][0]

    # Make a copy
    mat = [row[:] for row in matrix]
    det = 1.0

    for col in range(n):
        # Find pivot
        max_row = col
        for row in range(col + 1, n):
            if abs(mat[row][col]) > abs(mat[max_row][col]):
                max_row = row

        if max_row != col:
            mat[col], mat[max_row] = mat[max_row], mat[col]
            det *= -1

        if abs(mat[col][col]) < 1e-10:
            return 0.0

        det *= mat[col][col]

        # Eliminate below
        for row in range(col + 1, n):
            factor = mat[row][col] / mat[col][col]
            for j in range(col, n):
                mat[row][j] -= factor * mat[col][j]

    return det


def count_spanning_trees_multigraph(
    num_vertices: int, edges_with_multiplicity: List[List[int]]
) -> int:
    """
    Count spanning trees in a multigraph (edges can have multiplicity).

    Args:
        num_vertices: Number of vertices
        edges_with_multiplicity: List of [u, v, multiplicity]

    Returns:
        Number of spanning trees
    """
    laplacian = [[0] * num_vertices for _ in range(num_vertices)]

    for u, v, mult in edges_with_multiplicity:
        laplacian[u][u] += mult
        laplacian[v][v] += mult
        laplacian[u][v] -= mult
        laplacian[v][u] -= mult

    n = num_vertices - 1
    minor = [row[:n] for row in laplacian[:n]]

    return int(round(_determinant(minor)))


if __name__ == "__main__":
    # Example 1: Cayley's formula for complete graphs
    print("=== Example 1: Complete Graphs ===")
    for n in range(1, 7):
        trees = count_spanning_trees_complete(n)
        print(f"  K_{n}: {trees} spanning trees")
    # K_1=1, K_2=1, K_3=3, K_4=16, K_5=125, K_6=1296

    # Example 2: General graph - triangle
    print("\n=== Example 2: Triangle (K_3) ===")
    edges = [[0, 1], [1, 2], [0, 2]]
    count = count_spanning_trees_general(3, edges)
    print(f"Spanning trees: {count}")  # Should be 3

    # Example 3: Square with diagonal
    print("\n=== Example 3: Square with Diagonal ===")
    edges3 = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
    count3 = count_spanning_trees_general(4, edges3)
    print(f"Spanning trees: {count3}")  # 8 spanning trees

    # Example 4: Simple path
    print("\n=== Example 4: Simple Path ===")
    edges4 = [[0, 1], [1, 2], [2, 3]]
    count4 = count_spanning_trees_general(4, edges4)
    print(f"Spanning trees: {count4}")  # 1 (only the path itself)

    # Example 5: Multigraph
    print("\n=== Example 5: Multigraph ===")
    multi_edges = [[0, 1, 2], [1, 2, 1]]  # 2 edges between 0-1, 1 edge between 1-2
    count5 = count_spanning_trees_multigraph(3, multi_edges)
    print(f"Spanning trees: {count5}")  # 2 (can choose either of the 2 parallel edges)
