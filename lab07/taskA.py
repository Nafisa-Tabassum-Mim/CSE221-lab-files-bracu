import sys
input = sys.stdin.readline

node, edge, src, des = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

g = {i: [] for i in range(1, node + 1)}
for i in range(edge):
    g[u[i]].append((v[i], w[i]))

def dijkstra(G, s):
    d = {v: float('inf') for v in G}
    pi = {v: None for v in G}
    Q = list(G.keys())
    d[s] = 0

    while Q:
        min_value = float('inf')
        u = None
        for vertex in Q:
            if d[vertex] <= min_value:
                min_value = d[vertex]
                u = vertex

        Q.remove(u)

        for v, weight in G[u]:
            if v in Q:
                if d[v] > d[u] + weight:
                    d[v] = d[u] + weight
                    pi[v] = u

    return d, pi

distances, predecessors = dijkstra(g, src)

if distances[des] == float('inf'):
    print(-1)
else:
    print(distances[des])
    path = []
    current = des
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    print(*path)
