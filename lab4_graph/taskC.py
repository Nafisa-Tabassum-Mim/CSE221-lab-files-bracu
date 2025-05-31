node = int(input())
graph = [[0]*node for i in range(node)]

for i in range(node):
    line = list(map(int, input().split()))
    for j in range(line[0]):
        graph[i][line[j+1]] = 1
    
for row in graph:
    print(*row)