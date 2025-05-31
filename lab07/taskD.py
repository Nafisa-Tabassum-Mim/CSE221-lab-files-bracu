import sys
input = sys.stdin.readline
import heapq

node, edge, src, des = map(int, input().split())
weights = list(map(int, input().split()))
weight = {i + 1: weights[i] for i in range(node)}
# print(weight)
g = {i: [] for i in range(1, node + 1)}
    
for i in range(edge):
    line = list(map(int, input().split()))
    g[line[0]].append(line[1])
    
# print(g)

def dijkstra(G, s):
    d = {v: float('inf') for v in G}
    d[s] = weight[s]

    heap = [(weight[s], s)]

    while heap:
        dist_u, u = heapq.heappop(heap)
            
        for v in G[u]:
            if d[v] > d[u] + weight[v]:
                d[v] = d[u] + weight[v]
                heapq.heappush(heap, (d[v], v))

    return d

distances = dijkstra(g, src)

if distances[des] == float('inf'):
    print(-1)
else:
    print(distances[des])