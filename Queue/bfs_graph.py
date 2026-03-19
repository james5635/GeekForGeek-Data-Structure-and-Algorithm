from collections import deque


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj = [[] for _ in range(num_vertices)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs_connected(self, start):
        visited = [False] * self.num_vertices
        result = []
        queue = deque([start])
        visited[start] = True

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            for neighbor in self.adj[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result

    def bfs_disconnected(self):
        visited = [False] * self.num_vertices
        result = []

        for i in range(self.num_vertices):
            if not visited[i]:
                queue = deque([i])
                visited[i] = True
                component = []

                while queue:
                    vertex = queue.popleft()
                    component.append(vertex)

                    for neighbor in self.adj[vertex]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)

                result.append(component)

        return result


if __name__ == "__main__":
    adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

    print("Adjacency List:")
    for i, neighbors in enumerate(adj):
        print(f"  {i} -> {neighbors}")
    print()

    g = Graph(5)
    for u, neighbors in enumerate(adj):
        for v in neighbors:
            if v > u:
                g.addEdge(u, v)

    print("BFS for single connected component (starting from vertex 0):")
    print(g.bfs_connected(0))

    print("\nBFS for disconnected graphs:")
    result = g.bfs_disconnected()
    for i, component in enumerate(result):
        print(f"  Component {i}: {component}")
