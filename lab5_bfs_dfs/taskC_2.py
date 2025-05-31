from collections import deque, defaultdict
 
verticle, edge, src, des = map(int, input().split())
 
if src == des:
    print(0)
    print(src)
else:
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
 
    adj_list = defaultdict(list)
    for j in range(edge):
        adj_list[start[j]].append(end[j])
        adj_list[end[j]].append(start[j])
 
    for node in adj_list:
        adj_list[node].sort()
 
    visit = [False] * (verticle + 1)
    level = [-1] * (verticle + 1)
    parent = [None] * (verticle + 1)
 
    queue = deque()
    visit[src] = True
    level[src] = 0
    queue.append(src)
 
    while queue:
        u = queue.popleft()
        for v in adj_list[u]:
            if not visit[v]:
                visit[v] = True
                parent[v] = u
                level[v] = level[u] + 1
                queue.append(v)
 
    if not visit[des]:
        print(-1)
    else:
        print(level[des])
        path = []
        while des is not None:
            path.append(des)
            des = parent[des]
        print(*reversed(path))