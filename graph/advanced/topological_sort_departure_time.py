"""
Topological Sort Using Departure Time

Given a Directed Acyclic Graph (DAG), find the topological sort using
the departure time concept from DFS.

Concept:
- Arrival Time: Time at which a vertex is first explored in DFS
- Departure Time: Time at which all neighbors of a vertex have been explored
  and we are ready to backtrack

Key insight: Vertices sorted by decreasing departure time give a valid
topological ordering.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List, Dict, Tuple


class TopologicalSortDeparture:
    """Topological sort using DFS departure times."""

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj: List[List[int]] = [[] for _ in range(num_vertices)]
        self.time = 0

    def add_edge(self, u: int, v: int) -> None:
        """Add directed edge u -> v."""
        self.adj[u].append(v)

    def _dfs(self, vertex: int, visited: List[bool], departure: List[int]) -> None:
        """
        DFS that records departure time for each vertex.

        Args:
            vertex: Current vertex being explored
            visited: Array tracking visited vertices
            departure: Array to store departure times (index = time, value = vertex)
        """
        visited[vertex] = True

        for neighbor in self.adj[vertex]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, departure)

        # Record departure: vertex departs at current time
        departure[self.time] = vertex
        self.time += 1

    def topological_sort(self) -> List[int]:
        """
        Perform topological sort using departure times.

        Returns:
            List of vertices in topological order

        Raises:
            ValueError: If graph contains a cycle
        """
        visited = [False] * self.num_vertices
        departure = [-1] * self.num_vertices
        self.time = 0

        # DFS from all unvisited vertices
        for i in range(self.num_vertices):
            if not visited[i]:
                self._dfs(i, visited, departure)

        # Return vertices in decreasing order of departure time
        result = []
        for i in range(self.num_vertices - 1, -1, -1):
            result.append(departure[i])

        return result

    def get_departure_times(self) -> Dict[int, int]:
        """
        Get departure time for each vertex.

        Returns:
            Dictionary mapping vertex -> departure_time
        """
        visited = [False] * self.num_vertices
        departure_order = [-1] * self.num_vertices
        self.time = 0

        for i in range(self.num_vertices):
            if not visited[i]:
                self._dfs(i, visited, departure_order)

        vertex_departure = {}
        for time_idx in range(self.num_vertices):
            vertex = departure_order[time_idx]
            vertex_departure[vertex] = time_idx

        return vertex_departure


def topological_sort_departure_time(
    num_vertices: int, edges: List[Tuple[int, int]]
) -> List[int]:
    """
    Functional version: topological sort using departure time.

    Args:
        num_vertices: Number of vertices (0 to V-1)
        edges: List of (u, v) tuples for directed edges

    Returns:
        List of vertices in topological order
    """
    adj: List[List[int]] = [[] for _ in range(num_vertices)]
    for u, v in edges:
        adj[u].append(v)

    time = 0
    departure = [-1] * num_vertices

    def dfs(vertex: int, visited: List[bool]) -> None:
        nonlocal time
        visited[vertex] = True
        for neighbor in adj[vertex]:
            if not visited[neighbor]:
                dfs(neighbor, visited)
        departure[time] = vertex
        time += 1

    visited = [False] * num_vertices
    for i in range(num_vertices):
        if not visited[i]:
            dfs(i, visited)

    return [departure[i] for i in range(num_vertices - 1, -1, -1)]


if __name__ == "__main__":
    # Example 1: Using the class
    print("=== Example 1: Class-based approach ===")
    g = TopologicalSortDeparture(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    result = g.topological_sort()
    print(f"Topological Sort: {result}")

    departure_times = g.get_departure_times()
    print("Departure times:")
    for vertex in sorted(departure_times.keys()):
        print(f"  Vertex {vertex}: departure at time {departure_times[vertex]}")

    # Example 2: Functional approach
    print("\n=== Example 2: Functional approach ===")
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    result = topological_sort_departure_time(6, edges)
    print(f"Topological Sort: {result}")

    # Example 3: Course scheduling scenario
    print("\n=== Example 3: Course prerequisites ===")
    # 0 -> 1 means course 0 is prerequisite for course 1
    course_edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    order = topological_sort_departure_time(5, course_edges)
    print(f"Course order: {order}")
