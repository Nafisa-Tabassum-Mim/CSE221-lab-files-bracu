node, edge = list(map(int, input().split()))
u = list(map(int, input().split()))
v = list(map(int, input().split()))

graph = {}

for i in range(1, node + 1):
    graph[i] = []

for i in range(edge):
        graph[u[i]].append(v[i])
        graph[v[i]].append(u[i])

# print(graph)

count = 0
# for key, value in graph.items():
#     if len(value) % 2 != 0:
#         count += 1

for value in graph.values():
    if len(value) % 2 != 0:
        count += 1

# print(count)

if count == 0 or count == 2:
    print("YES")
else:
    print("NO")