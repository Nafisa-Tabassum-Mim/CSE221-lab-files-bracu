from math import gcd

node, query = list(map(int, input().split()))

graph = [[] for i in range(node+1)]

for i in range(1,node+1):
    for j in range(1,node+1):
        if i != j and gcd(i,j)== 1:
            graph[i].append(j)
            
# print(graph)

for i in range(query):
    x, k = list(map(int, input().split()))
    if k <= len(graph[x]):
        print(graph[x][k-1])
    else:
        print(-1)