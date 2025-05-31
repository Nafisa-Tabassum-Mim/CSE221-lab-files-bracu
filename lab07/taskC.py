import sys
input = sys.stdin.readline
import heapq

node, edge= map(int, input().split())

g = {i: [] for i in range(1, node + 1)}
for i in range(edge):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))

# print(g)
def dijkstra(G, s):
    d = {v: float('inf') for v in G}
    visited = {v: False for v in G}
    d[s] = 0

    heap = [(0, s)]

    while heap:
        dist_u, u = heapq.heappop(heap)
        visited[u] = True
        
        for v, weight in G[u]:
            if visited[v] == False:
                maximum = max(weight,d[u])
                if maximum < d[v]:
                  d[v] = maximum
                  heapq.heappush(heap, (d[v], v))

    return d

distances = dijkstra(g, 1)

for i in g:
    if distances[i] == float('inf'):
        print(-1, end=' ')
    else:
        print(distances[i], end=' ')