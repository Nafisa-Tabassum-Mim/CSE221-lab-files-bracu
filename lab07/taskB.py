import sys
input = sys.stdin.readline
import heapq

node, edge, src, des = map(int, input().split())

g = {i: [] for i in range(1, node + 1)}
for i in range(edge):
    line = list(map(int, input().split()))
    g[line[0]].append((line[1], line[2]))

def dijkstra(G, s):
    d = {v: float('inf') for v in G}
    pi = {v: None for v in G}
    d[s] = 0

    heap = [(0, s)]

    while heap:
        dist_u, u = heapq.heappop(heap)
            
        for v, weight in G[u]:
            if d[v] > d[u] + weight:
                d[v] = d[u] + weight
                pi[v] = u
                heapq.heappush(heap, (d[v], v))

    return d, pi

distances1, predecessors1 = dijkstra(g, src)
distances2, predecessors2 = dijkstra(g, des)
min_time = float('inf')
meeting_node = -1

for i in g:
    if distances1[i] != float('inf') and distances2[i] != float('inf'):
        max_time = max(distances1[i], distances2[i])
        if max_time < min_time or (max_time == min_time and i < meeting_node):
            min_time = max_time
            meeting_node = i

if meeting_node == -1:
    print(-1)
else:
    print(min_time, meeting_node)
