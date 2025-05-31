import heapq
N, M, S, D = map(int, input().split())
S -= 1
D -= 1
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))
    
def dijkstra():   
    INF = float('inf')
    dist = [[INF, INF] for _ in range(N)]
    dist[S][0] = 0

    queue = [(0, S)]

    while queue:
        cost, u = heapq.heappop(queue)
        for v, w in graph[u]:
            new_cost = cost + w
            if new_cost < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = new_cost
                heapq.heappush(queue, (new_cost, v))
            elif dist[v][0] < new_cost < dist[v][1]:
                dist[v][1] = new_cost
                heapq.heappush(queue, (new_cost, v))

    result = dist[D][1]
    print(result if result != INF else -1)
    
dijkstra()