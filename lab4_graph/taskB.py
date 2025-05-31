node, edge = list(map(int, input().split()))

u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

graph = {}

# for i in range(edge):
#     if u[i] not in graph:
#         graph[u[i]] = []
#     graph[u[i]].append((v[i],w[i]))

for i in range(1,node+1):
    graph[i] = []
for i in range(edge):
    graph[u[i]].append((v[i],w[i]))
    
# print(graph)

for key in graph:
    # print(key,':',*graph[key])
    print(f'{key}:',*graph[key])
