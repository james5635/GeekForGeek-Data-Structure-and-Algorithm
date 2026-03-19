from collections import deque


def zero_one_bfs(num_vertices, edges, source):
    graph = [[] for _ in range(num_vertices)]
    for u, v, w in edges:
        graph[u].append((v, w))

    dist = [float("inf")] * num_vertices
    dist[source] = 0

    dq = deque()
    dq.append(source)

    while dq:
        u = dq.popleft()

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

                if weight == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)

    return dist


def main():
    num_vertices = 9
    edges = [
        (0, 1, 0),
        (0, 2, 1),
        (1, 3, 1),
        (1, 4, 1),
        (1, 5, 1),
        (2, 6, 1),
        (2, 7, 0),
        (3, 8, 0),
        (4, 8, 0),
        (5, 8, 0),
        (6, 8, 0),
        (7, 8, 0),
    ]

    print("Graph with 9 nodes and binary (0/1) weight edges:")
    for i in range(num_vertices):
        neighbors = [(v, w) for u, v, w in edges if u == i]
        print(f"  Node {i} -> {neighbors}")
    print()

    print(f"Finding shortest distances from source {0} using 0-1 BFS")
    print(
        "0-1 BFS uses deque: appendleft for 0-weight edges, append for 1-weight edges"
    )
    print()

    distances = zero_one_bfs(num_vertices, edges, 0)

    result = [dist if dist != float("inf") else -1 for dist in distances]
    print(f"Shortest distances from node 0:")
    print(f"Result:   {result}")
    print(f"Expected: [0, 0, 1, 1, 2, 1, 2, 1, 2]")
    print()

    # Test Case 2: Simple graph
    print("Test Case 2: Simple 4-node graph")
    num2 = 4
    edges2 = [(0, 1, 0), (0, 2, 1), (1, 3, 1), (2, 3, 0)]
    distances2 = zero_one_bfs(num2, edges2, 0)
    print(f"Shortest distances from node 0: {distances2}")
    print(f"Expected: [0, 0, 1, 1]")
    print()

    # Test Case 3: Graph with all zero weights
    print("Test Case 3: All zero weights")
    num3 = 3
    edges3 = [(0, 1, 0), (1, 2, 0)]
    distances3 = zero_one_bfs(num3, edges3, 0)
    print(f"Shortest distances from node 0: {distances3}")
    print(f"Expected: [0, 0, 0]")
    print()

    # Test Case 4: Graph with all weight 1
    print("Test Case 4: All weight 1")
    num4 = 4
    edges4 = [(0, 1, 1), (1, 2, 1), (2, 3, 1)]
    distances4 = zero_one_bfs(num4, edges4, 0)
    print(f"Shortest distances from node 0: {distances4}")
    print(f"Expected: [0, 1, 2, 3]")


if __name__ == "__main__":
    main()
