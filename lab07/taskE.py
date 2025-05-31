import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

g = {i: [] for i in range(1, n + 1)}
for i in range(m):
    g[u[i]].append((v[i], w[i]))

def dijkstra_parity(G, start, end):
    dist = {v: [float('inf'), float('inf')] for v in G}
    dist[start][0] = 0
    dist[start][1] = 0

    heap = []

    for v, w in G[start]:
        p = w % 2
        dist[v][p] = w
        heapq.heappush(heap, (w, v, p)) 

    while heap:
        cost, u, last_parity = heapq.heappop(heap)
        if dist[u][last_parity] < cost:
            continue
        for v, w in G[u]:
            p = w % 2
            if p != last_parity:  
                if dist[v][p] > cost + w:
                    dist[v][p] = cost + w
                    heapq.heappush(heap, (dist[v][p], v, p))
        # print('dist',dist)
    res = min(dist[end][0], dist[end][1])
    return res if res != float('inf') else -1

print(dijkstra_parity(g, 1, n))
