import sys

sys.setrecursionlimit(2 * 100000 + 5)
node, edge = map(int, input().split())
adj = {}

for i in range(1, node + 1):
    adj[i] = []
for i in range(0, edge):
    u, v = map(int, input().split())
    adj[u].append(v)
    

visited = {}
cycle = False
def DFS(Adj, starting_node):
    for v in Adj:
        visited[v] = 0

    DFS_VISIT(Adj, starting_node)
    for vertex in Adj:
        if visited[vertex] == 0:
          DFS_VISIT(Adj, vertex)

def DFS_VISIT(Adj, vertex):
    global cycle
    visited[vertex] = 1
    for v in Adj[vertex]:
        if visited[v] == 0:
            DFS_VISIT(Adj, v)
        elif visited[v] == 1:
            cycle = True
    visited[vertex] = 2             

DFS(adj, 1)
if cycle == False:
    print('NO')
else:
    print('YES')