from collections import deque


def min_dist(n, src, adj):
    dist = [float("inf")] * n
    dist[src] = 0
    dq = deque([src])

    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)

    return dist


if __name__ == "__main__":
    n = 9
    adj = [[] for _ in range(n)]
    edges = [
        (0, 1, 0),
        (1, 2, 1),
        (0, 3, 1),
        (2, 4, 1),
        (2, 5, 0),
        (3, 6, 1),
        (5, 7, 0),
        (6, 8, 0),
    ]
    for u, v, w in edges:
        adj[u].append((v, w))

    assert min_dist(n, 0, adj) == [0, 0, 1, 1, 2, 1, 2, 1, 2]
    assert min_dist(
        4, 0, [[(1, 0), (2, 1)], [(0, 0), (3, 1)], [(0, 1), (3, 0)], [(1, 1), (2, 0)]]
    ) == [0, 0, 1, 1]
    assert min_dist(2, 0, [[(1, 1)], [(0, 1)]]) == [0, 1]
    print("All tests passed!")
