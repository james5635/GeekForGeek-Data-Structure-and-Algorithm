import sys
from collections import defaultdict


def getMinPathSum(graph, necessary, source, dest):
    INF = sys.maxsize
    V = len(graph)

    def dijkstra(src, dst):
        dist = [INF] * V
        dist[src] = 0
        visited = [False] * V

        for _ in range(V):
            u = -1
            min_dist = INF
            for i in range(V):
                if not visited[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i

            if u == -1 or dist[u] == INF:
                break
            visited[u] = True

            if u == dst:
                return dist[dst]

            for v in range(V):
                if not visited[v] and graph[u][v] != INF:
                    if dist[u] + graph[u][v] < dist[v]:
                        dist[v] = dist[u] + graph[u][v]

        return dist[dst]

    nodes_to_visit = necessary[:]
    total_cost = 0
    current = source

    for node in nodes_to_visit:
        cost = dijkstra(current, node)
        if cost == INF:
            return -1
        total_cost += cost
        current = node

    cost = dijkstra(current, dest)
    if cost == INF:
        return -1
    total_cost += cost

    return total_cost


if __name__ == "__main__":
    INF = 10**9
    graph = [
        [0, 2, INF, INF, INF, INF, INF],
        [2, 0, 2, INF, INF, INF, INF],
        [INF, 2, 0, 3, INF, INF, INF],
        [INF, INF, 3, 0, 2, INF, INF],
        [INF, INF, INF, 2, 0, 1, INF],
        [INF, INF, INF, INF, 1, 0, 2],
        [INF, INF, INF, INF, INF, 2, 0],
    ]

    necessary = [2, 4]
    source, dest = 0, 6
    expected = 12

    print(f"Minimum Path Sum: {getMinPathSum(graph, necessary, source, dest)}")
    print(f"Expected: {expected}")
