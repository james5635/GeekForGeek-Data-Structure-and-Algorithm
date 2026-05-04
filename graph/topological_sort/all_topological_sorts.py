"""
All Topological Sorts of a Directed Acyclic Graph (DAG)

Unlike standard topological sort which returns one valid ordering, this
algorithm finds ALL possible topological orderings of a DAG using backtracking.

Algorithm:
1. Compute in-degree for all vertices
2. Use backtracking: pick any unvisited vertex with in-degree 0
3. Mark it visited, reduce in-degrees of neighbors, and recurse
4. Backtrack: restore state to explore other possibilities

Time Complexity: O(V!) worst case (e.g., graph with no edges)
Space Complexity: O(V) for recursion stack and auxiliary arrays
"""


class DAG:
    """Directed Acyclic Graph supporting enumeration of all topological sorts."""

    def __init__(self, num_vertices: int) -> None:
        """
        Initialize a DAG with a given number of vertices.

        Args:
            num_vertices: Number of vertices in the graph (0-indexed).
        """
        self.v = num_vertices
        self.adj: list[list[int]] = [[] for _ in range(num_vertices)]
        self.indegree: list[int] = [0] * num_vertices

    def add_edge(self, src: int, dest: int) -> None:
        """
        Add a directed edge from src to dest.

        Args:
            src: Source vertex.
            dest: Destination vertex.
        """
        self.adj[src].append(dest)
        self.indegree[dest] += 1

    def all_topological_sorts(self) -> list[list[int]]:
        """
        Find all possible topological orderings of this DAG.

        Returns:
            A list of all valid topological orderings, each being a list of vertex indices.
        """
        visited = [False] * self.v
        result: list[list[int]] = []
        self._backtrack(visited, [], self.indegree[:], result)
        return result

    def _backtrack(
        self,
        visited: list[bool],
        path: list[int],
        indegree: list[int],
        result: list[list[int]],
    ) -> None:
        """
        Recursive backtracking helper to enumerate all topological sorts.

        Args:
            visited: Boolean array tracking visited vertices.
            path: Current partial topological ordering.
            indegree: Current in-degree counts (mutated during recursion).
            result: Accumulator for complete orderings.
        """
        found = False

        for i in range(self.v):
            if indegree[i] == 0 and not visited[i]:
                # Include vertex i in the current path
                visited[i] = True
                path.append(i)

                # Reduce in-degree of all neighbors
                for neighbor in self.adj[i]:
                    indegree[neighbor] -= 1

                # Recurse
                self._backtrack(visited, path, indegree, result)

                # Backtrack: restore state
                visited[i] = False
                path.pop()
                for neighbor in self.adj[i]:
                    indegree[neighbor] += 1

                found = True

        # If no vertex could be chosen, we have a complete ordering
        if not found:
            result.append(path[:])


if __name__ == "__main__":
    # Example: Graph from GFG article
    # Edges: 5->2, 5->0, 4->0, 4->1, 2->3, 3->1
    #
    #     4 ---> 0
    #     |      ^
    #     v      |
    #     1 <--- 3 <--- 2 <--- 5
    #
    print("All Topological Sorts of a DAG")
    print("=" * 40)

    g = DAG(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("Graph edges: 5->2, 5->0, 4->0, 4->1, 2->3, 3->1")
    print(f"Number of vertices: 6")
    print()

    all_sorts = g.all_topological_sorts()
    print(f"Total number of topological sorts: {len(all_sorts)}")
    print()

    for i, order in enumerate(all_sorts, 1):
        print(f"  {i:2d}. {order}")

    print()

    # Smaller example
    print("Smaller example: 0->1, 0->2, 1->3, 2->3")
    g2 = DAG(4)
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 3)

    sorts2 = g2.all_topological_sorts()
    print(f"Total topological sorts: {len(sorts2)}")
    for i, order in enumerate(sorts2, 1):
        print(f"  {i}. {order}")
