import heapq

node, edge, src, des = list(map(int, input().split()))
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

g = {}
for i in range(1, node + 1):
    g[i] = []
for i in range(edge):
    g[u[i]].append((v[i], w[i]))

def dijkstra(G, s):
    d = {v: float('inf') for v in G}
    pi = {v: None for v in G}
    d[s] = 0

    heap = [(0, s)]

    while heap:
        dist_u, u = heapq.heappop(heap)

        if dist_u > d[u]:
            continue
            
        for v, weight in G[u]:
            if d[v] > d[u] + weight:
                d[v] = d[u] + weight
                pi[v] = u
                heapq.heappush(heap, (d[v], v))

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
