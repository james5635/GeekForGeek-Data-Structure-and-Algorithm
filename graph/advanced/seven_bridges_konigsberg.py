"""
Seven Bridges of Konigsberg

The famous problem that started graph theory: Can one walk through the city
of Konigsberg crossing each of its seven bridges exactly once?

Euler proved in 1736 that this is impossible because the graph representing
the bridges has 4 vertices with odd degree. For an Eulerian path to exist,
at most 2 vertices can have odd degree.

This module provides utilities to model and solve the Konigsberg bridges
problem and similar bridge-walking problems.

Key Concepts:
- Model landmasses as vertices and bridges as edges
- An undirected graph has an Eulerian path iff it is connected and
  has 0 or 2 vertices of odd degree
- The Konigsberg graph has 4 odd-degree vertices, so no solution exists
"""

from typing import List, Dict, Tuple, Optional
from collections import defaultdict


def solve_konigsberg() -> Dict:
    """
    Solve the classic Seven Bridges of Konigsberg problem.

    The city had 4 landmasses (A, B, C, D) connected by 7 bridges:
    - A connected to B: 2 bridges
    - A connected to C: 2 bridges
    - A connected to D: 1 bridge
    - B connected to D: 1 bridge
    - C connected to D: 1 bridge

    Degrees: A=5, B=3, C=3, D=3 (all odd!)

    Returns:
        Dictionary with solution details
    """
    # Landmasses and bridges
    bridges = [
        ("A", "B"),
        ("A", "B"),  # 2 bridges between A and B
        ("A", "C"),
        ("A", "C"),  # 2 bridges between A and C
        ("A", "D"),  # 1 bridge between A and D
        ("B", "D"),  # 1 bridge between B and D
        ("C", "D"),  # 1 bridge between C and D
    ]

    # Calculate degrees
    degree: Dict[str, int] = defaultdict(int)
    for u, v in bridges:
        degree[u] += 1
        degree[v] += 1

    odd_vertices = [v for v, d in degree.items() if d % 2 != 0]

    return {
        "landmasses": list(degree.keys()),
        "degrees": dict(degree),
        "odd_degree_vertices": odd_vertices,
        "num_bridges": len(bridges),
        "has_eulerian_path": len(odd_vertices) <= 2,
        "has_eulerian_circuit": len(odd_vertices) == 0,
        "explanation": (
            f"The Konigsberg graph has {len(odd_vertices)} vertices with odd degree "
            f"{odd_vertices}. An Eulerian path requires at most 2 odd-degree vertices. "
            f"Since {len(odd_vertices)} > 2, no such path exists."
        ),
    }


class BridgeGraph:
    """Model a bridge-walking problem as a graph."""

    def __init__(self):
        self.adj: Dict[str, List[str]] = defaultdict(list)
        self.edge_count: Dict[Tuple[str, str], int] = defaultdict(int)

    def add_bridge(self, landmass1: str, landmass2: str) -> None:
        """Add a bridge between two landmasses."""
        self.adj[landmass1].append(landmass2)
        self.adj[landmass2].append(landmass1)
        key = (min(landmass1, landmass2), max(landmass1, landmass2))
        self.edge_count[key] += 1

    def get_degrees(self) -> Dict[str, int]:
        """Get degree of each vertex."""
        return {v: len(self.adj[v]) for v in self.adj}

    def get_odd_degree_vertices(self) -> List[str]:
        """Get vertices with odd degree."""
        return [v for v, d in self.get_degrees().items() if d % 2 != 0]

    def is_connected(self) -> bool:
        """Check if all vertices are connected."""
        if not self.adj:
            return True

        visited = set()
        start = next(iter(self.adj))
        stack = [start]
        visited.add(start)

        while stack:
            node = stack.pop()
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return visited == set(self.adj.keys())

    def has_eulerian_path(self) -> bool:
        """Check if an Eulerian path exists."""
        odd_count = len(self.get_odd_degree_vertices())
        return self.is_connected() and (odd_count == 0 or odd_count == 2)

    def has_eulerian_circuit(self) -> bool:
        """Check if an Eulerian circuit exists."""
        odd_count = len(self.get_odd_degree_vertices())
        return self.is_connected() and odd_count == 0

    def find_eulerian_path(self) -> Optional[List[str]]:
        """
        Find an Eulerian path if one exists.

        Returns:
            List of vertices in path order, or None if no path exists
        """
        if not self.has_eulerian_path():
            return None

        # Choose start vertex
        odd = self.get_odd_degree_vertices()
        if odd:
            start = odd[0]
        else:
            start = next(iter(self.adj))

        # Hierholzer's algorithm
        adj_copy = defaultdict(list)
        for v in self.adj:
            adj_copy[v] = list(self.adj[v])

        stack = [start]
        circuit = []

        while stack:
            v = stack[-1]
            if adj_copy[v]:
                next_v = adj_copy[v].pop()
                adj_copy[next_v].remove(v)
                stack.append(next_v)
            else:
                circuit.append(stack.pop())

        return circuit[::-1]

    def total_bridges(self) -> int:
        """Return total number of bridges."""
        return sum(self.edge_count.values())

    def analyze(self) -> Dict:
        """Analyze the bridge problem."""
        degrees = self.get_degrees()
        odd_vertices = self.get_odd_degree_vertices()

        return {
            "vertices": list(self.adj.keys()),
            "degrees": degrees,
            "total_bridges": self.total_bridges(),
            "odd_degree_vertices": odd_vertices,
            "is_connected": self.is_connected(),
            "has_eulerian_path": self.has_eulerian_path(),
            "has_eulerian_circuit": self.has_eulerian_circuit(),
        }


if __name__ == "__main__":
    # Example 1: Classic Konigsberg problem
    print("=== Seven Bridges of Konigsberg ===")
    result = solve_konigsberg()
    print(f"Landmasses: {result['landmasses']}")
    print(f"Degrees: {result['degrees']}")
    print(f"Odd degree vertices: {result['odd_degree_vertices']}")
    print(f"Has Eulerian Path: {result['has_eulerian_path']}")
    print(f"\nExplanation: {result['explanation']}")

    # Example 2: A graph that DOES have an Eulerian path
    print("\n=== Example: Graph with Eulerian Path ===")
    g = BridgeGraph()
    g.add_bridge("A", "B")
    g.add_bridge("B", "C")
    g.add_bridge("C", "D")
    g.add_bridge("D", "B")

    analysis = g.analyze()
    print(f"Degrees: {analysis['degrees']}")
    print(f"Has Eulerian Path: {analysis['has_eulerian_path']}")
    path = g.find_eulerian_path()
    if path:
        print(f"Eulerian Path: {' -> '.join(path)}")

    # Example 3: Graph with Eulerian Circuit
    print("\n=== Example: Graph with Eulerian Circuit ===")
    g2 = BridgeGraph()
    g2.add_bridge("A", "B")
    g2.add_bridge("B", "C")
    g2.add_bridge("C", "A")

    analysis2 = g2.analyze()
    print(f"Degrees: {analysis2['degrees']}")
    print(f"Has Eulerian Circuit: {analysis2['has_eulerian_circuit']}")
    path2 = g2.find_eulerian_path()
    if path2:
        print(f"Eulerian Circuit: {' -> '.join(path2)}")
