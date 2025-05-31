from collections import deque

n, m, S, D, K = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)


def bfs(start, end):
    visited = [False] * (n + 1)
    parent = [None] * (n + 1)
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)

    if visited[end] == False:
        return None

    path = []
    current = end
    while current != None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path


if S == D and S == K:
    print(0)
    print(S)
    exit()

path1 = bfs(S, K)
path2 = bfs(K, D)

if path1 == None or path2 == None:
    print(-1)
else:
    # Combining paths but avoiding repeating K twice
    full_path = path1 + path2[1:]
    print(len(full_path) - 1)
    print(*full_path)
