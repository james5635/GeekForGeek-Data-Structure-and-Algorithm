"""
Dijkstra's Shortest Path Algorithm
URL: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
Source: GeeksforGeeks

Problem:
Given a weighted undirected graph and a source vertex src, find the shortest
path distances from the source vertex to all other vertices in the graph.

Note: The graph does not contain any negative edge weights.

Examples:
Input: src = 0
       adj = [ [(1, 4), (2, 8)],
               [(0, 4), (4, 6), (2, 3)],
               [(0, 8), (3, 2), (1, 3)],
               [(2, 2), (4, 10)],
               [(1, 6), (3, 10)] ]

Output: [0, 4, 7, 9, 10]

Algorithm:
Dijkstra's algorithm is a greedy algorithm that finds the shortest path
from a source vertex to all other vertices.

Key Idea:
- Maintain an array dist[] where dist[v] = shortest distance from src to v
- Initialize dist[src] = 0, all others = infinity
- Use a min-heap (priority queue) to always process the vertex with
  minimum current distance
- For each popped vertex, update distances to its neighbors

Algorithm Steps:
1. Create dist array, initialize dist[src] = 0, others = infinity
2. Push (0, src) into priority queue
3. While PQ not empty:
   a. Pop vertex with minimum distance
   b. If popped distance > current dist, skip (stale entry)
   c. For each neighbor (v, weight):
      - If dist[u] + weight < dist[v]:
        update dist[v] = dist[u] + weight
        push (dist[v], v) into PQ
4. Return dist array

Time Complexity: O((V + E) * log V)
Space Complexity: O(V + E)
"""

import heapq
import sys


def dijkstra(adj, src):
    """
    Dijkstra's shortest path algorithm using min-heap.

    Args:
        adj: Adjacency list where adj[u] = [(v, weight), ...]
        src: Source vertex

    Returns:
        List of shortest distances from src to all vertices

    Time: O((V + E) * log V)
    Space: O(V + E)
    """
    V = len(adj)

    pq = []
    dist = [sys.maxsize] * V

    dist[src] = 0
    heapq.heappush(pq, (0, src))

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist


def dijkstra_with_path(adj, src):
    """
    Dijkstra's algorithm that also tracks the path.

    Returns:
        Tuple of (distances, parents)
    """
    V = len(adj)

    pq = []
    dist = [sys.maxsize] * V
    parent = [-1] * V

    dist[src] = 0
    heapq.heappush(pq, (0, src))

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, parent


def get_path(parent, src, dest):
    """
    Reconstruct path from src to dest using parent array.
    """
    if parent[dest] == -1 and dest != src:
        return None

    path = []
    current = dest

    while current != -1:
        path.append(current)
        current = parent[current]

    return path[::-1]


def dijkstra_matrix(graph, src):
    """
    Dijkstra's algorithm using adjacency matrix.
    Less efficient but works for matrix representation.

    Time: O(V²)
    """
    V = len(graph)

    dist = [sys.maxsize] * V
    visited = [False] * V

    dist[src] = 0

    for _ in range(V):
        u = -1

        for v in range(V):
            if not visited[v] and (u == -1 or dist[v] < dist[u]):
                u = v

        if dist[u] == sys.maxsize:
            break

        visited[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    return dist


class Dijkstra:
    """
    Class implementation of Dijkstra's algorithm.
    """

    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        """Add undirected edge."""
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def add_directed_edge(self, u, v, weight):
        """Add directed edge."""
        self.adj[u].append((v, weight))

    def shortest_path(self, src):
        """Get shortest paths from src."""
        return dijkstra(self.adj, src)

    def shortest_path_with_info(self, src):
        """Get shortest paths with path information."""
        dist, parent = dijkstra_with_path(self.adj, src)
        return dist, parent

    def print_shortest_paths(self, src):
        """Print all shortest paths from src."""
        dist, parent = dijkstra_with_path(self.adj, src)

        print(f"\nShortest paths from vertex {src}:")
        print("-" * 40)

        for v in range(self.V):
            if dist[v] == sys.maxsize:
                print(f"  {src} -> {v}: No path")
            else:
                path = get_path(parent, src, v)
                path_str = " -> ".join(map(str, path))
                print(f"  {src} -> {v}: {dist[v]:3d}  [{path_str}]")


def create_graph_from_edges(vertices, edges, directed=False):
    """
    Create adjacency list from edge list.

    Args:
        vertices: Number of vertices
        edges: List of (u, v, weight) tuples
        directed: If True, create directed graph

    Returns:
        Adjacency list
    """
    adj = [[] for _ in range(vertices)]

    for u, v, w in edges:
        adj[u].append((v, w))
        if not directed:
            adj[v].append((u, w))

    return adj


if __name__ == "__main__":
    print("=" * 60)
    print("DIJKSTRA'S SHORTEST PATH ALGORITHM")
    print("=" * 60)

    print("\n" + "-" * 60)
    print("TEST CASE 1: Standard Graph")
    print("-" * 60)

    adj = [
        [(1, 4), (2, 8)],
        [(0, 4), (4, 6), (2, 3)],
        [(0, 8), (3, 2), (1, 3)],
        [(2, 2), (4, 10)],
        [(1, 6), (3, 10)],
    ]

    print("\nGraph (adjacency list):")
    for i, neighbors in enumerate(adj):
        print(f"  Vertex {i}: {neighbors}")

    print("\nVisual representation:")
    print("       0\n      /|\\")
    print("    4/ 8|8\\")
    print("    /   |   \\")
    print("   1----2----3\n    \\   |3  /")
    print("   6\\  | /10")
    print("     \\ |/")
    print("      4")

    src = 0
    distances = dijkstra(adj, src)

    print(f"\nShortest distances from vertex {src}:")
    print("-" * 30)
    for v, d in enumerate(distances):
        if d == sys.maxsize:
            print(f"  {src} -> {v}: unreachable")
        else:
            print(f"  {src} -> {v}: {d}")

    expected = [0, 4, 7, 9, 10]
    print(f"\nExpected: {expected}")
    print(f"Result:   {distances}")
    print(f"Status:   {'PASS' if distances == expected else 'FAIL'}")

    print("\n" + "-" * 60)
    print("TEST CASE 2: Using Dijkstra Class")
    print("-" * 60)

    dg = Dijkstra(5)
    edges = [(0, 1, 4), (0, 2, 8), (1, 2, 3), (1, 4, 6), (2, 3, 2), (3, 4, 10)]

    for u, v, w in edges:
        dg.add_edge(u, v, w)

    dg.print_shortest_paths(0)

    print("\n" + "-" * 60)
    print("TEST CASE 3: With Path Reconstruction")
    print("-" * 60)

    dist, parent = dijkstra_with_path(adj, 0)

    print(f"\nPath information from vertex 0:")
    for v in range(len(adj)):
        if dist[v] != sys.maxsize:
            path = get_path(parent, 0, v)
            print(
                f"  To {v}: distance = {dist[v]}, path = {' -> '.join(map(str, path))}"
            )

    print("\n" + "-" * 60)
    print("TEST CASE 4: Graph with Unreachable Nodes")
    print("-" * 60)

    adj2 = [[(1, 2)], [(0, 2), (2, 1)], [(1, 1)], [(4, 5)], [(3, 5)]]

    print("\nGraph with disconnected components:")
    print("  Component 1: 0 - 1 - 2")
    print("  Component 2: 3 - 4")

    distances2 = dijkstra(adj2, 0)
    print(f"\nDistances from 0: {distances2}")
    print("(Nodes 3, 4 are unreachable)")

    print("\n" + "-" * 60)
    print("TEST CASE 5: From Edge List")
    print("-" * 60)

    vertices = 4
    edges = [(0, 1, 1), (0, 2, 4), (1, 2, 2), (1, 3, 6), (2, 3, 3)]

    adj3 = create_graph_from_edges(vertices, edges)

    print("\nEdges:", edges)
    distances3 = dijkstra(adj3, 0)
    print(f"Distances from 0: {distances3}")

    print("\n" + "=" * 60)
    print("ALGORITHM EXPLANATION")
    print("=" * 60)
    print("""
How Dijkstra's Algorithm Works:
--------------------------------

1. Initialize:
   - dist[src] = 0, all other dist = infinity
   - Insert (0, src) into priority queue

2. Main Loop (while PQ not empty):
   
   Step 1: Pop vertex with minimum distance
           PQ contains (distance, vertex)
   
   Step 2: Skip if this is a stale entry
           (we already found a shorter path)
   
   Step 3: For each neighbor v of u:
           if dist[u] + weight(u,v) < dist[v]:
               dist[v] = dist[u] + weight(u,v)
               push (dist[v], v) into PQ

3. Continue until PQ is empty

Why It Works:
-------------
- The priority queue always gives us the vertex with the
  smallest tentative distance
- Once we pop a vertex, we've found the shortest path to it
  (because all remaining paths must go through vertices with
   equal or greater distances)
- This only works because all edge weights are non-negative

Why Not With Negative Weights:
-----------------------------
If negative edges existed, a shorter path could be found
through a vertex not yet processed, breaking the algorithm's
guarantee.
""")

    print("=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)
    print("\nAdjacency List + Min Heap:")
    print("   Time:  O((V + E) * log V)")
    print("   Space: O(V + E)")
    print("\nAdjacency Matrix:")
    print("   Time:  O(V²)")
    print("   Space: O(V)")
    print("\nWhere V = vertices, E = edges")
