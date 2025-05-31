node, edge = list(map(int, input().split()))
u = list(map(int, input().split()))
v = list(map(int, input().split()))

in_graph = {}
out_graph = {}

for i in range(1, node + 1):
    in_graph[i] = []
    out_graph[i] = []

for i in range(edge):
        out_graph[u[i]].append(v[i])
        in_graph[v[i]].append(u[i])
        
# print(in_graph)
# print(out_graph)

output =[]
for key in in_graph:
    output.append((len(in_graph[key]))-(len(out_graph[key])))
    
print(*output)
    