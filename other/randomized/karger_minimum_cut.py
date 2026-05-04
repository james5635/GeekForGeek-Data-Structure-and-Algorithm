import random


class KargerMinCut:
    """Karger's algorithm for finding minimum cut in an undirected graph."""

    def __init__(self, vertices: int, edges: list[tuple[int, int]]):
        self.original_vertices = vertices
        self.original_edges = edges

    def _contract(self, u: int, v: int, parent: list[int]) -> int:
        """Contract edge (u, v) by merging u into v."""
        for i in range(len(parent)):
            if parent[i] == u:
                parent[i] = v
        return v

    def _count_edges(self, parent: list[int]) -> int:
        """Count edges between different components."""
        count = 0
        for u, v in self.original_edges:
            if parent[u] != parent[v]:
                count += 1
        return count

    def find_min_cut(self, iterations: int | None = None) -> int:
        """Find minimum cut using Karger's algorithm with multiple iterations."""
        if iterations is None:
            iterations = self.original_vertices**2 * 10

        min_cut = float("inf")
        n = self.original_vertices

        for _ in range(iterations):
            parent = list(range(n))
            vertices = n

            edges = self.original_edges[:]
            while vertices > 2:
                edge_idx = random.randint(0, len(edges) - 1)
                u, v = edges[edge_idx]

                root_u, root_v = parent[u], parent[v]
                while parent[root_u] != root_u:
                    root_u = parent[root_u]
                while parent[root_v] != root_v:
                    root_v = parent[root_v]

                if root_u != root_v:
                    parent[root_u] = root_v
                    vertices -= 1

            cut = self._count_edges(parent)
            min_cut = min(min_cut, cut)

        return min_cut


if __name__ == "__main__":
    vertices = 4
    edges = [
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 3),
    ]
    karger = KargerMinCut(vertices, edges)
    min_cut = karger.find_min_cut()
    print(f"Graph with {vertices} vertices")
    print(f"Edges: {edges}")
    print(f"Minimum cut: {min_cut}")
