from collections import deque

node, edge, S, D = list(map(int, input().split()))

u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

adj = {}

for i in range(1, node + 1):
    adj[i] = []
for i in range(0, edge):
    adj[u_list[i]].append(v_list[i])
    adj[v_list[i]].append(u_list[i])

for node in adj:
    adj[node].sort()
    
visited = {}
predecessor = {}


def bfs(G, s):

    for v in G:
        visited[v] = False
        predecessor[v] = None

    queue = deque()
    visited[s] = True
    queue.append(s)

    while queue:
        u = queue.popleft()

        for v in G[u]:
            if visited[v] == False:
                visited[v] = True
                predecessor[v] = u
                queue.append(v)
                
bfs(adj, S)

if S == D:
    print(0)
    print(S)
    exit()

path = []
current = D

if visited[current] == False:
    print(-1)
else:
    while current != None:
        path.append(current)
        current = predecessor[current]

    print(len(path) - 1)
    print(*reversed(path))


