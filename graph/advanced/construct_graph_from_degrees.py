"""
Construct a Graph from Given Degrees of All Vertices

Given a sequence of degrees, determine if a valid simple graph (no self-loops,
no multiple edges) can be constructed and if so, construct one.

Havel-Hakimi Algorithm:
1. Sort degrees in non-increasing order
2. Remove the first degree d
3. Subtract 1 from the next d degrees
4. If any degree becomes negative, impossible
5. Repeat until all degrees are 0 or impossible

Erdos-Gallai Theorem:
A sequence d1 >= d2 >= ... >= dn is graphical iff:
- Sum of degrees is even
- For every k from 1 to n:
  sum(d_i for i=1..k) <= k*(k-1) + sum(min(d_i, k) for i=k+1..n)

Time Complexity: O(n^2) for Havel-Hakimi
Space Complexity: O(n)
"""

from typing import List, Optional, Tuple
from collections import defaultdict


def is_graphical(degrees: List[int]) -> bool:
    """
    Check if a degree sequence can form a valid simple graph (Havel-Hakimi).

    Args:
        degrees: List of vertex degrees

    Returns:
        True if graphical, False otherwise
    """
    # Quick checks
    if any(d < 0 for d in degrees):
        return False
    if sum(degrees) % 2 != 0:
        return False  # Handshaking lemma: sum of degrees must be even
    if any(d >= len(degrees) for d in degrees):
        return False  # No vertex can have degree >= n in simple graph

    # Havel-Hakimi algorithm
    degs = sorted(degrees, reverse=True)

    while degs and degs[0] > 0:
        d = degs[0]
        degs = degs[1:]  # Remove first element

        if d > len(degs):
            return False  # Not enough vertices

        # Subtract 1 from next d elements
        for i in range(d):
            degs[i] -= 1
            if degs[i] < 0:
                return False

        degs = sorted(degs, reverse=True)

    return all(d == 0 for d in degs)


def construct_graph_havel_hakimi(degrees: List[int]) -> Optional[List[List[int]]]:
    """
    Construct a graph from degree sequence using Havel-Hakimi algorithm.

    Args:
        degrees: List of vertex degrees

    Returns:
        Adjacency matrix of constructed graph, or None if impossible
    """
    n = len(degrees)

    if not is_graphical(degrees):
        return None

    # Create list of (degree, original_index) pairs
    vertices = [(degrees[i], i) for i in range(n)]

    adj = [[0] * n for _ in range(n)]

    while True:
        # Sort by degree descending
        vertices.sort(key=lambda x: -x[0])

        if vertices[0][0] == 0:
            break  # All degrees are 0

        d, u = vertices[0]
        vertices = vertices[1:]  # Remove first vertex

        if d > len(vertices):
            return None

        # Connect u to next d vertices with highest degrees
        for i in range(d):
            deg_v, v = vertices[i]
            adj[u][v] = 1
            adj[v][u] = 1
            vertices[i] = (deg_v - 1, v)

    return adj


def construct_adjacency_list(degrees: List[int]) -> Optional[List[List[int]]]:
    """
    Construct graph and return as adjacency list.

    Args:
        degrees: List of vertex degrees

    Returns:
        Adjacency list, or None if impossible
    """
    adj_matrix = construct_graph_havel_hakimi(degrees)
    if adj_matrix is None:
        return None

    n = len(degrees)
    adj_list: List[List[int]] = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] == 1:
                adj_list[i].append(j)
                adj_list[j].append(i)

    return adj_list


def erdos_gallai(degrees: List[int]) -> bool:
    """
    Check if degree sequence is graphical using Erdos-Gallai theorem.

    Args:
        degrees: List of vertex degrees

    Returns:
        True if graphical, False otherwise
    """
    n = len(degrees)
    degs = sorted(degrees, reverse=True)

    # Sum must be even
    if sum(degs) % 2 != 0:
        return False

    # Check Erdos-Gallai inequalities
    for k in range(1, n + 1):
        left = sum(degs[:k])
        right = k * (k - 1) + sum(min(d, k) for d in degs[k:])
        if left > right:
            return False

    return True


if __name__ == "__main__":
    # Example 1: Valid degree sequence
    print("=== Example 1: Valid sequence [3, 3, 2, 2, 2] ===")
    degrees1 = [3, 3, 2, 2, 2]
    print(f"Is graphical (Havel-Hakimi): {is_graphical(degrees1)}")
    print(f"Is graphical (Erdos-Gallai): {erdos_gallai(degrees1)}")

    adj = construct_graph_havel_hakimi(degrees1)
    if adj:
        print("Adjacency matrix:")
        for row in adj:
            print(f"  {row}")

    # Example 2: Impossible sequence
    print("\n=== Example 2: Impossible [5, 5, 5, 5, 5] ===")
    degrees2 = [5, 5, 5, 5, 5]
    print(f"Is graphical: {is_graphical(degrees2)}")

    # Example 3: Adjacency list output
    print("\n=== Example 3: [2, 2, 1, 1] ===")
    degrees3 = [2, 2, 1, 1]
    adj_list = construct_adjacency_list(degrees3)
    if adj_list:
        for i, neighbors in enumerate(adj_list):
            print(f"  Vertex {i}: {neighbors}")

    # Example 4: Larger graph
    print("\n=== Example 4: [4, 4, 3, 3, 2, 2, 2] ===")
    degrees4 = [4, 4, 3, 3, 2, 2, 2]
    print(f"Is graphical: {is_graphical(degrees4)}")
    adj4 = construct_graph_havel_hakimi(degrees4)
    if adj4:
        print("Adjacency matrix:")
        for row in adj4:
            print(f"  {row}")
