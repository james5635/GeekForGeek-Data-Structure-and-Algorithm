"""
Erdos-Renyi Model for Generating Random Graphs

The Erdos-Renyi model is a fundamental model for generating random graphs.
Two variants:
1. G(n, M): Graph with n vertices and exactly M edges (uniformly chosen)
2. G(n, p): Graph with n vertices where each possible edge exists with probability p

Properties of G(n, p):
- Expected number of edges: p * n*(n-1)/2
- Probability of connectivity has a sharp threshold at p = ln(n)/n
- When p < 1/n: graph has small components
- When p > ln(n)/n: graph is almost surely connected
- When p = c/n (c > 1): giant component emerges

Time Complexity: O(n^2) for G(n, p), O(M) for G(n, M)
Space Complexity: O(n^2) or O(M) depending on representation
"""

import random
from typing import List, Tuple, Set, Dict


def erdos_renyi_gnm(n: int, m: int) -> List[List[int]]:
    """
    Generate random graph G(n, M): n vertices, exactly M random edges.

    Args:
        n: Number of vertices (0 to n-1)
        m: Number of edges

    Returns:
        Adjacency list of random graph

    Raises:
        ValueError: If m > n*(n-1)/2
    """
    max_edges = n * (n - 1) // 2
    if m > max_edges:
        raise ValueError(
            f"Cannot have {m} edges in graph with {n} vertices (max: {max_edges})"
        )

    # Select m unique edges
    all_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    selected = random.sample(all_edges, m)

    adj: List[List[int]] = [[] for _ in range(n)]
    for u, v in selected:
        adj[u].append(v)
        adj[v].append(u)

    return adj


def erdos_renyi_gnp(n: int, p: float) -> List[List[int]]:
    """
    Generate random graph G(n, p): each edge exists with probability p.

    Args:
        n: Number of vertices
        p: Probability of each edge (0.0 to 1.0)

    Returns:
        Adjacency list of random graph
    """
    if not 0.0 <= p <= 1.0:
        raise ValueError("p must be between 0 and 1")

    adj: List[List[int]] = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                adj[i].append(j)
                adj[j].append(i)

    return adj


def count_edges(adj: List[List[int]]) -> int:
    """Count total edges in graph."""
    return sum(len(neighbors) for neighbors in adj) // 2


def count_components(adj: List[List[int]]) -> int:
    """Count number of connected components."""
    n = len(adj)
    visited = [False] * n
    components = 0

    for i in range(n):
        if not visited[i]:
            components += 1
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)

    return components


def is_connected(adj: List[List[int]]) -> bool:
    """Check if graph is connected."""
    if not adj:
        return True
    return count_components(adj) == 1


def get_degree_distribution(adj: List[List[int]]) -> Dict[int, int]:
    """
    Get degree distribution of the graph.

    Returns:
        Dictionary mapping degree -> count of vertices with that degree
    """
    dist: Dict[int, int] = {}
    for neighbors in adj:
        d = len(neighbors)
        dist[d] = dist.get(d, 0) + 1
    return dist


def analyze_random_graph(n: int, p: float, num_trials: int = 100) -> Dict:
    """
    Analyze properties of G(n, p) over multiple trials.

    Args:
        n: Number of vertices
        p: Edge probability
        num_trials: Number of random graphs to generate

    Returns:
        Dictionary with average statistics
    """
    total_edges = 0
    connected_count = 0
    total_components = 0

    for _ in range(num_trials):
        adj = erdos_renyi_gnp(n, p)
        total_edges += count_edges(adj)
        if is_connected(adj):
            connected_count += 1
        total_components += count_components(adj)

    return {
        "n": n,
        "p": p,
        "num_trials": num_trials,
        "avg_edges": total_edges / num_trials,
        "expected_edges": p * n * (n - 1) / 2,
        "connectivity_probability": connected_count / num_trials,
        "avg_components": total_components / num_trials,
        "connectivity_threshold": (n - 1) * (n > 1)
        and __import__("math").log(n) / n
        or 0,
    }


def generate_connected_random_graph(n: int, p: float) -> List[List[int]]:
    """
    Generate a random G(n, p) graph that is guaranteed to be connected.

    Uses rejection sampling.

    Args:
        n: Number of vertices
        p: Edge probability

    Returns:
        Connected random graph
    """
    if p <= 0:
        raise ValueError("p must be positive")

    while True:
        adj = erdos_renyi_gnp(n, p)
        if is_connected(adj):
            return adj


if __name__ == "__main__":
    random.seed(42)

    # Example 1: G(n, M) model
    print("=== Example 1: G(n, M) Model ===")
    adj1 = erdos_renyi_gnm(6, 8)
    print(f"G(6, 8): {count_edges(adj1)} edges")
    for i, neighbors in enumerate(adj1):
        print(f"  Vertex {i}: {sorted(neighbors)}")

    # Example 2: G(n, p) model
    print("\n=== Example 2: G(n, p) Model ===")
    adj2 = erdos_renyi_gnp(8, 0.3)
    edges = count_edges(adj2)
    print(f"G(8, 0.3): {edges} edges (expected: {0.3 * 8 * 7 / 2:.1f})")
    print(f"Connected: {is_connected(adj2)}")
    print(f"Components: {count_components(adj2)}")

    # Example 3: Degree distribution
    print("\n=== Example 3: Degree Distribution ===")
    dist = get_degree_distribution(adj2)
    for degree in sorted(dist.keys()):
        print(f"  Degree {degree}: {dist[degree]} vertices")

    # Example 4: Connectivity analysis
    print("\n=== Example 4: Connectivity Analysis ===")
    for p_val in [0.1, 0.2, 0.3, 0.5]:
        result = analyze_random_graph(20, p_val, num_trials=50)
        print(
            f"  G(20, {p_val}): connectivity = {result['connectivity_probability']:.2f}"
        )

    # Example 5: Generate connected graph
    print("\n=== Example 5: Guaranteed Connected ===")
    conn_adj = generate_connected_random_graph(10, 0.2)
    print(f"Connected: {is_connected(conn_adj)}")
    print(f"Edges: {count_edges(conn_adj)}")
