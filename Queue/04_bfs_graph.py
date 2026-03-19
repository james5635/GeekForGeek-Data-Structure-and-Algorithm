from collections import deque


def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def bfs_single_component(adj, src, visited):
    queue = deque()
    visited[src] = True
    queue.append(src)
    while queue:
        u = queue.popleft()
        print(u, end=" ")
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)


def bfs_disconnected(adj, V):
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            bfs_single_component(adj, i, visited)
    print()


if __name__ == "__main__":
    V = 6
    adj = [[] for _ in range(V)]
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)
    add_edge(adj, 3, 5)
    add_edge(adj, 4, 5)

    print("BFS from source 0 (connected graph):")
    visited = [False] * V
    bfs_single_component(adj, 0, visited)
    print()
    print()

    V2 = 7
    adj2 = [[] for _ in range(V2)]
    add_edge(adj2, 0, 1)
    add_edge(adj2, 0, 2)
    add_edge(adj2, 3, 4)
    add_edge(adj2, 5, 6)

    print("BFS for disconnected graph:")
    bfs_disconnected(adj2, V2)
    print()

    V3 = 4
    adj3 = [[] for _ in range(V3)]
    add_edge(adj3, 0, 1)
    add_edge(adj3, 0, 2)
    add_edge(adj3, 1, 2)
    add_edge(adj3, 2, 3)

    print("BFS from source 2 (connected graph):")
    visited3 = [False] * V3
    bfs_single_component(adj3, 2, visited3)
    print()
