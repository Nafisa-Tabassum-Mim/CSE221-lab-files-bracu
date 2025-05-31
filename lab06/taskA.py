from collections import deque

course, req = map(int, input().split())
adj = {}
in_degree = [0] * (course + 1)

for i in range(1,course+1):
    adj[i]=[]

for i in range(req):
    u, v = map(int, input().split())
    adj[u].append(v)
    in_degree[v] += 1
    
# print(adj)
# print(in_degree)

q = deque()
for i in range(1, course + 1):
    if in_degree[i] == 0:
        q.append(i)
        
order = []

while q:
    node = q.popleft()
    order.append(node)
    for i in adj[node]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)
            
if len(order) == course:
    print(*order)
else:
    print(-1)

