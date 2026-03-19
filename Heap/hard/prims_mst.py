"""
Prim's Algorithm for Minimum Spanning Tree (MST)
URL: https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
Source: GeeksforGeeks

Problem:
Given a weighted undirected graph, find the Minimum Spanning Tree (MST)
and its total weight.

What is MST?
A Minimum Spanning Tree is a subset of the edges of a connected,
weighted graph that connects all the vertices with the minimum possible
total edge weight.

Prim's Algorithm:
- Greedy algorithm that grows the MST one vertex at a time
- Always picks the minimum weight edge that connects a vertex in MST
  to a vertex not yet in MST
- Uses a priority queue (min-heap) to efficiently find minimum edges

Algorithm Steps:
1. Create a key array initialized to infinity, key[0] = 0 for source
2. Create mstSet to track vertices included in MST
3. While all vertices not in MST:
   a. Pick vertex u with minimum key value not in MST
   b. Add u to MST
   c. Update key values of adjacent vertices not in MST
4. Return MST edges or total weight

Time Complexity: O((V+E) * log V) with priority queue
Space Complexity: O(V + E)
"""

import sys
import heapq
from collections import defaultdict


class Graph:
    """
    Graph class for Prim's MST algorithm.
    Supports both adjacency matrix and adjacency list representations.
    """

    def __init__(self, vertices, is_matrix=True):
        self.V = vertices
        self.is_matrix = is_matrix
        if is_matrix:
            self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        else:
            self.graph = defaultdict(list)

    def add_edge_matrix(self, u, v, weight):
        """Add edge to adjacency matrix."""
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def add_edge_list(self, u, v, weight):
        """Add edge to adjacency list."""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def min_key(self, key, mst_set):
        """
        Find vertex with minimum key value not in MST.

        Args:
            key: Array of key values
            mst_set: Boolean array indicating vertices in MST

        Returns:
            Index of vertex with minimum key
        """
        min_val = sys.maxsize
        min_index = 0

        for v in range(self.V):
            if not mst_set[v] and key[v] < min_val:
                min_val = key[v]
                min_index = v

        return min_index

    def prim_mst_matrix(self):
        """
        Prim's MST for adjacency matrix representation.

        Time: O(V²)
        Space: O(V)

        Returns:
            Tuple of (MST edges list, total weight)
        """
        key = [sys.maxsize] * self.V
        parent = [None] * self.V

        key[0] = 0
        mst_set = [False] * self.V
        parent[0] = -1

        mst_edges = []
        total_weight = 0

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True
            total_weight += key[u]

            if parent[u] != -1:
                mst_edges.append((parent[u], u, key[u]))

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not mst_set[v]
                    and self.graph[u][v] < key[v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return mst_edges, total_weight

    def prim_mst_matrix_heap(self):
        """
        Prim's MST using min-heap for adjacency matrix.

        Time: O(V² log V)
        Space: O(V)
        """
        key = [sys.maxsize] * self.V
        parent = [None] * self.V

        key[0] = 0
        mst_set = [False] * self.V

        pq = [(0, 0)]
        mst_edges = []
        total_weight = 0

        while pq:
            weight, u = heapq.heappop(pq)

            if mst_set[u]:
                continue

            mst_set[u] = True
            total_weight += weight

            if parent[u] is not None and parent[u] != -1:
                mst_edges.append((parent[u], u, weight))

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not mst_set[v]
                    and self.graph[u][v] < key[v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    heapq.heappush(pq, (key[v], v))

        return mst_edges, total_weight

    def spanning_tree(self):
        """
        Prim's MST using adjacency list and min-heap.
        Most efficient version.

        Time: O((V + E) * log V)
        Space: O(V + E)

        Returns:
            Total weight of MST
        """
        pq = []
        visited = [False] * self.V
        result = 0

        heapq.heappush(pq, (0, 0))

        while pq:
            weight, u = heapq.heappop(pq)

            if visited[u]:
                continue

            result += weight
            visited[u] = True

            for v, w in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(pq, (w, v))

        return result

    def print_mst(self, edges, total_weight):
        """Print MST edges and total weight."""
        print("\nMST Edges:")
        print("-" * 30)
        print(f"{'Edge':<15} {'Weight':>10}")
        print("-" * 30)

        for u, v, w in edges:
            print(f"{u} - {v:<10} {w:>10}")

        print("-" * 30)
        print(f"{'Total Weight:':<15} {total_weight:>10}")


def prim_mst_simple(adj, V):
    """
    Simple function to compute MST weight.

    Args:
        adj: Adjacency list
        V: Number of vertices

    Returns:
        Total weight of MST
    """
    pq = []
    visited = [False] * V
    result = 0

    heapq.heappush(pq, (0, 0))

    while pq:
        weight, u = heapq.heappop(pq)

        if visited[u]:
            continue

        result += weight
        visited[u] = True

        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))

    return result


def prim_mst_with_path(adj, V, src=0):
    """
    Prim's MST that also tracks the path.

    Args:
        adj: Adjacency list
        V: Number of vertices
        src: Source vertex (default 0)

    Returns:
        Tuple of (distances, parents)
    """
    dist = [sys.maxsize] * V
    parent = [-1] * V

    dist[src] = 0
    pq = [(0, src)]

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


if __name__ == "__main__":
    print("=" * 60)
    print("PRIM'S ALGORITHM FOR MINIMUM SPANNING TREE")
    print("=" * 60)

    print("\n" + "-" * 60)
    print("TEST CASE 1: Basic Graph (Adjacency Matrix)")
    print("-" * 60)

    g1 = Graph(5, is_matrix=True)
    edges = [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9),
    ]

    for u, v, w in edges:
        g1.add_edge_matrix(u, v, w)

    print("\nGraph vertices: 5")
    print("Edges:")
    for u, v, w in edges:
        print(f"  {u} -- {v}: weight = {w}")

    print("\nUsing adjacency matrix + min_key:")
    edges1, weight1 = g1.prim_mst_matrix()
    g1.print_mst(edges1, weight1)

    print("\n" + "-" * 60)
    print("TEST CASE 2: Same Graph (Adjacency List)")
    print("-" * 60)

    g2 = Graph(0, is_matrix=False)
    g2.V = 5

    for u, v, w in edges:
        g2.add_edge_list(u, v, w)

    mst_weight = g2.spanning_tree()
    print(f"\nMST Total Weight: {mst_weight}")

    print("\n" + "-" * 60)
    print("TEST CASE 3: Simple Graph")
    print("-" * 60)

    adj = [[] for _ in range(3)]
    add_edge = lambda u, v, w: (adj[u].append((v, w)), adj[v].append((u, w)))

    add_edge(0, 1, 5)
    add_edge(1, 2, 3)
    add_edge(0, 2, 1)

    print("\nGraph: 3 vertices")
    print("Edges: 0-1 (5), 1-2 (3), 0-2 (1)")

    weight = prim_mst_simple(adj, 3)
    print(f"\nMST Weight: {weight}")

    print("\n" + "-" * 60)
    print("TEST CASE 4: Larger Graph")
    print("-" * 60)

    g4 = Graph(6, is_matrix=True)
    larger_edges = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 4),
        (3, 4, 2),
        (4, 5, 6),
    ]

    for u, v, w in larger_edges:
        g4.add_edge_matrix(u, v, w)

    print("\nGraph: 6 vertices")
    print("Edges:")
    for u, v, w in larger_edges:
        print(f"  {u} -- {v}: {w}")

    edges4, weight4 = g4.prim_mst_matrix()
    g4.print_mst(edges4, weight4)

    print("\n" + "=" * 60)
    print("HOW PRIM'S ALGORITHM WORKS")
    print("=" * 60)
    print("""
1. Start with an arbitrary vertex (usually vertex 0)

2. Maintain two sets:
   - MST set: vertices already in MST
   - Fringe set: vertices connected to MST but not yet included

3. At each step:
   - Pick the minimum weight edge from MST to fringe
   - Add the new vertex to MST
   - Update all adjacent vertices' key values

4. Continue until all vertices are in MST

Key Property (Cut Property):
   The lightest edge crossing any cut must be part of some MST.
   This is why the greedy approach works!
""")

    print("=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)
    print("\n1. Adjacency Matrix (Naive):")
    print("   Time:  O(V²)")
    print("   Space: O(V)")
    print("\n2. Adjacency Matrix + Heap:")
    print("   Time:  O(V² log V)")
    print("   Space: O(V)")
    print("\n3. Adjacency List + Heap:")
    print("   Time:  O((V + E) log V)")
    print("   Space: O(V + E)")
    print("\nWhere V = vertices, E = edges")
