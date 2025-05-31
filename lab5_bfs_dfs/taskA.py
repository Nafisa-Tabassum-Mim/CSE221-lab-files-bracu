import sys
sys.setrecursionlimit(2 * 100000 + 5)
from collections import deque

city, road = list(map(int, input().split()))

adj={}
for i in range(1, city + 1):
    adj[i] = []
for i in range(road):
    # u_list = list(map(int, input().split()))  
    # adj[u_list[0]].append(u_list[1])
    # adj[u_list[1]].append(u_list[0])
    a,b = list(map(int, input().split()))  
    adj[a].append(b)
    adj[b].append(a)
    
# print(adj)

visited = {}

def bfs(G, s):

    for v in G:
        visited[v] = False
        
    queue = deque()
    visited[s] = True
    queue.append(s)

    while queue:
        u = queue.popleft()
        print(u, end=" ") 

        for v in G[u]:
            if visited[v] == False:
                visited[v] = True
                queue.append(v)

bfs(adj, 1)