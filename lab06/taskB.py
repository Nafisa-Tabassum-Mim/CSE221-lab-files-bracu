from collections import defaultdict, deque

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
color = [-1] * (n + 1)
max_group = 0

for i in range(1, n + 1):
    if not visited[i]:
        queue = deque([i])
        visited[i] = True
        color[i] = 0
        count = [1, 0]

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = 1 - color[u]
                    count[color[v]] += 1
                    queue.append(v)
                elif color[v] == color[u]:
                    count = [0, 0]
                    break

        max_group += max(count)

print(max_group)
