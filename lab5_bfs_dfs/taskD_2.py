from collections import deque

node, edge, S, D, K = list(map(int, input().split()))

adj = {}

for i in range(1, node + 1):
    adj[i] = []
for i in range(edge):
    a, b = list(map(int, input().split()))
    adj[a].append(b)

for node in adj:
    adj[node].sort()

visited = {}
predecessor = {}


def bfs(G, s, d):

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

    path = []
    current = d

    if visited[current] == False:
        return None
    else:
        while current != None:
            path.append(current)
            current = predecessor[current]
        path.reverse()
        return path

if S == D and S == K:
    print(0)
    print(S)
    exit()

path1 = bfs(adj,S, K)
path2 = bfs(adj,K, D)

if path1 == None or path2 == None:
    print(-1)
else:
    # Combining paths but avoiding repeating K twice
    full_path = path1 + path2[1:]
    print(len(full_path) - 1)
    print(*full_path)
