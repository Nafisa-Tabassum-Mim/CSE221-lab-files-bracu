node, edge = list(map(int, input().split()))
graph = [[0] * node for i in range(node)]

for i in range(edge):
    u, v, w = list(map(int, input().split()))
    graph[u-1][v-1] = w

# for i in range(node):
#     for j in range(node):
#         print(graph[i][j],end=' ')
#     print()

for i in graph:
    print(*i)

    
