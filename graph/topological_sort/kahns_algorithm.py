"""
Kahn's Algorithm - Topological Sorting using BFS

Kahn's Algorithm produces a topological ordering by repeatedly selecting
vertices with in-degree 0 (no dependencies), adding them to the result,
and reducing the in-degree of their neighbors.

Algorithm:
1. Compute in-degree for every vertex
2. Enqueue all vertices with in-degree 0
3. While queue is not empty:
   a. Dequeue a vertex and add it to the result
   b. For each neighbor, decrement its in-degree
   c. If a neighbor's in-degree becomes 0, enqueue it
4. If the result contains fewer vertices than the graph, a cycle exists

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from collections import deque


def kahns_algorithm(adj: list[list[int]]) -> list[int]:
    """
    Perform topological sort using Kahn's Algorithm (BFS-based).

    Args:
        adj: Adjacency list where adj[u] contains all vertices v
             such that there is a directed edge u -> v.

    Returns:
        A list representing a valid topological ordering.

    Raises:
        ValueError: If the graph contains a cycle.
    """
    n = len(adj)
    indegree = [0] * n

    # Compute in-degrees
    for u in range(n):
        for v in adj[u]:
            indegree[v] += 1

    # Enqueue all vertices with in-degree 0
    queue: deque[int] = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    result: list[int] = []

    # Process vertices in BFS order
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycle
    if len(result) < n:
        raise ValueError("Graph contains a cycle; topological sort not possible.")

    return result


def has_cycle(adj: list[list[int]]) -> bool:
    """
    Check if a directed graph contains a cycle using Kahn's Algorithm.

    Args:
        adj: Adjacency list representation of the graph.

    Returns:
        True if the graph contains a cycle, False otherwise.
    """
    try:
        kahns_algorithm(adj)
        return False
    except ValueError:
        return True


if __name__ == "__main__":
    # Example 1: Simple DAG
    #   0 -> 1 -> 2 -> 3
    #   4 -> 5 -> 1, 5 -> 2
    print("Example 1:")
    print("Graph edges: 0->1, 1->2, 2->3, 4->5, 5->1, 5->2")
    adj1: list[list[int]] = [[] for _ in range(6)]
    adj1[0].append(1)
    adj1[1].append(2)
    adj1[2].append(3)
    adj1[4].append(5)
    adj1[5].append(1)
    adj1[5].append(2)

    result1 = kahns_algorithm(adj1)
    print(f"Topological sort: {result1}")
    print()

    # Example 2: GFG example
    #   0 -> 1 -> 2
    #   3 -> 2, 3 -> 4
    print("Example 2:")
    print("Graph edges: 0->1, 1->2, 3->2, 3->4")
    adj2: list[list[int]] = [[] for _ in range(5)]
    adj2[0].append(1)
    adj2[1].append(2)
    adj2[3].append(2)
    adj2[3].append(4)

    result2 = kahns_algorithm(adj2)
    print(f"Topological sort: {result2}")
    print()

    # Example 3: Cycle detection
    print("Example 3 (cycle detection):")
    print("Graph edges: 0->1, 1->2, 2->0 (cycle)")
    adj3: list[list[int]] = [[] for _ in range(3)]
    adj3[0].append(1)
    adj3[1].append(2)
    adj3[2].append(0)

    try:
        kahns_algorithm(adj3)
    except ValueError as e:
        print(f"Caught expected error: {e}")

    # Example 4: Using has_cycle helper
    print()
    print("Example 4: Cycle detection with has_cycle()")
    print(f"  DAG (0->1, 1->2): has_cycle = {has_cycle([[1], [2], []])}")
    print(f"  Cyclic (0->1, 1->0): has_cycle = {has_cycle([[1], [0]])}")
