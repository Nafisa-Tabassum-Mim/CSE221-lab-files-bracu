from collections import deque

def bfs(start, graph, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    farthest_node = start

    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > dist[farthest_node]:
                    farthest_node = v
    return farthest_node, dist[farthest_node]

def find_diameter(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    u, _ = bfs(1, graph, n)
    v, diameter = bfs(u, graph, n)
    return diameter, u, v


if __name__ == "__main__":
    n = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    d, a, b = find_diameter(n, edges)
    print(d)
    print(a, b)