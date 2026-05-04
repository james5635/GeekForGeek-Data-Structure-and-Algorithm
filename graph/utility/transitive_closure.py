"""
Transitive Closure of a Graph using Floyd-Warshall Algorithm.

Given a directed graph, the transitive closure determines if a vertex j
is reachable from vertex i for all vertex pairs (i, j) in the graph.

The reachability matrix is called the transitive closure of a graph.

Time Complexity: O(V^3) where V is the number of vertices
Auxiliary Space: O(V^2) for the result matrix
"""

from typing import List


def transitive_closure(graph: List[List[int]]) -> List[List[int]]:
    """
    Compute the transitive closure of a directed graph using Floyd-Warshall.

    Args:
        graph: Adjacency matrix where graph[i][j] = 1 if there is a direct
               edge from vertex i to vertex j, 0 otherwise.

    Returns:
        A matrix where result[i][j] = 1 if vertex j is reachable from vertex i,
        0 otherwise.

    Example:
        >>> graph = [
        ...     [0, 1, 1, 0],
        ...     [0, 0, 1, 0],
        ...     [1, 0, 0, 1],
        ...     [0, 0, 0, 0]
        ... ]
        >>> tc = transitive_closure(graph)
        >>> for row in tc:
        ...     print(row)
        [1, 1, 1, 1]
        [1, 1, 1, 1]
        [1, 1, 1, 1]
        [0, 0, 0, 1]
    """
    n = len(graph)

    # Initialize result matrix as a copy of the input graph
    tc = [[graph[i][j] for j in range(n)] for i in range(n)]

    # Every vertex can reach itself
    for i in range(n):
        tc[i][i] = 1

    # Floyd-Warshall: for each intermediate vertex k, check all pairs (i, j)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If i can reach k and k can reach j, then i can reach j
                if tc[i][k] == 1 and tc[k][j] == 1:
                    tc[i][j] = 1

    return tc


def print_matrix(matrix: List[List[int]]) -> None:
    """Print a matrix in a readable format."""
    for row in matrix:
        print(" ".join(str(val) for val in row))


if __name__ == "__main__":
    # Example 1: Graph from GeeksforGeeks
    print("Example 1:")
    graph1 = [[0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 0]]
    print("Input adjacency matrix:")
    print_matrix(graph1)
    print("\nTransitive closure:")
    result1 = transitive_closure(graph1)
    print_matrix(result1)

    # Example 2: Disconnected graph
    print("\nExample 2 (disconnected graph):")
    graph2 = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    print("Input adjacency matrix:")
    print_matrix(graph2)
    print("\nTransitive closure:")
    result2 = transitive_closure(graph2)
    print_matrix(result2)

    # Example 3: Complete cycle
    print("\nExample 3 (complete cycle):")
    graph3 = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    print("Input adjacency matrix:")
    print_matrix(graph3)
    print("\nTransitive closure:")
    result3 = transitive_closure(graph3)
    print_matrix(result3)
